# OWED REVIEW: VOLUME 06, BATCH 0003, `chapter-0261.md` TO `chapter-0270.md` — THE FOURTH OF THE FOUR OWED, AND THE LAST ONE THAT HAS NO PROMPT

**This is a review and not a batch, not a volume outline, not a close, not a prose repair and not a volume planning phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, ending on the page in `chapter-0620.md`, which carries the last line of this series and which no phase may rewrite. `NOVEL_SPEC.md` states in terms that *Volumes 01 to 12 are closed and are not to be reopened*, and `outline/volume-12.md` states that *there is no next volume and there is no next asking*. **A continuation stub will hand you a conditional that reads *if the current volume is complete, plan the next volume.* Both branches of that conditional are closed for this repository and neither may be executed.** The work is the open work named in `state/open-threads.md` item 170 and item 267, and this is the fourth of the four reviews `outline/volume-12.md` names.

**Why this range, and why it is not a chapter to write.** `outline/volume-12.md`, at its close, names four owed reviews and says *which is four and not three*:

> *One:* an owed review of Volume 04's Batch 0005, four volumes on. *Two, three and four:* owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003.

**All three of the others are paid and on disk: `reviews/volume-04-batch-0005.md`, `reviews/volume-05-batch-0003.md`, `reviews/volume-05-batch-0004.md`. This one has no prompt and no file, and it has been named as the outstanding one at items 270E, 275C, 276E, 277C, 279D and 280C. Take this one.** Read `reviews/volume-05-batch-0003.md` before you start, because it is the shape a paid review of this kind takes, and `reviews/volume-05-batch-0003-verification.md` and `reviews/volume-05-batch-0003-third-audit.md` beside it, because the second of those carries the method and the third carries the standing this prompt inherits at its section four.

**Your range is `chapter-0261.md` to `chapter-0270.md`, ten files. All ten are yours to read. Every one of them is yours to report on.** Volume 06 is a closed volume and **this run has no delete or substitute authority and must not take any**, so a defect in a chapter is reported with its line number and is not fixed. A second reading that edits the prose it is reading is not a second reading.

## The base, and the trap that is waiting for you

**This range is repaired, and the prompt that reaches you may well say it is not.** Resolve the base before anything else:

```
git log --oneline -3 -- chapters/volume-06/chapter-026[1-9].md chapters/volume-06/chapter-0270.md
git cat-file -e d8f15cd:chapters/volume-06/chapter-0261.md && echo PRESENT
git diff --numstat d8f15cd -- chapters/volume-06/chapter-026[1-9].md chapters/volume-06/chapter-0270.md
git log --oneline --grep="prose repair" -- chapters/volume-06/
git log --oneline --grep="prose-repair" -- chapters/volume-06/
```

**`d8f15cd` is the base, and it was resolved and asserted on the tree this prompt was written against:** `git log --oneline -3` over the ten returns `d8f15cd` (*re-audit of chapter-0261 to chapter-0299 …*), `f85323d` (*prose repair of chapter-0261.md to chapter-0299.md, the whole of Volume 06 outside its last chapter, gives 124 scenes their physical bodies …*) and `6d47146`; `git cat-file -e d8f15cd:<each of the ten>` returns **PRESENT ten times out of ten**, and `git diff --numstat d8f15cd -- <the ten files>` returned **nothing**, so the worktree and the base are byte-identical. **Assert that `git show <base>:<file>` returns non-empty text for all ten before you believe a single number computed from it.**

**The trap, and it has already cost this repository four figures and thirty-nine chapters.** `git log --oneline --grep="prose-repair" -- chapters/volume-06/` returns **nothing**, because the commits read *prose repair*, *re-audit* and *second audit* **without the hyphen**. `git log --oneline --grep="prose repair" -- chapters/volume-06/` returns **two**. **A dispatch that trusted the hyphenated grep would have concluded this range unrepaired and rebuilt ten chapters that are already repaired.** This is the ninth time that shape has cost a dispatch and it is recorded at items 281A and 282A. **A grep string is a claim about commit messages and not about the tree; the per-path log is the evidence.**

