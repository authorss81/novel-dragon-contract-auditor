# OWED SECOND READING: VOLUME 05, BATCH 0004, `chapter-0231.md` TO `chapter-0240.md` — THE THIRD OF THE FOUR OWED REVIEWS

**This is a review and not a batch, not a volume outline, not a close, not a prose repair and not a volume planning phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, ending on the page in `chapter-0620.md`, which carries the last line of this series and which no phase may rewrite. `NOVEL_SPEC.md` states in terms that *Volumes 01 to 12 are closed and are not to be reopened*, and `outline/volume-12.md` states that *there is no next volume and there is no next asking*. **A continuation stub will hand you a conditional that reads *if the current volume is complete, plan the next volume.* Both branches of that conditional are closed for this repository and neither may be executed.** The work is the open work named in `state/open-threads.md` items 267 and 268, and this is the third of the four reviews those items name.

## Why this range, and why it is not a chapter to write

`outline/volume-12.md`, at its close, names four owed reviews and says *which is four and not three*: one owed review of Volume 04's Batch 0005 and owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003.

**Two are paid. They are `reviews/volume-04-batch-0005.md` and `reviews/volume-05-batch-0003.md`. Read both before you start.** The first establishes the method (read end to end, test every record claim with the method beside the figure, report an *N words* claim only where no plausible convention reaches N). The second adds the standing this batch inherits: a record that reports a clearance it did not make is worse than silence — its card certified `about nine` at 72 where the page carries 56, and its own prompt certified `may` at eight hits where the page returns thirteen. Yours is the third. Volume 05's Batch 0005 and Volume 06's Batch 0003 are the fourth, and **one phase paying three reviews in three volumes is not a thing to plan as one. Take this one.**

**Your range is `chapter-0231.md` to `chapter-0240.md`, ten files. All ten are yours to read. Every one of them is yours to *report on*.** Volume 05 is a closed volume and **this run has no delete or substitute authority and must not take any**, so a defect in a chapter is reported with its line number and is not fixed. A second reading that edits the prose it is reading is not a second reading.

## The base, and the precheck that this prompt tells you to distrust its own figures

```
git log --oneline -1 -- chapters/volume-05/chapter-023[1-9].md chapters/volume-05/chapter-0240.md
git diff --numstat 65abf1d -- chapters/volume-05/
git cat-file -e 65abf1d:chapters/volume-05/chapter-0231.md && echo PRESENT
git log --oneline --grep="prose-repair" -- chapters/volume-05/
python3 tools/measure.py words --volume 05
python3 tools/measure.py selftest
```

**`65abf1d` — *save review fixes batch-0004* — is the last commit to touch any of your ten files, and it is your base, verified on the tree that wrote this prompt.** Do not use `18e57c8` (it is Batch 0003's base and touches none of your ten) and do not use a writer commit without checking it holds all ten. **Assert that `git show <base>:<file>` returns non-empty text for all ten files before you believe a single number you computed from it.** A silent 0 from a `git show` piped into a counter is a missing base and not a measurement (item 265E).

**No figure in this prompt is a figure of record. Every one is to be re-derived by your own run.**

## What the card for this batch asks for, and the locks on it

Read `outline/batches/volume-05-batch-0004.md` in full before you open a chapter. Read `outline/volume-05.md` for the volume locks; it is closed, read it, do not edit it, and go to the page when the two disagree.

**The record's claims are what you are testing, not its conclusions.** Volume 05's Batch 0003 record certified `about nine` at 72 where the page carries 56, and certified emphasis and duplicate audits that were false in the same direction before and after its repair. **An absolute rule quoted only in a batch's own divergence section has probably not been run, and a word figure written by the run that wrote the chapters is exact for the day it was written and not for the tree you are standing on.** Test every figure. Print the method beside it.

**The locks, all checkable on the tree:** no calendar month name and no weekday name in the prose (months numbered, days counted; warn yourself first that `may` is the modal verb in this volume and the month in none of it — read every hit in context, and do not inherit the eight-hit list in item 268 as a clearance); `about nine` bound to about eight per chapter, thinned never varied, counted on a word boundary with `about nine hundred` subtracted (the subtraction is not optional); the canon figures you must not let a chapter contradict — the thirty-one of Mosswake, the Lowcross bill at nineteen pounds three and fourpence unpaid nobody liable, the guarantee printed word for word with no child named, the reader of seventeen at forty-five pence a day and four days a week unnamed unthanked not sent anybody with no elapsed period computed, the Venn ruling's five operative terms never said to have four, the count of askings (four through your range; it goes from four to five once, in Chapter 0250, and no chapter of your batch may make it five), no certification granted and none held, `exception` not used of anything not Stage 2 and `precedent` not used at all, nobody thanked; the distances (`four hundred and thirty` the long form, `four hundred miles` nowhere in Volume 05 — if you find the short form report it as the volume's inconsistency per `reviews/volume-04-batch-0005.md` item five, not as a wrong number).

