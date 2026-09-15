# Flexo CLI

The Flexo CLI is a git-style command line for [Layer 1](../services/layer1.md). It treats
a Flexo repository the way git treats a remote: you pull a branch's model to a file, edit
it, push it back, and branch and merge as you go.

- Repository: [Open-MBEE/flexo-cli-client](https://github.com/Open-MBEE/flexo-cli-client) (Java 17, Gradle)

## Commands

| Command | Does |
| --- | --- |
| `flexo init` | Starts Fuseki and Layer 1 in Docker, loads the cluster configuration, creates a default org, repo and branch, and writes `~/.flexo/config` |
| `flexo pull <branch> --output model.ttl` | Fetches a branch's model as RDF |
| `flexo push <branch> model.ttl` | Loads a file as the branch's new model |
| `flexo branch` | Lists, creates or deletes branches |
| `flexo merge` | Merges one branch into another |
| `flexo rm` | Removes a resource |
| `flexo remote` | Manages named Flexo servers, like git remotes |

Models move as Turtle, JSON-LD, RDF/XML or N-Triples.

## Authentication

Against the local stack `init` creates, the CLI authenticates automatically. Against a
production deployment it signs a JWT with an SSH key, so no password needs to be stored;
each remote in `~/.flexo/config` carries its own authentication settings.

## Getting it

```sh
git clone https://github.com/Open-MBEE/flexo-cli-client.git
cd flexo-cli-client
./gradlew installDist
./build/install/flexo/bin/flexo init
```

`init` needs Docker running.

## SysML v2 plugin

[flexo-cli-sysmlv2-plugin](https://github.com/Open-MBEE/flexo-cli-sysmlv2-plugin) adds
SysML v2 commands to the same CLI. It deploys a local
[SysML v2 API](../services/sysmlv2.md) in Docker against the Layer 1 stack, manages
SysML v2 remotes and links each to the Flexo remote that authenticates it, clones projects
from a remote to local with automatic ID mapping, and pulls and pushes models between the
two. Projects, branches, tags, commits, elements, relationships and queries are all
reachable from the command line.
