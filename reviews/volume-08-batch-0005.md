# Volume 08, Batch 0005 — Chapters 0391 to 0400 — first reading

**This file was written by the repair phase that applied the reading, for the reason Batch 0004's is: the review reached the repair as a run log, `logs/` is gitignored, and a review the next run cannot inherit is not a review. It is a record of what that reading found and of what was done about it, and it is not the review itself and cannot be mistaken for one.**

**Not certified as independent, and the reason has not changed in eight attempts.** The gate printed `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent` at the top of `logs/batch-0005.review.log`, and the run that produced the findings was asked for findings with no instruction to be agreeable, which is closer to independence than the fallback has ever come and is still not certified, because the run that inherited the log is not the run that wrote it. `state/phase-ledger.json` reads `phase-000-bootstrap` and `planned` at more than twenty phases out of date, which is open item 43, and the ledger that should have identified the reviewing run is the reason no entry in this register can be traced to a run.

## What the phase did

Wrote `chapters/volume-08/chapter-0391.md` to `chapter-0400.md`, which completed `outline/volume-08.md`. Updated `state/{current,batch-summary,chapter-summaries,character-state,continuity,open-threads}.md` and archived the prior `current.md` header. **Created no next prompt, and said so in `state/current.md` in its own words rather than leaving it implicit.**

## Locks that hold, verified mechanically

- **Zero question marks** across all ten chapters, which is the count-of-askings lock under both readings this project has held: no question put to a person, and no imperative that draws an answer. Seven askings, unmoved.
- **Zero calendar month names, zero weekday names, zero `this year`, zero `schedule`, zero `register`, zero modal `may`**, all as the card file and `outline/volume-08.md` require. Two weekday names went into first drafts and were cut before anything was measured.
- **The male-lead floor of three is met**: 0392 and 0398 carry Marek Kest as an absence with a cost named in another character's mouth, 0399 in person with his want in his own voice.
- **Chapter 0400 delivers the volume's stated close** and nothing else: a person who is ready and is not told what she is standing ready for, and a last line of *nothing is asked of anybody*.
- Prose is finished, scene-complete fiction. No meta text, no duplicated paragraphs, no new final enemy, and the planned ending is untouched: still Volume 12, still the local hearing.

## Findings, in severity order, and what happened to each

**1. `chapter-0399.md` contradicted itself on who the clerk was, and merged two people the state layer has kept apart for eight volumes. BLOCKER, APPLIED.**
The seventh paragraph said the woman who told Marek the thing *has not come back and has not sent for it and is not going to*. The twenty-seventh had the woman who keeps the ground floor say *I am the one who put it there. I have not slept properly since I did it.* Either the ground-floor woman is the clerk of about fifty-five, which makes the seventh paragraph false, or she is a separate person, which the chapter never says. She is a separate person: the clerk keeps minutes nineteen years in a room about four hundred yards off the old river road (`chapter-0370.md:5`, `chapter-0392.md:5`), and the other has been at the bottom of Marek's stairs about twenty years and takes his rent (`chapter-0399.md:9`). **This is open item 29's standing instruction breaking a ninth time, in a building nobody had thought to check, and item 29's own rule is what repaired it: the page beat the draft, the defect is recorded naming the phase that found it, and no closed chapter was reopened to separate it.** The chapter now says in the paragraph that introduces her that she is not the woman who came, that the other one keeps minutes about four hundred yards off the old river road and has been in that room nineteen years, and that this one has never been inside that building and does not know what was said in it. Her line is now a claim about her own carrying — she knows it did not get heavier because she has had one of her own going about the same length of time — and not about his. Nothing else in the chapter moved, including the want and the refusal to write it.

**2. The same merge was recorded nowhere in the state layer, in three files, as settled. BLOCKER, APPLIED.**
`state/chapter-summaries.md` said she had not slept properly *since she put it in his head*; `state/character-state.md` logged her as the second person keeping a thing with no form on it, without recording that she is distinct from the clerk; `state/batch-summary.md` said a man of thirty-eight *was told a true thing about his own want that was not the name, by a woman who keeps the ground floor of the house he rents*, which is the clerk's line and not hers. AGENTS.md requires a proposed canon change to be recorded rather than silently invented, and this one was the most consequential beat in the batch and was invisible to the next reader. All three are corrected with the wrong wording named beside the right one, and the three people are now named as three in the ledger.

**3. `chapter-0399.md:7` was wrong by eight weeks. HIGH, APPLIED.**
*A week ago a clerk came the whole of the distance to this room.* That visit is Chapter 0390, the second day of the second week of the eleventh month. Chapter 0399 is the fourth day of the third week of the first month of the seventh named year. A month in this calendar is four weeks, so the interval is **nine weeks**. Corrected on the page and in the three state files that carried it.

**4. `chapter-0392.md:5` was wrong by one week. MEDIUM, APPLIED.**
*A week ago she came the whole of the distance from that room to a rented room at the other end of it.* Chapter 0390 is the second week of the eleventh month and Chapter 0392 is the fourth week of the eleventh month. It is a fortnight. Corrected on the page and in the chapter summary.

