# Current State

Current phase: phase-001-outline (writer pass re-run, review findings applied; the existing Volume 01 and Batch 0001 outlines were audited against `OUTLINE_GUIDE.md` and repaired rather than rewritten. The outline work itself is finished, but the controller-level dispatch blockers below still decide which prompt actually runs next)

Current volume: 1

Current batch: 1 (`outline/batches/volume-01-batch-0001.md` cards exist; no prose drafted)

Last completed chapter: none

Last batch summary: none (no batch prose has been written)

## Read this first: who owns Chapters 1–10

- Chapters 1–10 belong to the writer run driven by `workspace/volume-01/batch-0001/PROMPT.md`, with `outline/batches/volume-01-batch-0001.md` as the authoritative card source.
- If you were dispatched from a planning-phase prompt (`phase-000-bootstrap`, `phase-001-outline`, `phase-002-batch-plan`) while those cards already exist, do not draft chapter prose. The cards are the plan; the batch prompt is the writer's instruction. Re-drafting Chapters 1–10 from a planning prompt produces duplicate prose and discards the canon locks the batch prompt carries.
- Never edit `state/phase-ledger.json`. Nothing in `scripts/` or `.github/` reads or writes it, so it can never be a source of truth, and `restore_controller_files` does not restore it, which means an edit there would survive and be committed.
- Findings in `logs/*.review.log` are self-reported by a writer run rather than produced by an independent reviewer. Check each one against the files before acting on it, and change only what the evidence supports.

Bootstrap deliverables present:

- `bible/premise.md`, `bible/world.md`, `bible/characters.md`, `bible/power-system.md`, `bible/themes.md`, `bible/terminology.md`, and an indexed `bible/README.md`.
- `outline/series.md` with the premise, protagonist spine, relationship architecture, central mystery, antagonist ladder, power stages and costs, distinctiveness, final conflict and choice, and all twelve volume arcs.
- `outline/ending.md` with the fixed ending, the Covenant of Many Seals, relationship resolutions, and the final-volume chapter plan.
- `outline/volume-01.md` and `outline/batches/volume-01-batch-0001.md` for Chapters 1–10.

Phase-001-outline pass (audit and repair, no prose): both files already carried the full required field set, so neither was rewritten. The audit confirmed all 13 required volume fields, all 11 required batch fields, and all 11 labelled fields on each of the ten chapter cards, plus the `### Chapter NNNN` header that supplies the twelfth line of the guide's card block, plus all ten of `OUTLINE_GUIDE.md`'s opening-chapter requirements. Four concrete gaps were repaired:

- `outline/batches/volume-01-batch-0001.md` gained an explicit five-beat shape — Batch beginning (1–2), Batch escalation (3–6), Batch midpoint (3–5), Batch climax (7–10), Batch aftermath (9–10) — plus a pressure-rotation line for the ten chapters.
- The named Volume 01 support cast is now bound to specific chapters in both files (Ivet Sarn, Hallis Dren, Sivra Oris, Ostyn Vare, Ruhl Dunnet, Odile Fenn), so a later batch cannot substitute an invented clerk, foreman, constable, or water-office clerk for a fixed one with a want and a refusal.
- A power-boundary note now states that Magistrate Rell's and the Mosswake court's own interim and closed-door orders are the court's authority, not Marek's Stage 2 exception. The word "exception" in the batch belongs only to the invalid draft he conceals in Chapter 5. The ambiguous "private exception" phrasing in the Chapter 6 and Chapter 8 cards and in two lines of `outline/volume-01.md` was changed to order language.
- `outline/volume-01.md` gained a support-cast placement map and a volume pressure rotation, and Ivet Sarn's later duty to explain her own delay is placed in Chapters 11–18.

The four canon values fixed by `workspace/volume-01/batch-0001/PROMPT.md` — "the present holder" with the article, the Chapter 8 panel's first line, the record the reading is taken against, and the reading's cost — were re-verified as unchanged in both files. The Chapter 8 panel still matches `state/continuity.md` word for word.

Review of that pass, applied in this fix pass: every finding was checked against the repository before anything changed, and the edits stayed inside this file, `state/continuity.md`, `state/open-threads.md`, `state/character-state.md`, and the batch handoff prompt. Three of the five needed a real change rather than a corrected description: the dispatch exposure is one phase instead of three because `workspace/phase-000-bootstrap/.done` exists and is tracked in git, the self-audit above counted twelve batch fields where the guide lists eleven, and the surname collision between Sivra Oris and Seryn Oris is now pinned in canon and in the batch prompt. The other two — the duplicate-prose and ledger risk in `phase-002-batch-plan`, and the fact that review runs as a writer rather than as a reviewer — needed better statements rather than different ones, because only the controller can remove either. One consequence is worth carrying forward: nothing reads the ledger, so it is permanently stale. No outline card, story beat, or canon value was changed, and the planned plot is untouched.

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

