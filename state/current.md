# Current State

Current phase: phase-001-outline (re-run and completed; the existing Volume 01 and Batch 0001 outlines were audited against `OUTLINE_GUIDE.md` and repaired rather than rewritten. Controller-level blockers below still prevent the documented handoff from happening on the next dispatch)

Current volume: 1

Current batch: 1 (`outline/batches/volume-01-batch-0001.md` cards exist; no prose drafted)

Last completed chapter: none

Last batch summary: none (no batch prose has been written)

Bootstrap deliverables present:

- `bible/premise.md`, `bible/world.md`, `bible/characters.md`, `bible/power-system.md`, `bible/themes.md`, `bible/terminology.md`, and an indexed `bible/README.md`.
- `outline/series.md` with the premise, protagonist spine, relationship architecture, central mystery, antagonist ladder, power stages and costs, distinctiveness, final conflict and choice, and all twelve volume arcs.
- `outline/ending.md` with the fixed ending, the Covenant of Many Seals, relationship resolutions, and the final-volume chapter plan.
- `outline/volume-01.md` and `outline/batches/volume-01-batch-0001.md` for Chapters 1–10.

Phase-001-outline pass (audit and repair, no prose): both files already carried the full required field set, so neither was rewritten. The audit confirmed the 13 required volume fields, the 12 required batch fields, and all 12 fields on each of the ten chapter cards, plus all ten of `OUTLINE_GUIDE.md`'s opening-chapter requirements. Four concrete gaps were repaired:

- `outline/batches/volume-01-batch-0001.md` gained an explicit five-beat shape — Batch beginning (1–2), Batch escalation (3–6), Batch midpoint (3–5), Batch climax (7–10), Batch aftermath (9–10) — plus a pressure-rotation line for the ten chapters.
- The named Volume 01 support cast is now bound to specific chapters in both files (Ivet Sarn, Hallis Dren, Sivra Oris, Ostyn Vare, Ruhl Dunnet, Odile Fenn), so a later batch cannot substitute an invented clerk, foreman, constable, or water-office clerk for a fixed one with a want and a refusal.
- A power-boundary note now states that Magistrate Rell's and the Mosswake court's own interim and closed-door orders are the court's authority, not Marek's Stage 2 exception. The word "exception" in the batch belongs only to the invalid draft he conceals in Chapter 5. The ambiguous "private exception" phrasing in the Chapter 6 and Chapter 8 cards and in two lines of `outline/volume-01.md` was changed to order language.
- `outline/volume-01.md` gained a support-cast placement map and a volume pressure rotation, and Ivet Sarn's later duty to explain her own delay is placed in Chapters 11–18.

The four canon values fixed by `workspace/volume-01/batch-0001/PROMPT.md` — "the present holder" with the article, the Chapter 8 panel's first line, the record the reading is taken against, and the reading's cost — were re-verified as unchanged in both files. The Chapter 8 panel still matches `state/continuity.md` word for word.

Added in the final bootstrap pass: the series-outline distinctiveness section and a final-conflict summary; worked power-system examples and reading limits that matter in court; a named Volume 01 support cast with fixed ages and the Venn term arithmetic; concrete work-place anchors (Inheritance Desk, source-leaf cabinet, Mosswake Roll Court, Reed Cut water office, public reading tables); new terminology entries and prose usage rules.

Active threats:

- Tavi Venn's winter-seed debt and the Venn field remain under the copied precedent until the local ruling is publicly used.
- The Dunn household may be named as guarantor by the harmful public-necessity sentence.
- Corvin Dray's seal-broker network can turn local corrections into portable precedent.
- Pell Vey and a sealed First Seat instruction may place the case beyond Mosswake.
- The batch outline plans a formal audit filing as the Chapter 10 endpoint; nothing has been filed in the absence of prose. Its recognition and scope are the first Volume 2 pressure.

Active promises:

- Resolve the Venn case for Tavi and Mara while showing the cost of the ruling's copied language.
- Give Nell a visible exit clause and preserve her independent work.
- Follow the red-thread clue from the Venn file to Ilyra Kest's erased record.
- Escalate the First Seat instruction without revealing the full Cinder Clause origin too early.

Long-range planned structure (not an active promise at this stage):

- Establish the later mixed Roll Assembly and succession crisis without changing the planned ending.

Current relationship pressure: Marek and Tamsin are professional colleagues whose evidence is becoming indispensable; Marek's secrecy damages trust, and Tamsin's independent preservation of copies challenges his assumption that he should control disclosure. Nell resents protective secrecy. Pell remains a trusted-looking supervisor whose procedural preference conceals institutional complicity.

