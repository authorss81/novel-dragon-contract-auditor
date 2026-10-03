# OWED SECOND READING: VOLUME 05, BATCH 0003, `chapter-0221.md` TO `chapter-0230.md` — THE SECOND OF THE FOUR OWED REVIEWS

**This is a review and not a batch, not a volume outline, not a close, not a prose repair and not a volume planning phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, ending on the page in `chapter-0620.md`, which carries the last line of this series and which no phase may rewrite. `NOVEL_SPEC.md` states in terms that *Volumes 01 to 12 are closed and are not to be reopened*, and `outline/volume-12.md` states that *there is no next volume and there is no next asking*. **A continuation stub will hand you a conditional that reads *if the current volume is complete, plan the next volume.* Both branches of that conditional are closed for this repository and neither may be executed.** The work is the open work named in `state/open-threads.md` item 170 and item 267, and this is one of the four reviews that item names.

## Why this range, and why it is not a chapter to write

`outline/volume-12.md`, at its close, names four owed reviews and says *which is four and not three*:

> *One:* an owed review of Volume 04's Batch 0005, four volumes on. *Two, three and four:* owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003.

**One is paid. It is `reviews/volume-04-batch-0005.md`, written by the phase that took `workspace/continuation/next-0005/PROMPT.md`. Read it before you start, because it establishes the method and it inherits one piece of unfinished business at `chapter-0050.md:85`.** Yours is the second. Volume 05's Batches 0004 and 0005 and Volume 06's Batch 0003 are the third and fourth, and **one phase paid four reviews four volumes apart, which is not a thing to plan as one. Take this one.**

**Your range is `chapter-0221.md` to `chapter-0230.md`, ten files. All ten are yours to read. Every one of them is yours to *report on*.** Volume 05 is a closed volume and **this run has no delete or substitute authority and must not take any**, so a defect in a chapter is reported with its line number and is not fixed. A second reading that edits the prose it is reading is not a second reading.

## The base, and the precheck that this prompt tells you to distrust its own figures

```
git log --oneline -- chapters/volume-05/chapter-022[1-9].md chapters/volume-05/chapter-0230.md
git diff --numstat 18e57c8 -- chapters/volume-05/
git cat-file -e 18e57c8:chapters/volume-05/chapter-0221.md && echo PRESENT
git log --oneline --grep="prose-repair" -- chapters/volume-05/
python3 tools/measure.py words --volume 05
python3 tools/measure.py selftest
```

**`18e57c8` — *save review fixes batch-0003* — is the last commit to touch any of your ten files, and it is your base.** Do not use `65abf1d` or `dedc831`: they are later commits on *other* files in the same volume and `git diff` against either will return a clean result for a range you did not measure. **`git show 9ae089f:chapters/volume-05/chapter-0221.md` will exit 128 and every structural counter piped from it will come back exactly zero** — that is a missing base and not a measurement, it is recorded at `state/open-threads.md` item 265E, and it has already happened once in this volume. **Assert that `git show <base>:<file>` returns non-empty text for all ten files before you believe a single number you computed from it.**

**No figure in this prompt is a figure of record. Every one is to be re-derived by your own run.** A figure printed in a prompt is bound to the page the prompt was written against, and this repository's own record is a chain of corrections longer than the sentence it corrects.

## What the card for this batch asks for, and the two locks on it

Read `outline/batches/volume-05-batch-0003.md` in full before you open a chapter. It is sixty thousand bytes and it carries the chapter cards and its own divergence section. **`outline/volume-05.md` is closed and is the volume outline of record; read it, do not edit it, and go to the page rather than to a line when the two disagree.**

**The record's claims are what you are testing, not its conclusions.** Volume 04's Batch 0005 record certified an absolute rule as holding and the rule was broken six times in four chapters; its word figures were 339 low because they were written before its own review repair. **An absolute rule quoted only in a batch's own divergence section has probably not been run, and a word figure written by the run that wrote the chapters is exact for the day it was written and not for the tree you are standing on.** Test every figure. Print the method beside it.

**The two locks, both checkable on the tree, both from `outline/volume-05.md`:**

