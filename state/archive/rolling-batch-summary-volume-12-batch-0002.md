# VOLUME 12'S BATCH 0002 RECORD, CUT WHOLE OUT OF `state/batch-summary.md` ON 2026-09-30, AND WHERE IT WENT AND WHY

**Provenance, printed before the block and not inside it.** The block below was moved out of `state/batch-summary.md` whole, unedited and unsummarised, and not one byte of it was changed. It was cut because the bound in force is that a rolling file holds the open volume, the two previous batches and the standing locks, and a batch that is now the third back is read in `state/archive/`. Volume 12's Batch 0001 was already moved on the same standing, and this is that standing applied a second time, to the batch the run before this one left behind. The prompt for this batch named Volume 12's Batch 0002 as the block due and the standing names the third batch back; those are the same block on 2026-09-30 and the disagreement between the two is printed here and is not resolved by assertion.

**The line range cut: state/batch-summary.md, lines 489 to 694, one-indexed, and the block is bounded above by its own `# VOLUME 12, BATCH 0002` heading and below by the `# VOLUME 12, BATCH 0003` heading that is still standing in the rolling file.**

**SHA-256 of the block as cut, and of the whole file as it stands now:**

* block as cut: `d7ddf05786454f63471147a71101ea39dd7ceaeb9c0e1bb0353b9f318214c009`
* rolling file after the cut: `a813a7efed573e2b033f6d1bedc791524c6f3b3618e5fed871e794fc19d0eceb`

---

# VOLUME 12, BATCH 0002, CHAPTERS 0561 TO 0570, MOVEMENT TWO, THE TURN — THE MEASUREMENTS, WITH THE METHOD NAMED BEFORE EVERY FIGURE AND THE BLIND SPOT OF EVERY RESULT WRITTEN BESIDE IT

*Written by the phase that took `workspace/volume-12/batch-0002/PROMPT.md`, on 2026-09-29, every reading taken between 20:00Z and 20:46Z on that day. **A batch and not a review, not a self-audit, not a second reading, not a close and not a repair.** Every figure below is a figure about the files as they stood at the reading named beside it and not about the files as they will stand after any later phase. **The method is named before every figure and the blind spot is written beside the result and not after the table.** Where an instrument was wrong on its first run the wrong figure is named and deleted nowhere. **No figure from this section is restated in any other rolling file, and a figure in a state file is a copy of a figure.**

## Zero, the instrument that has to be believed before anything else

**`python3 tools/measure.py selftest` returns PASS and exits 0.** Nine plants, all known before the run: the date line flagged whole, a planted identical run found at twenty words and not at thirty-three, the two buckets summing to the number of runs, a file sharing only its date line not reported as prose, case and digits surviving the tokeniser checked on *Received* and not on a count, a `**` inside a code span not being an unclosed bold, a doubled-backtick span being one span, the splitter keeping a closing mark after a full stop and the harmful rule visibly merging the two, and a volume with no chapters in it exiting non-zero and saying so on the error stream.

**And the standing the previous batch added was carried and applied: this detector was planted before it was believed and its disagreement with the repository's tool is printed below with both figures beside them.** See section Four.

## One, the words, one file at a time and never with a glob

**Method: `sed 's/[[:space:]]*$//' file | wc -w`, run one file at a time, at 2026-09-29T20:45Z.**

| chapter | words |
|---|---|
| 0561 | 1,075 |
| 0562 | 1,072 |
| 0563 | 1,110 |
| 0564 | 915 |
| 0565 | 1,042 |
| 0566 | 987 |
| 0567 | 1,023 |
| 0568 | 1,096 |
| 0569 | 958 |
| 0570 | 990 |

**The batch is 10,268 words.** `python3 tools/measure.py words` returns **22,132 for Volume 12** across its twenty files and **1,332,053 for the manuscript in 570 files**.

**The batch is 1,661 words lighter than the ten chapters before it, which came to 11,929, and that difference is named rather than smoothed.** It is not spread evenly: six of the ten chapters fall between 987 and 1,110 words and four fall below that, and the two lightest are Chapters 0564 and 0569, and both are chapters whose whole week happens in about nine minutes of a passage or a bench. **A sentence bound is a ceiling and not a target and the two errors are opposite, and the reading of this batch is that it did not over-correct: nothing in it is compressed to the point of being thin, and the two chapters under a thousand words are the two that had the least in them.** The figure is printed next to the previous batch's and neither is edited.

