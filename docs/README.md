# Flexo

Flexo is [Open-MBEE](https://www.openmbee.org/)'s architecture for model management. At
its centre is **Flexo MMS**, a collection of microservices that make up a
version-controlled store for model data whose native form is RDF, so a model is a graph
other tools can query, diff and merge rather than a file they have to parse. Around it are
domain APIs, clients and tools that share one contract — a SPARQL 1.1 quadstore
underneath, JSON Web Tokens between them — and each lives in its own repository with its
own documentation. This site is the map.

## Where to go

- **[Architecture](architecture.md)** — the layers, what each service is for, and how a
  request travels from a client to the quadstore and back.
- **[Getting started](getting-started.md)** — the Docker Compose stacks that bring up
  Flexo MMS, and the SysML v2 API on top of it, on one machine.
- **[Services](services/README.md)** — every service: Layer 1, Store, Authentication,
  the SysML v2 API, GraphQL, the Layer 0 dashboard and the deployment manifests.
- **[Clients and tools](tools/README.md)** — the git-style CLI, the MCP servers, the Python
  client, the SysML v2 Web Modeler, and the libraries and integrations around them.
- **[Community](community.md)** — where the conversation happens and how to contribute.

## Two APIs, one store

Flexo exposes the same versioned graph through two APIs, and a deployment can run either
or both.

| API | Speaks | For |
| --- | --- | --- |
| [Flexo MMS Layer 1](services/layer1.md) | REST over orgs, repos, branches, locks and commits; SPARQL 1.1 query and update against any of them | Anything expressed as RDF: requirements from Jama, ontologies, a system model, tabular data lifted to a graph |
| [SysML v2 API and Services](services/sysmlv2.md) | The OMG Systems Modeling API and Services REST platform-specific model — projects, commits, branches, tags, elements | SysML v2 modelling tools and clients that speak the standard, without knowing what is underneath |

The SysML v2 API translates onto Layer 1, so a SysML v2 project is a Layer 1 repository
and a SysML v2 commit is a Layer 1 commit: the same history, reachable either way.

## Flexo MMS and the earlier MMS

Flexo MMS is not a drop-in replacement for the earlier, document-oriented MMS (now
[exec-mms](https://github.com/Open-MBEE/exec-mms)), which stores JSON documents and is
documented at
[mms-reference-implementation.readthedocs.io](https://mms-reference-implementation.readthedocs.io/en/latest/index.html).
Flexo MMS stores RDF and versions the graph itself. Older repositories, images and documents
still call it *MMS5*; the two names refer to the same services.
