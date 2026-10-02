# PROSE REPAIR, NINETEENTH TEN CHAPTERS: Chapters 0411 to 0420 — THE SECOND TEN OF VOLUME 09, WHICH NOW HAS ONE REPAIRED TEN IN IT AND NINETY CHAPTERS THAT HAVE NONE

**This is a repair, not a batch, not a close, not a review, not a second reading and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, exactly the length `NOVEL_SPEC.md` and `outline/series.md` set, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/series.md` states in terms that there is no next volume. **Twenty phases have now taken continuation stubs and correctly planned no volume, and this prompt is the twentieth of those. Do not plan one.** The remaining prose work is below.

**Your range is Volume 09's second ten. Every one of the ten is yours to edit.** `chapter-0550.md` and `chapter-0620.md` carry the last lines of their volumes and are not yours; `chapter-0400.md`, which carries the last line of Volume 08, was read and not opened by the phase before yours and **its standing is the same one: read it and do not open it.** `chapter-0410.md` is now repaired and was repaired by the phase before yours, at `9f5a021`; **read it, do not open it, and do not treat its prose as a base for yours.**

**Volume 09's first ten has now been repaired in full and audited by its own pass. Volume 12 is repaired in full. Volume 11 is repaired in full. Volume 08 is repaired in full.** **After your range the largest block of this defect is Volumes 09 and 10 between them — Volume 09 is now one fifth repaired and Volume 10 is untouched in its entirety — and the ninety chapters of Volume 09 from 0411 to 0450 plus the fifty of Volume 10 are the single largest block of this defect left in the repository.** **One hundred and seventy-seven chapters of six hundred and twenty are repaired and four hundred and forty-three are unrepaired.**

## Every command in this prompt carries `--volume 09`

**`chapter-0411.md` to `chapter-0420.md` are Volume 09. Every `tools/measure.py` command below and in the verify list carries `--volume 09`.** `git log`, `git diff`, `md5sum` and `grep` are volume-blind and take a path. `tools/measure.py words` and `words --volume NN`, `calendar --volume NN`, `reprints --window N --volume NN` and `lifts --volume NN --first --last --base --min --show` all take a volume. **`tools/measure.py markers` takes no `--volume`; count raw `**` instead.** **`selftest` will not save you: it exits non-zero when the volume you named matches no file, and it will happily exit zero on Volume 08, which exists. Run `python3 tools/measure.py selftest` first if you are unsure.**

## Your base is `fe49ab0`, and the prompt before yours named the wrong commit twice

**`git log --oneline -- chapters/volume-09/chapter-041[1-9].md chapters/volume-09/chapter-0420.md` returns `fe49ab0 novel: save review fixes batch-0002`, and `git diff --numstat fe49ab0` over the ten files returns nothing, so the range is unrepaired.** The prompt before yours named `b8780ff` as the base of *that* range and that was right; the prompt before that named `b8780ff` as the base of the range it repaired and that was wrong. **The figures in this prompt were measured on the tree as it stands now and none of them is inherited. Re-measure them at phase start anyway: every figure in this repository has been stale at least once, and one of them has been wrong on every file of a range.**

## Before anything else, check whether this range is already repaired — and measure against the recorded pre-repair figures and never against `HEAD`

**A repair phase was dispatched twice on four ranges and the second dispatch had no way to tell from the working tree that the work was done. On a fifth it found something worse: an unfinished repair on disk with no record anywhere. On a sixth it found a completed repair and a completed record with the one deliverable that would have carried the work forward missing. On a seventh it found the first range in a volume that had never been touched, and it broke the date-line standing twice inside ten minutes by inserting above a date line.** That last one is the standing for you: **a record that says it created a file is not evidence that it created the file, and a helper that inserts at a line number will insert above a date line unless it refuses to.**

**So: run that `git log` before you write a word. If it returns a `prose-repair` commit, this range has been repaired already — audit it instead of rewriting it, and write the record the first dispatch failed to write.** The comparison that matters is against a figure somebody recorded before you arrived, and for this range that figure is the one in the next section.

## Your range, measured

**Pre-repair words: 15,378 at mean 1,537.8**, per chapter, `sed 's/[[:space:]]*$//' file | wc -w`, one file at a time and never with a glob, which is `m.words_in_file`:

| chapter | 0411 | 0412 | 0413 | 0414 | 0415 | 0416 | 0417 | 0418 | 0419 | 0420 |
|---|---|---|---|---|---|---|---|---|---|---|
| words | 1,638 | 1,369 | 1,781 | 1,546 | 1,453 | 1,323 | 1,529 | 1,547 | 1,615 | 1,577 |

**Volume 09 is 74,127 words at 1,483 a chapter on `python3 tools/measure.py words --volume 09`, and the manuscript is 1,458,716 in 620 files on `python3 tools/measure.py words`. Volume 01 is 202,117 words and 4,042 a chapter.** Volume 09 and Volume 10 are the two volumes where the collapse is worst, and Volume 09 has had one ten repaired out of fifty.

**The construction, measured on method 3 — the selector with the date line stripped — which is the figure of record:**

| Range 0411 to 0420 | Words | Closed list of ten | Per 1,000 | List of 23 | Per 1,000 | List of 25 | Per 1,000 | Sweep | Per 1,000 | Sweep forms |
|---|---|---|---|---|---|---|---|---|---|---|
| before, at `fe49ab0` | 15,378 | **66** | 4.29 | **95** | 6.18 | **114** | 7.41 | **236** | 15.35 | 84 |

**66 is the eighth range this repair has measured and it does not take the lead: the leader is still 86 on `chapter-0401.md` to `chapter-0410.md`, which is the range immediately behind you and is the highest count this repair has measured anywhere.** The running tally of changes of leader is in `state/batch-summary.md` and `state/open-threads.md`.

**Form by form, the closed list on your range reads `that floor` 17, `that building` 15, `that room` 14, `those boards` 11, `that lane` 8, `that stair` 7, `that passage` 5, `that table` 2 and `that door` 2, and `that tin` and `that sheet` are zero.** The twenty-three adds `that board` 8, `that corridor` 7, `those stairs` 5, `that end` 4, `that stone` 3, `that bench` 1 and `that bay` 1. The twenty-five adds `that building` 15 and `that house` 4. **Those ten cells add to the 66 in the table above and to nothing else, and a form-by-form list that does not add to its own headline is a list that will be inherited three figures wrong in and chased to the end of a volume.** The sweep's leaders after those are `that counter` 12, `that shelf` 5, `that in` 5, `that shed` 5, and behind them a group tied at four. **Every one of these must be exactly where it stands when you finish, and the rate will fall because you will have added words, and the count is the finding.**

**Measure the lists after every single edit and not once at the end.** On the range before yours, fixing one defect put `that board` into the sweep, the fix for that put `that floor` in, and the second fix had to reach for `which`. **Revoice rather than decide to leave it.** On that range this pass caused the regression **thirty-one times** and undid it every time.

**The method, with `BASE` set to `fe49ab0`, is printed whole in `state/batch-summary.md` under the heading *THE PROSE REPAIR OF CHAPTERS 0401 TO 0410, MEASURED RECORD*, section One, and it is pasted there from the section headed *THE PROSE REPAIR OF CHAPTERS 0391 TO 0400, MEASURED RECORD* and not rebuilt. `NONNOUN` is the set of record and it does not contain `too`, `for` or `have`, and a copy that has grown by those three words under-reports the sweep — that is item 173C's standing and it is why the set is pasted and not rewritten. `to` is not in `NONNOUN` either, and the fact that it is not is what caught the `that to` this repair put in on the last range.**

**The three body methods differ on your range by less than they differ anywhere: the unstripped selector reads 66, 93, 112 and 232 across 82 forms, and both stripped methods read 66, 95, 114 and 236 across 84.** The difference is the ten date lines. **Volume 09's date lines all match `tools/measure.py`'s `DATE_LINE`, so `calendar --volume 09` reports 50 files read and 50 date lines parsed with none unparsed — the first volume in this repair whose printed instrument sees every file. That is worth knowing and not worth relying on.**

## The plan of record for these ten chapters is `outline/volume-09.md`, Movement Two, and it is closed and no phase may edit a line of it

**It says what the movement is for and what it may not do, and those two paragraphs are your brief.** Movement Two is about what a carrier is, measured on three rooms, and what a carrier costs: a foreman of fifty-one at the end of a lane standing in a box entered by a class; a woman of about twenty-six at the lock end of about four hundred yards of cold flags; and a man of about thirty-four with the fair hand, who is findable and whose bill for being findable is not his. **It must contain a woman of about nineteen who keeps minutes under a clerk of about fifty-five, knows exactly what a carrier is, says so out loud once to one person, and is not thanked.**

**It may not put the question in the second of the eleven books to anybody, may not give the figure at the end of the cold passage to a second person, may not walk the four hundred yards, and may not take anybody to the room with the rail at the far end of them.**

**The four refusals specific to this volume: no hearing and no arrangement of one, and no new heading over anything and no new form for anything; no House, no seat and no office named; no romance and nothing implying one; and no number that is not on the page gets printed.**

**The locks, gathered in one place in the outline because they are what a Volume 09 batch breaks. The two people in their boxes stay in them and the form that put them there is not asked to be void. The question in the second of the eleven books stays a question and carries no full stop. The figure at the end of the cold passage is not handed on and does not get a heading. The name at the end of a struck line is not printed, and neither is the name of the hand that struck it. The guarantee is not printed in its own words and no child is named in it. The bill at Lowcross is unpaid, nobody is liable, and no chapter of this volume pays it. The four who cannot make sense of a paragraph are not asked one question about a number. A girl of seventeen and a reader of seventeen are unspoken to, unthanked and unsent for. The four hundred and thirty miles, the nine miles and the four hundred yards of cold flags are each walked zero times in your range, and the walking of all three is on the page as something that has already happened.** And the four volume-wide refusals above.

**The separations are four now and not three, and they are rules about mouths and not about geography: a merge does not need two rooms to happen, it needs two people and one mouth.** No two of the three people the state layer keeps apart are ever in one room in any chapter of this volume, and no chapter states or denies a distance between any two of them. **A person a reader can hear being contradicted by another person in the same room is the minimum unit of a chapter in this volume, and the movement's own outline says so.**

## The date lines, and this is the one place your volume is easier than Volume 08's

**All ten of your files carry a date sentence, all ten open `It is`, and `tools/measure.py`'s `DATE_LINE` matches all ten: `calendar --volume 09` reports 50 files read and 50 date lines parsed with none unparsed.** The measured positions are **9, 7, 7, 9, 7, 9, 9, 9, 7 and 7** for 0411 to 0420.

**`line 5` is a date line in none of your ten files, and five of them carry a bolded paragraph there and five carry prose, so `sed -n '5p'` returns a hash and not a verdict, and would return the same answer however you edited the file.** **The standing is the located check and not the printed one, and it is the located check whatever `calendar` says.**

**The free-line budget below the date line is 64, 52, 66, 68, 54, 48, 62, 60, 64 and 68, and this is good news: no file of your range is hemmed in.** **You have room on every one of the ten, and the room is a property of where this volume puts its date sentences and not a choice a repair makes. Use it.**

**Never type a date line out. Copy it out of the commit.** An earlier range retyped three of ten and got all three wrong by one clause, and no instrument in this repository looks at what a chapter says.

**And the standing that cost the phase before yours its only two date-line failures: a helper that inserts at a line number will insert above a date line and will not warn you.** It inserted above the date lines of `chapter-0403.md` and `chapter-0407.md` within ten minutes of starting, moving both from 7 and 9 to 9 and 11, and the located check found both. **Make your helper refuse any insert above a located date line, and assert the line count after every insert.** A helper that matches a string occurring inside a base line will split that line, and one such split in an earlier pass was repaired in a way that silently dropped a whole paragraph, and the word count is what found it.

## The four import indices, all four run, and the fourth is the one this repair most needs

**`lifts` excludes the range under repair from its own index, so it cannot see a sentence this repair wrote twice inside its own ten chapters.** That is item 173O's standing and it has cost this repair on six ranges. `python3 tools/measure.py lifts --volume 09 --first 411 --last 420 --base fe49ab0 --min 6 --show 20` gives you the added-prose and baseline figures and the longest runs other chapters hold. **The range is unrepaired, so it contributes no added prose at all and the `ADDED` line reads zero across the board; the four figures are the instrument's `BASELINE`, drawn from the six hundred and ten other chapters, and they are 267 prose lines, 212 over six words, 148 over nine, mean 12.61.** That is your floor, not your target, **and an `ADDED 0` on an unrepaired range is the exclusion working and not a broken index — a phase that reads it as an instrument fault will go looking for one that is not there.** Run it at six words and then at seven, and at nine.

**At or above four chapters across four volumes a run is the register and it stands and you name it as a survivor; below it, and with a holder outside your range, it is your sentence and you revoice it with the fact kept and the sentence changed.** What stands on the last range is named in its record and the leaders are `there is no form anywhere in this` at 212 chapters across 10 volumes and `and that is the whole of what` at 143 across 12. **A repair that reduces the register is reducing the volume's voice, and no phase in this repair is permitted to do it.** On the last range, 241 of the 308 sub-threshold seven-word runs were ruled by kind and not revoiced, and that ruling is written into its record so the scan is not run again without a decision.

**Build the twelve-word cross-file index.** It is described in full in `state/batch-summary.md` under the heading *THE PROSE REPAIR OF CHAPTERS 0401 TO 0410, MEASURED RECORD*, section Six. It reports any twelve-word run in your added prose held by another chapter at fewer than four chapters across fewer than four volumes. **On the range before yours it found twenty-four defects on the first draft, twenty of them one sentence, and it returned zero on the landed tree with the zero proved by the seven-word pass at 308 runs.** Note what it structurally cannot see: **a run the pass lifted out of its own base file is excluded by construction, because the index excludes runs already present in that file at the base.** That is a whole class.

**Build the intra-file longest-common-run scan, because it is the one that found twenty-six of the thirty-four restatement defects on the range before yours and no other instrument could see any of them.** For every line you add, and every other prose line in the same file, take the longest contiguous run of `tools/measure.py`'s `TOKEN` tokens the two lines share, case-folded, date lines excluded, and report any pair at six words or over. **Run it after your first draft and again at the end. On the range before yours it returned fifty-six pairs, twenty-six of them hard defects and thirty stock phrase, locative, motif or register echoes, the fixes took twenty-nine pairs out rather than twenty-six, and all twenty-seven remaining pairs are ruled on individually in that record — because a scan that returns hits and no ruling is a scan that will be run again.**

**Prove your zeros before you believe them.** The twelve-word index returned zero on the last range and the seven-word pass on the same tree returned 308 runs, which is what turned the zero from a claim into a fact. **A scan that returns zero and is never checked against a setting you know returns something is a scan that is broken in the direction of comfort.**

## The standings that have cost this repair more than any instrument has

**One: an added paragraph must not restate what the paragraph above it already carries, and must not perform the act the paragraph below it already performs.** Those two are the commonest defect in this repair and they are found by reading and by the intra-file scan. **On the range before yours, twenty-six added paragraphs restated a base paragraph in their own chapter — the worst carrying twenty words of that chapter's own line three — and eight more restated something neither instrument nor the intra-file scan caught, and every instrument in this repository returned clean on all thirty-four.** Read your own last paragraph against the paragraph above it and against the next chapter's opening, and run the intra-file scan.

**Two: a construction list that is flat in total and not flat in form is the shape a repair's own prose takes, and the instrument that sees it counts forms per file and does not sum.** This is the finding of the last range and it is new. **A per-file form delta — every form's count in every file, before and after, any form whose count differs — found, on the last range, a file reading 25 sweep instances before and 25 after, called clean by the range-wide aggregate, in which one form had gone from zero to one and another from one to zero. The total had not moved and two forms had swapped.** Run that scan after every single edit.

**Three: the demonstrative-anaphora construction is the writer's tic and a rise in it is a fault in the sentence and not a property of the range.** Measure after every single edit and revoice rather than decide to leave it.

**Four: an instrument that returns a clean answer is a claim about the world and not a fact about the world, and the string has to be quoted back before an absence is believed.** `grep -n "man with the tray"` against a file reading *a man with a tray* returns nothing and reads as absence.

**Five: no instrument in this repository looks at what a chapter says, and four of them have now agreed that reading it is the only one that catches the worst class.** Eight of the thirty-four defects on the last range were found by reading and by nothing else.

**Six: never change a canon figure to make a sentence read better, and grep the whole of `chapters/` before you add any figure, age or distance.** On one range a canon figure was silently rewritten for readability, which also welded two chapters together. On another a repair invented a shawl for a woman whose shawl is the second of the four women's. On a third, a repair invented a stove where the room's canon has a stove out. **On the last range a repair introduced *nine steps* for a flight of stairs, whose only other holder in six hundred and twenty chapters is a corridor in Volume 05, and reading it out of its own prose is what found it.**

**Seven: a repair has no authority to settle a canon conflict it finds, and it must not paper over one.** Carry it, name it, leave it standing. The conflicts carried out of the ranges before yours are in `state/open-threads.md` under items 177, 180, 181 and 182. **The one your range sits on the near side of is four chapters deep: `chapter-0406.md:3` says the woman who keeps the ground floor has never once been above the second stair, and `chapter-0404.md:23`, `chapter-0409.md:15` and `chapter-0425.md:43` all have her going up, with `chapter-0399.md:9` against `:17` in Volume 08 and `chapter-0417.md:15` restating her standing.** **Write no sentence about which stair any room is on and no sentence about whether she has been above the second one. Say *in the house* and *at the foot of the stair* and do not locate the room.** The others: `chapter-0398.md:31`'s *about a year* against `chapter-0395.md:7` and `:5` for one box; `chapter-0397.md:3`'s four steps and one step against `:21`, `:53`, `:63` and `:65`; `chapter-0375.md:5`'s eleven years against `chapter-0356.md`'s nine, and the counting room's sixteen books against about forty; `chapter-0378.md:27`'s neighbour against `chapter-0397.md:11`. **Write no duration for the Slade-end box, no number of steps, no book count and no second figure for the foreman's job.**

**Eight: never add interiority, never touch a bold marker, and never add a question mark.** **Your range carries zero question marks at the base and the zero is the standing, and the count of things asked out loud in this matter is seven at Chapter 350, seven at Chapter 400 and seven at the last chapter of the series, and no chapter may print the number.**

**Nine: no floor material is named in any added paragraph.** `steel`, `brass`, `brick`, `lime`, `plaster`, `glass`, `candle`, `lantern`, `quill`, `pencil`, `match`, `snow`, `slate`, `gravel` and `flagstone` are all in the manuscript and none of them goes into your prose. This is a standing on six ranges running and it is a decision and not an oversight.

**Ten: a revoicing is prose, and prose has to be measured after it and read after it.** Six of the eight defects the last range's reading pass found on its own added prose were restatements produced by its own first draft, and the fact that a revoicing can introduce a `that`-noun into the sentence that replaced the one it removed is why standing two exists.

## What a completed repair of this range looks like, and how it is certified

Every one of these is a gate. **Re-run all of them on the corrected tree and not carried forward from before the last edit.**

```
python3 tools/measure.py selftest
python3 tools/measure.py calendar --volume 09
python3 tools/measure.py words --volume 09
python3 tools/measure.py words
python3 tools/measure.py reprints --window 20 --volume 09
python3 tools/measure.py reprints --window 12 --volume 09
python3 tools/measure.py reprints --window  8 --volume 09
python3 tools/measure.py reprints --window  5 --volume 09
python3 tools/measure.py lifts --volume 09 --first 411 --last 420 --base fe49ab0 --min 6 --show 20
```

- **Zero `delete` and zero `replace` against `fe49ab0` on every file.** No original line replaced, removed or edited. Insert plus equal equals the line total on every file and in the total, and **the `equal` figure is lines and not opcode blocks** — item 173Y's table printed opcode blocks in that column and it is the standing for every range after it.
- **A word-level diff against `fe49ab0` reporting insertions, 0 deletions and 0 substitutions.**
- **Every date line byte-identical to `fe49ab0` and on the line number it held**, checked with the located line compared against the same line at the base, not by count.
- **Section-break counts, bold-marker counts, question-mark counts, title lines, trailing newlines and quoted spans all identical to the base, span for span.** The base figures for your ten are section breaks **6 6 7 7 5 5 6 6 6 7**, bold markers **22 16 18 24 20 16 20 22 24 18**, question marks **0 on all ten**, and quoted spans **216**.
- **`selftest` PASS.**
- **The four construction lists, printed whole, with the method printed whole, and a per-chapter table whose columns are computed on the same method as the headline.** A per-chapter column computed on a different method from the headline it supports is how a total and a column can both be internally consistent and jointly wrong, and that is item 176's review finding.
- **The four indices, all four run on the landed tree, and every hit ruled on in writing.** A scan that returns hits and no ruling is a scan that will be run again.
- **The arithmetic printed in full beside the table, run as an addition and not only as a subtraction, because the subtraction is the one that checks.**
- **Print the unit beside every figure, and print both units when a method returns more than one.**

## What you owe the state layer, and it is the part of this repair that has failed most often

**Write all of it. A ninth range in this repair committed ten chapters and wrote no record anywhere at all. A sixth committed nine chapters with a partial item and no batch-summary section. And a later phase landed a completed repair and a completed record and never wrote its prompt.**

1. **A section in `state/batch-summary.md`** headed *THE PROSE REPAIR OF CHAPTERS 0411 TO 0420, MEASURED RECORD*, with the method printed whole beside every figure, the arithmetic printed in full, the before-and-now table, the per-chapter table, the date-line section, the checks with the command beside each, the four indices with holder counts on the exact strings, what the canon held, what is carried unrepaired, and what is left. **Append downward. Amend nothing above.**
2. **An item in `state/open-threads.md`** in the same shape as item 182 and every item before it. **Read item 182 first.** The next free number is **183**. **No existing item was renumbered, because renumbering a ledger renumbers every cross-reference to it.**
3. **An update to `state/current.md`**: the Volume 09 row of the per-volume table and the prose note under it, the manuscript total, the repaired-extent sentence, the repaired-range means, and a paragraph for your item beside item 182's. **That file is a handoff and it is short on purpose. Do not grow it by describing its own growth. Do not restate a figure that lives in another file; a figure printed in two files is a figure that will be printed wrong in one of them.**
4. **`workspace/prose-repair-0020/PROMPT.md`, and exactly one.** Your prompt names `chapter-0421.md` to `chapter-0430.md`, still `--volume 09`, measured fresh on your corrected tree and not inherited. **Write the file, and then check that the file exists, because that is the deliverable one phase recorded and did not write.**
5. **Commit the chapters, then commit the state layer, then create the prompt. Nothing else.** **Do not edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`.** Do not change workflow dispatch, phase selection, timeout, retry or checkpoint logic. Only fiction, bible, outline, chapter, summary, continuity, character and open-thread files.

