# SysML v2 API and Services

The SysML v2 service implements the OMG Systems Modeling API and Services REST
platform-specific model on top of Flexo MMS. A SysML v2 tool talks to the standard API;
underneath, projects are Layer 1 repositories and commits are Layer 1 commits, so a SysML
v2 model gets the same branching, history, diffs and access control as any other graph in
Flexo.

- Repository: [Open-MBEE/flexo-mms-sysmlv2](https://github.com/Open-MBEE/flexo-mms-sysmlv2) (Java 21)
- Image: `openmbee/flexo-sysmlv2`
- Standard: [OMG Systems Modeling API and Services](https://www.omg.org/spec/SystemsModelingAPI/)

## What it serves

The REST resources of the standard:

| Resource | Notes |
| --- | --- |
| `/projects` | One project per Layer 1 repository, identified by UUID as the standard requires |
| `/projects/{id}/commits` | Element create, update and delete in one change set |
| `/projects/{id}/branches` | Branches, with an `Initial` branch created for a new project |
| `/projects/{id}/tags` | Fixed references to a commit |
| `/projects/{id}/commits/{id}/elements` | Elements and their owned elements at a commit |
| `/projects/{id}/commits/{id}/elements/{id}/relationships` | Relationships of an element |
| `/projects/{id}/query-results` | Queries against a project |

Elements are stored as RDF in the Layer 1 model graph and rendered back as the JSON the
standard defines. Callers authenticate with the same bearer token the rest of Flexo MMS
uses; the [Auth service](auth.md) issues it.

## Running it

The repository's `docker-compose/` directory starts the Flexo MMS prerequisites and the
SysML v2 API in front of them on port 8083; the token to use is in
`docker-compose/env/flexo-sysmlv2.env`.
The [getting started](../getting-started.md) page walks through it. A Postman collection
and a Bruno collection in the repository exercise every endpoint.

## Who talks to it

The [SysML v2 Web Modeler](../tools/web-modeler.md), the
[Python client](../tools/python.md), the [SysML v2 MCP server](../tools/mcp.md) and the
Flexo CLI's [SysML v2 plugin](../tools/cli.md#sysml-v2-plugin) all speak to this API, as
does any other tool built to the OMG standard.

## API reference

[flexo-sysmlv2-swagger](https://github.com/Open-MBEE/flexo-sysmlv2-swagger) carries
Kubernetes manifests that host a Swagger UI over a deployed SysML v2 API: an init
container fetches the OpenAPI document, and an initializer injects an `Authorization`
header so the "try it" requests work against a protected deployment.
