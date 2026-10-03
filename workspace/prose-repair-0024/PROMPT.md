# PROSE REPAIR, FIFTY CHAPTERS: Chapters 0301 to 0350 — THE WHOLE OF VOLUME 07, AND A CHAPTER THAT CARRIES THE LAST LINE OF THE VOLUME AND IS NOT YOURS

**This is a repair, not a batch, not a close, not a review, not a second reading and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/series.md` states in terms that there is no next volume. **This prompt names no volume to plan and no phase may plan one.**

**Your range is the whole of Volume 07: `chapter-0301.md` to `chapter-0350.md`, fifty chapters. Forty-nine of the fifty are yours to edit. `chapter-0350.md` carries the last line of Volume 07 and is not yours: read it, do not open it, and do not name it as a repair target.** `outline/volume-07.md` closes the volume at Chapter 350 in fifty chapters and its last line is on the page. That is the same standing `chapter-0400.md`, `chapter-0450.md`, `chapter-0500.md`, `chapter-0550.md` and `chapter-0620.md` carry. **Volume 07 is the first volume anyone has repaired that is not Volume 08, 09, 10, 11 or 12, and the first unrepaired volume to be reached: Volumes 01 to 07 were all untouched until now.**

**Read `outline/volume-07.md` before you open a chapter.** It is closed, it carries its own closing section, and it is the volume's plan and not a review of it. Its five movements are Chapters 0301–0310, 0311–0320, 0321–0330, 0331–0340 and 0341–0350; the midpoint reversal is declared at 0324 to 0327 and the climax at 0346 to 0348.

**What is repaired behind you, and what you may not touch.** Volume 08 is repaired from 0351 to 0399, Volume 09 from 0401 to 0449, **Volume 10 from 0451 to 0499**, Volume 11 from 0501 to 0549, and Volume 12 from 0551 to 0609. Read those ranges; do not open them, and do not treat their prose as a base for yours.

**The repaired extent, measured on the tree at item 232's close: 255 of 620 chapters, and 365 unrepaired.** Volumes 08, 09, 10 and 11 are repaired through all but their last chapter, Volume 12 through 0551 to 0609, and the repaired set is **255 chapters at 431,546 words at a mean of 1,692.3**. The unrepaired 365 is **Volumes 01 to 07 at 350, plus the five volume endings, plus Volume 12's `chapter-0610.md` to `chapter-0619.md` at 10.** **After your range the unrepaired 316 is Volumes 01 to 06 at 300, your own volume's `chapter-0350.md`, the four endings behind you, and Volume 12's ten — and the largest untouched block in this manuscript becomes Volumes 01 to 06 at three hundred chapters.**

**Volume 12's `chapter-0610.md` to `chapter-0619.md` carry no prose-repair commit and were never the target range of a prompt.** They stand with the prose of the earlier first-round repair that `workspace/prose-repair-0002/PROMPT.md` records as found defective, and no phase may settle whether they are repaired. They are not your range and not this prompt's business.

## Every command in this prompt carries `--volume 07`

## The four construction lists, measured, and they are your gates

These are figures of record for your forty-nine files at base, and every one of them must be identical when you finish. `chapter-0350.md` is excluded from all four and is said to be excluded beside each.

| Range 0301 to 0349, `chapter-0350.md` EXCLUDED | Words | Closed list of ten | Per 1,000 | List of 23 | Per 1,000 | List of 25 | Per 1,000 | Sweep | Per 1,000 | Sweep forms |
|---|---|---|---|---|---|---|---|---|---|---|
| at the base commit named below | **70,886** | **165** | 2.33 | **212** | 2.99 | **243** | 3.43 | **723** | 10.20 | 182 |

**165 is far below the 352 that Volume 10 carried, and that is the finding about this volume rather than a target: the defect in Volume 07 is not the demonstrative-anaphora construction.** Your added prose must not move any of the four lists. A rate that falls while a count holds is arithmetic and is not an improvement; print the count, not the rate, and print both.

**Method 3 is the figure of record and is printed whole so you cannot get it wrong.** `m.TOKEN` over the prose selector with the date line stripped, the four construction lists counted on `m.TOKEN` case-insensitively with `\b`-delimited whole forms, and the sweep over `\b(that|those)\s+([a-z]+)\b` less `NONNOUN`. **The sweep runs per file and the counters are summed. Never over the concatenated range: a sweep bigram must not straddle a file boundary, and concatenating mints one bigram at each seam.**

```python
import re, importlib.util, subprocess
from collections import Counter
spec = importlib.util.spec_from_file_location("m", "tools/measure.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
BASE = "<the base commit you resolve; see the precheck below>"
TEN  = ["those boards","that lane","that floor","that table","that door",
        "that stair","that room","that passage","that tin","that sheet"]
ADD  = ["that end","that landing","that bench","that sill","that corridor","that case",
        "those stairs","that step","that bay","that ground","that jug","that stone","that board"]
NEW  = ["that building","that house"]
LIST23 = TEN + ADD; LIST25 = LIST23 + NEW          # 10 + 13 + 2 = 25
NONNOUN = set("""is was has had are were be been being am i we he she it they you me my our
their there here then than when where which who whom whose what why how and or but if so as
a an the this these those no not nor do does did done can could will would shall should may
might must one two three four five six seven eight nine ten anybody anything someone something
nobody nothing everyone everything""".split())
DATE_EITHER = re.compile(r"^(This|It) is the .* day of the .* week of the .* month of the year after.*$")
DATE_THIRD  = re.compile(r"^The date is the .* day of the .* week of the .* month of the year after.*$")
def is_date(L): return bool(DATE_EITHER.match(L) or DATE_THIRD.match(L))
def b3(t):   # THE FIGURE OF RECORD: selector, THEN the date line stripped
    return " ".join(m.TOKEN.findall("\n".join(
        L for L in t.split("\n") if not is_date(L))))
def sweep(t):
    c = Counter()
    for mt in re.finditer(r"\b(that|those)\s+([a-z]+)\b", t, flags=re.I):
        if mt.group(2).lower() in NONNOUN: continue
        c[" ".join(mt.group(0).lower().split())] += 1
    return c
def cnt(t, forms):
    b = b3(t)
    return sum(len(re.findall(r"\b"+re.escape(f)+r"\b", b, flags=re.I)) for f in forms)
files = [f"chapters/volume-07/chapter-{n:04d}.md" for n in range(301,350)]
```

**`NONNOUN` is the set of record, pasted and not rebuilt. It does not contain `too`, `for`, `have` or `to`, and a copy grown by any of those four under-reports your sweep.**

## The structural gates, measured, and one of them will surprise you

| Gate | Base figure on your forty-nine |
|---|---|
| words | **70,886**, mean **1,446.7** a chapter |
| section rules (`---` alone on a line) | **262** |
| bold markers (`**` raw) | **408** |
| quotation marks (`"` raw) | **334** |
| **question marks** | **40, across 38 of the 49 files** |
| date lines parsed | **49 of 49** |

**The question marks are base text and there are forty of them, and this volume is the first repaired range that carries any.** Volume 10 carries zero. **Do not remove them, do not add any, and do not treat an interrogative as a defect to be fixed.** A repair that silently deletes a question mark is editing base text, and the gate is the count at base, not zero.

**The date-line positions are 11, 13, 11, 11, 9, 11, 11, 11, 11, 13, 11, 11, 11, 11, 9, 7, 9, 9, 9, 11, 7, 11, 15, 9, 11, 11, 11, 9, 11, 9, 7, 7, 7, 7, 7, 7, 5, 5, 7, 5, 7, 7, 9, 7, 7, 7, 7, 7, 7, and every one of them must reproduce at its own line number.** Note the spread: five files open at line 5, seven at line 7, and one at line 15. **Locate the date line with `m.DATE_LINE` itself and by nothing else.** A date line found by `startswith("It is ")` is a different function and several of your files carry a second `It is` that is not a date — check before you assume one candidate per file.

**Every added paragraph is a single line preceded by a blank line, and every chapter must keep its trailing newline.** A paragraph inserted at a line number with no blank line ahead of it is not a paragraph to a reader, and it is still exactly one prose line to every instrument in this repository, so fifty of them would dissolve into the base and every gate would return clean.

## The rules of the repair

1. **Insert-only. Zero deletions and zero substitutions against the base, on every file you own.** `git diff --numstat <base> -- chapters/volume-07/` must report insertions and **0** deletions across your forty-nine files, and every opcode must be an `insert`. A revoicing of your own added prose is made by replacing a line you added, which leaves the base line it follows untouched; that is allowed and it is how a defect gets fixed.
2. **Read every chapter you open in full before you add anything to it, and read the paragraph immediately above and the paragraph immediately below every place you insert.** Two thirds of the defects this repair has found were invisible to every instrument and were found by that reading.
3. **A contradiction is not a repetition.** No index in this repository can see prose that contradicts a base line, because a contradiction shares no run with the line it contradicts. You must check your added prose against the canon by reading and by grepping `chapters/`, not by trusting a clean scan.
4. **A restatement with its words changed shares no run with anything**, so the intra-file scan's six-word floor misses it by construction and not by setting.
5. **Do not print a number that is not on the page.** `outline/volume-07.md` closes at Chapter 350 and states that the count of things asked out loud in this matter is **seven**, that the figure at the end of the cold passage is not handed on and does not get a heading, and that the Lowcross bill stands at nineteen pounds three and fourpence. **Grep the whole chapter for a figure before you use one, and check that what you have written is the figure the chapter already gives.** If your added prose needs a number, the number is already on the page somewhere in that chapter and you must find it.
6. **The locks, all of which are checkable on the tree.** No hearing and no arrangement of one; no notice, post, commission, warrant, office, new heading over anything, or new form for anything. No House, no seat and no office named. No romance and nothing implying one. No new fixture in a room whose fixture list is closed. **Do not thank the girl of seventeen, do not ask the four who cannot read a paragraph, do not give anybody the sixteenth book, do not send the notice, do not walk the four hundred and thirty miles, do not light the lamp before about the seventh hour, and do not fund, pay or forgive the Lowcross bill.** A chapter that thanks her breaks this volume.
7. **The count stays at seven and does not become eight.** That is this volume's own lock and it is the sentence its closing section turns on.

## What the four standing instruments cannot see, and the two guards you must build before you write

`lifts` excludes your range from its own index, so a run whose holders are all inside your range is invisible to it. The intra-file scan is one file at a time. The twelve-word index cannot see a run whose only holders are your own. **None of them will find a duplicated paragraph you wrote twice, and the finding of the last repair of this kind was that three scans had to be built from scratch to find twenty-four defects that every standing index had passed.**

**Build these two guards and run them on candidates BEFORE the candidate reaches the disk, not after:**

- **A screening guard** that takes a candidate line and rejects it if it carries a run at or above eight words held anywhere outside your range, or a sweep bigram, or a banned floor material, or a question mark. Item 221's standing is that a candidate has to clear the cross-file holder count, the added-prose sweep count and the intra-file run **before** it is written, because three of that pass's own corrections created a fresh defect while removing another.
- **A number-word scan** over your added prose that checks every number word against the base of its own file. **A claim that your added prose carries no unprinted figure is a claim, and you have to run it.** The last repair asserted that its added paragraphs carried no numeral and no number word at all, and seventy-three of its 183 paragraphs carried a number word, one of which contradicted a base figure four lines above it.

**And run one more, because Volume 07's rooms are older than Volume 10's and their canon is in this volume and not in the one behind you:** a grep of every fixture, room and object your added prose names against `chapters/volume-07/` itself. **The fixture list of a room is closed by the chapter that fixes it, and an invented lid, an invented rail or an invented second door in a room that has one of each is the cheapest defect in this repair to create and the only one no instrument here can see.**

## The precheck, and the trap in it

Resolve the base commit first and print it. Then:

```
git log --oneline -- chapters/volume-07/chapter-03[0-4][0-9].md
git diff --numstat <base> -- chapters/volume-07/
python3 tools/measure.py words --volume 07
python3 tools/measure.py calendar
python3 tools/measure.py selftest
```

**Volume 07 has never been through this repair and carries no `prose-repair` commit, so a `git log` that prints nothing is the expected answer and the correct one. If it prints a repair commit, you are dispatched on a range that has already been repaired: audit it and say so, and do not rewrite repaired prose to buy a chapter written.** Items 212 and 217 record what happens when a phase is pushed to write a chapter it has no business writing, and both recorded the unmet rule rather than satisfying it destructively.

**A two-sided precheck is the standing and it is not optional.** A diff against a base the range was never repaired from returns nothing, and a prompt that reports nothing has told you the range is unrepaired. The reverse test is the one that settles it: `git diff --numstat <the commit before the range's earliest base> -- <your files>`. Item 203 read that test from the wrong end nine times over and it is the single most common way this repair hands a phase a false answer.

## What you owe the state layer

Append to `state/batch-summary.md`, under a heading naming your range, and do not amend anything above it:

- **Zero, One, Two, Three.** What you checked, with the command beside each figure; the construction table above re-measured with your own additions and every cell compared to its base cell; the per-chapter table for all forty-nine with words before and after and the four construction columns, computed on method 3; the arithmetic printed in full as an addition, so a paragraph a helper dropped is visible in the sum.
- **The date lines**, all forty-nine, with their line numbers, each compared to the same line at base.
- **The structural table above**, every cell, base and now.
- **Every defect you found in your own added prose, in a table with which instrument found it and why the standing instrument could not.** Name the ones that took a guard you had to build. **If you write prose that turns out to be defective, that is the finding of the range and it belongs in this record, not in a commit message.**
- **The locks**, each checkable and each with its citation.
- **What is left**, with the repaired extent re-measured by the method printed above and not carried forward from this prompt.

Then update `state/current.md`: the Volume 07 row of the per-volume table, the manuscript total re-run on the working tree, the repaired extent, and a paragraph for your item beside item 232's. Take your item number from the high-water mark in `state/open-threads.md` and **do not renumber anything**, because renumbering renumbers every cross-reference. `state/phase-ledger.json` is a controller file and no phase here may edit it.

**A figure you did not re-derive on the tree is a figure you inherited, and the chain of corrections in this repository's own record is longer than the sentence it corrects.** Re-measure; do not carry.

## Rules that hold whatever happens

**Do not edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, `state/phase-ledger.json`, or any outline.** `tools/measure.py` is an instrument and is not yours to change either; when an instrument is wrong, name the fault and print the case beside it, which this repair has done nine times.

**Do not plan a volume, do not open `outline/ending.md` for edit, and do not add a Volume 13.**

**Do not open a chapter outside your range.** Not a closed chapter, not a repaired one, not `chapter-0350.md`.

**Commit the chapters, then the state layer.** Chapter commit first, prose only. State second, `state/` only, with the item number in the message. Nothing else in either.
