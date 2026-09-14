# Getting started

Two Docker Compose stacks bring Flexo up on one machine. Both need
[Docker](https://www.docker.com/) with Compose.

## Flexo MMS

The [deployment repository](https://github.com/Open-MBEE/flexo-mms-deployment) starts
OpenLDAP, Apache Jena Fuseki and MinIO, then the Auth, Store and Layer 1 services against
them, on a bridged network. A pre-generated `cluster.trig` seeds Fuseki with the root
context and policies that make the default LDAP users administrators.

```sh
git clone https://github.com/Open-MBEE/flexo-mms-deployment.git
cd flexo-mms-deployment/docker-compose
docker compose up
```

The API is ready when Layer 1 logs `Responding at http://0.0.0.0:8080`. Two users exist
by default, `user01` / `password1` and `user02` / `password2`. Log in against the Auth
service and use the token it returns as a bearer token for Layer 1:

```sh
TOKEN=$(curl -su user01:password1 http://localhost:8082/login | jq -r .token)

curl -H "Authorization: Bearer $TOKEN" http://localhost:8080/orgs
```

From there the
[Layer 1 API documentation](https://www.openmbee.org/flexo-mms-layer1-openapi/) lists every
endpoint, and the directory holds a Postman collection and a Bruno collection that walk
through creating an organisation and a repository, loading a model, querying it and
committing a change. `docker compose -f docker-compose-graphdb.yml up` swaps Fuseki for
GraphDB; the README explains the one-time repository setup GraphDB needs.

## The SysML v2 API

The [SysML v2 service repository](https://github.com/Open-MBEE/flexo-mms-sysmlv2) carries
a Compose stack of its own that starts the Flexo MMS prerequisites and the SysML v2 API in
front of them:

```sh
git clone https://github.com/Open-MBEE/flexo-mms-sysmlv2.git
cd flexo-mms-sysmlv2
docker compose -f ./docker-compose/docker-compose.yml up -d
```

The API listens on port 8083 and the bearer token it expects is in
`docker-compose/env/flexo-sysmlv2.env`. Then `http://localhost:8083/projects` answers, and any client of the OMG Systems Modeling API — the
[Python client](tools/python.md), the [Web Modeler](tools/web-modeler.md), the
[SysML v2 MCP server](tools/mcp.md) — points at it. A Postman collection and a Bruno
collection in the repository cover the endpoints.

## From a terminal

The [Flexo CLI](tools/cli.md) folds the Layer 1 stack into one command. `flexo init`
starts Fuseki and Layer 1 in Docker, loads the cluster configuration, creates a default
organisation, repository and branch, and writes `~/.flexo/config`; after that, `push`,
`pull`, `branch`, `merge` and `remote` work the way they do in git.

## Running it for real

For a cluster, the deployment repository's Kubernetes manifests split the same stack into
deployments, services, an SSL ingress, and config maps for Layer 1, JWT, S3, LDAP and
logging. The [deployment page](services/deployment.md) describes what to fill in, and each
service's own documentation lists its environment variables.
