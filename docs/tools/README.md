# Clients and tools

The things people and programs use to work with a Flexo deployment. Each one lives in its
own repository under [Open-MBEE on GitHub](https://github.com/Open-MBEE).

## Command line

| Tool | Talks to | Repository |
| --- | --- | --- |
| [Flexo CLI](cli.md) | Layer 1, with git-style `init`, `push`, `pull`, `branch`, `merge`, `remote` | [flexo-cli-client](https://github.com/Open-MBEE/flexo-cli-client) |
| [SysML v2 plugin](cli.md#sysml-v2-plugin) | The SysML v2 API, from the same CLI | [flexo-cli-sysmlv2-plugin](https://github.com/Open-MBEE/flexo-cli-sysmlv2-plugin) |

## AI assistants

| Tool | Talks to | Repository |
| --- | --- | --- |
| [Layer 1 MCP server](mcp.md#layer-1-mcp-server) | Layer 1: orgs, repos, branches, SPARQL, locks, diffs, policies | [flexo-mms-layer1-mcp](https://github.com/Open-MBEE/flexo-mms-layer1-mcp) |
| [SysML v2 MCP server](mcp.md#sysml-v2-mcp-server) | The SysML v2 API: projects, commits, branches, elements | [flexo-mms-sysmlv2-mcp](https://github.com/Open-MBEE/flexo-mms-sysmlv2-mcp) |

## Programming

| Tool | Talks to | Repository |
| --- | --- | --- |
| [SysML v2 Python client](python.md) | The SysML v2 API | [sysmlv2-python-client](https://github.com/Open-MBEE/sysmlv2-python-client) |
| [flexo_syside](python.md#flexo_syside) | SysML v2 textual notation ↔ Flexo, via SysIDE | [flexo_syside](https://github.com/Open-MBEE/flexo_syside) |
| [Jama SDK](libraries.md#jama-sdk) | Requirements data from Jama stored in Flexo MMS | [flexo-mms-jama-sdk](https://github.com/Open-MBEE/flexo-mms-jama-sdk) |

## In the browser

| Tool | Talks to | Repository |
| --- | --- | --- |
| [SysML v2 Web Modeler](web-modeler.md) | The SysML v2 API: graphical rendering and textual editing | [sysmlv2-web-modeler](https://github.com/Open-MBEE/sysmlv2-web-modeler) |
| [Flexo PR Manager](libraries.md#flexo-pr-manager) | Model-based pull requests and reviews over Flexo projects | [flexo-pr-manager](https://github.com/Open-MBEE/flexo-pr-manager) |
| [Layer 0 dashboard](../services/dashboard.md) | The quadstore's named graphs, for administrators | [flexo-mms-layer0-dashboard](https://github.com/Open-MBEE/flexo-mms-layer0-dashboard) |

## Reference

| Project | Role | Repository |
| --- | --- | --- |
| [Flexo MMS ontology](libraries.md#flexo-mms-ontology) | The RDF vocabulary Flexo stores its own metadata in | [flexo-mms-ontology](https://github.com/Open-MBEE/flexo-mms-ontology) |
| [Performance test suite](libraries.md#performance-test-suite) | Postman collection and data generator for load testing the SysML v2 API | [flexo-performance-test](https://github.com/Open-MBEE/flexo-performance-test) |
