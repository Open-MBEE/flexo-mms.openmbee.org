# Layer 0 dashboard

The Layer 0 dashboard is an administrator's window straight onto the quadstore. Where
[Layer 1](layer1.md) shows the model through orgs, repos and branches, the dashboard shows
the named graphs those are made of, so an operator can inspect what Flexo has actually
stored and, when necessary, edit it in place.

- Repository: [Open-MBEE/flexo-mms-layer0-dashboard](https://github.com/Open-MBEE/flexo-mms-layer0-dashboard) (TypeScript)

## What it does

- Lists the named graphs in the dataset — metadata graphs, model graphs, the cluster
  context — and shows their contents.
- Lets an administrator edit triples in a graph directly, bypassing Layer 1's commit
  history. That makes it the tool for bootstrapping and repair, not for day-to-day
  modelling.

## Running it

It is a browser application: `npm install` then `npm run dev` (or the Yarn equivalents),
with the quadstore endpoint and credentials set in `.env.dev`. The defaults match the
Docker Compose stack in the [deployment repository](deployment.md).