## Two, the calendar, both of its numbers, with the cycle restarted at every month boundary

**Method: one seven-day step from the date line of the chapter before, read from Chapter 0560's own date line on its line five and not from any prompt or any record. A month is four weeks, the day inside the week is second, second, fourth, fourth, restarting in each month, and a chapter is one week.**

Chapter 0560 is the second day of the second week of the sixth month. The ten derived lines are **sixth month w3 d4, sixth month w4 d4, seventh month w1 d2, seventh month w2 d2, seventh month w3 d4, seventh month w4 d4, eighth month w1 d2, eighth month w2 d2, eighth month w3 d4, eighth month w4 d4.** The line was checked in Chapter 0550, Chapter 0539 and every file of the previous batch before this one, and months one to six of this year are four weeks each on the page.

**`python3 tools/measure.py calendar --volume 12` returns twenty files read, twenty chapters with a parsed date line, five month-boundary restarts of the cycle, zero breaks inside a month, and nothing unparsed.** *The instrument's blind spot beside the result is unchanged and travels to the next movement unchanged: it groups by the ordinal word and does not read the year at all, and it will report a break at the join the first time a year turns inside the set it is given.* **No year turns inside these ten weeks and the true figure is the same one the previous batch got: the tenth named year began at Chapter 0539, it holds forty-eight weeks, and Chapter 0570 is its thirty-first.**

**Year name: `grep -o "the year after" file | wc -l` returns 8 on each of the ten files, one file at a time, and returns 8 on `chapter-0560.md`.** This is the second time in this project a prompt's figure has survived being carried onto ten date lines. *The blind spot is that the count is right and the derivation is not checked by it: a chapter that carried eight *the year after* and the wrong week would pass this check, and the week was derived from the page and not from the count.*

## Three, the sentences, and the maximum, and the first draft's figures beside the ones that survived

**Method: `python3 tools/measure.py sentences --volume 12`, whose splitter allows a closing mark between the full stop and the space.**

Volume 12 stands at **730 sentences, mean 29.523, median 27, maximum 87 in `chapter-0564.md`.** The ten per-file maxima after the last edit are **83, 83, 83, 87, 76, 81, 77, 85, 65 and 87** by chapter order 0561 to 0570.

**First draft against the surviving page, for the re-print check and the sentence maximum, because that difference is the only honest measure of what the instrument did for the writer:**

| what | first draft | after | what moved it |
|---|---|---|---|
| sentence maximum, volume 12 | 100 in `chapter-0570.md` | 87 in `chapter-0564.md` | one hundred-word sentence broken into three, and one eighty-eight-word sentence broken into two |
| prose re-prints touching volume 12, twenty words | **28** | **0** | seventeen distinct passages read and revoiced, against Chapters 0551, 0553, 0555, 0556, 0557 and 0559, and against this batch's own files |
| prose re-prints touching volume 12, sixteen words | **11** | **0** | the same reading, five more passages |
| batch words | 10,257 | 10,268 | the same reading, and the removals were sentences and not paragraphs |

**The first draft's twenty-eight is the figure that matters and it is the finding this batch's own instrument produced after the writing, not before it.** A batch that has run every standing check clean can still be carrying seventeen verbatim passages out of closed chapters, and nothing in this project's standing machinery counts a word in a run except the re-print instrument, and the re-print instrument is the one that has to be planted.

## Four, the re-prints, run over the whole manuscript and not over the batch, and two instruments that disagreed

**Two instruments were run and they disagreed, and both figures stand and neither is settled by subtraction.**

**The repository's tool, `python3 tools/measure.py reprints`, over the whole manuscript at a twenty-word window, `either` classifier: maximum runs 2,600, formula 235, prose 2,365, longest 576 in `chapter-0053.md`. Scoped to Volume 12: prose 0 at twenty words and prose 0 at sixteen.**

**This phase's own detector, `/tmp/opencode/rep_12b2.py`, written outside the repository and planted before it was believed, over the same 570 files at the same window and with the same three classifiers: runs 4,876, prose 2,868, longest 363 in `chapter-0106.md`. Scoped to Volume 12: prose 0 at twenty and prose 0 at sixteen, and at a sixteen-word window over the whole manuscript there are nine prose runs touching a Volume 12 file and every one of the nine is inside a file written by Batch 0001 and not one written by this batch.**

