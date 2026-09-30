# THE PER-BATCH RECORD OF VOLUME 12 BATCH 0001 MOVED OUT OF `state/batch-summary.md` ON 2026-09-30, AND WHY, AND WHERE IT WENT

**Moved verbatim, whole and unedited, by the phase that wrote Chapters 0581 to 0590, into `state/archive/rolling-batch-summary-volume-12-batch-0001.md`. Nothing was deleted, summarised, condensed or paraphrased, and every figure inside a moved block stands as the run that wrote it measured it at the time.**

**The rule this moves them under is the one this file prints at its head: a rolling file holds the open volume, the two previous batches and the standing locks, and a closed volume, and the third batch back, is read in `state/archive/`.** Volume 12 is the open volume and this is its Batch 0001 record, which is the third batch back the moment Batch 0004's record lands, and this file was exceeded by one block in each of the five rolling files until this pass. **The whole of what moved out of it is the measurements of Volume 12's Batch 0001.**

**Two blocks moved out of it and they are the batch record and the fix pass that repaired it, because a fix pass that refers to *the section above* and has no section above is a broken pointer and a working surface that cannot be opened. One open item moved with them, and it is named here because the archive's own rule keeps an open item in the rolling layer and this move is the one place that rule and this bound pull against each other: item 154, which is a scope fault found by the fix pass, is now at `state/archive/rolling-open-threads-volume-12-batch-0001.md` and a Volume 12 writer who needs it opens that file and not this one. Items 155, 156 and 158 stay in this file and are not moved.**

**The prompt for Batch 0004 named Volume 12's Batch 0002 record as the block due to go when its own record landed. The standing and item 157 both name Batch 0001, and with Batch 0004's record in the file the two previous batches are Batch 0002 and Batch 0003, so Batch 0001 is the block that is out of the bound and Batch 0002 is not. Batch 0001 moved. Batch 0002 stayed, and the disagreement is printed here and is not resolved by assertion.**

**SHA-256 of the moved block, and the lines it occupied:** `7138ed1ef79fff98967dde5718947c4b04954108a847b9ea0d2a5f93726a4d5d` — `state/batch-summary.md` lines 484 to 649.

---

# VOLUME 12, BATCH 0001, CHAPTERS 0551 TO 0560, MOVEMENT ONE — THE MEASUREMENTS, WITH THE METHOD NAMED BEFORE EVERY FIGURE AND THE BLIND SPOT OF EVERY RESULT WRITTEN BESIDE IT

*Written by the phase that took `workspace/volume-12/batch-0001/PROMPT.md`, on 2026-09-29. **A batch and not a review, not a self-audit, not a second reading, not a close and not a repair.** Every figure below was taken at the reading named beside it, and every one is a figure about the files as they stood at that reading and not about the files as they will stand after any later phase. **The method is named before every figure and the blind spot is written beside the result and not after the table.** Where an instrument was wrong on its first run the wrong figure is named and deleted nowhere.

## Zero, the instrument that has to be believed before anything else

**`python3 tools/measure.py selftest` returns PASS and exits 0.** It plants nine cases whose answers are known before it runs: the date line flagged whole, a planted identical run found at twenty words and not at thirty-three, the two buckets summing to the number of runs, a file sharing only its date line not being reported as prose, case and digits surviving the tokeniser checked on *Received* and not on a count, a `**` inside a code span not being an unclosed bold, a doubled-backtick span being one span, the splitter keeping a closing mark after a full stop and the harmful rule visibly merging the two, and **a volume with no chapters in it exiting non-zero and saying so on the error stream.**

**And it was run before the chapters existed, which is the ninth plant and the one this batch inherits.** `python3 tools/measure.py sentences --volume 12` on an empty `chapters/volume-12/` prints `no chapter files matched volume volume-12; nothing was measured` on the error stream and exits 1. **The exit code is the measurement and the screen is the report, and a non-zero exit from that one line before the chapters exist is the tool working and is not a finding to record.**

