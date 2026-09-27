# Review: Volume 07, Batch 0002, Chapters 311 to 320

Phase reviewed: the writing run that took `workspace/volume-07/batch-0002/PROMPT.md`, commit `f33fc14`.
Reviewed: 2026-09-27, against the committed phase changes, on the run's own report and on the files.
Repair phase: the run that read `logs/batch-0002.review.log`, re-measured the ten files and this repository's state layer, and applied what could be applied. Its record is the newest section of `state/current.md` and the newest section of `state/batch-summary.md`.

This file is persisted here because `logs/` is gitignored. The reviewer's own output was never committed, and a review that exists only in an untracked log is a review the next run cannot inherit. It is also the artifact the review itself found missing: `reviews/` held Volume 06 Batches 0001 and 0002 and nothing for any chapter of Volume 07, and the batch's own closing record said so in terms — *A self-audit is not a review. A second pass by the writing hand is not a second reading.*

## The finding that governs every other finding here

**The review gate is not running an independent reviewer, and this review is not independent.**

`logs/batch-0002.review.log:1` reads `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`.

This is the same structural fault `reviews/volume-06-batch-0002.md` records for Volume 06, and it is unchanged. `.opencode/agent/novel-reviewer.md` declares `mode: subagent`; the runtime refuses a subagent for a top-level run and falls back to the default agent, which is the writing agent. The frontmatter sets `edit: deny` and `bash: deny`, and the fallback runs with both allowed, so *No files edited* at line 920 of that log was prompt text and not a permission. **This file is written by that same fallback, and it says so rather than claiming a second reading it did not get.**

**Consequence for the record, and it is the useful half:** the agent that graded the prose was the prose, and it returned eight findings, four of which the writing hand had itself declared and left open. It did not certify a clean batch. A self-review that catches the writing agent leaving a defect on the page is worth more than nothing and less than a review.

**The fix is one line of frontmatter, `mode: primary`, or a real subagent dispatch. `.opencode/agent/` and `scripts/` are controller-owned, neither was opened, and this needs a controller owner. It is still the first item in the list and it is now three batches old.**

## Process compliance — clean, and verified rather than inherited

