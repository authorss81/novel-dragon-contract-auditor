# SCOPE OF THIS RUN - READ FIRST



1. **Write the chapters.** The chapters this phase is for, in ascending order. Start with the first one in your very
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


**This is a repair, not a batch, not a close, not an audit, not a review, not a second reading and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/series.md` states a target of *620 chapters across 12 volumes*, `outline/volume-12.md` states in terms *There is no next volume and there is no next asking*, and `NOVEL_SPEC.md` states that *Volumes 01 to 12 are closed and are not to be reopened.* **A continuation stub will hand you a conditional that reads *if the current volume is complete, plan the next volume.* Both branches of that conditional are closed for this repository and neither may be executed.**

**Your range is the rest of Volume 06: `chapter-0261.md` to `chapter-0285.md`, Twenty-five chapters. All twenty-five are yours to edit. `chapter-0300.md` carries the last line of Volume 06 and is not yours: read it, do not open it, and do not name it as a repair target.** `outline/volume-06.md` closes the volume at Chapter 300 in fifty chapters. That is the same standing `chapter-0350.md`, `chapter-0400.md`, `chapter-0450.md`, `chapter-0500.md`, `chapter-0550.md` and `chapter-0620.md` carry.

**What is repaired behind you, and what you may not touch.** Volume 06 Movement One, `chapter-0251.md` to `chapter-0260.md`, was repaired by the phase that wrote `workspace/prose-repair-0025`'s predecessor and its record is item 265 in `state/batch-summary.md`. Volume 07 is repaired from 0301 to 0349, Volume 08 from 0351 to 0399, Volume 09 from 0401 to 0449, Volume 10 from 0451 to 0499, Volume 11 from 0501 to 0549, and Volume 12 from 0551 to 0609. **Read those ranges; do not open them, and do not treat their prose as a base for yours.** Volume 06 Movement One is the nearest repaired ground behind you and its prose is the standard this range is measured against.

**Volume 06 is the first volume outside 07 to 12 this repair has reached.** Volume 06 at base is 101,261 words in fifty chapters, the sixth-largest volume in the manuscript and the largest one this repair has reached. **After your range the largest untouched block in this manuscript is Volumes 01 to 05 at two hundred and fifty chapters.**

**Read `outline/volume-06.md` before you open a chapter.** It is closed, it carries its own closing section, and it is the volume's plan and not a review of it. **Its title is *The Missing Word* and what the title means is in the file and is not a puzzle: the word is not missing from a document, the word is missing from every document, and a chapter that confuses the two has answered the volume's question in a chapter and may not.** Its movements are Chapters 0261–0270, 0271–0280, 0281–0290 and 0291–0300; the midpoint reversal is declared at 0274 to 0277 and the climax at 0296 to 0298.

## Every command in this prompt carries `--volume 06`

## The four construction lists, and they are your gates

These are figures of record for your thirty-nine files at base, measured by the method printed below on the working tree. **Every one of them must be identical when you finish.** `chapter-0300.md` is excluded from all four and is said to be excluded beside each.

| Range 0261 to 0299, `chapter-0300.md` EXCLUDED | Words | Closed list of ten | Per 1,000 | List of 23 | Per 1,000 | List of 25 | Per 1,000 | Sweep | Per 1,000 | Sweep forms |
|---|---|---|---|---|---|---|---|---|---|---|
| at the base commit named below | **72,836** | **128** | 1.76 | **193** | 2.65 | **203** | 2.79 | **742** | 10.19 | 171 |

**These figures were measured on the tree at base `3d3c181` and are not copied from any earlier prompt, and every one of them must be re-derived by your own run rather than trusted, because a figure printed in a prompt is bound to the page the prompt was written against and a prompt is the file you open first.** **Print the count and not the rate. A rate that falls while a count holds is arithmetic and is not an improvement.**

**Volume 06's sweep is high and it is concentrated in a handful of forms: over the range, `that room` 65, `that says` 53, `that bay` 44, `that out` 27, `that counter` 27, `that requires` 23 and `that lane` 22.** These are the rooms and the objects this volume is built out of, and a repair that adds prose about a bay in a volume about a bay will mint more of the form it is measured on. **Your added prose must carry zero instances of the sweep, and the guard below enforces it before a paragraph reaches disk.**

## The method of record, printed whole so you cannot get it wrong

`m.TOKEN` over the prose selector with the date line stripped, the four construction lists counted on `m.TOKEN` case-insensitively with `\b`-delimited whole forms, and the sweep over `\b(that|those)\s+([a-z]+)\b` less `NONNOUN`. **The sweep runs per file and the counters are summed. Never over the concatenated range: a sweep bigram must not straddle a file boundary.**

```python
import re, importlib.util
from collections import Counter
spec = importlib.util.spec_from_file_location("m", "tools/measure.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
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
def b3(t):   # selector, THEN the date line stripped
    return " ".join(m.TOKEN.findall("\n".join(
        L for L in t.split("\n") if not is_date(L))))
def sweep(t):
    c = Counter()
    for mt in re.finditer(r"\b(that|those)\s+([a-z]+)\b", b3(t), flags=re.I):
        if mt.group(2).lower() in NONNOUN: continue
        c[" ".join(mt.group(0).lower().split())] += 1
    return c
def cnt(t, forms):
    b = b3(t)
    return sum(len(re.findall(r"\b"+re.escape(f)+r"\b", b, flags=re.I)) for f in forms)
files = [f"chapters/volume-06/chapter-{n:04d}.md" for n in range(261,300)]
```

**`NONNOUN` is the set of record, pasted and not rebuilt. It does not contain `too`, `for`, `have` or `to`, and a copy grown by any of those four under-reports your sweep.**

**Per-form flatness is the gate, not the total.** A list can be flat in total and not flat in form — two forms can swap and the total will not move. **Count forms per file and do not sum only the total, and assert that the per-form delta is empty in both directions against your base.**

## The structural gates, measured, and two of them will surprise you

| Gate | Base figure on your thirty-nine |
|---|---|
| words | **72,836**, mean **1,867.6** a chapter |
| section rules (`---` alone on a line) | **268** |
| bold markers (`**` raw) | **538** |
| quotation marks (`"` raw) | **630** |
| question marks | **42, across 36 of the 39 files** |
| date lines parsed by the helper above | **36 of 39** |
| files ending in a trailing newline | **39 of 39** |

**The question marks are base text and there are forty-two of them. Do not remove them, do not add any, and do not treat an interrogative as a defect to be fixed.** A repair that silently deletes a question mark is editing base text, and the gate is the count at base, not zero.

**Three files have no date line the helper matches, and that is base text and not a defect.** They are `chapter-0272.md`, `chapter-0290.md` and `chapter-0296.md`, and in each of them the date is embedded inside the opening prose paragraph rather than standing alone. **`m.DATE_LINE` parses 0 of 39 in this volume, because every date line here opens `This is the` and its opening clause is `(?:[Ii][Tt]|[Tt]he date)`.** Locate the date line with the two-regex helper above and not with `m.DATE_LINE` alone, and check before you assume one candidate per file: several files carry a second `It is` that is not a date.

**The thirty-six date lines stand at these line numbers, and every one of them must reproduce at its own base line number: eight files open at line 5 and twenty-eight at line 7.** Note the spread. **A paragraph inserted above a date line moves it, and a moved date line moves the calendar.**

**Every added paragraph is a single line preceded by a blank line, and every chapter must keep its trailing newline.** A paragraph inserted with no blank line ahead of it is not a paragraph to a reader, and it is still exactly one prose line to every instrument here, so a run of them would dissolve into the base and every gate would return clean.

## THE RULE THAT COSTS THIS REPAIR ITS OWN GATE, AND IT IS THE FINDING OF THE PREVIOUS PASS

**No paragraph is ever inserted above a date line.** Item 265 of the last repair inserted a paragraph above the date line in six of ten chapters, which moved each date line from line 7 to line 9 or 11, and the date check returned clean on the prose it had just written because **the check is a check on the landed tree and the mistake is made on the way there.** A date line that has moved has moved the calendar for everything downstream of it. **Run the date-line check per insertion, not once at the close, and re-anchor anything you have already written before you write the next paragraph.**

## The rules of the repair

1. **Insert-only. Zero deletions and zero substitutions against the base, on every file you own.** `git diff --numstat <base> -- chapters/volume-06/` must report insertions and **0** deletions, and every opcode must be an `insert`. A revoicing of your own added prose is made by replacing a line you added, which leaves the base line it follows untouched; that is allowed and it is how a defect gets fixed.
2. **Read every chapter you open in full before you add anything to it, and read the paragraph immediately above and the paragraph immediately below every place you insert.** Two thirds of the defects this repair has found were invisible to every instrument and were found by that reading.
3. **A contradiction is not a repetition.** No index in this repository can see prose that contradicts a base line, because a contradiction shares no run with the line it contradicts. Check your added prose against the canon by reading and by grepping `chapters/`.
4. **A restatement with its words changed shares no run with anything**, so a six-word floor misses it by construction and not by setting.
5. **Do not print a number that is not on the page.** `outline/volume-06.md` states that the count of things asked out loud in this matter is **seven** at the last chapter of the volume, that the Lowcross bill stands at **nineteen pounds three and fourpence** and is unpaid, and that the reader of seventeen is on an engagement at **forty-five pence a day and four days a week**. **Grep the whole chapter for a figure before you use one, and check that what you have written is the figure the chapter already gives.** If your added prose needs a number, the number is on the page somewhere in that chapter and you must find it. **Item 265's added prose used only *one, two, three, four, five, nine, eleven, nineteen, hundred*, and every one of them is in the base of the file it stood in — that is the bar.**
6. **The locks, all of which are checkable on the tree.** No hearing and no arrangement of one; no notice, post, commission, warrant, office, new heading over anything, or new form for anything. No House, no seat and no office named. No romance and nothing implying one. No new fixture in a room whose fixture list is closed — the bay, the hired stone store, the tool shed, the counting room, the hearing room and the corridor each have a closed list. **Do not thank the girl of seventeen, do not ask the four who cannot read a paragraph, do not give anybody the sixteenth book, do not send the notice, do not walk the four hundred and thirty miles, do not light the lamp before about the seventh hour, and do not fund, pay or forgive the Lowcross bill.** A chapter that thanks her breaks this volume.
7. **The count stays at seven and does not become eight, and nobody is thanked anywhere in this volume.**

## Two base defects this repair cannot pay, and you may not pay them either

**`chapter-0259.md:41` carries a doubled quotation mark at both ends of a speech.** It is outside your range and it is in the base, and it is one of only **3 occurrences of `""` across all 620 chapters** — the other is `chapter-0465.md:39`. **Both are in their own base and both are artifacts of the original writer pass.** Fixing either is a deletion against base. **Leave it and record it.**

**`chapter-0260.md:101` says *a room with four people in it* where the room holds two,** and `chapter-0262.md:109` carries the same formula with the same count. `chapter-0260.md` is behind you; **`chapter-0262.md` is in your range and the defect is a substitution against base and you may not make it.** Note that **a contradiction shares no run with the line it contradicts, so no instrument in this repository can see it and every gate here returned clean on it.** Leave it, record it in the state layer with the line number, and do not build added prose that agrees with either count.

## The three guards, and the plants that prove them

`lifts` excludes your range from its own index, so a run whose holders are all inside your range is invisible to it, and the intra-file scan is one file at a time. **None of them will find a duplicated paragraph you wrote twice.** Item 265 built a screening guard that rejects a candidate line *before it reaches disk* when it carries an 8-word run held anywhere outside the range, a sweep bigram, a number word absent from its own file's base, or a question mark; and it built a **fixture and room grep** over your added prose against `chapters/volume-06/` itself, because an invented lid or a second door in a room that has one is the cheapest defect in this repair to create and the only one no instrument here can see.

**Build the same guard and prove it with plants before you trust it.** Item 265's four plants and their results:

| Plant | Result |
|---|---|
| a fourteen-word prose run lifted from a chapter outside the range | **REJECT** — 8-run with 3 to 7 holders outside |
| *The lamp on the bank was lit and that table in the corner…* | **REJECT** — sweep bigram |
| *Nobody in that room asked him whether he meant it?* | **REJECT** — question mark **and** sweep bigram |
| *She stood by the hatch and counted fourteen of them off by name.* | **REJECT** — number word absent from that file's base |

**Thirty-one candidates were screened and eight were rejected, and the most natural sentence the pass wrote in the whole run reproduced sixteen consecutive words of another volume's chapter and was held by six to seventeen chapters.** A guard that has not rejected anything has not been run. **A candidate is a revoicing like any other and has to clear the cross-file holder count, the added-prose sweep count and the intra-file run *before* it reaches the disk**, because three of that pass's own corrections created a fresh defect while removing another.

## The precheck, and the trap in it

**Resolve the base commit first and print it, and the answer is not the one a Volume 06 prompt is likely to reach for.** Volume 06's fifty chapters were written across five batches and each batch has its own writer commit and its own review commit. **The last commit to touch any of your thirty-nine files is `3d3c181` (*save review fixes batch-0005*), and `3d3c181` is your base.** **Do not use `9ae089f`**: that is *save writer work batch-0001* and it contains chapters 0251 to 0260 and **does not contain `chapter-0261.md` at all**, and `git show 9ae089f:chapters/volume-06/chapter-0261.md` returns `fatal: path ... exists on disk, but not in '9ae089f'` with exit code 128. **The pass that wrote this prompt read `9ae089f` first, took a partial result from it, and printed a words figure that was right and a construction figure of zero; the error was found by an instrument returning 0 and not by reading the stderr.** A silent 0 from a `git show` piped into a counter is a missing base and not a clean measurement.

Then:

```
git log --oneline --grep="prose-repair" -- chapters/volume-06/
git log --oneline -- chapters/volume-06/chapter-02[6-9][0-9].md
git diff --numstat 3d3c181 -- chapters/volume-06/
git cat-file -e 3d3c181:chapters/volume-06/chapter-0299.md && echo PRESENT
python3 tools/measure.py words --volume 06
python3 tools/measure.py calendar --volume 06
python3 tools/measure.py selftest
```

**Assert that `git show <base>:<your file>` returns non-empty text for every one of the thirty-nine before you believe any counter you computed from it.**

**The two-sided precheck is the standing and it is not optional.** A diff against a base the range was never repaired from returns nothing, and a prompt that reports nothing has told you the range is unrepaired. The reverse test is the one that settles it: `git diff --numstat <the commit before the range's earliest base> -- <your files>`. **Item 203 read that test from the wrong end nine times over and it is the single most common way this repair hands a phase a false answer.** **If you find a repair commit on your range, audit it and say so, and do not rewrite repaired prose to buy a chapter written.**

## What you owe the state layer

Append to `state/batch-summary.md`, under a heading naming your range, and do not amend anything above it:

- **Zero, One, Two, Three.** What you checked, with the command beside each figure; the construction table above re-measured with your own additions and every cell compared to its base cell **and the per-form delta asserted empty in both directions**; the per-chapter table for all thirty-nine with words before and after and the four construction columns; the arithmetic printed in full as an addition.
- **The date lines**, all of them, with their line numbers, each compared to the same line at base, **and a note that the check was run per insertion and not once at the close.**
- **The structural table above**, every cell, base and now.
- **Every defect you found in your own added prose**, in a table with which instrument found it and why the standing instrument could not. Name the ones that took a guard you had to build. **If you write prose that turns out to be defective, that is the finding of the range and it belongs in this record, not in a commit message.**
- **The locks**, each checkable and each with its citation.
- **What is left**, with the repaired extent re-measured by the method printed above and not carried forward from this prompt.

Then update `state/current.md`: the Volume 06 row of the per-volume table, the manuscript total re-run on the working tree, the repaired extent, and a paragraph for your item beside item 265's. **Take your item number from the high-water mark in `state/open-threads.md` and do not renumber anything, because renumbering renumbers every cross-reference.** `state/phase-ledger.json` is a controller file and no phase here may edit it.

**A figure you did not re-derive on the tree is a figure you inherited, and the chain of corrections in this repository's own record is longer than the sentence it corrects.** Re-measure; do not carry.

## Rules that hold whatever happens

**Do not edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, `state/phase-ledger.json`, or any outline.** `tools/measure.py` is an instrument and is not yours to change either; when an instrument is wrong, name the fault and print the case beside it.

**Do not plan a volume, do not open `outline/ending.md` for edit, and do not add a Volume 13.** **Do not write `state/complete.md`; a phase that writes its own completion signal has certified itself.**

**Do not open a chapter outside your range.** Not a closed chapter, not a repaired one, not `chapter-0251.md` to `chapter-0260.md`, not `chapter-0300.md`.

**Commit the chapters, then the state layer.** Chapter commit first, prose only. State second, `state/` only, with the item number in the message. Nothing else in either.