## One, the words, one file at a time and never with a glob

**Method: `sed 's/[[:space:]]*$//' file | wc -w`, run one file at a time, at 2026-09-29T19:19:22Z.**

| chapter | words |
|---|---|
| 0551 | 1,156 |
| 0552 | 1,350 |
| 0553 | 1,214 |
| 0554 | 1,271 |
| 0555 | 1,205 |
| 0556 | 1,146 |
| 0557 | 1,119 |
| 0558 | 1,251 |
| 0559 | 1,134 |
| 0560 | 1,083 |
| **the batch** | **11,929** |

**`python3 tools/measure.py words` at the same reading returns Volume 12 at 11,929 and the manuscript at 1,321,850 in 560 files.** *Blind spot beside this result: a word count cannot see whether the words are the same words, and the thing a word count is worst at seeing in this volume is the most repeatable object in the manuscript, which is a refusal and not words on a page.*

## Two, the sentences, and the maximum, and the first draft's figures beside the ones that survived

**Method: `python3 tools/measure.py sentences --volume 12`, which splits on `(?<=[.!?])["'’”)*]*\s+` so that a closing quotation mark between the full stop and the space is kept with its sentence. Taken at 2026-09-29T19:19:22Z, on the files as they stand at the end of the run.**

**392 sentences, mean 29.454, median 27, maximum 78 in `chapter-0560.md`.** Per-file maxima by the same splitter, one file at a time: **67, 75, 71, 66, 76, 55, 73, 73, 75, 78.** The ceiling for this project is eighty-five to eighty-eight and the maximum is under it.

**And the first draft's figure, which is the only honest measure of what the instrument did for this batch.** The same command on the same ten files before any repair returned **297 sentences, mean 39.663, median 36, maximum 144 in `chapter-0560.md`.** The difference is **a maximum of 144 against a maximum of 78**, and it is the whole of what reading the ten files for length is worth. *The wrong figure is named and deleted nowhere.* *Blind spot beside both results: a ceiling is a ceiling and not a target, and the two errors are opposite — a batch that writes everything short has over-corrected and a batch that writes a hundred-and-eighty-word sentence has under-corrected, and only one of those shows up in a sweep.*

## Three, the calendar, both of its numbers, with the cycle restarted at every month boundary

**Method, read directly and by hand, one file at a time, against the date line printed in each file, at 2026-09-29T19:19:22Z.** The derivation starts at the date line on line five of `chapters/volume-11/chapter-0550.md`, which reads the fourth day of the fourth week of the third month of the tenth named year, and each of the ten is one seven-day step from the one before it.

| chapter | day | week | month |
|---|---|---|---|
| 0551 | second | first | fourth |
| 0552 | second | second | fourth |
| 0553 | fourth | third | fourth |
| 0554 | fourth | fourth | fourth |
| 0555 | second | first | fifth |
| 0556 | second | second | fifth |
| 0557 | fourth | third | fifth |
| 0558 | fourth | fourth | fifth |
| 0559 | second | first | sixth |
| 0560 | second | second | sixth |

**The day inside the week is second, second, fourth, fourth in every month and the cycle restarts three times in ten chapters, and no month in the ten comes out at three weeks.** *Blind spot beside this result: the check restarts at each month boundary on purpose, because a check that runs one global cycle across a run of chapters reports a break at the first chapter of a month, and there is no break there, and the way that reports a break is the way that is wrong.*

**The instrument's own reading, `python3 tools/measure.py calendar --volume 12`, at the same moment: files read 10, chapters with a parsed date line 10, month-boundary restarts of the cycle 3, breaks inside a month 0, unparsed none.** **The false break is not reported here and that is a fact about this set and not about the instrument: the tool groups by the ordinal word and does not read the year, and the ninth named year's name is a substring of the tenth's, and a tool that cannot read the year will always report a break where a year turned. That break has now been printed nine times in this project and it is not a defect in the page, and it will appear the first time a year turns inside whatever set the next phase gives the tool.** Both readings stand beside each other.