- The card file `outline/batches/volume-07-batch-0002.md` (11:32:04) predates every chapter file (11:40–11:43). Outline before prose held.
- Exactly one next-phase prompt was created, `workspace/volume-07/batch-0003/PROMPT.md`. No `batch-0004`.
- No controller file was touched: not `scripts/`, not `.github/workflows/`, not `.opencode/agent/`, not `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, `state/phase-ledger.json`.
- No chapter outside this batch was opened by the writing run, and the four this repair opened are named individually below, each with the reason it was opened.
- The ten word counts reproduced exactly as the run printed them: 1,907 / 1,608 / 1,588 / 1,489 / 1,421 / 1,287 / 1,396 / 1,358 / 1,452 / 1,426, total 14,932, measured per file with `sed 's/[[:space:]]*$//' file | wc -w` and summed one file at a time.
- The emphasis runs, the `no form` counts, the question marks and the locks were all inside their stated bounds on the files as written.

**One thing not to misread as a fault.** `workspace/volume-07/batch-0002/` carries `.wip-conflict` and no `.done`, so the runner's sorted walk selects this phase again and not Batch 0003. That is correct mid-phase behaviour: `scripts/novel_runner.sh:302` writes `.done` on the phase directory at the end, after the review and the repair, and `:303` clears `.wip-conflict`. The runner is the selector and `state/phase-ledger.json` is not, and the ledger still reads `phase-000-bootstrap` more than twenty phases out of date. **The ledger is a controller file, no phase may edit it, and an authoritative-looking file that is simply wrong is a standing trap that this review can name and cannot mend.**

## The eight findings the review returned, and what this repair did with each

### 1. The handoff is 1.87 MB against a stated bound of about 940,000, and it compounds at about 100 KB a batch. **Acted on. This was the one that could cost the gate.**

Measured with `wc -c` over the six rolling files in `state/` and summed: **1,225,227 bytes**, which is 130% of the bound. The cause was named in the files themselves and the remedy was named four times and not performed, because the phases that named it recorded that consolidation is not a writer's decision. **It is a review-repair decision and the review repair has now taken it.**

Five blocks were moved verbatim into `state/archive/`, all of them closed material and all of them under the rule the archive already states — *a rolling file holds the open volume, the two previous batches, and the standing locks; a closed volume is read here*:

| Moved | From | Bytes | Now in |
|---|---|---|---|
| The whole of Volume 06's record: plan, notes, outline repair, five per-batch records, three review repairs, the close, the close's notes | `state/batch-summary.md` | 121,402 | `state/archive/batch-summary-volume-06.md` |
| The Volume 06 thread ledger, outline rows to the close's three rows | `state/open-threads.md` | 163,797 | `state/archive/open-threads-volume-06-ledger.md` |
| The Volume 06 outline of record, its repair, the close, and the review repair of the close | `state/continuity.md` | 72,512 | `state/archive/continuity-volume-06-outline-and-close.md` |
| The two cast snapshots at Chapter 300 | `state/character-state.md` | 40,161 | `state/archive/character-state-chapter-300.md` |
| The remainders of the fifty per-chapter entries for Chapters 251 to 300, on the treatment Chapters 181 to 250 already have | `state/chapter-summaries.md` | 108,211 | `state/archive/chapter-summaries-chapters-251-to-300.md` |

Each rolling file carries a pointer at its head, a pointer in place at the cut, and a row in `state/archive/README.md`, which has a new section naming the cause and the rule. **Nothing was edited, summarised, condensed or deleted; each moved block was checked to be present byte for byte in its new file, and each of the fifty chapter entries was checked to reassemble from its two halves.**

**The six rolling files are 773,840 bytes after this repair's last state edit, which is 82% of the bound and leaves about 166,000 bytes of headroom for Batch 0003.** Every later state edit moves that figure and it is re-measured, not inherited.

**What the review did not say and this repair says anyway: the cause was not only growth.** The six files carried roughly 500,000 bytes of Volume 06 and closed-volume material that the archive rule had already retired and that no phase had moved. A writer appending a section to a file that is 130% of its bound is a writer with no room, and the six sections this batch added were about 200,000 bytes of that total.

### 2. Single-sentence paragraphs are the house style at 71% in Chapter 0311 against `AGENTS.md`'s two to six. **Diagnosed, inherited, and not restyled.**

Measured on Chapter 0311 as written: 30 of 42 prose paragraphs hold one sentence. Measured on closed Chapter 0301, which this batch did not write: 24 of 39, or 62%. The pattern is the manuscript's, not this batch's, and `AGENTS.md` asks for natural paragraphs with a one-line paragraph reserved for a deliberate beat, which is a real disagreement between the project's instruction and its three hundred chapters of practice.

**It was not fixed here, and the reason is a rule and not a preference: a review repair that restyles prose across a batch changes voice, and the batch's own closure record is the authority on what its ten chapters were.** Restyling closed prose is a repair item on the manuscript, it needs an owner, and it is now written down as one. Chapter 0311's own paragraphs were cut and re-cut where the repair touched them, and the movement's one-line beats were kept because they are the movement's signature.

### 3. The `about N` tic is the dominant texture at 262 instances in 14,932 words, and the metric that tracks it is blind to the problem. **The blind spot is closed; the prose is inherited.**

The bound in force — *`about nine` is under about eight per chapter on the counted figure, the page figures excluded* — measures the worst single phrase and returns a pass. It cannot see aggregate density, which is what a reader feels. Measured with the review's own case-sensitive method, the ten files carry 34 / 26 / 27 / 27 / 19 / 21 / 29 / 25 / 26 / 28 instances of `about <word or number>`, which is one every fifty-seven words in the first file.

**Two things were done. The measure was added to the standing checks with the reading that sees density, and the reading is now in the next writer's prompt.** A batch is now asked for its aggregate instances per thousand words as well as its worst single phrase, and the figures above are the first measurement of it on this batch. **The prose was not touched, because the density is the manuscript's: the same measure on closed Chapter 0301 returns 27, and the characters in this matter are identified by age and function as a matter of design, which is the one place a `about N` is load-bearing.**

### 4. Emphasis has become texture rather than stress at 12 to 24 markers a chapter. **Partly acted on, and the record corrected.**

True of the batch and inherited: closed Chapter 0301 carries 14 `**` markers. The finding that matters is not the count but the claim beside it — *no run spans a sentence* — which is a real check and returns clean.

**Two figures in the batch's own record did not reproduce, and both are corrected in the place that printed them.** The record prints ninety-six emphasis runs across the ten files; this repair's reading of the files as committed finds **99**, and **101** after its own two added runs, the difference being one run in Chapter 0311 and one in Chapter 0319. Two readings of one method disagreeing by three is the same class of finding as the sentence total that Volume 06's close could not reproduce, and it is recorded rather than argued.

**The craft half of the finding is answered in Chapter 0311 only, and by subtraction rather than by addition: the repair cut one of the chapter's four restatements of the batch's thesis, cut one of its two closing negations, and put the emphasis it did add on the one new line that carries stress.** No chapter was re-emphasised for the sake of a number.

### 5. Chapter 0311's engine is a lecture and its resistance is vestigial. **Acted on. This is the only prose the repair rewrote at length.**

The finding is correct and specific: the border law, the three things in one sentence, *a household is not a person* and *a class is a heading* were each said once to a man who said *Say it* once, and the two figures who could have opposed got a paragraph, a non-answer and an exit.

**What changed, in Chapter 0311, with the scene, the room, the figures, the money and the outcome all as they were.** The man of about thirty-four now puts the question the chapter was avoiding — *Then why is it me you are telling* — and is answered with three concrete reasons and a cost, and the answer is a reason about him and not a fifth statement of the thesis. The woman of about twenty-nine, whose day has passed, now has a book on the shelf behind the counter that would have the answer in it; she is not asked to open it, nothing asks her to open it, and the clerk does not open it. The man of about forty who wants three things put back a year now has the three of them on one sheet. The thesis is stated twice where it was stated four times, the chapter's *I will come back to the third of them* no longer promises a return it does not make, and the closing line no longer repeats Chapter 0319's.

**The locks held and were re-measured after every edit, not once at the end.** The count of askings is seven and did not move; the chapter's own question marks are one and are in a customer's mouth about a sheet; the `no form` frame is five, inside two to seven; the longest sentence is seventy-five words; every emphasis run holds one sentence; the card's five required runs are all still on the page; the House, its seat and its notary are still unnamed; nothing was thanked, sent or resolved; the box under the counter is still not a post. **The chapter is 2,099 words against 1,907, which is above every other file in its batch and inside the project's own ordinary-chapter guidance, and the growth is the resistance the review asked for and nothing else.**

### 6. Two live continuity defects, correctly found, both unrepaired. **Both repaired. This is the finding with the most plot-adjacent content and it needed care.**

**The first is Chapter 0303's date.** The file carried *the year after the year after the year after the year after next* — one year name too many, the sixth year — against its own card, its own chapter summary, the character state and the volume outline, all of which read the fifth name, and against the calendar the outline states, which puts the year boundary between Chapters 0302 and 0303. **Chapters 0301 and 0302 are in the fourth year, 0303 to 0320 in the fifth, and the page now says so in all twenty.** The repair is three words. **It is also a repair to a finished chapter of a completed batch, which the writing run was right not to do and which a review repair may do when the correct value is attested four times over and the defect is a single phrase; it is named here, in the state record, and in the archive of superseded figures, and the chapter's word count is corrected from 1,726 to 1,723 in all three places that printed it.**

**The second is a contradiction between the outline and two closed chapters.** `outline/volume-07.md` dated the question in the second of the eleven books to the ninth month of the year after the year after next. Closed Chapter 0260 and closed Chapter 0295 both date it to the ninth month of the year after next, and closed Chapter 0295 adds that it has been on that shelf *about fifty-eight weeks*, which is fourteen months from the ninth month of the year after next to Chapter 0295's own date and about two months if the outline were right. **The outline was the wrong document, the two closed chapters are self-consistent, and the outline now reads the year after next.** No closed chapter was opened to make this.

**What that unblocked, and it was not small.** The next writer had been told, twice and in strong terms, not to state any elapsed period between the entering of that question and any date in its batch, because two sources were a year apart and a period figure would commit it to one of them. **The two sources now agree, and `workspace/volume-07/batch-0003/PROMPT.md` has been amended to say so and to carry the corrected date, so that the constraint is lifted on the evidence and not by a writer's convenience.** The figure on the page — about fifty-eight weeks, as of Chapter 0295 — is the one a later writer may use, and the record names where it is.

### 7. The review gate has no artifact. **Acted on. This file is the artifact.**

`reviews/` held Volume 06 Batches 0001 and 0002 and nothing else, across thirteen batches and one volume. The batch's summary was candid that a self-audit is not a review, so this was a pending leg rather than a false claim, and it is the leg most likely to be lost if a phase ends early. It is now written, with the fallback named in its first section, which is the only honest way this project can currently write a review file.

### 8. Minor: the phase ledger is stale and the next-phase prompts are inflating. **Named, not acted on, and one of the two cannot be.**

`state/phase-ledger.json` reads `phase-000-bootstrap` more than twenty phases out of date. It is a controller file, the directory walk is the real selector, and no phase may edit it. The prompt inflation — 59,557 bytes for Batch 0002, 80,412 for Batch 0003 — is real and is the same growth the review found in the state layer, in the place a writer controls. **The Batch 0003 prompt was not trimmed, because every paragraph in it is a lock or a figure a later run will need, and cutting a lock to save bytes is a bad trade. It is recorded instead as the second half of the same finding.**

## What this repair found that the review did not, and it is the worst thing in the batch

**The batch re-used about two hundred words verbatim out of Chapter 0310 in Chapter 0314, about two hundred out of Chapter 0313 in Chapter 0319, and twelve whole paragraphs out of Batch 0001's chapters in five of its own, and its own record says the duplication sweep returned zero.**

That last clause is the part that matters. The record is not lying: the duplicate-paragraph test was run inside the batch's own ten files, and inside those ten files there was nothing. **Twelve exactly duplicated paragraphs run across the boundary into the batch that closed, and every one of them has the later file in Batch 0002** — seven paragraphs of Chapter 0320 lifted out of Chapter 0307, two of Chapter 0317 out of Chapter 0308, one each in Chapters 0311, 0313 and 0318 out of Chapters 0303 and 0304. Chapter 0320 is the chapter where the second hand becomes the point of view, and it opens with seven paragraphs lifted whole out of the chapter that introduced him, including the two that say who he is.

Measured on the unit this project names — one distinct forty-word tuple held in two or more distinct files, counted once however many instances hold it, compared at every position and never across a paragraph — the files as committed returned:

- **Sixty-word window, Chapter 0310 against Chapter 0314: 61 distinct tuples**, one contiguous verbatim run of about 120 words. It is the room, the shelf, the eleven books, the table, the chair, the two-foot window, the pane out of it for four years, the four-hundred-yard passage, the cold flags, the rail four feet off the floor, the clerk of about fifty-five, the four thousand entries and the absence of a name in any one of them.
- **Forty-word window, Chapter 0310 against Chapter 0314: 121 distinct tuples**, and **nineteen more between Chapter 0313 and Chapter 0319**, in four blocks: the two things under her table, the line in her own hand, the four lines off the fee board, and the second page with two boxes on it.
- **Exactly duplicated paragraphs across the twenty chapters of the volume: twelve**, and the test that found them is the one the batch ran and reported clean.

**The batch's record claimed both window sweeps at zero, and claimed in a second place that reworking three duplicated paragraphs had closed the forty-word window at the bound and two words lower. Both were false.** The three reworked paragraphs were the heads of four blocks and not the blocks. `reviews/volume-06-batch-0002.md` records the identical class of fault one volume earlier and in the same words — *six of the ten new chapters re-used large verbatim stretches from Batch 0001, and the batch's own duplicate test reported the batch clean* — and the same test returned zero here, because a duplication that runs to the end of a paragraph and stops short of the next is not a duplicated paragraph.

**All of it is repaired, in the later file of every pair, with every fact kept.** Chapter 0314's opening four paragraphs are re-cut and its dating sentence is re-cut; Chapter 0319's four under-the-table paragraphs and its drawer paragraph are reworded; Chapter 0320's seven lifted paragraphs are reworded one for one, including the two that say who the man is; Chapter 0317's passage and its woman of about twenty-six are reworded; and three shorter lifts in Chapters 0311, 0313 and 0318 are reworded, one of which is the movement's own thesis sentence. **The exactly duplicated paragraphs across the volume are now zero. The sixty-word and forty-word windows return zero inside the batch and against the other three hundred and one chapters, at the bound and two words lower. The fifteen-word window returns 135 across the batch's own ten files, against 225 before the repair, and those 135 are the movement's deliberate recurrence: the same room, the same board, the same drawer, the same two boxes, the same calendar strings, and the finding stated in three chapters on purpose.**

**And a third false figure, of the same kind, in the same file.** The record printed the manuscript at 971,515 across three hundred and twenty chapters, as the closed figure plus this batch's ten files. **That arithmetic left Batch 0001's ten chapters out of the manuscript entirely.** Re-measured after this repair: **Chapters 001 to 300 are 956,583; Batch 0001 is 15,443; Batch 0002 is 15,158; the manuscript is 987,184.** The old figure was out by 15,669. The correct figure and the wrong one stand side by side in the two state files that printed the wrong one.

## What checked out

- The count of askings is seven at the start of the batch and seven at the end, and no question mark in the batch is put to a person about a person. After the repair, still seven: Chapter 0311's new question is *Then why is it me you are telling*, which is a person asking a person a question, and it is printed **without a question mark**, in the house form for an asking that is not an asking, and it moves nothing.
- The ten dates step by exactly seven days, every one is in the fifth year, no chapter straddles the year boundary, and after the Chapter 0303 repair the sequence 0301 to 0320 is continuous across it.
- The `no form` frame is carried in all ten chapters, two to seven times each: 5 / 7 / 4 / 4 / 4 / 4 / 3 / 6 / 2 / 4.
- Question marks are sparse and every one is in a mouth: 1 / 1 / 1 / 0 / 2 / 1 / 0 / 0 / 1 / 0, seven in ten files.
- Emphasis: nine of ten files inside 10.3% and 13.1% on joint one and inside 13.0% and 16.6% on joint two, and no run in any file holds more than one sentence. **Chapter 0313 measures 13.12 on joint one under this repair's reading, which is two hundredths over a ceiling the batch's record gives as 13.1, in a file this repair did not edit and whose value was identical before it was touched. Both readings are printed and neither is deleted.**
- The sentence bound holds under this repair's reading and under the batch's: nothing of a hundred words or more and nothing over ninety, the longest sentence in the batch being eighty-three words in Chapters 0316 and 0320 here and eighty-eight in Chapters 0312 and 0314 there.
- Every mechanical check returns zero: punctuation followed by two spaces, a full stop followed by a lower-case word with the emphasis marker in the look-ahead, a marker inside a word, per-paragraph parity on `**`, a last-of-turn dialogue paragraph with an odd quotation count, four consecutive asterisks, an emphasis run spanning a line break or a blank line, card language, month names, weekday names, surnames the locks name, and *this year*.
- The batch invented no named figure, which is thirteen consecutive batches, and the man of about thirty-four, Marn Ottery, Tamsin Rook, the clerk of about fifty-five, the man of about sixty-one, the second hand, the carrier at ninepence and the four hundred blanks are all where the record left them.

## The repair, in one place

**Prose, seven chapters of this batch and one phrase in an eighth, all inside this batch or named:** Chapter 0303's year name; Chapter 0311's resistance, its cut restatement and its cut negation; Chapter 0314's lifted opening, its lifted dating sentence and a clause that was duplicated inside one sentence at its last line; Chapter 0318's two lifted narration clauses; Chapter 0319's four lifted paragraphs and one added emphasis run; Chapter 0320's seven lifted paragraphs and its lifted door-and-step sentence; Chapter 0317's lifted passage and lifted woman of about twenty-six; the clerk's stock answer at Chapter 0313's counter; and the movement's thesis sentence as Chapter 0318's own paragraph.

**Outline, one phrase:** the date of the question in the second of the eleven books, in `outline/volume-07.md`.

**Next-phase prompt, two items:** the ninth and the tenth, both of which told a third writer to leave two defects standing. Both are replaced with what is now true, and the elapsed-period constraint the ninth imposed is lifted on the evidence.

**State, five files archived and six corrected in place, five new sections appended, one header replaced and the old one archived verbatim:** the false zero, the wrong manuscript total, the wrong Chapter 0303 count, the two wrong per-file word lists, and the emphasis-run count.

**Figures after this repair, each with its method, and the method named because the figures are the fragile half:** per file, `sed 's/[[:space:]]*$//' file | wc -w`, one file at a time — **2,099 / 1,608 / 1,589 / 1,493 / 1,421 / 1,287 / 1,393 / 1,360 / 1,467 / 1,441, total 15,158**; Chapters 001 to 300, **956,583**; Batch 0001, **15,443**; the manuscript, **987,184**; the six rolling state files, **773,840 bytes** with `wc -c` over the six and summed.

## What this repair did not do, stated because a phase that tidies is a phase that lies

- **It did not restyle prose.** Findings 2, 3 and 4 are the manuscript's texture, they are measured now, and they are repair items with no owner.
- **It did not touch `state/phase-ledger.json`**, which is wrong and is a controller file.
- **It did not trim the next-phase prompt**, and it did not make the review gate independent, and it did not add the fifteen-word window to the standing check list, which is maintained by whoever owns the check list.
- **It did not open a closed chapter of any volume, except the single phrase in Chapter 0303 named in finding 6, which is attested wrong by four records and corrected in three places in this state layer.**
- **It did not change the plot.** No fact was added, removed or contradicted; the four hundred blanks, the eleven books, the question that is still a question, the two boxes, the season, the second hand, the nine miles and the four hundred and thirty miles are exactly where they were.