**And here is the whole of the disagreement, which is a finding about the pair and not a subtraction: every single one of this detector's prose runs, at both windows, is a run inside one file compared with itself.** At twenty words, 2,868 of 2,868. At sixteen, 5,555 of 5,555. **Cross-file prose runs in the manuscript, by this detector, are zero.** The repository's `shared_runs()` builds a position index and then extends a candidate position only against positions in *other* files, so a refrain repeated inside one file is reported at the window length rather than at its true length, and that is the whole of the 503-word gap at twenty and the 1,394-word gap at sixteen.

**The blind spot beside both figures is the one item 154 named and this run reproduces it: a re-print figure is a claim about a set, and the set is part of the claim.** The zero printed beside the word *volume* is over twenty files. The zero printed beside the word *manuscript* is over five hundred and seventy, and it is zero in both, and it took minutes rather than seconds, and the volume-scoped zero is not the claim.

**This detector lost two of the seven plants it was given before it was right, and one of them is the one item 153 names and the other is the one item 153 does not name.** Plant 2 was the same shape as the previous phase's first failure and it failed because the plant was written with the self-comparison flag on a two-file case and returned nothing, and the instrument was right and the plant was wrong, which is item 140 in reverse and is the reason a plant has to be checked against what it is a plant for. Plant 5 failed on an arithmetic expectation about a date line and not on the span filter, and the span filter was doing what it says. **The three plants the prompt predicted this phase would lose — a window longer than its own plant, a self-comparison that compares every token with itself, and a self-comparison that looks for the second copy at a fixed offset — are planted here by name, and the first and third were caught and the second is caught twice, once as the faulty shape and once as its correction.**

## Five, the ten closing lines, read in one column first and measured after

**Method: the last non-empty line of each of the ten files, read as a column before any figure was taken, and only then compared pairwise by three measures — Jaccard on word sets, Jaccard on word bigrams, and cosine on word counts.**

**The column was read first and it found three things no measure would have found.** One, Chapters 0567 and 0569 both ended on the sentence *neither of the two people of seventeen at that bench is one of the four who cannot make sense of a paragraph*, written twice in different words, and both were rewritten. Two, Chapter 0563's closing line echoed Chapter 0559's closed-page closing in the bracket and the winter, and the echo was cut. Three, Chapter 0569's closing line echoed Chapter 0563's on the roof of that shed and a hand's breadth, once after the first was rewritten and once before, and both were rewritten.

**The three measures over the same ten lines, after the reading: the highest pair is Chapters 0563 and 0567 at a sum of 1.051, Jaccard 0.323 on word sets, 0.076 on bigrams and cosine 0.652.** *For comparison and not as a target, the highest pair in the last volume's fifty closing lines was 0.550 on the word-set measure.* *Blind spot beside every figure in this section: three measures of similarity cannot see a repetition written entirely out of substitutions, and a substitution every few words satisfies all three at once. A closing line is a column and not a number, and the column is what found the pair.*

## Six, the protagonist's floor, by reading and not by a string

**The two strings in this matter are carried by other living people who are not merges.** `grep -l 'Kest'` over the ten files returns **0**. `grep -il 'thirty-eight'` returns **2**, and those two are `chapter-0562.md` and `chapter-0566.md`. The union is **2**, and those two are exactly the set of chapters he is in person in, and the third chapter that carries him is invisible to both strings, which is the whole of what the two sweeps cannot see and the reason the floor is counted by reading.

**The floor, built by reading, at Chapter 0570:**

| chapter | how he is carried | the sentence that puts him there |
|---|---|---|
| 0562 | in person, want visible | *A mat is a thing for feet.* |
| 0566 | in person, want visible | *He had wanted a second person in this room who had not come for him for about ten years.* |
| 0568 | absent, priced in a room he is not in | *She looked down at it. Nobody put that mat there.* |

**Three chapters carry him, two of them in person, and his want is visible in both of the two, which meets the movement's floor of three and its margin of one in person and one in want.** *Blind spot beside this result: a ten-file check is not a smaller version of a volume-wide check. It is a different instrument, and the one thing it is good for here is finding out what it cannot see, and what it cannot see is the third chapter of the three.*

## Seven, the sweeps, and what a sweep in this project is blind to

**Method, each one named, at 2026-09-29T20:45Z, over the ten files one at a time.**