**5. `chapter-0400.md:3` and `:5` were wrong by thirteen weeks. MEDIUM, APPLIED.**
*The fourth of the four came out onto that counter at the fourth hour four weeks ago*, and *the four weeks since the fourth of the four things came out onto the wood have not touched it.* That event is Chapter 0383, the fourth day of the third week of the ninth month. To Chapter 0400's position it is **seventeen weeks**. Both corrected.

**6. `chapter-0391.md` and `chapter-0400.md` had an arithmetic that does not add up, and 0400 inherited it. MEDIUM, APPLIED.**
Chapter 0391 moves a box four inches along a counter and then sets it down an inch short of where it had been, and then says in three separate places that this leaves it *a quarter of an inch* forward. Four inches out and one inch back leaves three inches. **In a volume whose whole method is exact small figures, a number that does not add up is not a poetic choice, it is a mangled figure, and it had already been copied into four state files.** The page now says three inches in all three places in 0391 and in the one place in 0400 that stated it, and 0400's *three months ago* became *ten weeks ago*, because ten weeks stand between the two chapters and a month is four weeks. All four state files corrected.

**7. No next-phase prompt was created. MEDIUM, DELIBERATE AND NOW REPAIRED.**
The writing phase closed the volume, wrote into `state/current.md` that it had created no next prompt, and stopped. `scripts/novel_runner.sh` selects a phase by walking for `PROMPT.md` in directories without a terminal marker, so there was no artifact for the pipeline to dispatch on. AGENTS.md asks for exactly one volume-close prompt once a volume completes. The reasoning was on the record and the gap was real. **`workspace/volume-08/volume-close/PROMPT.md` now exists and is the only next phase, and the header in `state/current.md` points at it.**

**8. No reviewer has checked this batch. MEDIUM, ADDRESSED IN FORM AND NOT IN FACT.**
`reviews/` held `volume-08-batch-0003.md` and `-0004.md` and no `-0005.md`. The gate failed open and the writing agent reviewed itself. AGENTS.md's quality gate requires *a reviewer has checked the result.* **This file discharges that requirement in form only, and the file says so on its own first line. The gate has now been asked the same question eight times and has answered it the same way every time, and not one entry in this register can be certified independent.** The gate is carried as one of the four debts and the standing claim is carried as item 82.

**9. The rolling state files are growing without bound. LOW, CARRIED AND NOT ACTED ON.**
`continuity.md` 273 KB, `batch-summary.md` 248 KB, `character-state.md` 186 KB, `open-threads.md` 186 KB, `chapter-summaries.md` 107 KB, and `state/archive/current-md-superseded.md` has reached 1,214 lines of superseded headers. AGENTS.md asks for summaries *compact and useful for the next batch*, and `outline/volume-08.md`'s own eighth craft rule names the remedy: consolidate by reference into `state/archive/` at a volume boundary. **This repair did not consolidate, because consolidating in the middle of a batch's own repair is how a state layer loses the row that told it to consolidate.** Carried as item 84 for the close, which is the phase the rule names.

**10. `state/phase-ledger.json` still reads `phase-000-bootstrap`, status `planned`. INFORMATIONAL, NOT EDITED.**
Untouched since initialization, across eight volumes. Controller file, correctly left alone by the writer, and unusable as a phase indicator. Carried as item 43.

## Two further findings the review did not make, and the standing rule they produce

**Eleven. Chapter 0397 said *a fortnight* where eight weeks stand, the same defect as findings three, four and five, in a chapter the review opened and did not flag.** The knock on that door is Chapter 0389, the second day of the first week of the eleventh month; Chapter 0397 is the second day of the first week of the first month of the seventh named year. Corrected. **Findings three, four, five and eleven are one finding, and the finding is that this project measures sentence length, emphasis, word counts and lifted phrases, and has never once measured an interval against the calendar — and the calendar is the only number in the volume a reader can check with a pencil on paper.** Item 80 is the rule: every interval is a seven-day step from the chapter before it unless the chapter says otherwise, and it is measured before it is written.

**Twelve. Chapter 0391 says a woman at that counter said a third thing out loud to her colleague *a fortnight ago*, and Chapter 0400 says she has said a third thing out loud to her *in about a month*. Those are eight weeks apart and the two chapters do not reconcile. NOT REPAIRED, AND DELIBERATELY.**
Neither figure can be derived from the page: neither week is depicted in any chapter, so a repair would be choosing between two loose recollections with nothing to decide between them, and **picking one is how item 31 and item 25 of this project were created.** It is carried as item 83 with both readings named. **A repair that guesses is worse than a defect that is recorded.**

## What the repair changed, in one place

**Five chapters: 0391, 0392, 0397, 0399 and 0400, and 60 words across the batch.** No event moved. No date in the calendar moved. The count of askings did not move and no question mark entered any of the ten files. No month name, no weekday name, no *this year*, no *schedule*, no *register* and no modal *may* entered any of them. The planned plot is untouched and the ending of record is unchanged. The next-phase prompt was created. The review was filed where a later run can inherit it.
