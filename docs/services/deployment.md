# Deployment

The deployment repository is the reference for running Flexo MMS as a whole: a Docker
Compose stack for one machine and Kubernetes manifests for a cluster, plus the guide that
documents them.

- Repository: [Open-MBEE/flexo-mms-deployment](https://github.com/Open-MBEE/flexo-mms-deployment)
- Guide: [flexo-mms-deployment-guide.readthedocs.io](https://flexo-mms-deployment-guide.readthedocs.io/en/latest/)

## Docker Compose

`docker-compose/` starts everything Flexo MMS needs on a bridged network:

| Container | Role | Local port |
| --- | --- | --- |
| OpenLDAP | Directory with two seeded users | 1389 |
| Apache Jena Fuseki | The quadstore, seeded with `cluster.trig` | 3030 |
| MinIO | S3-compatible storage for the Store service | 9000 |
| Auth service | LDAP login → JWT | 8082 |
| Store service | Large loads to MinIO | 8081 |
| Layer 1 service | The Flexo MMS API | 8080 |

A second compose file swaps Fuseki for Ontotext GraphDB. The directory also carries a
Postman collection and a Bruno collection for the API, and the
[getting started](../getting-started.md) page walks through a first session. The SysML v2
API has a [compose stack of its own](sysmlv2.md#running-it) that adds it to this one.

## Kubernetes

`k8s/` splits the same stack into deployments and services for the Auth, Store and Layer 1
services, an SSL-terminating ingress, and config maps and secrets for Layer 1, JWT, S3,
LDAP and logging. Fill in the hostnames, secrets and storage endpoints for your cluster,
then `kubectl apply` the directory. The manifests are a starting point rather than a Helm
chart; the README explains what each file configures.

## Configuration in general

Every Flexo service is configured through environment variables, and the same few
settings recur across them:

- the **quadstore** endpoints — query, update and graph store — for Layer 1;
- the **JWT** audience, issuer and secret, which must be identical everywhere;
- the **S3** endpoint, bucket and credentials for the Store service;
- the **LDAP** or identity-provider settings for authentication;
- the **root context**, the IRI under which Flexo names everything it stores.

The service pages on this site say what each service needs; the guide on ReadTheDocs lists
every variable.

## Images

All services publish images to [Docker Hub under `openmbee/`](https://hub.docker.com/u/openmbee).
