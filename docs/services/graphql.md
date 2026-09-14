# GraphQL

Flexo GraphQL serves a GraphQL schema over the model graph of a Flexo branch, compiling
each query to SPARQL. It gives front ends and scripts a typed, nested view of the model
without writing SPARQL by hand.

- Repository: [Open-MBEE/flexo-graphql](https://github.com/Open-MBEE/flexo-graphql) (TypeScript, Deno)
- Image: `openmbee/flexo-graphql`

## How it works

The server is given two files: a GraphQL **schema** describing the types in the model, and
a JSON-LD **context** mapping the schema's fields to RDF predicates. An incoming query is
translated into a SPARQL query using that mapping, sent to the SPARQL endpoint, and the
bindings are shaped back into the GraphQL response.

The endpoint is a pattern, so one server can front many models:

```sh
SPARQL_ENDPOINT='http://layer1:8080/orgs/${org}/repos/${repo}/branches/${branch}/query'
```

`${org}`, `${repo}` and `${branch}` are filled from the request, so a query is scoped to
exactly one branch of one repository.

## Features

- Filtering on scalar fields, with the usual comparison operators, in query arguments.
- Nested selection across relationships, resolved in one SPARQL query rather than N+1.
- **GraphiQL** in the browser for exploring the schema and trying queries.

## Running it

```sh
docker run -it --rm -v $(pwd)/res:/data \
  -e 'SPARQL_ENDPOINT=http://localhost:7200/repositories/${org}-${repo}' \
  openmbee/flexo-graphql
```

The mounted directory holds `schema.graphql` and `context.json`. Without Docker, the
repository runs under Deno with the Velociraptor script runner.
