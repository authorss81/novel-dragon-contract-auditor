# CORRECTION LANDED AFTER THIS PHASE RAN - THE SCOPE BLOCK BELOW IS VOID ON THIS RANGE

**This phase has finished. `workspace/prose-repair-0018/.done` exists, and the sentinel is the last file it wrote, not the first.**

**The `SCOPE OF THIS RUN` block immediately below is void on `chapter-0401.md` to `chapter-0410.md`, and it was added by `da38f4b novel: retire obsolete planning phases` after the range had already been repaired.** It contradicts this file's own gate further down, which says that if `git log --oneline -- chapters/volume-09/chapter-040[1-9].md chapters/volume-09/chapter-0410.md` returns a `prose-repair` commit, the range has been repaired already and is to be **audited instead of rewritten** — and it contradicts state items 182, 185, 187, 190, 191, 195, 197, 198 and 199, four of which state in terms that they wrote no prose on this range. **The range was repaired at `9f5a021` and then audited and revoiced by ten further records, so a phase obeying the block below writes 240 words into a finished range and records nothing, which is what happened: five paragraphs and 240 words were added to `chapter-0401.md` through `chapter-0405.md` and every figure in the state layer went stale by exactly that.**

**All five were withdrawn at item 200 by restoring the five files from `73df9a8`, and the range stands at 18,972 words against the 14,325 at its pre-repair base `b8780ff`.** The block was not rewritten, because it is a controller artifact and what that revision was meant to do is not this file's to say. **If this phase is dispatched again, the gate at the foot of this file governs and the block below does not.** The full record is in `state/batch-summary.md` under the heading *THE REVIEW FIX OF PROSE-REPAIR-0018, MEASURED RECORD*.

---

# SCOPE OF THIS RUN - READ FIRST

**This run writes Chapters 401 to 405 and nothing else.**

Chapters 406 to 410 are a later phase's work. Ignore any
instruction below that requires you to write them.


1. **Write the chapters.** Chapters 401 through 405, in ascending order. Start with the first one in your very
   first action: create that chapter file before doing anything else.
2. **Do not attempt any close, audit, or planning duty** listed below. Those
   belong to later phases. Ignoring them is required; attempting them fails this
   run.
3. **Do not create a next-phase prompt.** The pipeline creates it.
4. **Update only the state files** these chapters require, and nothing else.

Every rule below still binds the prose you write. But if a rule cannot be
satisfied inside this run's chapters, write the chapters anyway and record the
unmet rule in `state/open-threads.md` for a later phase.

**Producing finished chapters is the success condition for this run. Returning
without writing any chapter is a failure.**

# PROSE REPAIR, EIGHTEENTH TEN CHAPTERS: Chapters 0401 to 0410 — AND THIS IS THE FIRST TEN OF VOLUME 09, WHICH HAS HAD NO REPAIR OF ANY KIND IN IT