**And the year name, by the only method that can read one.** **Method: `grep -o "the year after" file | wc -l`, one file at a time.** It returns **eight on each of the ten files**, and it returns **eight on `chapters/volume-11/chapter-0550.md`**, and the prompt for this batch printed eight and the page agrees with it on all ten, **which is the first run in this project in which a figure handed to a phase in a prompt survived being carried onto ten date lines.** Item 151's standing is that a prompt is a record with fewer citations and a correct figure in one is exactly as likely to be dropped as a correct figure in a record; the difference this time is that the count was taken one file at a time at the end of the run and not once at the start of it. *Blind spot beside this result: a chapter that carries the name twice in a date line is counted once by this method and a chapter that carries none is not caught by it at all.*

**And no decision about a further year name was taken in this batch, and none had to be: ten weeks beginning at the fourth week of the third month of the tenth named year run into the fourth, fifth and sixth months of the same year and do not cross a boundary.** The form of that name is in the outline of record and no phase may attach it to a chapter.

## Four, the re-prints, run over two volumes and not over the batch, and two instruments that disagreed, and the heading this section carried before the fix pass said *over the manuscript* and did not

**The heading above was `the re-prints, run over the manuscript and not over the batch` and it was false, and the sentence it heads says which set was actually run in its third line, and a heading that contradicts the paragraph under it is a worse defect than a wrong figure because a reader takes the heading first and stops.** The set was Volumes 11 and 12 together, sixty files, and not the manuscript. **The claim is corrected in the heading and the wrong one is named here and is not deleted, and this is the second time this batch's own record has described a set wider than the one it ran over — the first being the file count, printed two sections below and corrected in place.**

**The instrument this phase wrote, at `/tmp/opencode/rep_12b1.py`, outside the repository, because a writing phase does not edit an instrument another phase may be relying on.** It aligns by token value and not by index, extends every match to its full maximal length, compares a file against itself as well as against every other file, filters formula by the character span of every date line before tokenising, and de-duplicates by dominated position and not by merging. Its own classifier carries no vocabulary at all, only date spans, **because a formula list that is doing the classifying must not contain a room.**

**It was wrong on three of its six plants before it was right, and every failure was a number rather than a crash**, and the three failures are item 153 in `state/open-threads.md` and are not repeated here. `python3 /tmp/opencode/rep_12b1.py --selftest` returns PASS and exits 0.

**Run over Volumes 11 and 12 together, so that a pair crossing the volume boundary is visible to this batch and not only to a later one, at 2026-09-29T19:17Z:**

- **At a twenty-word window: prose runs touching a Volume 12 file, 0.** The two prose runs that remain across the sixty files of Volumes 11 and 12 are both inside Volume 11 and both are that volume's own recorded findings — twenty-nine words at `chapter-0530.md` against `chapter-0539.md`, and twenty at `chapter-0525.md` against `chapter-0534.md`. *Both figures in this bullet were re-measured at the fix pass and the ones printed here before it were wrong: the file count was given as **the hundred files of Volumes 11 and 12** and the set is **sixty** (Volume 11 at fifty files and this batch's ten), and the first run was given as **thirty words** and it is **twenty-nine**. Both wrong figures are named here and are superseded, and neither is deleted. The first is a wrong object and the second is a wrong number on a right object, and a record that carries a wrong file count is not re-runnable by anybody who counts the files.*
- **At a sixteen-word window: prose runs touching a Volume 12 file, 0.**

**And the run that was missing, which the scope above could not see, and which the fix pass ran over the whole manuscript rather than over the two volumes.** The pair this batch's own instrument was scoped to miss is the standing of item 136 — a phase that verifies a volume and stops has verified a volume and not a book — and here the volume boundary that mattered was not the one the instrument was widened across. **Over all five hundred and sixty files at a twenty-word window, with date lines filtered and each maximal run counted once on its own extended start, `chapter-0493.md` against `chapter-0551.md` returned a thirty-two-word prose run: *if a second of a second were put in front of her tomorrow there would be nowhere in this empire for her to put the fact that she did not want it*.** The count is thirty-two counting the leading *if*; a reading that starts the window at *a second* returns thirty-one, and both readings are printed because a figure taken from a start the reader cannot see is a figure the reader has to take on trust.

