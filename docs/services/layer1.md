# Layer 1 service

The Layer 1 service is Flexo MMS: the REST API that gives a SPARQL quadstore the shape
of a version-controlled model repository. Everything else in Flexo either sits on top of
it or supports it.

- Repository: [Open-MBEE/flexo-mms-layer1-service](https://github.com/Open-MBEE/flexo-mms-layer1-service) (Kotlin, Ktor)
- Image: `openmbee/flexo-mms-layer1-service`
- Documentation: [Layer 1 on ReadTheDocs](https://flexo-mms-deployment-guide.readthedocs.io/en/latest/flexo-mms-layer1-service/index.html)
- API reference: [flexo-mms-layer1-openapi](https://www.openmbee.org/flexo-mms-layer1-openapi/)

## The model

Layer 1 arranges the graph into a small vocabulary borrowed from version control:

| Resource | Meaning |
| --- | --- |
| **Organization** | The top-level owner of repositories |
| **Repository** | A model and its whole history |
| **Branch** | A named, movable line of commits; new repositories start with `master` |
| **Commit** | One change to a branch's model graph, recorded as the SPARQL update that produced it |
| **Lock** | A named, fixed reference to a commit, so a state can be queried by name |
| **Diff** | The triples added and removed between two commits |
| **Scratch** | A working graph on a repository, outside the commit history, for staging and experiment |
| **Policy**, **Group**, **Collection** | Access control: who may do what, to which resources |

Every one of these is itself RDF in the quadstore, described by the
[Flexo MMS ontology](../tools/libraries.md#flexo-mms-ontology): the metadata graph and the
model graphs live in one dataset.

## Reading and writing

Reading a model is SPARQL 1.1 **query** against a branch, a lock or a scratch, posted to
`/orgs/{org}/repos/{repo}/branches/{branch}/query` and its siblings; a query may also be
run across the repository as a whole, or against a diff. Layer 1 rewrites the query so it can only see the
graphs the caller is allowed to see.

Writing is one of:

- a SPARQL 1.1 **update** posted to a branch, which becomes a commit;
- a **load** to a branch's `graph`, which replaces its model with an RDF file — sent directly or, for
  large files, staged through the [Store service](store.md) so the quadstore can `LOAD` it
  by URL;
- a **diff**, which materialises the difference between two commits for inspection or for
  merging.

The endpoints are conventional REST: `GET`/`PUT`/`PATCH`/`DELETE` on orgs, repos,
branches, locks, scratches, policies, groups and collections, `HEAD` to check for
existence, and `POST` for queries, updates and loads. The
[OpenAPI reference](https://www.openmbee.org/flexo-mms-layer1-openapi/) lists them all.

## Authentication and access control

Layer 1 does not authenticate anyone itself. It trusts a JWT signed with a key it shares
with the [Auth service](auth.md) and reads the caller's identity and groups from it.
Policies then decide, per request, whether that caller holds the needed permission on the
resource, with permissions inheriting down from org to repo to branch. A deployment may
respond to a denied request with 404 so an unprivileged caller cannot tell whether the
resource exists.

## Configuration

Layer 1 is configured by environment variables — the quadstore's query, update and
graph-store endpoints, the JWT audience, issuer and secret, the Store service URL and the
root context. The
[deployment repository](deployment.md) sets them for Docker Compose and Kubernetes, and
the service documentation lists them in full.

## API reference

[flexo-mms-layer1-openapi](https://github.com/Open-MBEE/flexo-mms-layer1-openapi)
generates the OpenAPI document from the service and publishes it at
[openmbee.org/flexo-mms-layer1-openapi](https://www.openmbee.org/flexo-mms-layer1-openapi/).
The deployment repository also carries Postman and Bruno collections that walk through the
API against a local stack.