1. **No calendar month name and no weekday name may appear in the prose of Volume 05.** Months are numbered and days are counted. The card's own instruction is that *a check of every file a batch writes for the twelve month names and the seven day names must be run before the batch closes, and every instance found must be corrected on the page before the batch closes*. **You cannot correct it — Volume 05 is closed — so run the check and report every instance with its line number.** **Warn yourself about one thing before you run it, or you will spend the run on it: `may` is the modal verb in this volume and the month in none of it.** A naive run returns raw hits and every one of them is the modal. On your ten files it returns **eight raw hits, all `may`, all eight the modal verb**, at `chapter-0222.md:73`, `0223:23`, `0225:37`, `0225:45`, `0228:15`, `0228:91`, `0228:99`, `0229:13` — *what may be asked*, *a person who may be entered*, *a person may only be in one*, *you may ask*, *you may ask me anything*, *a person may send anybody anything*, *what a person may do with a piece of paper*, *a person who may be served*. **Zero weekday names and zero month names other than the modal `may`.** Across the whole of Volume 05 the same naive run returns twenty-seven raw hits, all `may`, all the modal, and **the lock holds across all fifty chapters.** Run it, read the surrounding line, and move on; the finding is that a lock whose only near-miss is a homograph has to be checked by reading and not by matching.
2. **`about nine` is bound to about eight per chapter, and it is thinned and never varied.** Volume 05's Batch 0005 measured 3 to 8, median 6. **Your ten have already been measured and the lock holds**, so spend your run on something else: `chapter-0221` to `chapter-0230` carry **5, 7, 4, 5, 6, 6, 6, 3, 6, 8 — range 3 to 8, median 6.0, total 56**, with `grep -o -i "about nine\b" | wc -l` less `grep -o -i "about nine hundred" | wc -l`. **You must subtract "about nine hundred" yourself and the subtraction is not optional**: a raw count of `about nine\b` matches the `about nine` inside `about nine hundred`, and it inflates `chapter-0221` from 5 to 9 and `chapter-0228` from 3 to 7. **A lock measured with the wrong denominator is a lock that has not been measured**, and that is the same fault as a construction list flat in total and not flat in form. **One lead to carry, and it belongs to the third owed review rather than to you:** the same method on Batch 0005's ten files returns `chapter-0250.md` at **1**, and the card for that batch claims *Batch 0005 ran 3 to 8*. A card figure that does not reproduce is a finding for whoever reviews that batch, and it is named here so it is not lost.

**And the canon figures you must not let a chapter contradict, each checkable by `grep -ro` over `chapters/`:** the **thirty-one** of Mosswake is thirty-one and is a figure in three places; the **Lowcross bill** is nineteen pounds three and fourpence, unpaid, nobody liable; the **guarantee** stands offered and unanswered on a bank about four hundred and forty foot long with about sixty children under sixteen inside it and is printed word for word and not paraphrased; the **reader of seventeen** is on a written engagement at forty-five pence a day and four days a week, is unnamed, is not thanked, is not going to start, and **no elapsed period may be computed from her engagement**; the **Venn ruling** has five operative terms and is never said to have four; the **count of things asked out loud** goes from four to five, once, in Chapter 0250, and **no chapter of this batch may make it five**; **no certification is granted in Volume 05 and none is held**; the word **exception** is not used of anything that is not a Stage 2 instrument and the word **precedent** is not used at all; **nobody is thanked anywhere in this volume**.

**And the distance.** Volume 05 carries `four hundred and thirty` 134 times. `four hundred miles` occurs nowhere in Volume 05. **Chapter 0195 of Volume 04 carries the manuscript's one instance of the short form and it is reported at `reviews/volume-04-batch-0005.md` section one, item five, and Volume 03 uses the short form twelve times for the same river — so if you find the short form in your range, report it as the volume's inconsistency and not as a wrong number, and say which of those two you think it is.**

## Two methods the review before you established, and one warning