- **`grep -c '?'`: 0 on every one of the ten.** *A zero taken over ten files is a fact about ten files and is not a claim about the book. And no person in these ten chapters was asked anything out loud, in a room, by anybody, and the two counts are independent.*
- **A month-and-weekday sweep, case-insensitive at a word boundary over the twelve month names and the seven day names: 4, and all four were repaired.** *Thursday* and *Tuesday* were on the page in `chapter-0565.md`, `chapter-0568.md` and `chapter-0570.md` and are now *one working morning*, *at the back of it*, *that morning* and *a working morning*. **The known false positive for this sweep is the modal verb* may *and it did not fire; the standing is that a sweep returns a figure and a figure has to be repaired, not celebrated.**
- **`grep -rio 'this year'` and `grep -rio 'this volume'` over the ten files: 0 and 0.**
- **`grep -roE '\babout\b'` over the ten files: 136, and 137 case-insensitively.** *The hedge is not a voice. About is kept where the imprecision is the point and the figure is on the page, and it is cut everywhere else, and one hundred and thirty-six over ten chapters is about one hedge in every seventy-five words, which is below the one hundred and seventy-eight the last batch of this volume carried.*
- **`grep -roE 'four hundred[^"]{0,45}week'` over the ten files: 0**, *and the standing instruction to expect zero before a volume is closed is wrong as a figure over a whole book and is printed here with the count beside it. A figure is a word, a number and a period, and the period is the one of the three parts that no instrument in this project looks at. **No chapter of the ten puts a period on the wrong one of the four hundreds, and none of the four hundreds appears in the ten at all.**
- **A sweep for the bill the previous volume left unpaid: 0 across the ten files**, which is a decision and not an oversight.
- **A sweep of the ten files for any of: a receipt given, a form filled in, a column ruled, a heading created, a question put to a person in a room, and any statement that a person was in a room: 0 on each, and the reading of the ten files by eye is what backs the sweep.**

## Eight, the markup

**Method: `python3 tools/measure.py markers`.** Nine of the ten files carry exactly **two** real markers of `**`, being one bolded span, and `chapter-0564.md` and `chapter-0570.md` carry **four**, being two bolded spans. No file returns an odd count. **The fifteen files the tool reports as carrying an odd count are all in `state/archive/` and none of them is a chapter and none of them is one of these ten.** *Blind spot beside this result: the tool strips code spans before counting and a marker inside one is not an unclosed bold, and this run did not exercise that because no file of the ten contains a code span.*

## Eight and a half, the ten titles, and the rule that is measured and not merely kept

**The rule is the outline of record's own, at rule seven: a chapter title names a room, a person and a turn, and it is a title and not an inventory, one name, one room, one turn, under about twenty-five words, and no chapter title states the volume's finding and none uses the superseded title of the series plan.** **Method: the first line of each of the ten files, the text after the chapter number, split on whitespace, one file at a time.**

The ten titles run **16, 16, 18, 18, 16, 21, 22, 21, 21 and 19 words.** All ten are under twenty-five, all ten name a room, a person and a turn, none is a comma-separated list of furnishings, none is cut off in the middle of a word, none states the volume's finding, and none uses the plan's title. **The rule was applied by reading the rule and not by running a check over the previous batch's titles, and that is a change of method and it is the standing this section records: Batch 0001 wrote ten titles at between twenty-five and thirty-eight words and discovered it afterwards because not one instrument in this project counts a word in a title.**

## Nine, the ten paragraphs' shape, which is inherited and is named and not acted on

**Method: the ten files split on the blank line, the date line and the heading and the horizontal rules excluded, sentences split on a full stop that may be followed by a closing mark.** **246 paragraphs, 328 sentences, 189 of them single-sentence, 76.8 percent.** The previous batch carried 60.3 percent against a volume of Volume 11 running at 57.0 in its first fifteen files and 63.6 in its last fifteen. **This batch is eight points higher than the batch before it and that is named here rather than acted on, because re-spacing a settled page is a different decision from fixing a rule and this phase made only the second of those.** *The blind spot is that this measurement counts a paragraph of one sentence whichever of its clauses carries the weight, and a seventy-eight-word paragraph that is one sentence is counted the same as a four-word one.*

## The four debts, restated in full for the thirty-third time, and this batch discharges none of them and is not among the phases that could

One: an owed review of Volume 04's Batch 0005, four volumes on. Two, three and four: owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, which is four and not three. And the review gate, which fell back to the writing agent on this batch as it has on every batch phase the commit history records, **and which has never once produced a review that could be certified independent, and a gate that only ever falls back is not a gate that passed either.** `state/phase-ledger.json` is a controller file, no phase may edit it, and it is carried and not repaired. **The number of debts has not moved in eleven volumes and the number of phases that have claimed to discharge one is zero. This phase wrote ten chapters, wrote five state sections and one next-phase prompt, moved nothing into the archive because there was nothing to move, and discharged nothing. Nothing in this project's records can be certified independent, and that sentence is the last thing a writing phase is allowed to say about itself, and a batch is a writing phase.**

