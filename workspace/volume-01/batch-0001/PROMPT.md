Read in this order before writing: `AGENTS.md`, `NOVEL_SPEC.md`, `bible/terminology.md`, `bible/power-system.md`, `bible/characters.md`, `bible/world.md`, `bible/themes.md`, `outline/ending.md`, `outline/series.md`, `outline/volume-01.md`, `outline/batches/volume-01-batch-0001.md`, then `state/current.md`, `state/continuity.md`, `state/open-threads.md`, `state/batch-summary.md`, `state/character-state.md`, and `state/chapter-summaries.md`.

This is the first batch. No previous chapter prose exists, so there is no voice window to read. Use the bible and state as long-term memory.

## Authoritative source

`outline/batches/volume-01-batch-0001.md` is the single source of truth for Chapters 1–10. It already contains the batch goal, midpoint, climax, and one card per chapter with POV, location, immediate goal, resistance, information revealed, action or decision, emotional change, power or resource change, continuity fact, ending type, and next-chapter pull. Do not restate, summarize, or re-derive those cards in this prompt, and do not substitute a different plan. If a card and a bible file appear to disagree, the card wins for that chapter and the conflict is recorded in `state/continuity.md` as a proposed canon change.

Two earlier planning phases (`phase-001-outline` and `phase-002-batch-plan`) can still be dispatched and can rewrite that card file, so four specific values are fixed here as canon for this batch. If the card file disagrees with any of them on the page, this prompt wins and the discrepancy is recorded in `state/continuity.md`:

- The substituted phrase is always “the present holder,” with the article, quoted verbatim from `bible/terminology.md`. Never “present holder” alone.
- The Chapter 8 panel reads `Named: the present holder of the Venn field.` The ruling in that same chapter voids Tavi's personal debt, so the reading cannot name Tavi; the reversal works because the file now reaches whoever occupies the field.
- The Chapter 8 reading is taken against the operative filed Venn record after the ruling, including the court's public-necessity gloss, not against the sealed source leaf and not against the fraudulent summary.
- The cost of that reading is fatigue, counterpressure, an ash taste, and headaches that persist into the next day or two. It is not a collapse, and it is not free.

## What this batch must do

Write Chapters 1–10 as complete finished scenes in `chapters/volume-01/chapter-0001.md` through `chapter-0010.md`. Each chapter is one real scene with physical space, work, dialogue, subtext, character thought, and a changed situation at the end. Approximately 2,200–3,200 words per chapter is a guide, not a quota. Never pad, never split a finished scene to hit a number, and never write an outline, list of beats, or status summary in place of prose.

The batch's shape:

- Chapters 1–5: ordinary work, the field visit, the second household, Pell's refusal, and the trust break with Nell and Tamsin.
- Chapters 6–10: the public rehearing, the ruling and its cost, the public reading, Corvin's ledger and arrest, and the formal audit request filed into Chancery custody.

## Hard mechanics for this batch

- Marek performs no magic in Chapters 1–7. He is a Stage 0 Clerk's Eye: comparison, witness work, dates, ink, seal pressure, and who was in the room.
- The one Roll-Answer appears in Chapter 8, after the limited audit authorized in Chapter 7 has actually been exercised at the rehearing, after the ruling, and at the cost set out in the Authoritative source section above. It is exactly three lines and reports only the current legal effect of the operative filed record, including the court's own public-necessity gloss. Use the wording in the card. Chapter 9 must show the cost still being paid: Marek is tired, tastes ash, and has the headache, and he cannot lie about one named obligation.
- No valid exception, counter-seal, mixed warrant, true-name reading, Roll Assembly, or Stage 2 ability appears anywhere in this batch. The invalid draft exception in Chapter 5 is a document that cannot be used, and it is evidence of Marek's flaw rather than a power.
- The court's public-necessity sentence must appear verbatim from `bible/terminology.md` and must be the mechanism by which the ruling reaches the Dunn file. The winning ruling is what creates the second vulnerable household.
- Keep Corvin Dray a local criminal and a constrained witness, never the final threat. The sealed First Seat instruction is an administrative form; it does not name Seryn Oris and does not explain who authorized it.
- Two characters share the surname Oris and must never be merged. Sivra Oris is the Reed Cut water keeper and the scale counterparty to the Venn instrument; she speaks at the Reed Cut gate in Chapter 2, within her own competence, and is named again only when the Chapter 8 ruling preserves her gate and navigation duty. Seryn Oris is the off-page First Seat and the final antagonist: she is not present, not named, and not credited with any action in this batch, and the First Seat instruction is her seat's paperwork rather than a personal order. Sivra never answers for the First Seat and never becomes a mouth for a power she does not hold.
- The red-thread-like mark in the copied Venn page is an unexplained clue. Do not identify it as Ilyra's work in this batch.
- No romance begins. Tamsin and Marek stay professional colleagues whose trust is damaged, not repaired by a victory.
- Follow the prose usage rules in `bible/terminology.md`, including the words the narration must avoid.

## After the batch

Update `state/chapter-summaries.md` with two to five sentences per chapter. Update `state/batch-summary.md` with a new entry for this batch using the format already in that file. Update `state/character-state.md` so every principal's entry reports what actually happened on the page. Update `state/current.md`, `state/continuity.md`, and `state/open-threads.md` with the new canon facts, power costs, custody chain, arrested parties, and the audit request now held in higher-office custody. Keep all of these compact enough that a later batch can read the whole files. Do not create a new canon rule without recording it in `bible/` and in `state/continuity.md` at the same time. Never edit `state/phase-ledger.json`, `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, or `opencode.json`; those are controller-owned and are restored from the controller, so an edit there would be committed as your work and discarded later.

Then inspect `outline/volume-01.md`. Chapters 11–50 remain, so create exactly one next directory, `workspace/volume-01/batch-0002/`, with a detailed `PROMPT.md` for Chapters 11–20 and author-facing cards in `outline/batches/volume-01-batch-0002.md`. Do not create any further phase prompt, volume-close prompt, or volume outline.
