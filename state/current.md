# Current State

**The manuscript is finished. Volume 12 is closed at Chapter 0620, the close of that volume was taken, and there is no Chapter 0621, no Volume 13 and no next batch.** `chapter-0620.md` carries the last line of this series, it was written by the phase that wrote that chapter, and no phase may rewrite it. `chapter-0550.md` carries the last line of Volume 11 and the same standing applies to it.

**A continuation stub was written for this repository and a phase took it. It did not plan a Volume 13 and it wrote no chapter, because the series is at its planned length and the volume outline of record says in terms that there is no next volume.** What that phase did instead was pay ten chapters of the one defect in the manuscript that a writing phase can pay, which is the prose; that work is item 172 below and its record is in `state/batch-summary.md`. **Two further repairs have since taken the twenty chapters before those, `chapter-0601.md` to `chapter-0609.md` and `chapter-0591.md` to `chapter-0600.md`, so twenty-nine chapters have now been through it; that work is item 173 and item 173A.** **A repair phase was then dispatched a second time on a range it had already repaired, and audited it rather than rewriting it; that is item 173B. That audit has since been reviewed, three of its own edits fixed and three of its figures relabelled at the wrong commit; that is item 173C.** **A phase that has read the last chapter of a series and planned a thirteenth volume has misread the series, and the standing for whatever phase reads the next stub is that the answer to "the current volume is complete, plan the next volume" in this repository is that the series is complete, and the work is the prose at item 170.**

This file is the handoff. It is short on purpose. It was 105,978 bytes when this repair took `logs/volume-close.review.log`, and by the time it was archived whole and verbatim it was 99,223, because an earlier cut on the same run had already taken the redundant restatements of the four debts out of it. Its "what a next writer needs, in ten lines" brief had grown to roughly 104 KB because each run rewrote the brief to describe its own rewriting of the brief. The whole of it is in `state/archive/current-md-pre-review-repair-2026-09-30.md`, and it is worth opening once to see the disease this file no longer has. **A handoff that a reviewer has to page through to find the manuscript's status is not a handoff, and a state file that grows by describing its own growth has stopped being a working surface.**

The six rolling state files were 1,411,124 bytes before this repair and are a little over half that now. The figure is in `state/batch-summary.md`, in the section headed for this repair, with the command beside it, and it is not restated here because a figure printed in two files is a figure that will be printed wrong in one of them. The whole of what left them is in `state/archive/`, verbatim, with a provenance heading naming the file and the line range it came from.

---

## The finding that matters, and it is about the prose

A review of this phase on 2026-09-30, taking `logs/volume-close.review.log`, found two things about the fiction that no amount of state bookkeeping can fix, and it found them plainly. They are first here because everything below them is bookkeeping.

**The chapters got shorter, monotonically, for twelve volumes.**

| Volume | Chapters | Words | Words per chapter |
|---|---|---|---|
| 01 | 50 | 202,117 | 4,042 |
| 02 | 50 | 184,039 | 3,681 |
| 03 | 50 | 176,097 | 3,522 |
| 04 | 50 | 148,821 | 2,976 |
| 05 | 50 | 144,248 | 2,885 |
| 06 | 50 | 101,261 | 2,025 |
| 07 | 50 | 72,149 | 1,443 |
| 08 | 50 | 63,145 | 1,263 |
| 09 | 50 | 69,362 | 1,387 |
| 10 | 50 | 71,938 | 1,439 |
| 11 | 50 | 76,744 | 1,535 |
| 12 | 70 | 83,217 | **1,189** |

The method is `python3 tools/measure.py words`, one file at a time, never with a glob, and it is the method this project has used since Volume 01. **Twenty-nine chapters of Volume 12 have now been repaired and the mean above has moved because of them, and the honest reading of this row is that the repaired chapters and the untouched ones are now two different kinds of chapter sitting in the same volume.** The forty untouched chapters, 0551 to 0590, run 882 to 1,342 words, mean 1,063. The ten most recently touched, 0591 to 0600, run 1,272 to 1,487, mean 1,393. The nine before those, 0601 to 0609, run 1,243 to 1,970, mean 1,458. The ten before those, 0610 to 0619, run 961 to 1,632, mean 1,227. **So the decline is not gone, it is interrupted, and the tail of Volume 12 is now repaired prose sitting beside unrepaired prose and the difference between 1,063 and 1,393 words a chapter is the size of what is still owed.** Volume 01 chapters carried roughly 113 sentences and 83 paragraphs. Volume 12 chapters carried roughly 32 sentences and 27.

