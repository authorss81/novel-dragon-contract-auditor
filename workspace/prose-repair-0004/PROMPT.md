# Prose repair, fourth ten chapters: Chapters 0581 to 0590, the last ten of Movement Four

**This is a repair, not a batch, not a close, not a review, and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, exactly the length `NOVEL_SPEC.md` and `outline/series.md` set, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/volume-12.md` states in terms that there is no next volume. **Three phases have now taken continuation stubs and correctly planned no volume. Do not plan one.** The remaining prose work is below and it is most of the manuscript.

## Read before writing

`state/current.md` in full, **item 173 and item 173A** of `state/open-threads.md`, and the three sections of `state/batch-summary.md` headed *THE PROSE REPAIR OF CHAPTERS 0610 TO 0619*, *THE PROSE REPAIR OF CHAPTERS 0601 TO 0609* and *THE PROSE REPAIR OF CHAPTERS 0591 TO 0600*. Then read `chapter-0581.md` to `chapter-0590.md` as prose, and read a repaired range beside them — `chapter-0591.md` to `chapter-0600.md` is the nearest and was repaired in the phase that wrote this prompt's predecessor, and the point of the exercise is what those ten chapters look like and not what they are.

## The finding

Chapter length fell monotonically across twelve volumes, from about 4,000 words a chapter in Volume 01 to about 1,050 in Volume 12, and the demonstrative-anaphora construction — *that tin, those boards, that lane* — rose with it. The volume outlines describe complete scenes. The delivered pages are compressed summaries of those scenes. `AGENTS.md` asks for physical space, action, sensory detail, dialogue, subtext, character thought and emotional consequence, and that is not reachable in a thousand words. **The manuscript is structurally complete and canonically sound and it is not publishable as it stands, and this is the only open item in the repository that a writing phase can pay.**

**The remaining scope, said plainly, because a phase that reads the last chapter of a series and plans a thirteenth volume has misread the series twice in this repository already.** Twenty-nine chapters are repaired: 0610 to 0619, 0601 to 0609, then 0591 to 0600. **Volumes 08, 09, 10 and 11 are untouched in their entirety**, and the first forty chapters of Volume 12 are untouched: 0551 to 0590, a mean of 1,063 words a chapter against the 1,396 of the ten just repaired. **Five hundred and ninety-one chapters are unrepaired. Ten chapters is a tenth of one volume against a defect that spans four, this repair at this rate is fifty-nine phases across the manuscript and twenty-four phases across the four volumes where the collapse is worst, and that is a scope decision belonging to a person and not to a phase.** Say so in your own record rather than implying the job is nearly done.

## The task

**Open `chapter-0581.md` through `chapter-0590.md` for edit and repair the prose. Write no new chapter and plan no volume.**

These ten are the last ten chapters of Movement Four, immediately before the range just repaired, and they are untouched. The work is length and variation, not plot. For each chapter:

- **Keep every scene beat in the order it is already in.** Nothing is added to the plot, removed from it, reordered, or contradicted.
- **Give the scene its body back.** The physical arrangement of the room, where objects sit and what they are made of, what a body is doing while its owner is not speaking, the light and the hour and the weather. These chapters are about people doing very little in rooms, and the very little is the point, so the repair is in the doing and not in the plot.
- **Vary the sentence rhythm.** The delivered prose runs at one length and one cadence. The repaired chapters should not.
- **Set the rooms down from what is already on the page.** These rooms are described in earlier chapters of the same volume — the sill, the bench, the tin, the daylight over the wall, the corridor, the ledger, the mark on a shoulder. **Grep the whole of `chapters/` before you add any detail, and expect to find that most of what you want to describe is already written down six chapters away in the same room. That is not a reason to invent, it is the finding.**

### The concentration on this range, measured before you open it, because you must not inherit the last range's list

**This is the one instruction in this prompt that two previous phases got wrong in opposite directions, and the third got it right and the standing is now three ranges old.** The last pass widened the list of named forms from ten to twenty-three and printed both rates side by side, and that is the shape a record should be in. **This range is a different range again, and its leaders are neither the previous range's nor the one before it.** On the instruments printed whole in the section headed *THE PROSE REPAIR OF CHAPTERS 0591 TO 0600* in `state/batch-summary.md`, `chapter-0581.md` to `chapter-0590.md` stands at:

- **9,925 words, 106 hits of the closed list of ten named forms, 10.68 per 1,000** — the highest pre-repair rate of the three ranges already done, against 8.78 on 0591 to 0600 and 11.18 on 0601 to 0609. **Per chapter: 0581 11, 0582 9, 0583 11, 0584 4, 0585 8, 0586 15, 0587 19, 0588 17, 0589 7, 0590 5.** Deal with 0587 and 0588 first and they are the two shortest chapters of the ten as well.
- **Its closed-list leaders are `that floor` 34, `that room` 24, `those boards` 14, `that door` 12 and `that stair` 10, and a single form leads at thirty-four.** `that floor` is the largest single-form count this repair has met on any range.
- The wider sweep of **every** demonstrative plus noun in those ten files, with a function-word tail excluded because `that is` and `that has` are subordinators, returns **274 hits in 9,925 words, 27.61 per 1,000**. Its leaders include **`that sill` 31, `that building` 17, `that corridor` 14, `that end` 11, `that board` 11, `that stone` 7, `that ground` 7 and `that house` 7** — **and `that sill`, `that building`, `that board`, `that stone` and `that house` are in neither the closed list of ten nor the widened list of twenty-three.** **`that building` at seventeen is a form this repository has never counted in any list.**

**If you widen the list, print the old and the new rate side by side and say plainly which forms you added, because a figure with an undisclosed method behind it is how this repository got a set of numbers that reproduced under none.** And say plainly that a closed list of named forms measures the concentration this repair works on and not the whole of item 170.

## What must not change

These are hard. Check each one before the phase ends.

- **The date line of every chapter, byte for byte.** `sed -n '5p' | md5sum` on the working tree and on `git show HEAD:chapters/volume-12/chapter-0NNN.md`. This is the single most important check in the phase: a repair that moved a date would move the calendar for the rest of the series.
- **Zero question marks.** The count of things asked out loud in this matter is seven, it has not moved, and it is printed in no chapter. Do not add a question.
- **The person each chapter closes in.** This volume's framing is third person and its interiority is first person, opened by a bold line, **and that is a strong default and not a rule**: 106 chapters of the 620 in this manuscript end their last section in first person. **The test that holds is narrow and checkable: keep each chapter's closing section in the person its original closed in.** A first-person line inside a run of dialogue is the speaker's and is left alone. **The working scan is printed in the section headed *THE PROSE REPAIR OF CHAPTERS 0601 TO 0609* in `state/batch-summary.md`, with its four plants. Use it as printed and do not rebuild it in `/tmp`.** When you scan, subtract the bold interiority and the dialogue lines first. Four instruments have now been built in this repository that failed to do one of those two things; one reported forty-seven false errors and one reported none, and an instrument that reports none is the same failure in the other direction.
- **The section breaks.** A `---` line is architecture, not punctuation. **Each of the ten files must end the phase with the same number of `---` lines its original had.**
- **Canon.** Every figure, object, duration, distance, age and named absence stays. **An age is the easiest thing on this list to invent by accident and so is a room's furniture: a closed list of figures and objects is not a licence to add one.** Grep all of `chapters/` for any detail before you add it, and if the only hits are this manuscript's other and unrelated people or other rooms, it is a new fact and it does not go in. The previous pass drafted a planked trestle table into a room whose table is deal with its far edge into the wall, and a high window into a shed whose light comes off the roof, and took both out. The four figure-types that must not be confused stay four distinct types. Do not print the name at the foot of the struck line, and do not resolve the fourth item on the wall board, the question on the shelf, the drawer, the box under the far end of the boards, or anything else the volume holds open.
- **Never change a canon figure to make a sentence read better, however good the reason.** The last repair rewrote one word in `chapter-0602.md`, from eleven *weeks* to eleven *years*, and it was very probably a correction, and it was still put back, because a prose repair has no authority to decide a canon question and the tension was left standing and visible for a person to settle. **Do not settle it. If you find one of those, put the original word back and record the tension.**
- **Never lift a sentence out of another chapter, in either direction.** The previous pass took 62 words from `chapter-0606.md` into `chapter-0600.md` and three more passages from `0601.md`, `0606.md`, `0581.md` and `0584.md` into its own range, and `python3 tools/measure.py reprints --window 20 --volume 12` went from 4 to 16 over a ceiling of 4. **Take the volume's own facts and write them out in fresh words. A repair that greps for a description and then copies what it finds has made the volume say the same thing twice.** Note the circularity and the trap: **this range contains `chapter-0581.md` and `chapter-0584.md`, which are two of the four chapters the last pass lifted from.** The passage in 0581 and 0584 about the sill and the daylight is canon and it must not be re-typed into this range a fourth time.
- **The chapter must agree with itself, and it must agree with the chapters that own the events near it.** Read the last paragraph of each chapter you open against the paragraph above it, against the opening premise of the chapter after it, **and against any chapter in the volume that owns a beat this chapter has come near.** The previous pass drafted the courier turning round for the first time in eleven years into `chapter-0600.md`, and that beat belongs to `chapter-0606.md` and is undone in `chapter-0609.md`. **Every instrument in this repository passed that file with the error standing in it.** It was found by reading `chapter-0606.md` for an unrelated reason. **The neighbours are not enough: read the chapters that own the events your chapter is near, and they are not the chapters either side of it.**
- **Nothing resolved, nobody thanked, nobody forgiven, nobody sent for.**
- **The unmade decision** about whether the woman of twenty-four takes a colleague's judgment stays unmade, in either direction.
- **`chapter-0620.md` is not opened by this phase.** It carries the last line of the series.
- **Write a record.** A repair with no record is not a repair; it is a diff. Two passes in this repository have changed chapters and written nothing, and that is the reason a review was the only thing that looked at them.

## Verify before finishing

Run these and put the results in the state record with the command beside each figure.

```
python3 tools/measure.py selftest
python3 tools/measure.py calendar --volume 12
python3 tools/measure.py reprints --window 20 --volume 12
```

- **Re-prints are the check most likely to catch a mistake, and on this range it is more likely than usual, because the range contains two of the chapters the last pass copied out of.** The baseline for Volume 12 is **four prose runs** and none of them was made by any of the three previous repairs; they are the `chapter-0586.md` case-and-blanks passage and the `chapter-0614.md` pot sentence, in files no repair has opened. **Do not go above four.** All three previous repairs broke this ceiling at least once and each was caught, twice by the phase itself and once by the review of it.
- Section-break count per file must equal the original's. `for n in $(seq 581 590); do f=chapters/volume-12/chapter-0$n.md; echo "$n $(grep -c '^---$' $f) $(git show HEAD:$f | grep -c '^---$')"; done` — the two numbers on each line must match.
- Person of the final section must equal the original's, on the scan printed above, with the bold interiority and the dialogue subtracted first. Plant it four ways before you believe it.
- Question-mark count across the ten files: zero.
- All ten date lines byte-identical to `HEAD`.
- Month and weekday names: the only permitted hit is the modal verb *may*.
- `this year`, `this volume`, `this novel`: zero.
- Bold markers even in every file.
- **Report the named-form rate before and after with the method printed whole, not described.** Use `m.words_in_file` for every word figure — and note that it takes a path, so reading the working tree while claiming to read a commit is how the last record printed one figure three times; for a committed blob apply the same definition, `sum(len(line.rstrip().split()) for line in handle)`, to the text `git show` returns. **Say plainly that a closed list of named forms measures the concentration this repair works on and not the whole of item 170.**

## State and the next phase

Append one section to `state/batch-summary.md` with the measured record, the method beside every figure, **and any regression this phase introduced and then fixed — a repair that reports only its successes has not been measured, and the last one produced the worst defect in this repair's history and reported nothing for a while.** Add or extend an item in `state/open-threads.md` for what remains, and keep `state/current.md` short; it has been trimmed once already for bloat and its own complaint is at its head, so update the counts there and do not restate a figure that belongs in the batch summary.

**Then create exactly one next phase prompt** and no more, at `workspace/prose-repair-0005/`, for the same work on the next ten chapters, which after this phase are `chapter-0571.md` to `chapter-0580.md`. **Measure their concentration before you name them in that prompt, because the leaders have changed on every range so far and a prompt that inherits the previous prompt's table leaves the new leaders standing. The remaining scope after this phase is still most of the manuscript and the next prompt should say so in its own words.**
