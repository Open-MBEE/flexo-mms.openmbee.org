# Libraries and integrations

## Flexo MMS ontology

[flexo-mms-ontology](https://github.com/Open-MBEE/flexo-mms-ontology) is the RDF
vocabulary Flexo describes itself in: the classes and properties for organizations,
repositories, branches, commits, locks, policies, groups and the rest of what
[Layer 1](../services/layer1.md) stores in the quadstore alongside the models. The
repository carries the ontology and a diagram of it. Anything that queries a Flexo dataset
directly — the [Layer 0 dashboard](../services/dashboard.md), a report, a migration — reads
these terms.

## Jama SDK

[flexo-mms-jama-sdk](https://github.com/Open-MBEE/flexo-mms-jama-sdk) is a TypeScript
library, for Node.js, Deno or the browser, for querying and iterating all the requirements
data of a Jama project that has been stored in Flexo MMS. It is published to npm as
[`@openmbee/mms5-jama-sdk`](https://www.npmjs.com/package/@openmbee/mms5-jama-sdk).

## Flexo PR Manager

[flexo-pr-manager](https://github.com/Open-MBEE/flexo-pr-manager) is a small web service
for **model-based pull requests** against Flexo projects. It lists projects and branches,
records a pull request with its source and target branches and commit snapshots, tracks
reviews (`COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`) and status, and generates the
source, target and base commit URLs a diff tool such as LemonTree needs. FastAPI with a
static front end and SQLite, shipped as one Docker container.

## Performance test suite

[flexo-performance-test](https://github.com/Open-MBEE/flexo-performance-test) is a Postman
collection and data generator for load-testing a [SysML v2 API](../services/sysmlv2.md)
deployment: it generates a large model, feeds it through the Collection Runner from a CSV,
and times project creation, commits and element retrieval.

## Modelling tool integrations

Any tool that implements the OMG Systems Modeling API and Services can use Flexo's
[SysML v2 API](../services/sysmlv2.md) as its repository. The
[SysML v2 Web Modeler](web-modeler.md), [flexo_syside](python.md#flexo_syside) and the
[SysML v2 MCP server](mcp.md#sysml-v2-mcp-server) are the integrations Open-MBEE
maintains; the Open-MBEE [Slack](../community.md) is where others are discussed.