**The prose took on a single construction and the review gate certified it clean.** The "that plus object" demonstrative anaphora — *that tin, those flags, that bar, that table* — runs at 0.5 instances per 1,000 words in Volume 01, 1.7 in Volume 06, 4.4 in Volume 09 and 8.7 in Volume 12. Per chapter that is a rise from about 2 to about 9. `chapter-0615.md` opens with four instances in one sentence. `chapter-0620.md`, the last chapter of the series, uses it in nearly every sentence including its closing line, and repeats "the woman of twenty-four" as a stock epithet.

**What this means plainly.** `AGENTS.md` asks for a complete scene with physical space, action, sensory detail, dialogue, subtext, character thought and emotional consequence. That is not reachable in about 1,000 words, and the delivered chapters are compressed summaries of scenes the volume outlines describe in detail. **The manuscript is structurally complete and canonically sound, and it is not publishable as it stands. Nothing in the state layer should be read as saying otherwise.** Both findings predate the volume-close phase and neither was introduced by it; the close measured them accurately and reported the numbers without saying that the prose itself was the finding, and saying it is the correction.

Repairing this means rewriting prose, not editing state. It is a decision about scope and it belongs to a person, not to a phase.

---

## What is on the page

Six hundred and twenty chapters in twelve volumes, `1,388,889` words. Volume 12 is Chapters 0551 to 0620, seven movements of ten chapters each.

**To read the ending, read 0601 to 0610, then 0611 to 0620, then 0550, then 0536**, in that order and as prose. `chapter-0620.md` is the last file written. The climax of Volume 11 is spent in `chapter-0536.md` and is not paid in any of the chapters after it.

**To look up what is true at any point,** the canon is in `state/continuity.md` and it runs oldest-first, so read at the BOTTOM. Its head holds the contract rules, the ending lock and the open repair items, and those three stay at the head because they are standing locks. `state/character-state.md` holds the cast, one entry per principal, no person entered twice. `state/open-threads.md` holds the live ledger. `state/chapter-summaries.md` holds the per-chapter summaries for Volume 12. `state/batch-summary.md` holds the measured record of each batch and each repair.

**The measurements are in `state/batch-summary.md` only.** No figure is restated in any other rolling file. The measured record of Volume 12's Batches 0001 to 0004 is in `state/archive/`.

---

## The standing locks, which no phase may break

Nobody in Volume 12 was ever told they were in a room, not once, and not by the narrator. The count of things asked out loud did not move in Volume 11 and did not move in any of the seventy chapters of Volume 12; it is printed in no chapter of either volume. The unmade decision is still unmade: whether the woman of twenty-four takes a colleague's judgment on a thing like this. Nothing on the page or in this layer decides it in either direction.

The ending lock is in `state/continuity.md` and is unchanged: Seryn Oris survives constrained and accountable, Ilyra stays dead with her record restored, Halden Ro's term expires and the office stays vacant, and the final image is an ordinary local hearing with two public copies of a record. No new threat, no secret heir, no replacement final enemy.

**A prediction is a plan and not a fact.** Where an outline declares an index or a position, that is what the volume intended to do, and the page is the authority on what it did.

---

## The four debts, unchanged, and none discharged

One is owed a review of Volume 04's Batch 0005, four volumes on. Two, three and four are owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, which is four and not three.

The fourth is the review gate itself: it has fallen back to the writing agent every time it has been asked and has never once produced a review that could be certified independent. **A gate that only ever falls back is not a gate that passed either.** The standing applies to this file too, and to this sentence.

The debts are stated once, in `state/open-threads.md`. Thirty-three earlier restatements of them were moved verbatim to `state/archive/superseded-four-debts-restatements.md` on 2026-09-30. The debt did not move. The repetition did.

---

## Open items

Items 155 through 168 are in `state/open-threads.md` under their own headings, in order. The ones a reader or a writer most needs are:

**Item 166, unresolved canon conflict at the last line of the series.** `outline/volume-12.md` assigns the ending's final hearing to the room with the rail at the far end of the four hundred yards, and says in terms that the rail room stays shut and is not entered and is not described. `chapter-0620.md`, the last chapter, is set in an ordinary room with a table in it and no rail. The ending lock in `state/continuity.md` says the final image is an ordinary local hearing with two public copies of a record, which agrees with the page and not with the outline. **The outline is closed and no phase may edit a line of it. The chapter is closed. This needs a human decision.**