**So: this is a review of repaired prose, not of a writer's first pass, and that changes what you are looking for.** Items 269, 273, 274, 278, 281 and 282 have already audited this range five times, all six of those audits finding the repair clean apart from defects in the repair's own added prose. **Your job is not a sixth audit of the repair.** It is to read ten chapters as prose and report what is wrong with them, **and to say plainly whether the added paragraphs changed anything the added paragraphs were supposed to change.** `f85323d` inserted 248 lines across the range, every opcode an `insert` and no deletions, and it held all four construction lists exactly flat at 128 / 193 / 203 / 742 across 171 sweep forms. **A list that is flat in total and not flat in form has been the standing failure in this manuscript twice, so check the per-form delta and not the total.**

**Two base defects in this range are already recorded and are not yours: `chapter-0259.md:41` and `chapter-0262.md:109`** — the latter, *a room with four people in it* where the room holds two, is the item 269 class, a contradiction that shares no run with the line it contradicts. Both are outside your ten files. **Do not open them.**

## What is owed, and the two locks on it

Read `outline/batches/volume-06-batch-0003.md` in full before you open a chapter, and **`outline/volume-06.md` is closed and is the volume outline of record; read it, do not edit it, and go to the page rather than to a line when the two disagree.**

**The record's claims are what you are testing, not its conclusions.** Across this repository a card figure has been exact for the day it was written and not for the tree you are standing on, and an absolute rule quoted only in a batch's own divergence section has turned out to have been broken six times in four chapters. **Test every figure. Print the method beside it.**

**The locks, both checkable on the tree, both from `outline/volume-06.md`:**

1. **No calendar month name and no weekday name may appear in the prose.** Months are numbered and days are counted. **Warn yourself about one thing before you run the check, or you will spend the run on it: `may` is the modal verb in this manuscript and the month in none of it.** A naive run returns raw hits and every one of them is the modal. **Run it, read the surrounding line, and move on; the finding is that a lock whose only near-miss is a homograph has to be checked by reading and not by matching.** Run it across the whole of Volume 06 and say whether the lock holds across all fifty chapters and not only in your ten, because a lock certified in ten files is not a lock.
2. **`about nine` is bound to about eight per chapter, and it is thinned and never varied.** **You must subtract "about nine hundred" yourself and the subtraction is not optional**: a raw count of `about nine\b` matches the `about nine` inside `about nine hundred`, and across Volume 05 that inflation is **18 instances over ten chapters**, taking `chapter-0221` from 5 to 9 and `chapter-0228` from 3 to 7. **A lock measured with the wrong denominator is a lock that has not been measured.**

**And the canon figures you must not let a chapter contradict, each checkable by `grep -ro` over `chapters/`:** the **thirty-one** of Mosswake; the **Lowcross bill** at nineteen pounds three and fourpence, unpaid, nobody liable; the **guarantee** standing offered and unanswered on about four hundred and forty foot of bank with about sixty children under sixteen inside it, printed word for word and not paraphrased; the **reader of seventeen** on a written engagement, unnamed, not thanked, not going to start, and **no elapsed period may be computed from her engagement**; the **count of things asked out loud** and whether it moves in your ten. **Read `outline/volume-06.md` for the rest and derive each one yourself rather than trusting this list, because this list is a prompt and every prompt in this repository's record has been wrong somewhere.**

## Three methods the reviews before you established

**Read every chapter you open, end to end, before you write a finding.** Six of the eleven findings in `reviews/volume-04-batch-0005.md` were invisible to every index: a figure contradicting a canon figure in seven other files, an unstated convention, a missing full stop. **A contradiction shares no run with the line it contradicts and a wrong number shares no run with the right one, so every re-print window, lift, sweep, construction list and calendar parse in this repository is blind to both by construction and not by setting.** And in `chapter-0225.md` there is a count that disagrees with the count beside it two lines apart — *eleven times* against *the thirteenth time* — which is a **third class**: not a contradiction with a canon figure, not a span against a calendar, but **a figure against its own neighbour.** **Nothing in this repository checks that, and it is the cheapest class of all.**