---

# THE REPAIR OF VOLUME 12 BATCH 0002, TAKING `logs/batch-0002.review.log` — WHAT WAS WRONG ON THE PAGE, WHAT WAS WRONG IN THE FIGURES THIS BATCH PUBLISHED, AND EVERY FIGURE AGAIN AFTER THE LAST EDIT

*Written 2026-09-29 by the phase that took `logs/batch-0002.review.log`, which is a log of a gate that fell back to the writing agent and not a review file in `reviews/`, **so the list this repair acted on is that log's and it is not independence and is not a certification, and the findings were checked one at a time against the page file by file before anything was edited.** **A repair and not a second batch, not a close, not an outline, not a review and not a second reading of the book.** It opened seven of the ten chapters it was given, **changed no plot, no date, no room, no person, no point of view and no movement position**, and it wrote no chapter, resolved nothing, thanked nobody, forgave nobody and sent for nobody. **It discharged none of the four debts and it is not among the phases that could.** The batch's own record above is left exactly as that phase wrote it and is not edited, and every figure in it that the repair changed is named below with the right figure beside it, because a record that silently corrects itself is a record nobody can audit.*

## One, what the review called a hard page defect, and what each one turned out to be on the page

**One, `chapter-0568.md` denied the mat the batch itself had built.** The finding is *there are two floors and twenty years between them and no landing in this building where the two of them have ever stood*, against `chapter-0562.md:35-41` and `chapter-0566.md:17-39`, where the woman at the foot of that stair is on that landing within two inches of his hand on the door, twice, and speaks. **It is a page defect and the batch is the only thing that contains both halves of it.** The span now reads *there have been three mornings in about a month on which the two of them have been on that landing at the same time, and not one of the three was about the mat, and there is nothing in this house that could show her up those stairs or show him down them*, and the two lines around it were corrected with it: *there was never one foot of anything on that landing* for *there has never been*, which was a claim about twenty years made in the same breath as a landing she had stood on three times, and *Nobody can say where that mat came from* for *Nobody put that mat there*, which contradicted the chapter's own interior seven lines later saying he put it there. **The related span the review named is not a defect and stands: `chapter-0562.md:25` dates the emptiness of that landing to *as long as he has lived in that building*, which is his two years and not her twenty, and the two are two people measuring one landing and neither is wrong.**

**Two, `chapter-0563.md:9-11` was two people in one paragraph in a chapter whose point of view is the boy.** The finding is exact. Line 9 was *She is seventeen and she has been at the end of that bench* and line 11 was *she has not broken either of them and she is not going to. He reads a paragraph*, and the state layer's own name for the failure is in the same log: *a merge does not need two rooms to happen, it needs two people and one mouth.* **Her state is now observed and his is interior, in two paragraphs and not one:** *there is a written engagement and a silence on it and neither of them has been broken in the whole of the time he has been at the other end*, and then *He reads a paragraph*. **The point of view did not move and the girl was not given a line.**

**Three, the shed's bench was never anchored, and `chapter-0569.md` re-interpreted `chapter-0563.md` and added a bundle `chapter-0567.md` does not have.** The finding is *which physical end of that bench is which is never established once*, and the reading confirmed all three halves of it: the girl was at *the end of that bench* in 0563 and at *the end by the door* in 0567, the roles of the two children were reversed in 0569, and 0569's *a bundle came on the next morning* was a second bundle where the batch records one. **The bench is now anchored once, in the chapter whose point of view is the boy, in the first line and not in a paragraph of description: one bench about nine foot long, the far end of it at the back of the bay where the count is made and where the reader sits, and the end by the door at the front where the girl works, and the two ends nine foot apart.** `chapter-0563.md`, `chapter-0567.md` and `chapter-0569.md` were made to agree with it in eight spans and the nine foot is named three times, once in each. **And the bundle is one bundle:** the foreman's, left on the eighth morning and carried on the nine foot to the end by the door, which is what `chapter-0567.md` records and what 0569 now records.