**What that run is, and it is not a theft.** It is Halla Wray's own sentence, said out loud in that shed in `chapter-0493.md` about a girl of seventeen at the back of a bench, and `chapter-0551.md` is the foreman of fifty-one remembering the sentence that is the reason she began putting the bundle at the end of her own bench. **The recall is the chapter. The finding is not that the words came back and it is that thirty-two of them came back identical.**

**And it is repaired, and the repair is a revoicing and not a deletion.** The three beats of the remembered sentence are all still on the page in `chapter-0551.md`: that a girl of seventeen had not been asked one thing in about a year, that anybody in this matter includes the girl at the back of that bench, and that an offer of a second of a second would find nowhere to go. **The third is now carried in different words — *that a second of a second put in front of that girl tomorrow would go nowhere in nine hundred buildings, and that a person who did not want a thing had no way of holding the knowing of it on to anything* — and the longest run of identical words between the two chapters is now five, at *a second of a second*.** `chapter-0493.md` is a closed chapter and was not opened.

**The figures, before and after, on one line and from the same instrument and the same window.** **At a twenty-word window over the whole manuscript, date lines filtered: prose runs touching a Volume 12 file were 1 before the repair and are 0 after it, and the one was thirty-two words at `chapter-0493.md` against `chapter-0551.md`.** The batch's own bullet above printed 0 for this quantity, and it printed it over Volumes 11 and 12 together, and the pair was in Volume 10.

**At a sixteen-word window over the whole manuscript, the claim of 0 printed above is also false against the page, and it is not repaired, and the reason is printed rather than a number.** The same run returns **three** prose runs touching a Volume 12 file, the longest **nineteen** words, and all three are in the sixteen-to-nineteen band that `state/archive/volume-10-close.md` records as a canon formula band which a sixteen-word threshold cannot separate from a defect: *there is no paper in this empire that asks a person of seventeen whether she would rather not and* at `chapter-0551.md` against `chapter-0338.md` and `chapter-0306.md`, nineteen words and the same two words both times, and *no full stop at the end of it and her own name is at the foot of it* at `chapter-0558.md` against `chapter-0382.md`, eighteen. **The first is the refusal formula of this book and it is where Halla Wray's argument comes from, and it is spoken in four earlier volumes. It is canon and not a defect and it is named here so that a later phase reading this section does not repair it.** The zero printed above is superseded and is not deleted, and the sixteen-word figure that replaces it is three.

**What the fix pass cannot see, beside every figure in this section.** A re-print detector reports re-prints and not repetitions, it aligns by token value and therefore reads two sentences that differ only in punctuation as one run, and it was given a word window and not an intention. **It found thirty-two words of Halla Wray's sentence coming back in a chapter two volumes later and it could not tell whether the writer meant them to, and the meaning was settled by reading `chapter-0493.md` and `chapter-0551.md` side by side and not by the number.** The instrument in this repository was scoped to two volumes when the question was a book, and the book is five hundred and sixty files.

**And what the first draft of the batch held, before any repair.** At a twenty-word window over Volume 12, **three** prose runs, the largest forty-seven words at `chapter-0553.md` against `chapter-0560.md`. At a sixteen-word window, **six**, and one of them was a window occurring **twice inside `chapter-0557.md`**, which is the class this batch's own first instrument could not see and the repository's can. **The repository's tool, over the whole manuscript at a twenty-word window under the *either* classifier, returned prose 2,395 before this batch's repairs and returns 2,367 after them, and the difference is twenty-eight.**