**Read every chapter you open, end to end, before you write a finding.** Six of the eleven findings in `reviews/volume-04-batch-0005.md` were invisible to every index: a figure contradicting a canon figure in seven other files, an unstated convention, a missing full stop. **A contradiction shares no run with the line it contradicts and a wrong number shares no run with the right one, so every re-print window, lift, sweep, construction list and calendar parse in this repository is blind to both by construction and not by setting.**

**This manuscript's *"N words"* device has no stated convention anywhere in `outline/`, and the printed instances disagree with each other — 5, 6, 5, 8, 6, 12 and 21 whitespace tokens are each called *four words* somewhere in the manuscript.** **You may report an *N words* claim as a defect only where the quoted span is so far from N that no plausible convention reaches it.** Do not report one at 6 or 8 tokens; do report one at 21. The table of instances is in `reviews/volume-04-batch-0005.md` section one, item three, and it names one live defect in `chapter-0050.md` that is outside your range and is not yours.

**And the warning, which is the most useful thing in this prompt:** *a line number in a file no phase has edited is a citation that resolves, and a line number in a file a phase has edited is a citation of a position and not of a text.* Volume 05 has never been through the prose repair and none of your ten files has been edited since `18e57c8`, so every line number you print will still resolve. **If you find yourself wanting to fix something, that is the moment to write it down instead — a review that edits what it reads cannot be cited as a reading.**

## What you owe the state layer

**Write one file: `reviews/volume-05-batch-0003.md`,** in the shape of the one before it — who wrote it and the statement that it is not independent; why this range; what it did not do; the prose defects located with line numbers; the record claims that hold and the ones that do not, each with its method printed beside the figure; the standing each finding produces; what is left.

**Then append to the state layer and do not amend anything above it:** a section in `state/batch-summary.md` headed for this reading, with the item number in the heading; an item in `state/open-threads.md`; the per-volume row and the manuscript total in `state/current.md`, re-run on the working tree; and a short record in `state/continuity.md` of what was checked and what was found. **Take your item number from the high-water mark in `state/open-threads.md` and do not renumber anything, because renumbering renumbers every cross-reference.**

**Create exactly one next phase prompt**, at `workspace/review-debt-0002/PROMPT.md`, for **Volume 05's Batch 0004, `chapter-0231.md` to `chapter-0240.md`**, in this shape, so that the four owed reviews are four phases and not one. **Resolve its base before you write it and print the base in it**: `git log --oneline -1 -- chapters/volume-05/chapter-023[1-9].md chapters/volume-05/chapter-0240.md` should return `65abf1d` *save review fixes batch-0004*, **assert `git cat-file -e 65abf1d:chapters/volume-05/chapter-0231.md` before you write that down, and if it does not hold, write the commit you verified instead of the one you expected.** A prompt that hands the next phase a wrong base has cost this repository four figures already.

## Rules that hold whatever happens

**Do not edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, `state/phase-ledger.json`, or any outline, including `outline/batches/`.** `tools/measure.py` is an instrument and is not yours to change either; when an instrument is wrong, name the fault and print the case beside it.

**Do not open a chapter for edit.** Not a closed chapter, not a repaired one, not `chapter-0220.md`, not `chapter-0250.md`, not `chapter-0620.md`. **Do not write `state/complete.md`; a phase that writes its own completion signal has certified itself.**

**Do not plan a volume, do not open `outline/ending.md` for edit, and do not add a Volume 13.** **Do not repair prose.** If you find a prose defect, that is the finding and it belongs in `reviews/`, not in a chapter file.

**Commit `reviews/` first, then `state/`, then the one prompt.** Nothing else in any commit. And **print the command beside every figure, and if you cannot print the command, do not print the figure** — because this phase and the four before it have between them found that a total can hold to the digit while every citation beneath it is wrong, that a closed list can be flat in total and not flat in form, and that a record which certifies something clean is worse than a record which is silent.

---

**Three owed reviews remain after this one: Volume 05's Batch 0004, Volume 05's Batch 0005, and Volume 06's own Batch 0003. The review gate itself remains a controller-owned defect and is not among them and may not be fixed by any writing phase — `state/open-threads.md` item 171 records it, and no review any phase writes may be described as independent until a controller owner changes it.**