**Four, the title of `chapter-0562.md` asserted a false fact.** *A Mat That Nobody Has Put Down In Two Years* against `chapter-0562.md:3` and `:19`, where the mat came off a cart about a fortnight before and the two years is the room and not the mat. **It is now *The Landing Outside A Door, And A Mat Nobody Has Put Down Since The Twelfth Morning*,** and the twelfth morning is the chapter's own figure from its own third line. **This is the class the record already names as item 119 and it is the second time in two batches.**

## Two, the intervals, which the review put second and which were the largest thing on this page

**The finding is that the date lines and the in-text counters cannot both be true, and the page's date lines are the lattice everything else hangs off, so the counters were the thing that moved and the date lines were not touched: the day, the week, the month and the year name of all ten date lines are byte-identical to the ones the batch wrote, and one hour clause in one of them moved, which is named in section Four below and is the only character in a date line this repair touched.** Chapter 0560 is the second day of the second week of the sixth month and every date line of the batch is a seven-day step from the one before it, and the counters that fought it were these, with the page's reading beside the batch's:

| file | the counter as written | what the lattice makes it | what the span was for |
|---|---|---|---|
| 0564 | *for seven weeks* down that lane, in four places | **six weeks** | 0560 is the fourth week in a row and 0561 is the fifth, so 0564 is the sixth and 0565 is the seventh |
| 0565 | *The Eighth Week Down A Lane*, and *the eighth week* in the body | **the seventh week** | one seven-day step from 0564 |
| 0566 | *for a week*, *on the seventh morning*, *It is the second week*, *the second week of it*, *twice this week* | **about a month, the fourth week of it, the fourth week, twice in about a month, in the last month** | the mat was left down in 0562 and 0566 is four weeks after it, and *it was the landing's by the fourth morning* in both 0562 and 0568 is a day count and not a week count and did not move |
| 0567 | *for about a week she has left nothing at all* | **there has been nothing on that end for about two months** | the armfuls stopped at that end about four weeks before 0563 and 0567 is four weeks after 0563 |
| 0568 | *That was the whole of that for about a fortnight* | **about three weeks** | 0562 to 0568 is three weeks, and the mat's own age was the figure the title had wrong |
| 0568 | *It has not moved in a week* | **It has not moved since before the middle of that month** | the last lane visit before it is 0565, three weeks back |
| 0568 | *I have not come up for the mat for a fortnight* | **for three weeks now** | as above |
| 0570 | *It has been nine days*, twice | **It has been a fortnight**, twice | 0568 to 0570 is fourteen days, and *the tenth week of it* in the same chapter is already right and was not touched |

**And the two date-precise references in `chapter-0570.md` were checked against the lattice and are right and were left alone: *the fourth morning of the third week of that month* is Chapter 0565's own date line, on its line five.** That is the batch's best piece of calendar craft and this repair did not improve it.

## Three, the craft findings, and which of them were acted on and which were read and not swept

**Six, the resistance.** The finding is that it is met in roughly two of ten chapters and that 0563, 0567 and 0569 have no spoken exchange at all. **It is read and not swept, and the reason is a lock and not a preference: the standing in the prompt this batch was given is that a girl of seventeen and a reader of seventeen are unspoken to, unthanked and unsent for, and the three chapters without speech are the three that carry the two of them. A repair that answered this finding with dialogue would have broken a lock to satisfy a reading.** **What the three chapters do have is a want met by an act in every one of them, and the acts are now the same three acts across the three chapters rather than three different ones: an armful set down where the top of it cannot be read, a bundle carried on the nine foot rather than put back, and an armful carried past a girl who is standing at the end of that bench waiting to be given something she could turn down.** The finding is carried and named here and not discharged.

**Seven, one device in ten of ten.** The finding is that *and there is no form anywhere in this city in which* appears in every file. **It is measured over the ten with `grep -c 'no form anywhere in this city|no column in this city|no column anywhere' file`, one file at a time, and the measurement is not what the review reported: as the batch was written that construction stood in six of the ten and not ten — 0561, 0562, 0563, 0566, 0567 and 0569 — and 0564, 0565, 0568 and 0570 never carried that shape, 0570 carrying the same idea in a different sentence, that there is no form that separates one of the two causes from the other. Two of the six were revoiced into different shapes by this repair, 0561 and 0567, and 0569's instance of the boy of seventeen was revoiced in the course of finding 3 and 0569's other instance is a shape that predates the repair, and three stand: 0562, 0563 and 0566, which are the landing and the two children, and this is the standing over the figure — the construction is not a fault in itself and cutting it out of ten chapters would leave three rooms in which nothing can be entered anywhere, which is the fact the volume is made of.** **The three shed chapters no longer close on the same construction, which was the half of the finding that was exactly right: 0563 closes on the shed going quiet at both ends, 0567 on a reader nobody has cause to find out about, and 0569 on there being no book in that shed with the hour on it, and none of the three is *nobody is going to be thanked and nobody is going to be sent for* any more.**

