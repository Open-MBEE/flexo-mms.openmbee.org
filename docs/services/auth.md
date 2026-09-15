# Authentication

Flexo MMS separates authentication from everything else. An authentication service turns
a credential into a signed JSON Web Token; [Layer 1](layer1.md) and the other services
verify the token with a shared secret and read the caller's identity and groups from it.
Two authentication services exist; a deployment picks whichever fits its identity
provider.

## Auth service

The original service authenticates a client against an LDAP directory.

- Repository: [Open-MBEE/flexo-mms-auth-service](https://github.com/Open-MBEE/flexo-mms-auth-service) (Kotlin, Ktor)
- Image: `openmbee/flexo-mms-auth-service`
- Documentation: [Auth service on ReadTheDocs](https://flexo-mms-deployment-guide.readthedocs.io/en/latest/flexo-mms-auth-service/index.html)

A client sends HTTP Basic credentials to `/login`; the service binds to LDAP with them,
looks up the user's groups, and returns a JWT carrying the username and group memberships.
The Docker Compose stack pairs it with OpenLDAP and two seeded users.

```sh
curl -u user01:password1 http://localhost:8082/login
```

Configuration is by environment variable: the LDAP URL, bind credentials, base DN and
group query, and the JWT audience, issuer, secret and lifetime.

## SSO auth service

The SSO service is a Spring Boot replacement for organisations that authenticate through
an identity provider rather than a directory.

- Repository: [Open-MBEE/flexo-mms-sso-auth-service](https://github.com/Open-MBEE/flexo-mms-sso-auth-service) (Java, Spring Boot)

It offers:

- **OAuth2 / OIDC login** against a configured provider, ending in a Flexo JWT;
- **API keys** for service-to-service calls and automation, managed through the service
  and exchanged for JWTs;
- **JWT generation and validation** with the same claims Layer 1 expects;
- user profile lookup;
- **SQLite** for development and **PostgreSQL** for production.

It runs on port 3000 by default and is configured through `application.yml`; the
repository's README covers the provider settings and the database options.

## What the token carries

Whichever service issues it, the token is what the rest of Flexo sees. Layer 1's policies
are written against the username and groups in its claims, so the JWT audience, issuer and
secret must match across the authentication service, Layer 1, the [Store service](store.md)
and the [SysML v2 API](sysmlv2.md) — the [deployment](deployment.md) manifests keep them
in one place.
