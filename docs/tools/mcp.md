# MCP servers

Two [Model Context Protocol](https://modelcontextprotocol.io/) servers put Flexo in front
of an AI assistant — one for each of Flexo's APIs. Both are Python, built on FastMCP with
the streamable HTTP transport, and both default to **read-only** so an assistant can
explore a model without being able to change it until you say so.

## Layer 1 MCP server

Wraps the [Layer 1](../services/layer1.md) REST API as MCP tools.

- Repository: [Open-MBEE/flexo-mms-layer1-mcp](https://github.com/Open-MBEE/flexo-mms-layer1-mcp)

| Tools for | Covering |
| --- | --- |
| Structure | Reading and managing organizations, repositories and branches |
| Models | Reading, loading, querying and committing RDF with SPARQL |
| Version control | Locks, and diffs between commits |
| Access control | Policies, groups and collections |

With `READ_ONLY=true` (the default) only the read and query tools are registered.
`MMS_URL` names the Layer 1 endpoint. The `Authorization` header on an MCP request is
forwarded to Layer 1, so the assistant acts as the user who is logged in, with that user's
policies applied.

```sh
docker run -d -p 8000:8000 \
  -e MMS_URL=https://your-flexo-mms-server \
  -e READ_ONLY=false \
  flexo-mms-layer1-mcp
```

## SysML v2 MCP server

Wraps the [SysML v2 API](../services/sysmlv2.md) as MCP tools.

- Repository: [Open-MBEE/flexo-mms-sysmlv2-mcp](https://github.com/Open-MBEE/flexo-mms-sysmlv2-mcp)

`SYSMLV2_URL` names the API; `READ_ONLY=true` (the default) exposes only the `GET`
endpoints; `MCPPATH` moves the MCP endpoint from `/mcp`. Bearer tokens from the MCP client
are forwarded to the API.

```sh
SYSMLV2_URL=https://api.example.com READ_ONLY=true python server.py
```

Then point an MCP client at `http://localhost:8000/mcp`, with an `Authorization: Bearer …`
header if the deployment needs one.