Current power state: Stage 0 Clerk's Eye at the opening. Marek can compare records and question witnesses but has no independent authority, valid exception, counter-seal, or magical reading. The first unstable Seam-Sight and the first Roll-Answer are planned only after he exercises the limited Venn audit authorized in Chapter 7 at the Chapter 8 rehearing; the reading is shallow and leaves fatigue, counterpressure, an ash taste, a headache lasting into the next day or two, and a temporary inability to lie about one named obligation. No Stage 2 power appears in Volume 1.

Next phase: the writer run for Chapters 1–10, driven by `workspace/volume-01/batch-0001/PROMPT.md`. That prompt names `outline/batches/volume-01-batch-0001.md` as the authoritative card source and fixes four values as canon so a re-run of an earlier planning phase cannot silently change them: the article in "the present holder," the Chapter 8 panel's first line as `Named: the present holder of the Venn field.`, the record the Chapter 8 reading is taken against, and the reading's cost. The previous repair note described the prompt and the card file as duplicates; that was a misreading and has been resolved. No additional phase prompt was created, and none should be until batch 0001 finishes.

Planning references: `outline/volume-01.md`; `outline/batches/volume-01-batch-0001.md`; `outline/series.md`; `outline/ending.md`.

State file map: `state/current.md` (this file), `state/continuity.md` (canon), `state/open-threads.md` (threads and blockers), `state/chapter-summaries.md` (per chapter), `state/batch-summary.md` (per batch), `state/character-state.md` (per principal). `state/phase-ledger.json` is controller-owned and is never written by a writing phase.

## Open blockers requiring a controller or maintainer decision

These are recorded here because every writing phase reads this file. None of them can be fixed from a writing phase, and none may be fixed by editing a controller file.

1. **The batch prompt will not be dispatched next.** `scripts/novel_runner.sh` selects the first `PROMPT.md` directory lacking `.done`/`.blocked`, in sorted order. All four prompt directories are currently unmarked, so the next three dispatches re-run `phase-000-bootstrap`, then `phase-001-outline`, then `phase-002-batch-plan` before reaching `volume-01/batch-0001`. Bootstrap re-runs also get the planning timeout rather than the batch timeout. Fixing this means marking the three earlier phases done or changing the selector, which is controller territory.
2. **`workspace/phase-002-batch-plan/PROMPT.md` would re-draft Chapters 1–10 as prose and would instruct the writer to update the phase ledger.** If it is dispatched before batch 0001, two writers produce the same ten chapters. Its ledger instruction also conflicts with the agent rule that `state/phase-ledger.json` is controller-owned, and `restore_controller_files` does not restore the ledger, so an obedient writer would have that edit committed. The prompt belongs to another phase and was not edited here.
3. **Two earlier phases can rewrite the authoritative card file.** `phase-001-outline` and `phase-002-batch-plan` both write `outline/batches/volume-01-batch-0001.md`. The card contradictions found in review (the Chapter 8 panel naming Tavi after the ruling voided her debt, and the missing article in the quoted substituted phrase) were corrected in the card file, and the batch prompt now carries the same values as canon so a re-run cannot silently reintroduce them, but only a controller can stop the rewrite itself.
4. **The review step does not run as a reviewer.** `scripts/novel_runner.sh` and `.github/workflows/novels.yml` both pass `--agent novel-reviewer` to `opencode run`, which only accepts primary agents, while `.opencode/agent/novel-reviewer.md` declares `mode: subagent`. The runner falls back to the default writer agent, so the review log was produced by the writer with edit access, "do not edit files" is only advisory, and the model probe never probes the reviewer. The same agent file also sets `bash: deny`, so it could not inspect the diff it is asked to review, and review output goes only to gitignored `logs/`, so no `reviews/volume-01/*.md` artifact is ever produced.
5. **`PHASE_SYSTEM.md` describes a ledger-driven selector that does not exist.** The documented selector reads `state/phase-ledger.json` with volume, batch, chapter range, status, attempts, lease expiry, and base commit; the implementation scans prompt files, and the ledger has none of those fields. Nothing in the repo reads or writes the ledger. Documentation and implementation disagree, and `PHASE_SYSTEM.md` is controller-owned.

Until at least items 1 and 2 are resolved by the controller, treat `workspace/volume-01/batch-0001/PROMPT.md` as the only prompt that should run for Chapters 1–10.