**This is a repair, not a batch, not a close, not a review, not a second reading and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, exactly the length `NOVEL_SPEC.md` and `outline/series.md` set, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/series.md` states in terms that there is no next volume. **Nineteen phases have now taken continuation stubs and correctly planned no volume, and this prompt is the nineteenth of those. Do not plan one.** The remaining prose work is below and it is most of the manuscript.

**Your range is Volume 09's first ten and it is the chapter `chapter-0401.md` opens Volume 09 on.** Every one of the ten is yours to edit. `chapter-0550.md` and `chapter-0620.md` carry the last lines of their volumes and are not yours; `chapter-0400.md`, which carries the last line of Volume 08, was read and not opened by the phase before yours and **its standing is the same one: read it and do not open it.**

**Volume 11 is repaired in full and has been audited as well as repaired. Volume 12 is repaired in full. Volume 08 is repaired in full, and its fifth and last ten has now been repaired, audited and re-audited.** **After your range the largest block of this defect is Volumes 09 and 10 between them, and your range is the first ten of one of them.** **One hundred and sixty-seven chapters of six hundred and twenty are repaired and four hundred and fifty-three are unrepaired.** Volumes 09 and 10 were untouched in their entirety and are now one repaired ten smaller.

## Every command in this prompt carries `--volume 09`, and a phase that carries the previous prompt's flag forward will measure Volume 08 and get a clean answer

**`chapter-0401.md` to `chapter-0410.md` are Volume 09. Every `tools/measure.py` command below and in the verify list carries `--volume 09`.** `git log`, `git diff`, `md5sum` and `grep` are volume-blind and take a path. `tools/measure.py words` and `words --volume NN`, `calendar --volume NN`, `reprints --window N --volume NN` and `lifts --volume NN --first --last --base --min --show` all take a volume. **`tools/measure.py markers` takes no `--volume`; count raw `**` instead.** **`selftest` will not save you: it exits non-zero when the volume you named matches no file, and it will happily exit zero on Volume 08, which exists. Run `python3 tools/measure.py selftest` first if you are unsure.**

## Your base is `b8780ff`, and the prompt before yours named the wrong commit twice

**`git log --oneline -- chapters/volume-09/chapter-040[1-9].md chapters/volume-09/chapter-0410.md` returns `b8780ff novel: save review fixes batch-0001`, with `d264a08 novel: save writer work batch-0001` before it, and that is the base of every figure in this prompt.** `git diff --numstat b8780ff` over the ten files returns nothing, so the range is unrepaired.

**The phase before yours repaired Volume 08's last ten and the prompt it worked from named `b8780ff` as the base of *that* range, which was wrong: `b8780ff` is the base of this range.** The range it actually repaired has base **`a9a6b52 novel: save review fixes batch-0005`**. Two figures in that prompt were stale and both were named in the record rather than corrected in place; one of them, its free-line counts below the date lines, was wrong on every file of the ten. **The figures here were measured on the tree as it stands now and none of them is inherited. Re-measure them at phase start anyway: every figure in this repository has been stale at least once.**

## Before anything else, check whether this range is already repaired — and measure against the recorded pre-repair figures and never against `HEAD`

**A repair phase was dispatched twice on four ranges and the second dispatch had no way to tell from the working tree that the work was done. On a fifth it found something worse: an *unfinished* repair on disk with no record anywhere. On a sixth it found a completed repair and a completed record with the one deliverable that would have carried the work forward missing: `workspace/prose-repair-0018/PROMPT.md`, which is this file, was recorded as created by the phase before yours and did not exist.** That last one is the standing for you: **a record that says it created a file is not evidence that it created the file, and check the file.**

**So: run that `git log` before you write a word. If it returns a `prose-repair` commit, this range has been repaired already — audit it instead of rewriting it, and write the record the first dispatch failed to write.** The comparison that matters is against a figure somebody recorded before you arrived, and for this range that figure is the one in the next section.

## Your range, measured

**Pre-repair words: 14,325 at mean 1,432.5**, per chapter, `sed 's/[[:space:]]*$//' file | wc -w`, one file at a time and never with a glob, which is `m.words_in_file`:

| chapter | 0401 | 0402 | 0403 | 0404 | 0405 | 0406 | 0407 | 0408 | 0409 | 0410 |
|---|---|---|---|---|---|---|---|---|---|---|
| words | 1,916 | 1,622 | 1,346 | 1,423 | 1,320 | 1,173 | 1,568 | 1,190 | 1,145 | 1,622 |

**Volume 09 is 69,362 words at 1,387 a chapter on `python3 tools/measure.py words --volume 09`, and the manuscript is 1,453,951 in 620 files on `python3 tools/measure.py words`. Volume 01 is 202,117 words and 4,042 a chapter.** Volume 09 and Volume 10 are the two volumes where the collapse is worst and nothing has been touched, and your range is the first ten chapters anyone has repaired in either of them.

**The construction, measured on method 3 — the selector with the date line stripped — which is the figure of record:**

| Range 0401 to 0410 | Words | Closed list of ten | Per 1,000 | List of 23 | Per 1,000 | List of 25 | Per 1,000 | Sweep | Per 1,000 | Sweep forms |
|---|---|---|---|---|---|---|---|---|---|---|
| before, at `b8780ff` | 14,325 | **86** | 6.00 | **110** | 7.68 | **120** | 8.38 | **240** | 16.75 | 87 |

**86 is the highest count this repair has measured anywhere, on a range whose mean is 1,432.5 words.** The five ranges of Volume 08 before yours read 33, 34, 7, 34 and 56 on the same list, and **the fifth of those five took the lead at 56 and yours takes it back at 86, which by the running tally in `state/batch-summary.md` and `state/open-threads.md` is the seventh change of leader in seven ranges — the sixth of the seven being `chapter-0391.md` to `chapter-0400.md` at 56.** **A range whose count is high is a range where the writer's tic is the construction, which is exactly the tic that a repair under length pressure produces, and the last two ranges in Volume 08 each took four or more revoicing passes for that reason.**

**Form by form, the closed list on your range reads `that floor` 31, `that room` 21, `those boards` 15, `that lane` 7, `that passage` 4, `that door` 3, `that table` 2, `that stair` 2, `that sheet` 1 and `that tin` 0, and the twenty-three adds `those stairs` 11, `that board` 5, `that stone` 4, `that end` 2, `that bench` 1 and `that case` 1, and the twenty-five adds `that building` 5 and `that house` 5.** **Those ten cells add to the 86 in the table above and to nothing else, and a form-by-form list that does not add to its own headline is a list that will be inherited three figures wrong in and chased to the end of a volume.** The sweep's leaders after those are `that counter` 15, `that week` 5 and `that in` 4, and behind them seven forms are tied at three: `that bag`, `that doorway`, `that for`, `that on`, `that stool`, `that wall` and `that window`. **Every one of these must be exactly where it stands when you finish, and the rate will fall because you will have added words, and the count is the finding.**

**Measure the lists after every single edit and not once at the end.** On the last range in Volume 08, fixing one defect put `that gets` into the sweep, the fix for that put `that standing` in, and the second fix had to reach for `which`. **Revoice rather than decide to leave it.**

**The method, with `BASE` set to `b8780ff`, is printed whole in `state/batch-summary.md` under the heading *THE PROSE REPAIR OF CHAPTERS 0391 TO 0400, MEASURED RECORD*, section One, which is the record standing immediately above this range's re-audit and not the re-audit itself, and it is pasted there from the section headed *THE PROSE REPAIR OF CHAPTERS 0551 TO 0560* and not rebuilt. `NONNOUN` is the set of record and it does not contain `too`, `for` or `have`, and a copy that has grown by those three words under-reports the sweep — that is item 173C's standing and it is why the set is pasted and not rewritten. `to` is not in `NONNOUN` either, and the fact that it is not is what caught the one sweep instance a previous pass put in.**

**The three body methods differ on your range by less than they differ anywhere in Volume 08, and the difference is still the date lines: the unstripped selector reads 85, 107, 117 and 231 across 83 forms, and both stripped methods read 86, 110, 120 and 240 across 87.**

## The plan of record for these ten chapters is `outline/volume-09.md`, Movement One, and it is closed and no phase may edit a line of it

**It says what the movement is for and what it may not do, and those two paragraphs are your brief.** It opens on the counter at the top of four flights, eleven years after a box of about four hundred blanks went under it, and on the fee board behind that counter, which carries four items and not one of them time. It must contain the older woman at the other end of the same boards saying once, out loud, what a carrier is, and not being thanked; the young man from the shipping floor, who told her in Chapter 0391 that a clerk who moves a box is a clerk who has made a statement about it; and a man from the yard with a satchel, who is a courier and cannot be told anything and asks for nothing.

**It may not send anybody, may not thank anybody, may not fill a ruled space under a printed heading, may not walk the four hundred yards, may not put a question to anybody, and may not move the number of things asked out loud in this matter.**

**The count of things anybody has asked out loud in this matter is seven, and it is printed in no chapter of this volume and may be printed in none you write. Nobody is thanked, nobody is forgiven, nobody is sent for, and nothing is resolved.** **No new person, no new fixture, no new figure, no new plot.**

**The calendar, and it is one line of arithmetic you must not do.** A month in this calendar is four weeks and the day inside the week is the inherited cycle of second, second, fourth, fourth, restarting with each month. **Never compute a month-count. No calendar month name and no weekday name goes into anything this project writes, including this record.** **The seventh named year is the year after the year after the year after the year after the year after next, written out in full at every occurrence and abbreviated nowhere, and all ten of your date lines carry it. Do not shorten it and do not move a date line.** `chapter-0401.md` is the second day of the first week of the second month of that year, and that is the only date in the outline and no phase may write a second one.

**The locks, gathered in one place in the outline because they are what a Volume 09 batch breaks.** The two people in their boxes stay in them and the form that put them there is not asked to be void. The question in the second of the eleven books stays a question and carries no full stop. The figure at the end of the cold passage is not handed on and does not get a heading. The name at the end of a struck line is not printed, and neither is the name of the hand that struck it. The guarantee is not printed in its own words and no child is named in it. The bill at Lowcross is unpaid, nobody is liable, and no chapter of this volume pays it. The four who cannot make sense of a paragraph are not asked one question about a number. A girl of seventeen and a reader of seventeen are unspoken to, unthanked and unsent for. **The four hundred and thirty miles, the nine miles and the four hundred yards of cold flags are each walked zero times in your range, and the walking of all three is on the page as something that has already happened.** And the four refusals specific to this volume: **no hearing and no arrangement of one, and no new heading over anything and no new form for anything; no House, no seat and no office named; no romance and nothing implying one; and no number that is not on the page gets printed.**

**The separations are four now and not three, and they are rules about mouths and not about geography: a merge does not need two rooms to happen, it needs two people and one mouth.** No two of the three people the state layer keeps apart are ever in one room in any chapter of this volume, and no chapter states or denies a distance between any two of them. **A person a reader can hear being contradicted by another person in the same room is the minimum unit of a chapter in this volume, and the movement's own outline says so: a room is not a scene until somebody in it is contradicted by somebody else in it, and the first movement of Volume 08 had ten rooms and almost no contradictions.**

## The date lines, and this is the one place your volume is easier than the last

**All ten of your files carry a date sentence, all ten open `It is`, and `tools/measure.py`'s `DATE_LINE` matches all ten: `calendar --volume 09` reports 50 files read and 50 date lines parsed with none unparsed.** That is the first volume in this repair whose printed instrument sees every file, and it is worth knowing and not worth relying on. The measured positions are **7, 9, 7, 9, 7, 7, 9, 9, 9 and 7** for 0401 to 0410.

**`line 5` is a date line in none of your ten files**, and every one of the ten carries prose there — `chapter-0401.md`'s line 5 is a bolded paragraph and `chapter-0402.md`'s is the line that names Tamsin Rook — so `sed -n '5p'` returns a hash and not a verdict, and would return the same answer however you edited the file. **The standing is the located check and not the printed one, and it is the located check whatever `calendar` says:** the located date-line check is what caught five paragraphs inserted above three date lines on the range before last, and the located check is what you will use.

**The free-line budget below the date line is 74, 56, 48, 48, 56, 42, 58, 34, 34 and 60, and this is good news: no file of your range is hemmed in.** The last four ranges of Volume 08 each had files with four and eight free lines, and one of them grew by 149 words. **You have room on every one of the ten, and the room is a property of where this volume puts its date sentences and not a choice a repair makes. Use it.**

**Never type a date line out. Copy it out of the commit.** An earlier range retyped three of ten and got all three wrong by one clause, and no instrument in this repository looks at what a chapter says.

## The four import indices, all four run, and the fourth is the one this range most needs

**`lifts` excludes the range under repair from its own index, so it cannot see a sentence this repair wrote twice inside its own ten chapters.** That is item 173O's standing and it has cost this repair on five ranges. `python3 tools/measure.py lifts --volume 09 --first 401 --last 410 --base b8780ff --min 6 --show 20` gives you the added-prose and baseline figures and the longest runs other chapters hold. **The range is unrepaired, so it contributes no added prose at all and the `ADDED` line reads zero across the board; the four figures are the instrument's `BASELINE`, drawn from the six hundred and ten other chapters, and they are 229 prose lines, 187 over six words, 122 over nine, mean 11.44.** That is your floor, not your target, **and an `ADDED 0` on an unrepaired range is the exclusion working and not a broken index — a phase that reads it as an instrument fault will go looking for one that is not there.**

**Run the added-against-added index at six words, then at seven.** It excludes every run already present in the same file at the base, holds the token stream across the whole manuscript with date lines and section breaks stripped, and reports any run another chapter also holds. **At or above four chapters across four volumes it is the register and it stands and you name it as a survivor; below it, and with a holder outside your range, it is your sentence and you revoice it with the fact kept and the sentence changed.**

**Build the twelve-word cross-file index.** It is described in full in `state/batch-summary.md` under the heading *THE PROSE REPAIR OF CHAPTERS 0381 TO 0390, MEASURED RECORD*, section Six, with the holder counts on the exact strings printed beside every entry. It reports any twelve-word run in your added prose held by another chapter at fewer than four chapters across fewer than four volumes. **On the last range it found the only three defects in the landed prose and `lifts` did not report one of them; on the range before that it returned zero, and that zero was proved rather than assumed.**

**Build the intra-file longest-common-run scan, because it is the one that found all five defects on the range before yours and none of the other three could see any of them.** For every line you add, and every other prose line in the same file, take the longest contiguous run of `tools/measure.py`'s `TOKEN` tokens the two lines share, case-folded, date lines excluded, and report any pair at six words or over. **Run it after your first draft and again at the end.** On the range before yours it returned twenty-six pairs, five of them hard defects and twenty-one stock-phrase, locative or motif echoes. **The five fixes took eight of those pairs out and not five, the eighteen that were left are ruled on individually in the record, and all eighteen are — because a scan that returns hits and no ruling is a scan that will be run again.**

**Prove your zeros before you believe them.** The twelve-word index returned zero on the last range and the seven-word pass on the same tree returned seventy runs, which is what turned the zero from a claim into a fact. **A scan that returns zero and is never checked against a setting you know returns something is a scan that is broken in the direction of comfort, and that has happened in this repair twice.**

## The standings that have cost this repair more than any instrument has

**One: an added paragraph must not restate what the paragraph above it already carries, and must not perform the act the paragraph below it already performs.** Those two are the commonest defect in this repair and they have been found by reading on every range. **The last range had five of them, all in prose this repair had written, and every instrument in this repository returned clean on all five.** Read your own last paragraph against the paragraph above it and against the next chapter's opening, and run the intra-file scan.

**Two: the demonstrative-anaphora construction is the writer's tic and a rise in it is a fault in the sentence and not a property of the range.** Measure after every single edit and revoice rather than decide to leave it.

**Three: an instrument that returns a clean answer is a claim about the world and not a fact about the world, and the string has to be quoted back before an absence is believed.** `grep -n "man with the tray"` against a file reading *a man with a tray* returns nothing and reads as absence.

**Four: no instrument in this repository looks at what a chapter says, and four of them have now agreed that reading it is the only one that catches the worst class.** A sentence beginning with a lower-case *and* once carried through every index and every count and was found by reading. Five duplication defects on the last range were found by reading and by nothing else.

**Five: never change a canon figure to make a sentence read better, and grep the whole of `chapters/` before you add any figure, age or distance.** On one range a canon figure was silently rewritten for readability, which also welded two chapters together. On another a repair invented a shawl for a woman whose shawl is the second of the four women's. On a third, a repair invented a stove where the room's canon has a stove out.

**Six: a repair has no authority to settle a canon conflict it finds, and it must not paper over one.** Carry it, name it, leave it standing. The conflicts carried out of the ranges before yours are in `state/open-threads.md` under items 177, 180 and 181 and the items they name, including **`chapter-0375.md:5`'s eleven years against `chapter-0356.md`'s nine, and the counting room's sixteen books against about forty in two other chapters.** Four conflicts sit inside the range before yours and three of them are inside Volume 09's neighbouring chapters: `chapter-0398.md:31` gives one box as *about a year* against `chapter-0395.md:7`'s and `chapter-0395.md:5`'s two other durations for the same box; `chapter-0397.md:3` gives four steps and one step against four steps at `:21`, `:53` and `:63` and the door with two coats of paint at the top of them at `:65`; `chapter-0399.md:9` has a woman who has never been above the second stair and `:17` has her carrying a lamp up. **Every line number in that sentence is on the working tree as it stands now and not at `a9a6b52`, and that is the whole of the difference: the repair of that range inserted 14, 12 and 10 lines into those three files, and the records that carry the same three conflicts give the base numbers.** **A repair has no authority to settle any of them, and Volume 09 picks all three up again.**

**Seven: never add interiority, never touch a bold marker, and never add a question mark.** **Your range carries zero question marks at the base and the zero is the standing, and the count of things asked out loud in this matter is seven at Chapter 350, seven at Chapter 400 and seven at the last chapter of the series, and no chapter may print the number.**

**Eight: no floor material is named in any added paragraph.** `steel`, `brass`, `brick`, `lime`, `plaster`, `glass`, `candle`, `lantern`, `quill`, `pencil`, `match`, `snow`, `slate`, `gravel` and `flagstone` are all in the manuscript and none of them goes into your prose. This is a standing on five ranges running and it is a decision and not an oversight.

**Nine: a revoicing is prose, and prose has to be measured after it and read after it.** Six of the eight defects the phase before last found on its own added prose were produced by its own revoicings, made to satisfy `lifts`.

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
python3 tools/measure.py lifts --volume 09 --first 401 --last 410 --base b8780ff --min 6 --show 20
```