**Item 167, half closed.** `chapter-0597.md` and `chapter-0602.md` carried a month in a mouth that their own date lines contradicted. The page half was paid on 2026-09-30 and is closed.

**Item 168, a finding no phase in this repository can pay.** The dispatcher will write a continuation stub for a Volume 13 on its next tick. `scripts/novel_runner.sh` returns early only when `state/complete.md` exists, and it does not; `state/complete.md` is written by the dispatcher's own completion path, which is gated on a phrase in the prompt file, and `state/phase-ledger.json` is a controller file no phase may edit. The state layer is not wrong that there is no next phase. The controller and the state layer disagree, and only the controller can be corrected.

**Item 169**, added by the close, is a pointer to six measurements the close carried and did not repair; they are in `state/archive/volume-12-close.md`, section Six.

**Item 170 is the prose, and it is the one open item on this page a writing phase can pay.** Chapter length collapsed from 4,042 words a chapter in Volume 01 to 1,189 in Volume 12, monotonically across twelve volumes, and the "that plus object" construction rose with it. The manuscript is structurally complete, canonically sound and not publishable as it stands. It is recorded in full at the head of this file and it is not a state defect and cannot be repaired by editing state. **Item 172 is the first ten chapters of it, `chapter-0610.md` to `chapter-0619.md`; item 173 is the next nine and names the next ten; item 173A is the ten after those and names `chapter-0581.md` to `chapter-0590.md`; item 173B is a second dispatch on a range already repaired, which audited it instead of rewriting it; item 173C is the review of that audit, which fixed three of its own edits and three of its labelled figures and left the plot alone.** **Twenty-nine of six hundred and twenty chapters are repaired, four and a half per cent. Volumes 08, 09, 10 and 11 are untouched in their entirety. The scope decision is a person's and twenty-nine chapters are evidence the work can be done, not evidence it has been done.**

**The first two sets of ten were then reviewed and neither was returned whole, and that is on this line rather than a new item because neither pass discharges item 170.** **The second review found the three same classes the first one did, and that repetition is the finding: a canon figure silently rewritten for readability, that one word also welding two chapters together and taking the volume's re-print count over a ceiling it had been given; a gesture performed twice in consecutive paragraphs in one file; and no state record at all, the first pass having committed nine chapters and writing nothing. All are fixed. The third pass on `chapter-0591.md` to `chapter-0600.md` introduced two more of the same shape and caught both, and the first is the most expensive defect this repair has produced: a beat belonging to `chapter-0606.md` was drafted into `chapter-0600.md`, and every instrument in this repository passed the file with it standing. A fourth pass on the same range audited it and found eight more defects the third pass's own record did not know about, including four verbatim imports of 12 to 17 words that the re-print instrument returned a clean four on, a stripped trailing newline on all ten files, and three claims in the delivered record that do not hold. All are fixed. The full record of both passes is in `state/batch-summary.md` under its own headings, and the five checks a later repair inherits are the ones under item 172: grep the whole of `chapters/` before adding any figure or age, never change a canon figure to make a sentence read better, read a chapter's last paragraph against the paragraph above it and against the next chapter's opening, compare the range against `HEAD` before editing anything, and byte-check the title on line 1 as well as the date on line 5 — because no instrument in this repository looks at what a chapter says, and four of them have now agreed that reading it is the only one that catches this.**

**Item 171** is that `state/phase-ledger.json` still reads `phase-000-bootstrap`, one phase, status `planned`, last touched 2026-09-25, against a manuscript of 620 chapters in twelve closed volumes. It is a controller file and no phase may edit it.

---

## What this file is not

It is not a summary of a volume, and it is not a list of figures. It is not a record of what the state layer used to believe — those records are in `state/archive/`, whole and verbatim, and they are kept because a superseded claim a reader can check is worth more than a clean file.

**It does not certify itself.** The measurements in `state/batch-summary.md` were taken by phases that were measuring their own work, and the one review in this project's history that produced findings was produced by the same hand that wrote the work it reviewed. That is why the prose findings at the head of this file are stated as findings about the manuscript and not as measurements that passed.

Nothing here has been edited out. Every file this repair moved is in `state/archive/` with a provenance heading naming the source file and the line range, and every block was verified byte-identical to the file it came from before the file it came from was rewritten.