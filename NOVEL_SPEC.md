# Novel Specification

Title: The Dragon Contract Auditor
Repository slug: novel-dragon-contract-auditor
Genre: legal fantasy / court mystery
Male lead: A legal clerk who audits dragon contracts
Length target: 620 chapters
Relationship policy: One slow-burn relationship. Decided in the bible phase: Tamsin Rook is the only slow-burn relationship, and it does not begin in Volume 1.
Power rule: Growth must be earned through practice, cost, failure, relationships, and changed decisions. The lead must not become instantly overpowered unless the approved genre premise requires it.

## Premise
A young clerk discovers that dragon contracts are secretly rewriting human inheritance law.

## Ending
The empire accepts a legal system that cannot be controlled by dragon bloodline alone.

## Status
**Two hundred and sixty chapters of finished prose exist, 881,832 words: Volume 01 closed at Chapter 50 (202,117 words), Volume 02 closed at Chapter 100 (184,039), Volume 03 closed at Chapter 150 (176,097), Volume 04 closed at Chapter 200 (148,821), Volume 05 closed at Chapter 250 (144,248), and Volume 06 open and ten chapters in (26,510).** The first five volumes are closed and are not to be reopened. The bible (`bible/`), the series outline (`outline/series.md`), the fixed ending (`outline/ending.md`), the volume outlines (`outline/volume-01.md` through `outline/volume-06.md`) and the batch cards (`outline/batches/`) all exist. Long-form memory lives in `state/`, and the six files there are archives of just under 5 MB in total as last measured: **use `grep -n` to find a heading and read the range under it, and read none of them whole.** `state/current.md` is newest-first and carries a read cap in its header. The five append-only files are newest-at-the-BOTTOM; `state/current.md` is the only one that runs the other way. `stat -c '%s' state/*.md` is the authority on the sizes and they move with every run that changes a state file.

**The live next phase is Volume 06 Batch 0002, Chapters 261–270, the second movement, at `workspace/volume-06/batch-0002/PROMPT.md`; read it before drafting anything, and read the bottom of `state/continuity.md` in the order that prompt names, which begins with the Batch 0001 record. One section now sits at the foot of that file above the ones the prompt names, headed *THE READING A BOUND HAS ONE LOAD-BEARING CLAUSE, AND TWO JOINTS STILL LOOSE, AT CHAPTER 260*, and a writer who intends to hold the sentence bound should read it, because it says which clause of the pinned reading the batch's compliance actually rests on.** The batch behind it is closed and is not to be re-run: `workspace/volume-06/batch-0001/` holds a `.retired` marker and `outline/batches/volume-06-batch-0001.md` holds its closing section.

**Two standing cautions carried into that prompt.** A review of Batch 0001 has been read and repaired; its findings are persisted at `reviews/volume-06-batch-0001.md` rather than in `logs/`, which is gitignored, and the repair record is the newest section of `state/current.md`. And the review gate is **not running an independent reviewer** — the agent it dispatches declares itself a subagent, the runtime refuses that for a top-level run, and the review was in fact produced by the writing agent. That is a controller-owned defect, it was not fixed here, and no review in this project may be described as independent until a controller owner changes it.