- **Zero `delete` and zero `replace` against `b8780ff` on every file.** No original line replaced, removed or edited. Insert plus equal equals the line total on every file and in the total, and **the `equal` figure is lines and not opcode blocks** — item 173Y's table printed opcode blocks in that column and it is the standing for every range after it.
- **A word-level diff against `b8780ff` reporting insertions, 0 deletions and 0 substitutions.**
- **Every date line byte-identical to `b8780ff` and on the line number it held**, checked with the located line compared against the same line at the base, not by count.
- **Section-break counts, bold-marker counts, question-mark counts, title lines, trailing newlines and quoted spans all identical to the base, span for span.** The base figures for your ten are section breaks **7 5 5 5 6 4 6 4 4 5**, bold markers **20 18 10 14 14 10 20 14 14 18**, question marks **0 on all ten**, and quoted spans **166**.
- **`selftest` PASS.**
- **The four construction lists, printed whole, with the method printed whole, and a per-chapter table whose columns are computed on the same method as the headline.** A per-chapter column computed on a different method from the headline it supports is how a total and a column can both be internally consistent and jointly wrong, and that is item 176's review finding. **On the range before yours the columns read 59, 83, 98 and 229 when computed on raw file text where the headline reads 56, 79, 94 and 226, and the difference is four chapter headings and ten date lines.**
- **The four indices, all four run on the landed tree, and every hit ruled on in writing.** A scan that returns hits and no ruling is a scan that will be run again.
- **The arithmetic printed in full beside the table, run as an addition and not only as a subtraction, because the subtraction is the one that checks.**
- **Print the unit beside every figure, and print both units when a method returns more than one.**

