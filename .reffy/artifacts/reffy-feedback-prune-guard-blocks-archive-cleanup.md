# Reffy feedback: the 5% prune guard blocks archive cleanup in small projects

A note for the Reffy developers, from the `durable-forms` project. Observed on reffy 1.12.1, 2026-11-24.

## Summary

The `archive-change` skill tells the agent to clean up after an archive with `reffy remote push --prune`, and never to use `--force` to do it. In a small project the mass-deletion guard refuses that prune every time, so the skill has no compliant path. The stale copies of the archived change stay on the remote unless a human approves an exception.

## What happened

1. `reffy plan archive add-monad-thread` moved the change to `changes/archive/2026-11-25-add-monad-thread/`.
2. A plain `reffy remote push` published the archived copy and left the seven old `changes/add-monad-thread/` documents on the remote.
3. Following the skill, `reffy remote push --dry-run --prune` listed exactly those seven paths under "Would delete" and nothing else. The skill's condition for pruning was met.
4. The same dry run reported: "A real push would be refused: it deletes more than 5% of the project's remote documents. Add --force to override."
5. The skill says: "Never add `--force` to get an archive cleanup through the mass-deletion guard." The agent stopped there.
6. The project owner approved `--prune --force` as a one-off exception. It deleted the seven paths and nothing else.

The same result occurred on both workspaces the manifest lists (`lasm-v1` and `nuveris-v1`).

## Why it will recur

The guard measures deletions against the project's own remote documents, not the whole workspace. This project had 59 remote documents at the time (52 local plus the 7 stale ones), so the seven deletions were 11.9%. Measured against the workspaces they would have been 2.3% (of 304) and 0.5% (of 1290).

A change with `k` files trips the guard in any project with fewer than `20 × k` remote documents:

| Change contents | Files | Trips the guard below |
|---|---|---|
| proposal, tasks, one spec | 3 | 60 documents |
| proposal, tasks, design, one spec | 4 | 80 documents |
| proposal, tasks, design, four specs (this case) | 7 | 140 documents |

The smallest valid change has three files, so every archive in a project under 60 documents hits the guard. This project has 52.

## The conflict

The guard and the skill are each reasonable alone. The guard protects against pruning from a checkout that is missing another branch's plans. The skill's ban on `--force` stops an agent from waving that protection away. Together they leave archive cleanup, the one prune the skill prescribes, impossible in a small project without a human overriding the skill.

## Suggestions

In order of preference:

1. **Exempt archive moves from the guard.** When a path to delete is under `changes/<change-id>/` and the same push holds `changes/archive/<date>-<change-id>/`, the deletion is a move, not a loss. Do not count it toward the 5%. This keeps the guard intact for the case it exists for.
2. **Add a scoped prune.** For example `reffy remote push --prune-change <change-id>`, which deletes only that change's old paths and needs no guard. The skill could then name that command, and `reffy plan archive` could offer it directly.
3. **Add an absolute floor.** Apply the percentage only above a minimum number of deletions (say 10 or 20), so small projects are not caught by rounding.

Whichever lands, the `archive-change` skill should say what to do when the guard refuses a prune whose deletions are all under the archived change. At present it only covers the case where they are not.

## Evidence

Dry run on `lasm-v1` before the forced prune (the `nuveris-v1` output was identical apart from the workspace id):

```
Remote push dry run (no changes made)
Workspace id: lasm-v1
Project id: durable-forms
Mode: prune
Plan: add 0, update 9, unchanged 43, delete 7
Would delete:
- .reffy/reffyspec/changes/add-monad-thread/design.md
- .reffy/reffyspec/changes/add-monad-thread/proposal.md
- .reffy/reffyspec/changes/add-monad-thread/specs/construction/spec.md
- .reffy/reffyspec/changes/add-monad-thread/specs/front-matter/spec.md
- .reffy/reffyspec/changes/add-monad-thread/specs/horizon/spec.md
- .reffy/reffyspec/changes/add-monad-thread/specs/inheritance/spec.md
- .reffy/reffyspec/changes/add-monad-thread/tasks.md
A real push would be refused: it deletes more than 5% of the project's remote documents. Add --force to override.
```

Remote document counts after the forced prune: `lasm-v1` 297, `nuveris-v1` 1283.