1. **The batch prompt still will not be dispatched next, and the exposure is one phase rather than three.** `scripts/novel_runner.sh:24-31` walks `find workspace -name PROMPT.md -type f | sort` and takes the first directory holding neither `.done` nor `.blocked`. `workspace/phase-000-bootstrap/.done` exists and is tracked in git, so bootstrap is already skipped and will not consume a dispatch. This phase receives `.done` at `novel_runner.sh:240` after its review and fix passes, which leaves `workspace/phase-002-batch-plan` as the next dispatch. The single controller action that restores the handoff is to mark `workspace/phase-002-batch-plan` done, or to correct its prompt, not to mark the earlier phases.
2. **`workspace/phase-002-batch-plan/PROMPT.md` is that next dispatch, and it would re-draft Chapters 1–10 as prose and would instruct the writer to update the phase ledger.** Its line 3 says to write Chapters 1–10 as complete finished scenes and its line 5 says to update the phase ledger. It carries no authoritative-source or canon-lock section, so a re-draft from it can silently reintroduce the Chapter 8 card contradictions that were just repaired, and two writers would produce the same ten chapters. Its ledger instruction also conflicts with the agent rule that `state/phase-ledger.json` is controller-owned, and `restore_controller_files` (`novel_runner.sh:115-122`) restores only the seven controller files, not the ledger, so an obedient writer's ledger edit would be committed. The prompt belongs to another phase and was not edited from here. Instead, the ownership rule is now written at the top of this file and in `state/open-threads.md`, both of which every writing phase is instructed to read, so a writer that follows its own instructions still cannot produce a duplicate batch or touch the ledger. The dispatch order itself remains controller territory.
3. **Two earlier phases can rewrite the authoritative card file.** `phase-001-outline` and `phase-002-batch-plan` both write `outline/batches/volume-01-batch-0001.md`. The card contradictions found in review (the Chapter 8 panel naming Tavi after the ruling voided her debt, and the missing article in the quoted substituted phrase) were corrected in the card file, and the batch prompt now carries the same values as canon so a re-run cannot silently reintroduce them, but only a controller can stop the rewrite itself.
4. **The review step does not run as a reviewer.** `scripts/novel_runner.sh` and `.github/workflows/novels.yml` both pass `--agent novel-reviewer` to `opencode run`, which only accepts primary agents, while `.opencode/agent/novel-reviewer.md` declares `mode: subagent`. The runner falls back to the default writer agent, so the review log was produced by the writer with edit access, "do not edit files" is only advisory, and the model probe never probes the reviewer. The same agent file also sets `bash: deny`, so it could not inspect the diff it is asked to review, and review output goes only to gitignored `logs/`, so no `reviews/volume-01/*.md` artifact is ever produced. Confirmed from inside the phase-001 review run itself: that run executed under the writer system prompt, so its findings were self-reported. `novel_runner.sh:223` then gates the fix pass on a keyword match against the review log (`finding|problem|issue|contradiction|repetition|outline-like|meta`), which is why a second writer pass is now applying those findings. Treat every review log as a set of claims to verify, never as authority.
5. **`PHASE_SYSTEM.md` describes a ledger-driven selector that does not exist.** The documented selector reads `state/phase-ledger.json` with volume, batch, chapter range, status, attempts, lease expiry, and base commit; the implementation scans prompt files, and the ledger has none of those fields. Nothing in the repo reads or writes the ledger, and `PHASE_SYSTEM.md` is controller-owned. The consequence to plan around is that the ledger is permanently stale: it still reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0`, `range: null`, and `actualModel: null` even though this phase has completed its writer and review passes. Treat this file and the directory markers, not the ledger, as the record of what has actually happened, and do not try to correct the ledger from a writing phase. `MODEL_VERIFICATION.md` and `logs/models.log` have no ledger backing either.

Until at least item 2 is resolved by the controller, treat `workspace/volume-01/batch-0001/PROMPT.md` as the only prompt that should run for Chapters 1–10, and follow the ownership rule at the top of this file if a planning prompt is dispatched instead.