**And the two instruments disagreed about the same ten files at a sixteen-word window, and the disagreement is printed rather than subtracted.** The repository's tool returned **two** prose runs in Volume 12 and named the longest at sixteen words in `chapter-0553.md`; the detector this phase wrote returned **one** and did not name the pair. **The difference is a run the repository's merger produced and this phase's de-duplication by dominated position dropped, which is the shape item 152 is about, reproduced inside this batch's own instrument on its first run.** After the repairs both return zero over Volume 12 at sixteen and at twenty. *Blind spot beside every figure in this section: the instrument reports re-prints and not repetitions, and it cannot see two chapters that close on the same sentence written twice in different words.*

**The repository's whole-manuscript figures at the same reading, for the record: at a twenty-word window, *date* classifier formula 200 and prose 2,392, *terms* classifier formula 201 and prose 2,391, *either* classifier formula 225 and prose 2,367, longest prose run 576 words in `chapter-0053.md`.** At a sixteen-word window over Volume 12 alone: formula 10, prose 0, longest 0. *Blind spot beside that: the repository's instrument has a branch that reports a window occurring twice inside one file as a run whether or not a second occurrence exists anywhere, so it over-reports at a sixteen-word window and does nothing at twenty, and its merger chains nearby runs into one span with holes in it, which is why a figure produced by it and a figure produced by dominated-position de-duplication differ by one run on a set of ten.*

## Five, the ten closing lines, read in one column first and measured after

**Method: the last non-empty line of each of the ten files, read as a column before any figure was taken, and only then compared pairwise by three measures — Jaccard on word sets, cosine on word counts, and Jaccard on word bigrams.**

**The column was read first and it found two pairs that the measures would not have found at all.** The first reading found that Chapters 0555 and 0559 both closed on the chain going along at the front of that bench under a hand that had been on it eleven years, written twice in different words with the substitutions close enough that no n-gram measure in this repository can see it. **Chapter 0559's closing line was rewritten and the second reading of the column is clean.** The first reading also found that Chapter 0554's closing paragraph opened as an inventory of that room's furnishings and it was cut back to the plate.

**The three measures over the same ten lines, after the reading: the highest pair is Chapters 0556 and 0560 at Jaccard 0.406 on word sets, 0.123 on bigrams and 0.014 on word counts.** Those two are in different rooms and their only common words are ordinary ones. *For comparison and not as a target: the highest pair in the last volume's fifty closing lines was 0.550 on the word-set measure, and the highest pair on the sum of the three was a different pair at 0.431, 0.788 and 0.286 — two rankings of the same fifty lines disagreeing about which pair is worst, which is why the reading comes first.* *Blind spot beside every figure in this section: three measures of similarity cannot see a repetition written entirely out of substitutions, and a substitution every few words satisfies all three at once. A closing line is a column and not a number.*

## Six, the protagonist's floor, by reading and not by a string

**The two strings in this matter are carried by other living people who are not merges, and they are carried here by nobody at all.** `grep -l 'Kest'` over the ten files returns **0** and `grep -il 'thirty-eight'` returns **2**, and the union is **2**, and those two are `chapter-0554.md` and `chapter-0556.md`. **The union is exactly the set of chapters he is in person in, and the third chapter that carries him is invisible to both strings, which is the whole of what the two sweeps cannot see and the reason the floor is counted by reading.**

**The floor, built by reading, at Chapter 0560:**

| chapter | how he is carried | the sentence that puts him there |
|---|---|---|
| 0554 | in person | *What he wanted was a room with a second person in it who had not come for him.* |
| 0556 | in person | *The second plate was on the other side of that table on all three of those mornings and he washed it on two of them.* |
| 0557 | absent, priced in a room he is not in | *At about the sixth hour the stair did not go up.* |

**Three chapters carry him, two of them in person, and his want is visible in one of the two, which meets the movement's floor of three and its margin of one in person.** *Blind spot beside this result: a ten-file check is not a smaller version of a volume-wide check. It is a different instrument, and the one thing it is good for here is finding out what it cannot see, and what it cannot see is the third chapter of the three.*

