# Services

Each Flexo service is a container image under
[`openmbee/` on Docker Hub](https://hub.docker.com/u/openmbee) and a repository under
[Open-MBEE on GitHub](https://github.com/Open-MBEE). The
[architecture](../architecture.md) page explains how they fit together; this page lists
them.

## Flexo MMS

The collection of microservices at the centre of the architecture: the versioned RDF
store and the services that stand directly beside it.

| Service | Role | Repository |
| --- | --- | --- |
| [Layer 1](layer1.md) | The model management API: orgs, repos, branches, locks, commits, diffs, policies; SPARQL query and update | [flexo-mms-layer1-service](https://github.com/Open-MBEE/flexo-mms-layer1-service) |
| [Store](store.md) | Stages large model files in S3-compatible storage for the quadstore to `LOAD` | [flexo-mms-store-service](https://github.com/Open-MBEE/flexo-mms-store-service) |
| [Authentication](auth.md) | Exchanges an LDAP credential for a JWT | [flexo-mms-auth-service](https://github.com/Open-MBEE/flexo-mms-auth-service) |
| [SSO authentication](auth.md#sso-auth-service) | OAuth2/OIDC login, API keys and JWTs, on Spring Boot | [flexo-mms-sso-auth-service](https://github.com/Open-MBEE/flexo-mms-sso-auth-service) |
| [Layer 0 dashboard](dashboard.md) | Administrator's web UI over the named graphs in the quadstore | [flexo-mms-layer0-dashboard](https://github.com/Open-MBEE/flexo-mms-layer0-dashboard) |

## Domain APIs

| Service | Role | Repository |
| --- | --- | --- |
| [SysML v2 API and Services](sysmlv2.md) | The OMG Systems Modeling API REST platform-specific model, over Layer 1 | [flexo-mms-sysmlv2](https://github.com/Open-MBEE/flexo-mms-sysmlv2) |
| [GraphQL](graphql.md) | A GraphQL schema over any branch, compiled to SPARQL | [flexo-graphql](https://github.com/Open-MBEE/flexo-graphql) |

## API documentation and deployment

| Project | Role | Repository |
| --- | --- | --- |
| [Layer 1 OpenAPI](layer1.md#api-reference) | Generates and publishes the Layer 1 OpenAPI reference | [flexo-mms-layer1-openapi](https://github.com/Open-MBEE/flexo-mms-layer1-openapi) |
| [SysML v2 Swagger UI](sysmlv2.md#api-reference) | Kubernetes manifests for a Swagger UI over a SysML v2 API deployment | [flexo-sysmlv2-swagger](https://github.com/Open-MBEE/flexo-sysmlv2-swagger) |
| [Deployment](deployment.md) | Docker Compose stack and Kubernetes manifests for the whole of Flexo MMS | [flexo-mms-deployment](https://github.com/Open-MBEE/flexo-mms-deployment) |