## What you owe the state layer, and it is the part of this repair that has failed most often

**Write all of it. A ninth range in this repair committed ten chapters and wrote no record anywhere at all. A sixth committed nine chapters with a partial item and no batch-summary section. And the phase before yours landed a completed repair and a completed record and never wrote this prompt.**

1. **A section in `state/batch-summary.md`** headed *THE PROSE REPAIR OF CHAPTERS 0401 TO 0410, MEASURED RECORD*, with the method printed whole beside every figure, the arithmetic printed in full, the before-and-now table, the per-chapter table, the date-line section, the checks with the command beside each, the four indices with holder counts on the exact strings, what the canon held, what is carried unrepaired, and what is left. **Append downward. Amend nothing above.**
2. **An item in `state/open-threads.md`** in the same shape as item 181 and every item before it. **Read item 181 first.** The next free number is **182**. **No existing item was renumbered, because renumbering a ledger renumbers every cross-reference to it.**
3. **An update to `state/current.md`**: the Volume 09 row of the per-volume table and the prose note under it, the manuscript total, the repaired-extent sentence, the repaired-range means, and a paragraph for your item beside item 181's. **That file is a handoff and it is short on purpose. Do not grow it by describing its own growth. Do not restate a figure that lives in another file; a figure printed in two files is a figure that will be printed wrong in one of them.**
4. **`workspace/prose-repair-0019/PROMPT.md`, and exactly one.** Your prompt names `chapter-0411.md` to `chapter-0420.md`, still `--volume 09`, measured fresh on your corrected tree and not inherited. **Write the file, and then check that the file exists, because that is the deliverable the last phase recorded and did not write.**
5. **Commit the chapters, then commit the state layer, then create the prompt.** Nothing else. **Do not edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`.** Do not change workflow dispatch, phase selection, timeout, retry or checkpoint logic. Only fiction, bible, outline, chapter, summary, continuity, character and open-thread files.

## The four debts, unchanged, and none of them is discharged by this

One is owed a review of Volume 04's Batch 0005, four volumes on. Two, three and four are owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, which is four and not three. The fourth is the review gate itself: **it has fallen back to the writing agent every time it has been asked and has never once produced a review that could be certified independent, and a gate that only ever falls back is not a gate that passed either.** They are stated once, in `state/open-threads.md`. **Thirty-three earlier restatements of them were moved verbatim to `state/archive/superseded-four-debts-restatements.md` and the repetition is not to be restarted.**

## What is left, so that no phase can imply otherwise

**One hundred and sixty-seven chapters of six hundred and twenty have been through this repair, twenty-seven per cent, and your range is ten of them.** Volume 11 is repaired in full, Volume 12 in full, Volume 08 in full. **Volumes 09 and 10 are untouched apart from whatever your range makes of it, ninety chapters after it, and they are the single largest block of this defect left in the repository.**

**Four hundred and fifty-three chapters are unrepaired, seventy-three per cent, and every one of them is in Volumes 01 to 10.** Ten chapters is a tenth of one volume against a defect that spans six volumes. **This repair at this rate is forty-six phases across the manuscript, and forty-six is the figure the arithmetic gives: four hundred and fifty-three at ten a phase, and forty-five phases would leave three chapters standing at the end of it. It is ten phases across the hundred chapters of Volumes 09 and 10, where nothing has been touched, and nine of those ten are after your range, and the whole of it is a person's decision and not a phase's.** **One hundred and sixty-seven chapters are evidence that the work can be done and not evidence that it has been done, and fifty of those hundred and sixty-seven have had one pass while five have had three or more, which is itself the argument for repairing forward rather than auditing back.**

**And the honest finding, which no amount of state bookkeeping can fix: the manuscript is structurally complete, canonically sound and not publishable as it stands.** Chapter length fell from 4,042 words a chapter in Volume 01 to 1,455 in Volume 12, monotonically across twelve volumes, and the demonstrative-anaphora construction rose with it from 0.5 instances per 1,000 words to 8.7. **That is what you are repairing and it is a decision about scope and it belongs to a person.**