## Seven, the sweeps, and what a sweep in this project is blind to

**Method, each one named, at 2026-09-29T19:19:22Z.**

- **`grep -c '?'` over the ten files, one file at a time: 0 on every one of them.** *A zero taken over ten files is a fact about ten files and is not a claim about the book. And no person in these ten chapters was asked anything out loud, in a room, by anybody, and the two counts are independent — a question mark in a mouth is punctuation and is not an asking, and there is not one of either in these ten files.*
- **A month-and-weekday sweep, case-insensitive at a word boundary over the twelve month names and the seven day names: 0.** *The known false positive for that sweep is the modal verb* may *and it did not fire here; the standing is that a sweep returns zero and a zero is not evidence until the shape of the blindness has been checked, and the shape here is that the sweep cannot see a date written in a form this project does not use.*
- **`grep -rio 'this year'` and `grep -rio 'this volume'` over the ten files: 0 and 0.**
- **`grep -roE '\babout\b'` over the ten files: 178, and 180 case-insensitively.** *The hedge is not a voice. About is kept where the imprecision is the point and the figure is on the page, and it is cut everywhere else, and one hundred and eighty over ten chapters of about twelve hundred words each is about one hedge in every sixty-six words, which is lower than the nine hundred and eighty-nine the last volume's fifty files carry and is a batch reading its own figures and not hiding behind them.*
- **`grep -roE 'four hundred[^"]{0,45}week'` over the ten files: 0**, and *the standing instruction to expect zero before a volume is closed is wrong as a figure over a whole book and is printed here with the count beside it.* A figure is a word, a number and a period, and the period is the one of the three that no instrument in this project looks at. **No chapter of the ten puts a period on the wrong one of the four hundreds, and none of the four hundreds appears in the ten at all.**
- **A sweep for the name of the protagonist, for the name at the foot of a struck line and for the phrase the last volume printed zero times across fifty files: 0 in all three.** *A fixed pattern cannot see a name it was not written for, and a name that has never been printed is the correct answer and not a clean row.*

## Eight, the markup

**Method: `python3 tools/measure.py markers`.** Each of the ten files carries exactly **two** real markers of `**`, being one bolded span, and no file returns an odd count. **The fifteen files the tool reports as carrying an odd count are all in `state/archive/` and none of them is a chapter and none of them is one of these ten.** *Blind spot beside this result: the tool strips code spans before counting and a marker inside one is not an unclosed bold, which is item 139 and which this run did not exercise because no file of the ten contains a code span.*

## Eight and a half, the ten titles, and a rule this batch was given and broke in all ten files

**The rule is the outline of record's own, at `outline/volume-12.md` rule seven, and it is a rule and not a taste: *a chapter title names a room, a person and a turn, and it is a title and not an inventory. One name, one room, one turn, under about twenty-five words. And no chapter title states the volume's finding, and no chapter title uses the superseded title of the series plan, and the card heading is a working descriptor and not the title, and the writer writes the title.*** The outline of record is closed and no phase may edit a line of it, and the rule was available to this batch and was not applied to any of the ten.

**Method: the first line of each of the ten files, the text after the chapter number, split on whitespace, one file at a time, taken at the fix pass.** The ten titles ran **25, 38, 26, 27, 37, 25, 29, 29, 31 and 29 words, and eight of the ten are at or over twenty-five and the shortest is exactly twenty-five.** Not one of the ten named a room. **All ten are now under twenty-five — 22, 24, 20, 23, 20, 22, 21, 22, 18 and 24 — and each names a room, a person and a turn**, using the room names the continuity layer already fixes: the shed on the Slade at 0551, 0555 and 0559; the room at the back of that floor at 0552 and 0558; the ground floor of a rented house at 0553 and 0557; the room taken by the week at 0554; the back room at 0556; and the room she has not let at 0560.