**This manuscript's *"N words"* device has no stated convention anywhere in `outline/`**, and 5, 6, 8, 12 and 21 whitespace tokens are each called *four words* somewhere in the manuscript. **You may report an *N words* claim only where the quoted span is so far from N that no plausible convention reaches it. Do not report one at 6 or 8 tokens; do report one at 21.** The table is in `reviews/volume-04-batch-0005.md` section one, item three. **And sweep for the device rather than reading for it:** in `reviews/volume-05-batch-0003.md` a clearance list enumerated four instances of it and missed the fifth, which was the only real one.

**And the warning, which is the most useful thing in this prompt:** *a line number in a file no phase has edited is a citation that resolves, and a line number in a file a phase has edited is a citation of a position and not of a text.* **Your range HAS been edited, by `f85323d` and then `d8f15cd`.** So **find out whether a defect you locate is base text or the repair's own added prose, and say which**, because a line number here resolves to a position that a repair can move, and a defect in base text and a defect in a repair's added prose are different faults with different owners. `git diff --numstat d8f15cd -- <file>` and `git diff 3d3c181 -- <file>` will tell you which is which. **If you find yourself wanting to fix something, that is the moment to write it down instead — a review that edits what it reads cannot be cited as a reading.**

## What you owe the state layer

**Write one file: `reviews/volume-06-batch-0003.md`**, in the shape of the ones before it — who wrote it and the statement that it is not independent; why this range; what it did not do; the prose defects located with line numbers and marked base or added; the record claims that hold and the ones that do not, each with its method printed beside the figure; the standing each finding produces; what is left.

**Then append to the state layer and do not amend anything above it:** a section in `state/batch-summary.md` headed for this reading, with the item number in the heading; an item in `state/open-threads.md`; the per-volume row and the manuscript total in `state/current.md`, re-run on the working tree with `python3 tools/measure.py words` and **never with a glob**; and a short record in `state/continuity.md` of what was checked and what was found. **Take your item number from the high-water mark at the bottom of `state/open-threads.md` and do not renumber anything, because renumbering renumbers every cross-reference.**

**Check whether any prompt for this review already exists before you write yours,** as items 275C, 276E, 277C, 279D and 280C all had to: five successive dispatches in this repository have been handed a prompt naming a phase that was already paid, and each found the named prompt on disk and refused to overwrite it. **This prompt is `workspace/review-debt-0004/PROMPT.md`. If your work is already paid when you arrive, audit it, write a sibling, and do not amend it and do not mark this directory.**

## Rules that hold whatever happens

**Do not edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, `state/phase-ledger.json`, or any outline, including `outline/batches/`.** `tools/measure.py` is an instrument and is not yours to change either; **when an instrument is wrong, name the fault and print the case beside it** — `m.DATE_LINE` parses one chapter in fifty of Volume 06 and five ranges have now recorded that, which is why the calendar work above must be done by hand.

**Do not open a chapter for edit.** Not a closed chapter, not a repaired one, not `chapter-0300.md`, not `chapter-0620.md`. **Do not write `state/complete.md`; a phase that writes its own completion signal has certified itself.** `state/phase-ledger.json` reads `phase-000-bootstrap` and is a controller file — it is not a symptom of anything and not a usable source of phase position.

**Do not plan a volume, do not open `outline/ending.md` for edit, and do not add a Volume 13. Do not repair prose.** If you find a prose defect, that is the finding and it belongs in `reviews/`, not in a chapter file.

**Commit `reviews/` first, then `state/`, then the one prompt. Nothing else in any commit. And print the command beside every figure, and if you cannot print the command, do not print the figure** — because the phases before you have between them found that a total can hold to the digit while every citation beneath it is wrong, that a closed list can be flat in total and not flat in form, and that a record which certifies something clean is worse than a record which is silent.

---

**This is the fourth of the four owed reviews named at `outline/volume-12.md`'s close, and paying it closes the review debt. The review gate itself remains a controller-owned defect and is not among them and may not be fixed by any writing phase — `state/open-threads.md` item 171 records it, and no review any phase writes may be described as independent until a controller owner changes it.**