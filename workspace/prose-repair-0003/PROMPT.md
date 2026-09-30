# Prose repair, third ten chapters: Chapters 0591 to 0600, the last ten of Movement Five

**This is a repair, not a batch, not a close, not a review, and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, exactly the length `NOVEL_SPEC.md` and `outline/series.md` set, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/volume-12.md` states in terms that there is no next volume. **Two previous phases have now taken continuation stubs and correctly planned no volume. Do not plan one. The work is below.**

Read before writing: `state/current.md` in full, item 173 of `state/open-threads.md`, and the two sections headed *THE PROSE REPAIR OF CHAPTERS 0610 TO 0619* and *THE PROSE REPAIR OF CHAPTERS 0601 TO 0609* in `state/batch-summary.md`. Then read `chapter-0591.md` to `chapter-0600.md` as prose, and read the repaired range `chapter-0601.md` to `chapter-0619.md` beside them, because the point of the exercise is what those ten chapters look like and not what they are.

## The finding

Chapter length fell monotonically across twelve volumes, from about 4,000 words a chapter in Volume 01 to about 1,050 in Volume 12, and the demonstrative-anaphora construction — *that tin, those boards, that lane* — rose with it. The volume outlines describe complete scenes. The delivered pages are compressed summaries of those scenes. `AGENTS.md` asks for physical space, action, sensory detail, dialogue, subtext, character thought and emotional consequence, and that is not reachable in a thousand words. **The manuscript is structurally complete and canonically sound and it is not publishable as it stands, and this is the only open item in the repository that a writing phase can pay.**

**The remaining scope, said plainly, because a phase that reads the last chapter of a series and plans a thirteenth volume has misread the series twice in this repository already.** Nineteen chapters have been repaired: 0610 to 0619, then 0601 to 0609. Volume 12 now runs at 78,968 words and its untouched first fifty chapters, 0551 to 0600, run 779 to 1,342 words each with a mean of 1,044, while the nine just repaired run 1,243 to 1,970 with a mean of 1,458. **Repaired prose is now sitting beside unrepaired prose in the same volume and the gap between 1,044 and 1,458 words a chapter is the size of what is still owed.** Volumes 08, 09, 10 and 11 are untouched in their entirety. **Ten chapters is a tenth of one volume against a defect that spans four, this repair at this rate is a hundred and thirty phases, and that is a scope decision belonging to a person and not to a phase.** Say so in your own record rather than implying the job is nearly done.

## The task

**Open `chapter-0591.md` through `chapter-0600.md` for edit and repair the prose. Write no new chapter and plan no volume.**

These ten are the last ten chapters of Movement Five, immediately before the two repaired ranges, and they are untouched. The work is length and variation, not plot. For each chapter:

- **Keep every scene beat in the order it is already in.** Nothing is added to the plot, removed from it, reordered, or contradicted.
- **Give the scene its body back.** The physical arrangement of the room, where objects sit and what they are made of, what a body is doing while its owner is not speaking, the light and the hour and the weather. These chapters are about people doing very little in rooms, and the very little is the point, so the repair is in the doing and not in the plot.
- **Vary the sentence rhythm.** The delivered prose runs at one length and one cadence. The repaired chapters should not.

### The concentration on this range, measured before you open it, because you must not inherit the last range's list

**This is the one instruction in this prompt that the previous two phases got wrong in opposite directions.** Across `chapter-0591.md` to `chapter-0600.md`, on the instrument printed whole in the section headed *THE PROSE REPAIR OF CHAPTERS 0610 TO 0619* in `state/batch-summary.md`, the ten named forms stand at `that floor` **18**, `that room` **14**, `that passage` **12**, `those boards` **9**, `that door` **9**, `that table` **7**, `that stair` **7**, `that tin` **5**, `that lane` **4**, `that sheet` **0**, being 85 hits in 9,677 words, **8.78 per 1,000**. Deal with the top of that list first. **`that passage` and `those boards` are near the bottom of them on the range just repaired and are third and joint fourth here, so a phase that reuses the previous range's table will leave this range's leaders standing.**

**And the closed list of ten is a closed list, which is the instrument's own admitted blind spot, and on this range it is a wide one.** A sweep of every demonstrative-plus-noun in those ten files, which a closed list cannot do, puts **`that end` 13, `that landing` 13, `that bench` 12, `that sill` 10, `that corridor` 8, `that case` 8** in or near the lead, and **not one of those six is in the list of ten forms this repository has been measuring with since the first repair.** A demonstrative re-anchors an object the reader is already holding; after the first mention in a scene, reach for a plain article, a pronoun, or a fresh anchoring instead. **If you widen the list, print the old and the new rate side by side and say plainly which forms you added, because a figure with an undisclosed method behind it is how this repository got a set of numbers that reproduced under none.**

## What must not change

These are hard. Check each one before the phase ends.

- **The date line of every chapter, byte for byte.** Compare against `git show HEAD:chapters/volume-12/chapter-059N.md | grep "^It is"`. A repair that moved a date would move the calendar for the rest of the series. This is the single most important check in the phase.
- **Zero question marks.** The count of things asked out loud in this matter is seven, it has not moved, and it is printed in no chapter. Do not add a question.
- **The person each chapter closes in.** This volume's framing is third person and its interiority is first person, opened by a bold line, **and that is a strong default and not a rule**: 106 chapters of the 620 in this manuscript end their last section in first person, twenty of them in Volumes 01 and 02. **The test that holds is narrow and checkable: keep each chapter's closing section in the person its original closed in.** A first-person line inside a run of dialogue is the speaker's and is left alone. **When you scan for a violation, subtract the bold interiority and the dialogue lines first.** Four instruments have now been built in this repository that failed to do one of those two things; one reported forty-seven false errors and one reported none, and an instrument that reports none is the same failure in the other direction. The working scan is printed in the section headed *THE PROSE REPAIR OF CHAPTERS 0601 TO 0609* in `state/batch-summary.md`, with its four plants and the numbers they returned. **Use it as printed and do not rebuild it in `/tmp`.**
- **The section breaks.** A `---` line is architecture, not punctuation. **Each of the ten files must end the phase with the same number of `---` lines its original had.**
- **Canon.** Every figure, object, duration, distance, age and named absence stays. **An age is the easiest thing on this list to invent by accident, and the previous repair gave the woman at the foot of a stair an age of fifty-one that exists nowhere in the six hundred and twenty chapters.** Before you add any figure, object, duration, distance or age, grep all of `chapters/` for it; if the only hits are this manuscript's other and unrelated people, it is a new fact and it does not go in. The four figure-types that must not be confused stay four distinct types. Do not print the name at the foot of the struck line, and do not resolve the fourth item on the wall board, the question on the shelf, the drawer, or anything else the volume holds open.
- **Never change a canon figure to make a sentence read better, however good the reason.** The last repair rewrote one word in `chapter-0602.md`, from eleven *weeks* to eleven *years*, and it was very probably a correction — eleven weeks appears nowhere else in Volume 12 and that chapter says eleven years twice itself. **It was still put back, because a prose repair has no authority to decide a canon question, and the tension was left standing and visible for a person to settle.** If you find one of those, put the original word back and record the tension. Do not settle it.
- **The chapter must agree with itself and with its neighbour.** Read the last paragraph of each chapter you open against the paragraph above it, and against the opening premise of the chapter after it. **A paragraph you add between two original paragraphs must not perform the act either neighbour performs.** The last repair put a gesture on the page in `chapter-0609.md` and then left the original line doing the same gesture four lines beneath it, and a re-print scan, a calendar scan, a question-mark count and a closing-person scan all passed it. **No instrument in this repository looks at what a chapter says, and that is the only one that catches this class.**
- **Nothing resolved, nobody thanked, nobody forgiven, nobody sent for.**
- **The unmade decision** about whether the woman of twenty-four takes a colleague's judgment stays unmade, in either direction.
- **`chapter-0620.md` is not opened by this phase.** It carries the last line of the series.
- **Write a record.** The previous phase changed ten chapters and wrote no state record at all, and that is the reason a review was the only thing that looked at them and the reason three defects survived into the repository. A repair with no record is not a repair; it is a diff.

## Verify before finishing

Run these and put the results in the state record with the command beside each figure.

```
python3 tools/measure.py selftest
python3 tools/measure.py calendar --volume 12
python3 tools/measure.py reprints --window 20 --volume 12
```

- **Re-prints are the check most likely to catch a mistake.** Copying a canon set-piece from another chapter verbatim, or rewording one to match its neighbour, raises the run count against a chapter this phase never opened. The baseline for Volume 12 is **four prose runs** and none of them was made by either previous repair; all four are one passage, the `chapter-0586.md` case-and-blanks set-piece against the same words in 0619, at four sliding offsets of one twenty-word window, so the volume holds one duplication of it and not four. **Do not go above four.** Both earlier repairs broke this ceiling and both were caught, once by the phase itself and once by the review of it.
- **Section-break count per file must equal the original's.** `for n in $(seq 591 600); do f=chapters/volume-12/chapter-0$n.md; echo "$n $(grep -c '^---$' $f) $(git show HEAD:$f | grep -c '^---$')"; done` — the two numbers on each line must match.
- **Person of the final section must equal the original's,** on the scan printed above, with the bold interiority and the dialogue subtracted first.
- Question-mark count across the ten files: zero.
- All ten date lines byte-identical to `HEAD`.
- Month and weekday names: the only permitted hit is the modal verb *may*.
- `this year`, `this volume`, `this novel`: zero.
- Bold markers even in every file.
- **Report the named-form rate before and after with the method printed whole, not described.** Use `m.words_in_file` for every word figure — and note that it takes a path, so reading the working tree while claiming to read a commit is how the last record printed one figure three times; for a committed blob apply the same definition, `sum(len(line.rstrip().split()) for line in handle)`, to the text `git show` returns. **Say plainly that a closed list of named forms measures the concentration this repair works on and not the whole of item 170.**

## State and the next phase

Append one section to `state/batch-summary.md` with the measured record, the method beside every figure, **and any regression this phase introduced and then fixed — a repair that reports only its successes has not been measured.** Add or extend an item in `state/open-threads.md` for what remains, and keep `state/current.md` short; it has been trimmed once already for bloat and its own complaint is at its head, so update the counts there and do not restate a figure that belongs in the batch summary.

**Then create exactly one next phase prompt** and no more, at `workspace/prose-repair-0004/`, for the same work on the next ten chapters. **The remaining scope after this phase is still most of the manuscript and the next prompt should say so in its own words.**