**And the other two prohibitions in the same rule, checked and clear.** No title states the volume's finding, and **the one that came closest was `chapter-0559.md`'s, which carried *more of it is not the same as the chance to say no* — that is the volume's argument stated as a maxim, and a title that states the argument is the prohibition, and it is out.** No title uses the superseded title of the series plan. No title is cut off in the middle of a word and none is a comma-separated list of furnishings.

**Why this was missed, and the standing, and it is a sentence.** This project's instruments count people, question marks, columns, years, weeks and words in runs, and **not one of them counts a word in a title, and so a rule with a number in it went unchecked in ten files while six instruments ran clean over the same ten.** The review that found the batch's titles long also recorded that the problem was *not covered by any standing lock*, and that was true of the instruments and false of the volume, because the rule was in the outline of record the whole time and the standing is item 147's: **a rule nobody measures is a rule nobody is keeping, and the file that carries the rule is not the file anybody reads at the end of a batch.**

**And what did not change, so that the fix is not mistaken for a rewrite.** **Ten titles and nothing else.** Not one sentence of the ten chapters was touched by this repair. The paragraph shape is unchanged and still runs **229 paragraphs, 392 sentences, 138 of them single-sentence, 60.3 percent, against 57.0 in the first fifteen files of Volume 11 and 63.6 in its last fifteen** — that rate is inherited and is not a regression in this batch, and it is named here and not acted on, because re-spacing a settled page is a different decision from fixing a rule and this pass made only the second of those.

## Nine, the first draft's figures beside the surviving ones, in one place, because that difference is the only honest measure

| what | first draft | after | what moved it |
|---|---|---|---|
| sentence maximum, volume 12 | 144 in `chapter-0560.md` | 78 in `chapter-0560.md` | forty-three sentences read by hand and broken |
| sentence count, volume 12 | 297 | 392 | the same forty-three |
| sentence mean, volume 12 | 39.663 | 29.454 | the same |
| prose re-prints touching volume 12, twenty words | 3 | 0 | the detector, planted, over Volumes 11 and 12 together |
| prose re-prints touching volume 12, twenty words, **over the whole manuscript** | not run by the writing phase | **1, and then 0** | the fix pass, and the one was thirty-two words at `chapter-0493.md` against `chapter-0551.md`, revoiced |
| prose re-prints touching volume 12, sixteen words | 6 | 0 | the detector and the repository's tool, and one self-run |
| prose re-prints touching volume 12, sixteen words, **over the whole manuscript** | not run by the writing phase | **3, and left at 3** | the fix pass; all three are in the canon sixteen-to-nineteen formula band and naming the band is the repair |
| prose runs, whole manuscript, twenty words, *either* classifier | 2,395 | 2,367 | the same repairs |
| batch words | 12,163 | 11,929 | the same forty-three sentences broken |
| the two protagonist strings | 0 and 2 | 0 and 2 | nothing; the floor was read |

**And the three instruments disagreed with each other twice in this run, and both disagreements are printed above with both figures beside them and neither is settled by subtraction.** A check that returns zero is evidence of nothing until the shape of the damage it is blind to has been checked, and a blind check is written down as blind in the same record that claims it clean.

## The four debts, restated in full for the thirty-first time, and this batch discharges none of them and is not among the phases that could

One: an owed review of Volume 04's Batch 0005, four volumes on. Two, three and four: owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, which is four and not three. And the review gate, which fell back to the writing agent on Volume 11's Batch 0005 and has fallen back on every batch phase the commit history records, and has never once produced a review that could be certified independent, **and a gate that only ever falls back is not a gate that passed either.** `state/phase-ledger.json` is a controller file, no phase may edit it, and it is carried and not repaired. **The number of debts has not moved in eleven volumes and the number of phases that have claimed to discharge one is zero. This phase wrote ten chapters, wrote five state sections and one next-phase prompt, and discharged nothing. Nothing in this project's records can be certified independent, and that sentence is the last thing a writing phase is allowed to say about itself, and a batch is a writing phase.**

---