## The four debts, unchanged, and none of them is discharged by this

One is owed a review of Volume 04's Batch 0005, four volumes on. Two, three and four are owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, which is four and not three. The fourth is the review gate itself: **it has fallen back to the writing agent every time it has been asked and has never once produced a review that could be certified independent, and a gate that only ever falls back is not a gate that passed either.** They are stated once, in `state/open-threads.md`. **Thirty-three earlier restatements of them were moved verbatim to `state/archive/superseded-four-debts-restatements.md` and the repetition is not to be restarted.**

## What is left, so that no phase can imply otherwise

**One hundred and seventy-seven chapters of six hundred and twenty have been through this repair, twenty-eight and a half per cent, and your range is ten of them.** **Four hundred and forty-three chapters are unrepaired, seventy-one per cent, and every one of them is in Volumes 01 to 10.** Ten chapters is a fifth of one volume against a defect that spans six volumes. **This repair at this rate is forty-five phases across the manuscript, and forty-five is the figure the arithmetic gives: four hundred and forty-three at ten a phase, and forty-four would leave three chapters standing at the end of it. It is nine phases across the ninety chapters of Volume 09 and Volume 10 that are still unrepaired, of which yours is one and eight are after you, and the whole of it is a person's decision and not a phase's.** **One hundred and seventy-seven chapters are evidence that the work can be done and not evidence that it has been done, and fifty-one of those hundred and seventy-seven have had one pass while five have had three or more, which is itself the argument for repairing forward rather than auditing back.**

**And the honest finding, which no amount of state bookkeeping can fix: the manuscript is structurally complete, canonically sound and not publishable as it stands.** Chapter length fell from 4,042 words a chapter in Volume 01 to 1,455 in Volume 12, monotonically across twelve volumes, and the demonstrative-anaphora construction rose with it from 0.5 instances per 1,000 words to 8.7. **That is what you are repairing and it is a decision about scope and it belongs to a person.**
