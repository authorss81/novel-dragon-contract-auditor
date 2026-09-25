# Batch Summaries

Rolling long-term memory, one entry per completed batch, newest last. A later batch reads this whole file plus `state/current.md` and `state/continuity.md`; keep each entry short enough that the file stays readable in full.

No batch prose has been written yet.

## Format for each entry

`### Volume NN, Batch NNNN (Chapters X–Y) — <short title>`

Then, in this order:

- **Goal and outcome:** what the batch set out to do and what actually happened, in two or three sentences.
- **New canon:** only facts that change the world, the power rules, or a character's standing. Do not restate the cards.
- **Costs and consequences:** what Marek paid physically, materially, or relationally, and what remains unpaid.
- **Carried forward:** the open threads this batch advanced, and the exact question the next batch inherits.

Do not put scene description, prose excerpts, or chapter-by-chapter retellings here. Per-chapter detail belongs in `state/chapter-summaries.md`.