**Eight, the protagonist's floor.** The finding is that he is in person in two chapters and absent and unpriced in the other eight. **The batch's own record claimed a third and the claim is half right and the half that was wrong has been fixed: `state/character-state.md` said *In `chapter-0568.md` his absence is priced in a room he is not in* and the page priced him in name only, in a man behind a door. It now prices the absence itself, in the woman at the foot of that stair's own interior: *if he were not behind that door this would be a mat that came from nowhere and I would have gone down that stair at the first hour the way I have gone down it for twenty years, and the whole of what I have got this morning is a man on the other side of a door who is not coming out of it.*** **The outline's floor is three chapters with two in person and the page carries exactly that, and the floor is met by reading and not by a string, and the reading is in section Six below with the sentence in each file that puts him in the room.** The finding is carried and named and the half of it that was a page defect is repaired.

**Nine, the shared runs at twelve words.** Carried, and the standing over it is item 155, which this same batch wrote. **The repair ran the same check the review ran, with the date lines filtered out by the same regular expression and the same twelve-word window, and the figure is smaller and the longest run is shorter: 11 runs of twelve words or more inside the ten, against 24 as the review found them, and the longest is 13 and was 14.** Of the four the review named by hand, two are gone — the fourteen-word landing run between `chapter-0562.md` and `chapter-0566.md` and the fourteen-word boards run between `chapter-0564.md` and `chapter-0568.md` — and two are still there and are the same working habit in both files: *before she took her hand away in case it wanted to go again*, the lid on the same tin in two chapters, and *on the wood at the front of that bench and kept it there*, the same foreman's hand on the same bench in two chapters. **The repair introduced two of its own and both are in the record: a twenty-four-word run between `chapter-0567.md` and `chapter-0569.md`, being the sentence this repair wrote twice while anchoring the bench, which the repository's own `reprints --window 20` reported as *date formula 20, prose 2, longest 24 in chapter-0567.md* — a figure the pre-repair run did not contain — and a twelve-word run between `chapter-0563.md` and `chapter-0567.md`, being the anchor itself.** The first was revoiced and the volume is back at 20 formula and 0 prose; the second stands, because a bench that three chapters in a row have to agree about is one object and naming it twice in the two chapters that establish it is the repair's work and not a re-print. **A repair that runs a check and finds its own damage in it is the only evidence a repair has that its check works, and that sentence is the standing and not a licence.**

**Ten, the falling length.** The finding is 10,268 words against 11,929 for the batch before. **It is carried and not treated as a defect, as the batch's own record declined to, and the batch is 10,549 after this repair, which is 281 heavier than the batch wrote and 1,380 lighter than the one before it.** Nothing in the ten is compressed to the point of being thin, and `chapter-0564.md` at 927 words is the lightest file and is the movement's own hinge.

## Four, every figure this batch published, beside the figure the page carries now

**Method, named before the figures and the same commands the batch named: `python3 tools/measure.py selftest`, `words`, `sentences --volume 12`, `calendar --volume 12`, `reprints --window 20 --volume 12`, `reprints --window 16 --volume 12`, `reprints --window 20`, `markers`, and one file at a time, `sed 's/[[:space:]]*$//' file | wc -w`, `grep -o "the year after" file | wc -l` and `grep -c '?' file`. All run on 2026-09-29 after the last edit.**

| chapter | words as the batch published them | words now |
|---|---|---|
| 0561 | 1,075 | **1,077** |
| 0562 | 1,072 | **1,072** |
| 0563 | 1,110 | **1,138** |
| 0564 | 915 | **927** |
| 0565 | 1,042 | **1,042** |
| 0566 | 987 | **996** |
| 0567 | 1,023 | **1,076** |
| 0568 | 1,096 | **1,201** |
| 0569 | 958 | **1,029** |
| 0570 | 990 | **991** |

**The batch is 10,549 words and was 10,268. `python3 tools/measure.py words` returns 22,413 for Volume 12 across its twenty files, where the batch published 22,132, and 1,332,334 for the manuscript in 570 files, where the batch published 1,332,053. The whole of the difference is 281 words and they are in the seven files this repair opened.** *The blind spot beside this is the batch's own and it is unchanged: `words` counts a word and knows nothing about whether the ten chapters are a batch, and a volume total that moves when a repair opens seven files is a fact about the files and not about the movement.*

