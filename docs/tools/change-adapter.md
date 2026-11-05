# Flexo Change Adapter

The Flexo Change Adapter connects a Flexo branch to a CI system. It is a small,
self-hosted service that polls one [Layer 1](../services/layer1.md) branch, records every
head it observes in a durable journal, and hands each change to the CI runner you
configure — GitHub Actions, GitLab or Jenkins — with the validation bound to the exact
revision it saw, even if the branch has moved on by the time the job runs.

- Repository: [Open-MBEE/flexo-change-adapter](https://github.com/Open-MBEE/flexo-change-adapter) (TypeScript, Node.js 24)
- Status: initial alpha; the configuration, CLI and state format may change before 1.0

## What it does

| Responsibility | How |
| --- | --- |
| **Observe** | Polls the branch at `/orgs/{org}/repos/{repo}/branches/{branch}`; the first read is a *baseline*, every later head a *branch change* |
| **Retain** | Commits each event, the actions it queued and the checkpoint together in SQLite, so a restart loses nothing and a queued action keeps its original destination |
| **Pin** | Resolves a change to a Layer 1 **lock** on the observed commit and reads the model graph through it, checking the commit and ETag before and after, so the validated graph is the one that was observed |
| **Validate** | Runs the selected checkers on that pinned revision and keeps the inputs, reports and results as evidence |
| **Publish** | Optionally writes a JSON activity feed of the newest events for other applications to read |

The pieces are independent: a feed-only configuration observes and publishes without any
CI, a generic trigger starts a pipeline with the revision's metadata and nothing else, and a
validation action carries the model itself to the runner.

## Checkers and runners

An action pairs a **task** with a **target**. Each is a registered implementation chosen in
configuration; there are no configurable commands or plugins to load.

| Task | Checks | Runs on |
| --- | --- | --- |
| `engine-validation` with `engine: opensysml` | Syntax and semantics of the SysML v2 text with [OpenSysML](https://github.com/Open-MBEE/OpenSysML) | GitHub, GitLab, Jenkins |
| `engine-validation` with `engine: sysml-toolkit` | The same, with the SysML Toolkit | GitHub, GitLab, Jenkins |
| `shacl-validation` | The RDF model graph against a project-chosen SHACL rule | GitHub, GitLab, Jenkins |
| `ci-trigger` | Nothing itself: starts a pipeline or job with the revision and event metadata | GitLab, Jenkins |

The text engines read a bundle of `.sysml` and `.kerml` files that the model's producer
publishes as artifacts in the same Flexo repository and binds, by digest, into the RDF graph
of the revision; the adapter verifies every digest before the engine runs. Each reviewed
engine profile pins the engine version and standard library it executes. Passing a check
says the selected engine accepted the pinned revision; it is not a claim of complete
standards conformance.

On GitHub the runner is a private *execution repository* carrying the same reviewed worker
source: inputs are retained there as Git objects and the workflow receives their
identities, never a Flexo credential. On GitLab and Jenkins, validation runs on dedicated
self-hosted workers that share a durable directory with the adapter; generic triggers need
only an API token.

## Configuration

One versioned JSON file selects the source, where state and the feed live, and the actions:

```json
{
  "schema_version": 1,
  "id": "satellite",
  "state_directory": "./satellite",
  "source": {
    "type": "flexo",
    "endpoint": "https://flexo.example",
    "organization": "research",
    "repository": "satellite",
    "branch": "main"
  },
  "observation": { "mode": "poll", "interval_seconds": 30 },
  "feed": { "type": "json-feed", "path": "./satellite/output/activity.json" },
  "actions": [
    {
      "id": "opensysml",
      "on": ["branch-change"],
      "task": { "type": "engine-validation", "engine": "opensysml", "profile": "syntax-semantic-v1" },
      "target": { "type": "github", "owner": "research", "repository": "satellite-checks" }
    }
  ]
}
```

`on` selects `branch-change`, `baseline` or both. Paths resolve relative to the file.
Credentials never appear in it: the adapter reads a Flexo bearer token from `FLEXO_TOKEN`
(or `FLEXO_USERNAME` and `FLEXO_PASSWORD`, exchanged at the
[Auth service](../services/auth.md)) and the CI tokens from the environment variables the
target names. The repository's `examples/configuration/` holds a starting point for each
runner.

## Running it

```sh
git clone https://github.com/Open-MBEE/flexo-change-adapter.git
cd flexo-change-adapter
npm ci

npm run adapter -- check  --config adapter.json          # validate offline, no credentials
npm run adapter -- run    --config adapter.json --once   # one poll and delivery round
npm run adapter -- status --config adapter.json          # inspect retained state
npm run adapter -- run    --config adapter.json          # keep polling
```

`check` is offline and creates no state. A `compose.configured.yaml` runs the same
commands in a container with the configuration mounted read-only and `/data` as the
persistent volume. The adapter is a source release rather than an npm package, and the
repository's `just` recipes bring up a local Jenkins for trying the triggers without a
hosted account.

## Limits

Polling samples the branch head, so commits made between two polls are not seen
individually; one process watches one branch. Verified validation is only as trustworthy
as the worker: the watcher and the worker must run the same reviewed source and locked
dependencies, which together form the *validator identity* retained with every result.
The repository's [status page](https://github.com/Open-MBEE/flexo-change-adapter/blob/main/docs/status.md)
records what has been verified on which platform.