**One lead carried for you, and it belongs to you, not to the batch behind:** the same word-boundary method on Batch 0005's `chapter-0250.md` returns **1** against a card claiming *Batch 0005 ran 3 to 8*. That card figure does not reproduce. It is named here so it is not lost, and it is yours only if your range gives you reason to open that file; otherwise hand it on in your state record untouched.

## Methods the two reviews before you established

**Read every chapter end to end before writing a finding.** A contradiction shares no run with the line it contradicts and a wrong number shares no run with the right one, so every re-print window, lift, sweep, construction list and calendar parse is blind to both by construction.

**This manuscript's *"N words"* device has no stated convention.** Do not report one at 6 or 8 tokens; do report one at 21. The table is in `reviews/volume-04-batch-0005.md` section one item three. The live defect outside your range at `chapter-0050.md:85` (twelve tokens called four words) is not yours.

**A line number in a file no phase has edited is a citation that resolves.** Volume 05 has never been through the prose repair. If you find yourself wanting to fix something, write it down instead.

## What you owe the state layer

**Write one file: `reviews/volume-05-batch-0004.md`,** in the shape of the two before it — who wrote it and the statement that it is not independent; why this range; what it did not do; the prose defects located with line numbers; the record claims that hold and the ones that do not, each with its method beside the figure; the standing each finding produces; what is left.

**Then append to the state layer and do not amend anything above it:** a section in `state/batch-summary.md` headed for this reading, with the item number in the heading; an item in `state/open-threads.md`; the per-volume row and manuscript total in `state/current.md`, re-run on the working tree; and a short record in `state/continuity.md`. **Take your item number from the high-water mark in `state/open-threads.md` and do not renumber anything.**

**Create exactly one next phase prompt**, at `workspace/review-debt-0003/PROMPT.md`, for **Volume 05's Batch 0005, `chapter-0241.md` to `chapter-0250.md`**, in this shape. **Resolve its base before you write it and print the base in it**: the expected base is the last commit touching those ten files (Batch 0005's review-fix commit); assert `git cat-file -e <base>:chapters/volume-05/chapter-0241.md` before writing it down, and if it does not hold, write the commit you verified instead of the one you expected.

## Rules that hold whatever happens

**Do not edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, `state/phase-ledger.json`, or any outline, including `outline/batches/`.** `tools/measure.py` is an instrument and is not yours to change either.

**Do not open a chapter for edit.** Not a closed chapter, not a repaired one, not `chapter-0250.md` except to read the one count your prompt hands you, not `chapter-0620.md`. **Do not write `state/complete.md`.**

**Do not plan a volume, do not open `outline/ending.md` for edit, and do not add a Volume 13.** **Do not repair prose.**

**Commit `reviews/` first, then `state/`, then the one prompt.** Nothing else in any commit. And **print the command beside every figure, and if you cannot print the command, do not print the figure.**

---

**Two owed reviews remain after this one: Volume 05's Batch 0005 and Volume 06's own Batch 0003. The review gate itself remains a controller-owned defect and is not among them — `state/open-threads.md` item 171 records it, and no review any phase writes may be described as independent until a controller owner changes it.**