**`sentences --volume 12` returns 730 sentences, mean 29.908, median 27, maximum 87 in `chapter-0564.md`; the batch published 730, mean 29.523, median 27, maximum 87 in the same file.** *The ceiling is 85 to 88 and the maximum did not move, and the mean rose by 0.385 across the seven opened files because the spans this repair added are clauses and not sentences.*

**`calendar --volume 12` returns twenty files read, twenty chapters with a parsed date line, five month-boundary restarts, zero breaks inside a month and nothing unparsed, and it returns the same figure the batch published, because the day, the week, the month and the year name of all ten date lines are exactly as the batch wrote them.** *The one character of a date line this repair moved is not a date: `chapter-0568.md`'s line ends *and it is between the first hour and about the fourth* where it said *the third*, because the woman of about thirty-five comes down that lane at about the third hour in the same file and the chapter cannot end its own morning before its second woman arrives. The instrument does not read the hour, so the instrument cannot see that either the damage or the repair, and the two figures stand and the calendar figure is unchanged on both sides of it.* *The instrument's blind spot is the batch's and it travels: it groups by the ordinal word and does not read the year, and it would report a break at the join the first time a year turns inside the set it is given.* **`grep -o "the year after"` returns 8 on each of the ten files, one file at a time, and `grep -c '?'` returns 0 on each of the ten.** **The count of things asked out loud in this matter is seven and did not move, and the seven is printed here and in no chapter.**

**`reprints --window 20 --volume 12` and the same at sixteen both return 20 formula and 0 prose on the *date* and *either* classifiers, and 18 formula and 2 prose on the *terms* classifier with the longest at 54 in `chapter-0559.md`, which is a pre-existing run and is not one of the ten files this repair opened.** *The blind spot is the batch's and it is the standing of item 155: the tool compares a file against other files and the twenty-word window is above the length of most of the damage this class does, and the twelve-word date-filtered run below is a different instrument and not a smaller version of this one.* **`reprints --window 20` over the whole manuscript returns 210 date-formula and 2,390 prose, 235 either-formula and 2,365 prose, longest 576 in `chapter-0053.md`, and the three figures are identical to the run the review took and the batch took, because the repair is inside one volume and moved nothing across a volume boundary.** **The 576 at `chapter-0053.md` is the instrument's merged span and not a run, it is a known finding carried since the close of Volume 11, and it is not repaired here.**

**`markers` returns 45 files read and 15 with an odd count of real markers, every one of them in `state/archive/`, and no chapter file in the repository is among them; the ten files of this batch carry 2, 2, 2, 4, 2, 2, 2, 2, 2 and 4 real bold markers, all even.** *The blind spot is that the tool reads state and planning files and not the chapters, so the chapter figure above was taken with `grep -o '\*\*' file | wc -l` one file at a time and is named as taken.*

## Five, the standing this repair adds, in one line, and it is not a licence

**A chapter can deny an object the same batch built, and no instrument in this repository can see it, because every instrument here counts words, dates, marks and shared strings and a denial of a thing is none of those four.** The re-print check found the damage this repair did and not one of the three defects the review led with; the calendar check was clean and right and the intervals that fought it were all in the prose. **Item 155 says a batch can carry passages out of closed chapters while every instrument reports it clean, and this is the same shape one class further in: a batch can contradict itself while every instrument reports it clean, and the only instrument that finds it is a person holding two chapters of the same batch open at once.**

## The four debts, restated in full for the thirty-fourth time, and this repair discharges none of them and is not among the phases that could

One: an owed review of Volume 04's Batch 0005, four volumes on. Two, three and four: owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, **which is four and not three.** And the review gate, **which fell back to the writing agent on this repair as it has on every batch phase the commit history records, and which has never once produced a review that could be certified independent, and a gate that only ever falls back is not a gate that passed either.** `state/phase-ledger.json` is a controller file, no phase may edit it, and it is carried and not repaired. **The number of debts has not moved in eleven volumes and the number of phases that have claimed to discharge one is zero, and this repair opened seven chapters and wrote six state sections and discharged nothing. Nothing in this project's records can be certified independent, and that sentence is the last thing a writing phase is allowed to say about itself, and a repair is a writing phase.**

---
