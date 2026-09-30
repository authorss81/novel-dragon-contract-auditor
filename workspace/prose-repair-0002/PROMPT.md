# Prose repair, second ten chapters: Movement Seven, Chapters 0601 to 0609

**This is a repair, not a batch, not a close, not a review, and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, exactly the length `NOVEL_SPEC.md` and `outline/series.md` set, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/volume-12.md` states in terms that there is no next volume. **A previous phase took a continuation stub that said "if the current volume is complete, plan the next volume" and correctly did not plan one. Do not plan one. The work is below.**

Read before writing: `state/current.md` in full, item 170 and item 172 of `state/open-threads.md`, and the section headed *THE PROSE REPAIR OF CHAPTERS 0610 TO 0619* in `state/batch-summary.md`. Then read `chapter-0601.md` to `chapter-0620.md` as prose. The previous phase's ten repaired chapters are the model for what this one is for.

## The finding

Chapter length fell monotonically across twelve volumes, from about 4,000 words a chapter in Volume 01 to about 1,050 in Volume 12, and the demonstrative-anaphora construction — *that tin, those boards, that lane* — rose with it. The volume outlines describe complete scenes. The delivered pages are compressed summaries of those scenes. `AGENTS.md` asks for physical space, action, sensory detail, dialogue, subtext, character thought and emotional consequence, and that is not reachable in a thousand words. **The manuscript is structurally complete and canonically sound and it is not publishable as it stands, and this is the only open item in the repository that a writing phase can pay.**

## The task

**Open `chapter-0601.md` through `chapter-0609.md` for edit and repair the prose. Write no new chapter and plan no volume.**

The work is length and variation, not plot. For each chapter:

- **Keep every scene beat in the order it is already in.** These are the climax movement, Chapters 0601 to 0610, and the beats are load-bearing. Nothing is added to the plot, removed from it, reordered, or contradicted.
- **Give the scene its body back.** The physical arrangement of the room, where objects sit and what they are made of, what a body is doing while its owner is not speaking, the light and the hour and the weather. These chapters are about people doing nothing much in rooms, and the nothing much is the point, so the repair is in the doing and not in the plot.
- **Reduce the demonstrative re-anchoring.** A demonstrative re-anchors an object the reader is already holding. After the first mention in a scene, reach for a plain article, a pronoun, or a fresh anchoring instead. The defect concentrates, and **you must measure the concentration on the nine chapters you are opening, because the leaders are not the leaders next door.** Across `chapter-0601.md` to `chapter-0609.md` the counts are `that table` 20, `that door` 15, `that room` 15, `that floor` 14, `that stair` 9, `that tin` 8, `those boards` 6, `that passage` 5, `that sheet` 4 and `that lane` **1** — `that lane`, which led the previous ten chapters, is all but absent from these, and `that door` and `that room`, joint second on this range, were not mentioned at all in the previous phase's list. Deal with the top forms on your own range first.
- **Vary the sentence rhythm.** The delivered prose runs at one length and one cadence. The repaired chapters should not.

## What must not change

These are hard. Check each one before the phase ends.

- **The date line of every chapter, byte for byte.** Compare against `git show HEAD:chapters/volume-12/chapter-060N.md | grep "^It is"`. A repair that moved a date would move the calendar for the rest of the series. This is the single most important check in the phase.
- **Zero question marks.** The count of things asked out loud in this matter is seven, it has not moved, and it is printed in no chapter. Do not add a question.
- **The person each chapter closes in.** This volume's framing is third person and its interiority is first person, opened by a bold line, **and that is a strong default and not a rule**: 106 chapters of the 620 in this manuscript end their last section in first person, twenty of them in Volumes 01 and 02, and inside Volume 12 the exceptions are the closing paragraph of `chapter-0601.md` and the interiority of `chapter-0603.md`, which no section break closes. The previous phase printed that rule as absolute and then, having printed it, broke it in two of its own files. **The test that holds is narrow and checkable: keep each chapter's closing section in the person its original closed in.** A first-person line inside a run of dialogue is the speaker's and is left alone. When you scan for a violation, subtract the bold interiority and the dialogue lines first — three instruments have now been built here that failed to do one of those two things and reported forty-seven false errors or none.
- **The section breaks.** A `---` line is architecture, not punctuation. **Each of the nine files must end the phase with the same number of `---` lines its original had.** The previous repair left `chapter-0610.md` with six against an original four, having split its interiority and pulled the material out under new breaks, which is also how first person got into its framing.
- **Canon.** Every figure, object, duration, distance, age and named absence stays. **An age is the easiest thing on this list to invent by accident: the previous repair gave the woman at the foot of that stair an age of fifty-one and no age for her exists anywhere in the six hundred and twenty chapters.** Before you add any figure, object, duration, distance or age, grep all of `chapters/` for it; if the only hits are this manuscript's other and unrelated people, it is a new fact and it does not go in. The four figure-types that must not be confused stay four distinct types. Do not print the name at the foot of the struck line, and do not resolve the fourth item on the wall board, the question on the shelf, the drawer, or anything else the volume holds open.
- **The chapter must agree with itself and with its neighbour.** Read the last paragraph of each chapter you open against the paragraph above it, and against the opening premise of the chapter after it. The previous repair had `chapter-0610.md` remove a coin in its new closing section and keep it in the paragraph beneath, and `chapter-0611.md` opens on the eighth morning with it gone. **A re-print scan, a calendar scan and a question-mark count all passed that, because none of them looks at what a chapter says.**
- **Nothing resolved, nobody thanked, nobody forgiven, nobody sent for.**
- **The unmade decision** about whether the woman of twenty-four takes a colleague's judgment stays unmade, in either direction.
- **`chapter-0620.md` is not opened by this phase.** It carries the last line of the series.

## Verify before finishing

Run these and put the results in the state record with the command beside each figure.

```
python3 tools/measure.py selftest
python3 tools/measure.py calendar --volume 12
python3 tools/measure.py reprints --window 20 --volume 12
```

- **Re-prints are the check most likely to catch a mistake.** Copying a canon set-piece from another chapter verbatim raises the run count against a chapter this phase never opened. The baseline for Volume 12 is **four prose runs** and none of them was made by the previous phase; the previous phase went to eight, caught it, and got back to four. Do not go above four. **A run is not a duplication: all four baseline runs are one passage, the `chapter-0586.md` case-and-blanks set-piece against the same words in 0619, at four sliding offsets of one twenty-word window.**
- **Section-break count per file must equal the original's.** `for n in $(seq 601 609); do echo -n "$n "; echo $(grep -c '^---$' chapters/volume-12/chapter-0$n.md) $(git show HEAD:chapters/volume-12/chapter-0$n.md | grep -c '^---$'); done` — the two numbers on each line must match.
- **Person of the final section must equal the original's.** The scan must subtract the bold interiority and the dialogue lines before it counts anything.
- Question-mark count across the nine chapters: zero.
- All nine date lines byte-identical to `HEAD`.
- Month and weekday names: the only permitted hit is the modal verb *may*.
- `this year`, `this volume`, `this novel`: zero.
- **Report the named-form rate before and after with the method printed whole, not described.** The instrument printed in the section headed *THE PROSE REPAIR OF CHAPTERS 0610 TO 0619* in `state/batch-summary.md` is self-contained, borrows `tools/measure.py`'s tokenizer and can be pasted as it stands. **The previous phase's classifier was in `/tmp`, was not in the repository, and not one absolute figure it printed reproduced; word counts and rates both.** Use `m.words_in_file` for every word figure, and say plainly that a closed list of ten named forms measures the concentration this repair works on and not the whole of item 170.

## State and the next phase

Append one section to `state/batch-summary.md` with the measured record, the method beside every figure, and any regression this phase introduced and then fixed — **a repair that reports only its successes has not been measured.** Add an item to `state/open-threads.md` for what remains. Keep `state/current.md` short; it has been trimmed once already for bloat and its own complaint is at its head.

**Then create exactly one next phase prompt** and no more, at `workspace/prose-repair-0003/`, for the same work on the next ten chapters. The remaining scope after this phase is still most of the manuscript, and the next phase should say so.

**Ten chapters is a tenth of one volume against a defect that spans four. This is a scope decision that belongs to a person, and each phase should say so in its own record rather than implying the job is nearly done.**
