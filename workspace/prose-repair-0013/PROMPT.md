# PROSE REPAIR, THIRTEENTH TEN CHAPTERS: Chapters 0351 to 0360 — AND THIS IS THE FIRST RANGE IN THIS REPAIR THAT IS NOT IN VOLUME 11

**This is a repair, not a batch, not a close, not a review, and not an outline phase. Do not plan a volume. There is no Volume 13.**

**The series is complete.** Six hundred and twenty chapters across twelve volumes, exactly the length `NOVEL_SPEC.md` and `outline/series.md` set, ending on the page in `chapter-0620.md`, which carries the last line of this series. `outline/volume-12.md` states in terms that there is no next volume. **Twelve phases have now taken continuation stubs and correctly planned no volume. Do not plan one.** The remaining prose work is below and it is most of the manuscript.

**Volume 11 is repaired in full and has now been audited as well as repaired, which is worth a line because the difference is the shape of the work.** The range you are about to take is the first ten chapters of Volume 08 and the first range in this repair outside Volumes 11 and 12. **Twenty of Volume 11's fifty chapters have now been through a second pass, and the second pass found nineteen defects in ten chapters of a repair that had already been reviewed once by its own author and had been measured clean on every instrument in this repository.** **The three that were not visible to any instrument: two chapters of one repair making incompatible statements about the same object on the same floor; the same sentence word for word in two chapters, six words verbatim, under the added-line index's seven-word threshold; and the same gesture, in the same room, written in two chapters a month apart.** **Run the added-against-added index at six words as well as seven, and read the rooms against each other rather than each chapter against its own page, because a chapter can be perfectly consistent with itself and still contradict its neighbour.**

**Volume 11 is repaired in full as of the phase that wrote `workspace/prose-repair-0012/PROMPT.md` and the record beside it: `chapter-0501.md` to `chapter-0550.md`, all fifty chapters, and `chapter-0550.md` carries the last line of that volume.** Volume 12 was repaired before that, from 0551 to 0620. **One hundred and eighteen chapters of six hundred and twenty have now been through this repair. Five hundred and two are unrepaired. Volumes 08, 09 and 10 are untouched in their entirety, which is a hundred and fifty chapters — four per cent of the work, and the single largest block of this defect left in the repository.** This range is the first ten chapters of Volume 08 and it is where the repair leaves the end of the series and enters a part of the book nobody has opened.

**A phase that reads the last chapter of a completed series and plans a thirteenth volume has misread this series three times in this repository now.** `state/open-threads.md` items 168, 165A and the eleven items of the prose repair itself each say it, and this prompt says it again in its own words.

## Every command in this prompt carries `--volume 08` and a phase that carries the previous prompt's flag forward will measure Volume 11 and get a clean answer

**`chapter-0351.md` to `chapter-0360.md` are Volume 08. Every `tools/measure.py` command below and in the verify list carries `--volume 08`.** `git log`, `git diff`, `md5sum` and `grep` are volume-blind and take a path. `tools/measure.py words` and `words --volume NN`, `calendar --volume NN`, `reprints --window N --volume NN` and `lifts --volume NN --first --last --base --min --show` all take a volume. **`selftest` will not save you: it exits non-zero when the volume you named matches no file, and it will happily exit zero on Volume 11, which exists.** Run `python3 tools/measure.py selftest` first if you are unsure.

**Volume 11's and Volume 08's figures are not interchangeable and this is worth saying before you measure anything.** Volume 11 is 95,348 words over fifty chapters, 1,907 a chapter, on `python3 tools/measure.py words --volume 11`. Volume 08 is **63,145 words over fifty chapters, 1,263 a chapter**, on `python3 tools/measure.py words --volume 08`. Volume 01 is 202,117 words and 4,042 a chapter. Volume 08 has the lowest per-chapter mean of any volume in this manuscript except Volume 07, and it is where the collapse is worst.

## The finding

Chapter length fell monotonically across twelve volumes, from about 4,000 words a chapter in Volume 01 to about 1,050 in Volume 12, and the demonstrative-anaphora construction — *that tin, those flags, that lane* — rose with it. The volume outlines describe complete scenes. The delivered pages are compressed summaries of those scenes. `AGENTS.md` asks for physical space, action, sensory detail, dialogue, subtext, character thought and emotional consequence, and that is not reachable in thirteen hundred words. **The manuscript is structurally complete and canonically sound and it is not publishable as it stands, and this is the only open item in the repository that a writing phase can pay.**

**Volume 08's defect is length and not the construction, and this is the single most important difference between this range and the twelve that came before it.** On this range the closed list of ten named forms runs at **2.13 per 1,000**, against 4.88 on 0501 to 0510 before its repair, 5.38 on 0521 to 0530, 6.54 on 0511 to 0520 and 11.18 on 0601 to 0609. **A phase that opens these ten chapters expecting the Volume 11 concentration will measure the wrong thing, cut the wrong sentences and lengthen the wrong lines.** What Volume 08 needs is length and variation and it needs them badly; the construction is a secondary matter here and the count is already low.

**The remaining scope, said plainly. After this phase, one hundred and twenty-eight chapters of six hundred and twenty are repaired and four hundred and ninety-two are unrepaired — seventy-eight per cent. Volumes 08, 09 and 10 would then hold a hundred and forty unrepaired chapters between them, which is twenty-eight per cent of what is left and is still the largest single block in the repository. Ten chapters is a tenth of one volume against a defect that spans six volumes, this repair at this rate is forty-nine phases across the manuscript and fourteen across the three untouched ones, and that is a scope decision belonging to a person and not to a phase.** Say so in your own record rather than implying the job is nearly done.

## The task

**Open `chapter-0351.md` through `chapter-0360.md` for edit and repair the prose. Write no new chapter and plan no volume.**

**These ten are the first ten of Volume 08 and the work is length and variation, not plot. For each chapter:**

- **Keep every scene beat in the order it is already in.** Nothing is added to the plot, removed from it, reordered, or contradicted.
- **Give the scene its body back.** The physical arrangement of the room, where objects sit and what they are made of, what a body is doing while its owner is not speaking, the light and the hour and the weather.
- **Vary the sentence rhythm.** The delivered prose runs at one length and one cadence. The repaired chapters should not.
- **Set the rooms down from what is already on the page.** Grep the whole of `chapters/` before you add any detail. That is not a reason to invent, it is the finding.
- **Never append to an original line and never place an added paragraph inside an original paragraph.** Both happened on earlier ranges and both were removed. At the line level the diff must report **zero `replace` opcodes**, which is a stronger statement than a word-level diff and is the shape this repair should be in.
- **Check the material of every object you name, and check the floor.** Two defects in one recent range were floor materials.
- **Give the added prose to a reader who has the classes of defect to look for and no list of things to write, and act on what comes back.** It found fifteen defects on one range, thirty-nine on another, and it is the cheapest instrument in this repository for what the instruments cannot see and it takes one call.

## Before anything else, check whether this range is already repaired

**A repair phase was dispatched twice on one range and the second dispatch had no way to know from the repository that the work was done. A range was dispatched twice again and found eight defects in a completed repair. A range was committed and wrote no record at all. Measure first, every time.**

**Record your own baseline as a hash before you edit anything, and compare against that hash for the rest of the phase.**

```
BASE=$(git rev-parse HEAD); echo "$BASE"

for n in $(seq 351 360); do f=chapters/volume-08/chapter-0$n.md
  echo "$n $(python3 -c "print(sum(len(l.rstrip().split()) for l in open('$f')))")"; done
```

**Compare that against the recorded pre-repair figures for this range, which are 1,528 1,630 1,406 1,674 1,642 1,678 1,413 1,336 1,556 1,643, a total of 15,506 words at 2.13 closed-list hits per 1,000 and 33 hits — the table printed below, measured with the printed instrument against `ec83e35`.** If the ten files are at those figures the range is unrepaired and this phase should repair it. If they are not, then either the range is already repaired — in which case check `state/batch-summary.md` for a record of it, and this phase owes a re-audit and a record and not a second rewrite — or somebody else has edited it, in which case `git log --oneline -- chapters/volume-08/chapter-03[56][0-9].md` says who and from what, and read their record before you write into the range. At the time this prompt was written that log returned only batch commits and no prose repair. **Do not compare the working tree against `git show HEAD:$f`. At the start of a phase those two are the same tree by construction, so that comparison is a tautology and it will always report that the range is untouched.**

## The concentration on this range, measured before you open it, because the leaders have changed on twelve ranges running

**This is the one instruction phases have got wrong in opposite directions. The leaders have changed on every range for twelve ranges running, and a phase that inherits the previous prompt's table is handling the wrong noun.** On the instruments printed whole in the section headed *THE PROSE REPAIR OF CHAPTERS 0541 TO 0549* in `state/batch-summary.md`, **`chapter-0351.md` to `chapter-0360.md` stands at `ec83e35` at:**

- **15,506 words, 33 hits of the closed list of ten named forms, 2.13 per 1,000** — against 4.88 on 0501 to 0510 before its repair and 5.49 on 0511 to 0520 after its audit, 5.38 on 0521 to 0530, 4.96 on 0541 to 0549, 6.41 on 0551 to 0560, 7.77 on 0561 to 0570, 8.43 on 0571 to 0580, 10.68 on 0581 to 0590, 8.78 on 0591 to 0600 and 11.18 on 0601 to 0609. **This is by a wide margin the lowest pre-repair rate any range in this repair has measured, and the low rate is not good news: it says this range's chapters are short without being repetitive, and the work here is to add scene and not to cut sentences.**
- **Per chapter, words: 1,528 1,630 1,406 1,674 1,642 1,678 1,413 1,336 1,556 1,643. Per chapter, closed-list hits: 2 2 1 2 1 4 4 9 2 6.** The concentration is not even across the ten and it is not two chapters: **`chapter-0358.md` at nine and `chapter-0360.md` at six carry fifteen of the thirty-three**, and `chapter-0353.md` and `chapter-0355.md` carry one each.
- **Per form, closed list of ten: `that room` 19, `that lane` 5, `that door` 3, `that stair` 3, `that passage` 2, `that table` 1, and `those boards`, `that floor`, `that tin` and `that sheet` all at zero.** **Three of the ten are at zero where the last range had two, and the leader `that room` at nineteen is a closed-list form that led the last range at twenty-seven.**
- The two widened lists are also measured on this tree: **the twenty-three stands at 46 = 2.97 per 1,000 and the twenty-five at 51 = 3.29**, and per chapter the twenty-three reads **2 4 2 3 1 13 4 9 2 6** and the twenty-five **2 4 2 3 3 13 4 10 2 8**, summing to 46 and 51. **`that sill` and `that board` are not leaders here as they were on the last range; the two forms that are on the twenty-three and large on this range are `that bay` and `that counter`.**
- The wider sweep of **every** demonstrative-plus-noun bigram in those ten files, with a function-word tail excluded because `that is` and `that has` are subordinators, returns **178 hits in 15,506 words, 11.48 per 1,000, across 89 distinct forms**. Its leaders are **`that room` 19, `that counter` 12, `that out` 8, `that bay` 8, `that shelf` 6, `that lane` 5, `that window` 4, `that either` 4, `that building` 4, `those stairs` 3, `that stair` 3, `that since` 3.** **`that room`, the leader, is a physical fixture. `that counter` at twelve is second and is on neither the closed list nor the twenty-five, and `that out`, `that either` and `that since` are the discourse tail and are counted, excused in a finding, and not to be written.**
- **`that building` is a form to watch here and it is a different building from any of the last range's.** Read which noun belongs to which room before you name a floor or a room at all.
- **Paste the method whole from the section named below and do not rebuild it: the exclusion set of record does not contain `too`, `for` or `have`, and a copy that grew by those three words under-reports this sweep by three hits and three forms, and a figure that reproduces under no method is how this repository got a set of numbers that reproduced under none.** **And fix the one thing in it that is wrong before you paste it, and this is the eighth range on which it has to be said: the body helper as printed strips any line beginning `It is `, which deletes prose. Use `m.prose_lines`, which is this module's own selector and which its docstring says selects date lines "and not by a `startswith("It is ")`" — or strip on the full formula — and say in your record which of the two you used. Print both figures, and on Volume 08 there is a third reason, which is the next section.**

**If you widen the list, print the old and the new rate side by side and say plainly which forms you added, because a figure with an undisclosed method behind it is how this repository got a set of numbers that reproduced under none.** And say plainly that **a closed list of named forms measures the concentration this repair works on and not the whole of item 170.**

## The date-line check on this volume is different from every other range in this repair, and it will pass on all ten files while checking nothing

**This is the first thing to get right and it is new.** **Volume 08's chapters do not all open their date line with `It is the`. Twenty-two of its fifty files open it with `This is the`, and all ten of this range's files do:**

```
grep -c "^This is the " chapters/volume-08/chapter-035[1-9].md chapters/volume-08/chapter-0360.md
```

**`tools/measure.py`'s own `DATE_LINE` requires `It is the`, so it matches none of them. `python3 tools/measure.py calendar --volume 08` reports *no date line* for `chapter-0351.md` through `chapter-0360.md` and for twenty-eight of the volume's fifty files in all, and the whole-formula locator printed in every prompt in this repair —**

```
grep -n "^It is the .* day of the .* week of the .* month of the year after" chapters/volume-08/chapter-0$n.md
```

**— returns zero lines in all ten. It will print nothing, exit zero, and every check built on it will report clean.** That is the seventh time this repository has walked into a check that fails silently and the first one where the whole-formula locator itself returns nothing, and it is worth knowing that `sed -n '5p' | md5sum` reports SAME whether or not the date moved.

**The locator for this range is the formula with either opener:**

```
grep -nE "^(This|It) is the .* day of the .* week of the .* month of the year after" chapters/volume-08/chapter-0$n.md
```

**and it must return exactly one line in each of the ten. Record the line number it returns and check the date line is on the same line number as at `$BASE`, by `md5sum`, in all ten — and run the line-5 check as well, and say in your record which files line 5 is a date line in.** On this range the date lines stand at **9, 9, 7, 7, 9, 7, 7, 9, 7, 7**, so the line-5 check tests a date line in no file at all and line 7 and line 9 are where the work is. **And never let an added paragraph land above a date line.** A range before last landed three above theirs and `sed -n '5p'` reported SAME on all three; the range before that landed one above its own and the line-number check was the only thing that saw it.

**Do not edit `tools/measure.py`. It is a controller-adjacent measuring instrument and it is not wrong: its `DATE_LINE` says what it matches, and a volume that opens half its date lines differently is a fact about the volume, not a defect in the module. Record the discrepancy in your own state record and move on.**

## Read before writing

`state/current.md` in full, **items 173O, 173P, 173Q, 173R and 173S**, and items 173, 173A, 173B, 173C, 173D, 173E, 173F, 173G, 173H, 173I, 173J, 173K, 173L, 173M and 173N of `state/open-threads.md`. Then the section of `state/batch-summary.md` headed *THE PROSE REPAIR OF CHAPTERS 0501 TO 0510* — **whose section One is thirty-nine defects an independent read found in that pass's own added prose, the largest set any single read in this repair has produced, three quarters of them restatements of the chapter's own preamble** — *THE PROSE REPAIR OF CHAPTERS 0511 TO 0520* — **whose section One is fifteen defects no instrument could see** — *THE PROSE REPAIR OF CHAPTERS 0521 TO 0530*, *THE PROSE REPAIR OF CHAPTERS 0531 TO 0540*, *THE PROSE REPAIR OF CHAPTERS 0541 TO 0549* — **including its section Four, six regressions that pass introduced and fixed** — *THE PROSE REPAIR OF CHAPTERS 0551 TO 0560* — **whose section One holds the method printed whole for every figure** — *THE PROSE REPAIR OF CHAPTERS 0571 TO 0580* and its **section NINE**, and *THE PROSE REPAIR OF CHAPTERS 0601 TO 0609*, **which is where the closing-person scan is printed, and where it is printed with a plant that does not behave**. Then `outline/volume-08.md`, and read `chapter-0351.md` to `chapter-0360.md` as prose.

## The standing facts about Volume 08 that a repair of this range has to know

- **Read `outline/volume-08.md` before you write and do not edit a line of it.** It is a closed plan of record.
- **Volume 08 is not Volume 11 and its fixtures are its own.** Every figure, object, duration, distance, age and named absence in the ten files is canon and every one stays. An age is the easiest thing on that list to invent by accident and so is a room's furniture and so is a floor. **Grep all of `chapters/` for any detail before you add it, and if the only hits are other rooms or other and unrelated people, it is a new fact and it does not go in.** The range before last wrote and removed, in one phase and without an instrument noticing, a woman who had not left a room she is five chapters of leaving, a man in a coat a month before the volume's first time of it, four hundred feet beside four hundred yards, and a worn place in wood no chapter records — that is the ordinary rate of invention to expect from yourself and the reason every one of them was written against a grep and caught by a reader.
- **The demonstrative construction is at 2.13 per 1,000 on this range and that is low.** Do not cut sentences to chase a number that is already the lowest in the repair. **Write no figure beginning "about four hundred" anywhere and grep the number before you write any figure near it**: about four hundred blanks *a year* out of a case, about four hundred blanks *in total* in the box that is not the case, about four hundred sheets a year with a line cut in the strip, and about four hundred and thirty miles of river are four distinct types and this manuscript has confused them before.
- **`iron`, `steel` and `brass` return zero hits in all fifty files of Volume 11. Check the same three in Volume 08 before you write any of them, and if the volume has no word for the material of a thing then the material of that thing does not go in your prose either.**
- **Check the floor of every room you set down.** Two defects in one recent range were floor materials, one of them a room whose own prose forbids describing its contents twice. **If you cannot grep the fact out of the volume, do not name it.**

## The traps in this range, and the traps are new because the leader is new

**Read this list as the classes to look for and not as a list of things to write.** Every one of them is a fixture canon already settles somewhere in this manuscript, and a paragraph that re-narrates one of them in the words of the chapter that settled it is the defect this repair exists to remove — **not** the existence of the fixture.

- **The leader changed for the fifth time in six ranges, and the volume changed with it.** **`that room` is nineteen and leads this range and `that counter` is twelve and is second**, where on the range just repaired `that room` was twenty-seven and `that floor` twenty-two and `that counter` was not mentioned at all. **That is the standing this prompt exists to enforce: the leaders have changed on every range for twelve ranges running, and this range is the first in a different volume.** Read which noun belongs to which room before you name a floor or a room at all.
- **`that out`, `that either` and `that since` are the discourse tail.** They are counted in the sweep, excused in a finding, and not to be written. `that morning`, `that makes`, `that used` and the rest of the tail are the same.
- **The standing furniture traps that recur across every range and are new here only because the range is new:** the four feet of bare wall and the one nail nothing has ever hung on, which `chapter-0351.md`'s own title names and which five chapters of this volume repeat; a sheet on a table from the second hour; four steps and a landing; the lamp in that room not lit and not going to be; the chandler's shop below with its tar and rope and lamp oil; a column that will not agree with itself, which is `chapter-0351.md`'s own title and which this range's plot turns on. **Grep every one of them across `chapters/` before you name it in new prose, and if the only hits are this manuscript's other and unrelated people or other rooms, it is a new fact and it does not go in.**
- **The range before this one had two findings worth carrying forward whole, and both cost more than any instrument caught.**
  - **The same sentence written twice inside one pass's own ten chapters, and neither index in this repository can see it, because `lifts` excludes the range under repair from its own index — selftest plant 11 is that exclusion.** Run the added-line index beside it:

    ```
    python3 - <<'PY'
    import importlib.util, difflib, subprocess
    spec=importlib.util.spec_from_file_location("m","tools/measure.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    BASE="ec83e35"   # your own hash
    added={}
    for n in range(351, 361):
        f=f'chapters/volume-08/chapter-{n:04d}.md'
        o=subprocess.run(['git','show',f'{BASE}:{f}'],capture_output=True,text=True).stdout.split('\n')
        w=open(f,encoding='utf-8').read().split('\n')
        added[n]="\n".join(w[j] for t,i1,i2,j1,j2 in difflib.SequenceMatcher(None,o,w,autojunk=False).get_opcodes() if t=='insert' for j in range(j1,j2))
    toks={n:m.TOKEN.findall(added[n].lower()) for n in added}
    def longest(a,b):
        A,B=toks[a],toks[b]; best=(0,'')
        for i in range(len(A)):
            for j in range(len(B)):
                k=0
                while i+k<len(A) and j+k<len(B) and A[i+k]==B[j+k]: k+=1
                if k>best[0]: best=(k,' '.join(A[i:i+k]))
        return best
    for a in added:
        for b in added:
            if a<b:
                k,seg=longest(a,b)
                if k>=7: print(k,'words',f'{a} <-> {b}:',seg[:110])
    print('no in-range run at 7+ if nothing above printed')
    PY
    ```

  - **Neither of those two indices can see a sentence you wrote that lifts an ORIGINAL line out of a chapter of your own range, which is the commonest import of all, because the room you are revoicing is the room the neighbouring chapters are already describing.** On the range before this one the review found sixteen words of added prose in one chapter that were a neighbouring chapter's own original line, word for word, and `lifts` returned nothing and the added-line index returned nothing. Run the third index as well, and **count the holders before you act on anything it returns** — on that range it returned one run of eight words which turned out to be the volume's stock connective, held by eighty-eight chapters across twelve volumes:

    ```
    python3 - <<'PY'
    import importlib.util, difflib, subprocess
    spec=importlib.util.spec_from_file_location("m","tools/measure.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    BASE="ec83e35"   # your own hash
    added={}; orig={}
    for n in range(351, 361):
        f=f'chapters/volume-08/chapter-{n:04d}.md'
        o=subprocess.run(['git','show',f'{BASE}:{f}'],capture_output=True,text=True).stdout.split('\n')
        w=open(f,encoding='utf-8').read().split('\n')
        added[n]="\n".join(w[j] for t,i1,i2,j1,j2 in difflib.SequenceMatcher(None,o,w,autojunk=False).get_opcodes() if t=='insert' for j in range(j1,j2))
        orig[n]=" ".join(o)
    def longest(a,b):
        A,B=m.TOKEN.findall(a.lower()),m.TOKEN.findall(b.lower()); best=(0,'')
        for a1,b1,L in difflib.SequenceMatcher(None,A,B,autojunk=False).get_matching_blocks():
            if L>best[0]: best=(L," ".join(A[a1:a1+L]))
        return best
    for a in added:
        for b in orig:
            if a==b: continue
            k,seg=longest(added[a],orig[b])
            if k>=8: print(k,'words ADDED',a,'<- ORIGINAL',b,':',seg[:110])
    PY
    ```

    Eight words is the threshold and not seven, because a shared frame like `at the far end of the` is this book's own connective and chasing it edits the voice out of the book. Report what stands and say why it stands: **a run held by four or more chapters across four or more volumes is the register's stock formula and is not yours to remove; a run held by one or two chapters is that chapter's clause and is yours; and a run held by a chapter LATER in the volume than yours is canon echoing you and not you lifting canon.** Check the month on each holder's date line before you call a run a lift — and on Volume 08 read the month off a line that opens `This is the`, not `It is the`.

- **And the finding underneath both of those: a holder is not canon because it is on the page.** On the range before this one the added prose in one chapter was a twenty-four-word transcription of a sentence in a chapter of Volume 12 — **and that sentence was itself added prose written by an earlier repair, not canon.** `lifts` returned the run and would not have told you which direction it ran. **Ask whether a holder is ORIGINAL before you ask which month it is: a date line decides between two originals, or between an original and a repair's own earlier telling. It cannot decide between canon and prose a repair wrote after reading canon.**

## What must not change

These are hard. Check each one before the phase ends.

- **The date line of every chapter, byte for byte, and on the line number it held.** The check is `md5sum` of the line the **either-opener formula** finds, which returns exactly one line in all ten on this volume. See the section above for why the prompt's own printed locator returns nothing here. Both it and the line-5 check must be identical to `$BASE`, and the line number must be the line number. **This is the single most important check in the phase, and on this volume it is the one check that has to be built differently from every prompt before it.**
- **The title line too, byte for byte.** `sed -n '1p' | md5sum` on both sides. **A title in this volume can name a fixture the body contradicts, and this range's own titles do — `chapter-0351.md`'s is four steps, a landing, a sheet from the second hour, four feet of wall and a column, and its body is about a man whose fair hand copies out other men's figures. If you find a figure in a title that the body contradicts, leave it, record the tension, and do not settle it.**
- **Zero question marks.** The count of things asked out loud in this matter has not moved in this repair and is printed in no chapter. Do not add a question — and note that a pass had to change a drafted counterfactual of the form *"if he had heard it he would have come the last nine foot and put one question to her"* into *"and said one word to her"*, because a question-shaped object in a counterfactual reads as an asking that has not been counted.
- **The person each chapter closes in.** This volume's framing is third person and its interiority is first person, opened by a bold line, **and that is a strong default and not a rule**. **The test that holds is narrow and checkable: keep each chapter's closing section in the person its original closed in.** A first-person line inside a run of dialogue is the speaker's and is left alone. **The working scan is printed in the section headed *THE PROSE REPAIR OF CHAPTERS 0601 TO 0609* in `state/batch-summary.md`, with its plants. Use it as printed and do not rebuild it in `/tmp`, and give it this range's file list.** **Its dialogue filter strips a line that starts or ends with a quotation mark, so a line with the speech set into a sentence is counted as narration and returns FIRST; that plant does not behave and the last four passes reported it rather than tidying it, and you should do the same.** When you scan, subtract the bold interiority and the dialogue lines first, and **remember that it is the person of the closing section and not of any section: a closing section is the last one, and a first-person section followed by a third-person one is a third-person chapter.** Plant it before you believe it. **These ten chapters carry raw `**` counts of 8 10 14 10 16 12 16 14 12 14, which is more interiority in the middle of the range than any Volume 11 range has, and a phase that adds interiority here has to earn it.**
- **The section breaks.** A `---` line is architecture, not punctuation. **Each of the ten files must end the phase with the same number of `---` lines its original had.** For this range the originals are **6 6 5 6 5 6 6 4 6 5** — **measure them, do not take this line's word for it if the two disagree, and if they disagree, say so and use the file.** The command is `for n in $(seq 351 360); do f=chapters/volume-08/chapter-0$n.md; echo "$n $(grep -c '^---$' $f) $(git show $BASE:$f | grep -c '^---$' $f)"; done` and the two numbers on each line must match, **where `$BASE` is the commit hash you recorded at the start of the phase and not an offset.**
- **Canon.** Every figure, object, duration, distance, age and named absence stays. **Never change a canon figure to make a sentence read better, however good the reason, and never change a canon noun for rhythm.** One repair rewrote one word in one chapter, from eleven *weeks* to eleven *years*, and it was very probably a correction, and it was still put back. The pass before that changed one original noun, from *stone* to *sill*. Do not settle such a thing. If you find one, put the original word back and record the tension.
- **Never lift a sentence out of another chapter, in either direction, and the instrument that polices it is a command.**

  ```
  python3 tools/measure.py lifts --volume 08 --first 351 --last 360 --base $BASE --min 6 --show 20
  ```

  It returns, for each prose line you added and for each prose line the base commit held, **the longest run of words that stands contiguously, in that order, in one single other chapter of the manuscript**, indexed over the six hundred and ten chapters outside your range so a run has to leave it to count, with the date line and the `---` rules out of the token stream on both sides. It has two plants in `selftest`, so run `selftest` before you trust it. **And read the BASELINE line it prints, because the added figure on its own means nothing in this manuscript.** On this range the baseline is **307 prose lines, 275 over six words, 175 over nine, mean 11.64**, which is the highest of any range this repair has measured. **A repair that chases every run the added figure returns will edit this book's voice out of it. Do not revoice on the added figure alone.**
  - **When you report an instance out, check first that the instance is one you wrote.** A previous record reported removing an instance that was **original**, still at its base commit, and still on the page. No count was ever wrong because of it, and the record was, which is worse.
  - **Your own prose is in scope, and a run the volume already had is not yours to remove.** The last range left five nine-word runs standing, all of them the register's stock connectives, and reported them rather than removing them. **Expect to find runs and expect to leave some of them.**
  - **What is real, and what reading finds, is re-narration of a fixture the chapter's own room has already settled.** The largest lifts on the last three ranges were all of that kind: four flights of stone with a rail on the open side, a halfway window at the height of a man's chest, and a fourth-hour light down at a slant. **Take the volume's own facts and write them out in fresh words, and when you revoice a lift, keep the fact and change the sentence.** **And measure a correction against canon and not only against the range, because a correction that restores canon has the strongest pull in this repository toward canon's own phrasing — the facts are the same facts in the same order and the sentence wants to end where canon's ends. Three drafts of one such fix came in at eighteen, nine and eight words out of canon, and reading caught none of them.**
- **A line number in a record is a citation of an original line in a file this repair did not touch, and of nothing else.** Four canon citations in one record were pre-repair numbers presented as current ones, **all four on files that pass had opened.** **In a file you have edited, cite the quoted text and the chapter**; the number is a convenience that goes stale the moment an insertion lands above it.
- **An added paragraph must not perform the act the paragraph above it does, and this is the commonest defect in this repair.** A read of all ten chapters in one range found and fixed forty-four items; the range before that fifty-three; another found fifteen; the range before this one found thirty-nine in added prose that no instrument could see, **and three quarters of those were an added paragraph opening by restating what the chapter's own preamble already carried.** **The classes it finds are: an added sentence restating a figure the chapter already carried; an added paragraph performing an act the paragraph above it already performs; a whole added paragraph that was three restatements wearing a coat; a word used three times in six lines until it read as a muddle; a word given a verb to one subject that the page has given the same verb to another; and an added paragraph saying a thing the chapter's own page contradicts.** Read every paragraph you add against the paragraph above it and the paragraph below it, and read added paragraphs against added paragraphs. **Where an added paragraph sets up an act, it belongs *above* the original line that performs the act and not below it, because the order of the beats is the order the original had — and one range had six paragraphs that did the reverse.**
- **Do not alter a character's speech, and if you do, do not then certify in your record that you did not.** A delivered record claimed *"every line between quotation marks is the original's"* and the check returned nine IDENTICAL and one CHANGED. **Run that grep before you make the claim, and do not print a claim you have not run a command for.** Compare against the commit hash you recorded at the start of the phase.
- **Check that not one word of the original was removed, and run that diff after every editing pass and not once at the end.** A word-level diff of each file against `$BASE` must report zero deleted runs and zero substitutions. At the line level the same diff must report **zero `replace` opcodes**, and that is the stronger statement: not one original line re-voiced, extended or split.
- **A chapter can disagree with itself without any sentence being wrong on its own terms, and reading is the only way that is found.** Ten conflicts are carried unsettled and none is settled by a repair. **Take the canon fact from the commit and read the two lines either side of it before you write, and if you cannot settle a conflict, do not add to its count either — draft the sentence, see the page contradict it, and take the sentence out rather than let a third measurement stand beside two that disagree.**
- **Name the commits beside your figures and never write an offset on its own.** Three records in this repair have labelled a baseline one commit out, because a build commit that touches no chapter sits between the repair and the record. **Also check that a column of per-chapter figures sums to the total printed beside it.**
- **The chapter must agree with itself, and it must agree with the chapters that own the events near it. Read the chapters that own the events your chapter is near, and they are not the chapters either side of it.** Read `chapter-0351.md`, `chapter-0354.md`, `chapter-0356.md`, `chapter-0358.md` and `chapter-0360.md` before you repair any of them, because the four steps and the landing and the sheet from the second hour and the four feet of wall and the column that will not agree with itself, the stair and the counter and the gate at the bottom of the lane, the counter and the bay and the rack that goes down all day, and the two chapters carrying nine and six of the range's thirty-three instances are all settled there. Read `chapter-0361.md` to `chapter-0370.md` beside them, and read `chapter-0371.md` to `chapter-0380.md` if your chapter's events reach into them.
- **Nothing resolved, nobody thanked, nobody forgiven, nobody sent for.**
- **The unmade decision** about whether the woman of twenty-four takes a colleague's judgment is a decision of Volume 11 and is unmade there in both directions. **Do not settle it here and do not carry it into Volume 08.**
- **`chapter-0620.md` and the last chapter of Volume 08 are not opened by this phase beyond being read.** Volume 08 runs 0351 to 0400 and its last line is in `chapter-0400.md`; Volume 12's is in `chapter-0620.md` and carries the last line of the series. **Read `chapter-0400.md`. Open neither.**
- **Write a record.** A repair with no record is not a repair; it is a diff. Four phases in this repair have committed chapters and written no record, and the fourth time is the reason this bullet is not last in the list. Report any regression this phase introduced and then fixed — **a repair that reports only its successes has not been measured.** **And print the number of words your first draft contained and the number your landed pass contains, because a pass drafts more than it keeps and the reader of its own draft is the cheapest instrument in this repository: one range drafted 4,732 words and kept 3,558, and printed both.**

## Verify before finishing

Run these and put the results in the state record with the command beside each figure. **`--volume 08` on every one of them.**

```
python3 tools/measure.py selftest
python3 tools/measure.py calendar --volume 08
python3 tools/measure.py reprints --window 20 --volume 08
python3 tools/measure.py reprints --window 12 --volume 08
python3 tools/measure.py reprints --window 8  --volume 08
python3 tools/measure.py reprints --window 5  --volume 08
python3 tools/measure.py lifts --volume 08 --first 351 --last 360 --base $BASE --min 6 --show 20
```

**`selftest` is eleven plants, two of which are the `lifts` command. If you add to it, plant it.**

- **Re-prints: print the window beside the figure, and print all three classifiers, because the figure is a fact about the window and not about the volume.** Over Volume 08 on the working tree at `ec83e35`, the `either` figures are **47 / 155 / 787 / 2,934** at the twenty-, twelve-, eight- and five-word windows, with the longest runs **56 in `chapter-0389.md`, and 61 in `chapter-0380.md` at both the twelve- and eight-word windows, and 80 in `chapter-0376.md` at five.** **Volume 08's twenty-word re-print count is 47 where Volume 11's is 4, and that difference is a property of the volume and not of your work: measure your own baseline and print the tool beside it, and do not carry Volume 11's figure forward.** **The runs by which `terms` exceeds `either` are date lines, and this is not a defect in either classifier:** `terms` calls a run prose when fewer than half its tokens sit inside a formula *term*, a date line is mostly prepositions, ordinals and the word *year*, and `date` catches all of the lines its own selector matches — **which on this volume is twenty-six of fifty files and not all fifty, for the reason set out above.** Print all three buckets and read the runs before you report any of them as prose duplication.
- Section-break count per file must equal the original's, and the command for it is printed in the list above.
- **Trailing newline: every file must end in one.** `for n in $(seq 351 360); do f=chapters/volume-08/chapter-0$n.md; [ -n "$(tail -c 1 $f)" ] && echo "$n NO-NEWLINE"; done` must print nothing. **It is worth running `od -c` on the last three lines of one file, because `sed -n '5p'` and `git diff --stat` cannot see what is at the end of a file and one pass in this repair changed a file's shape by a single trailing newline without any other instrument noticing.**
- **Read your own added sentences for verbatim runs against every chapter of the volume, including chapters you are not opening, with the `lifts` command above and not with `reprints --window 20`, and read the added figure against the baseline it prints beside it. Run all three indices printed in the traps list and not one.**
- **Person of the final section must equal the original's, on the scan printed above, with the bold interiority and the dialogue subtracted first. Plant it before you believe it.**
- Question-mark count across the ten files: zero.
- **All ten date lines byte-identical to `$BASE` and on the line number they held, located by the either-opener formula, and all ten title lines likewise.**
- Month and weekday names: **the only permitted hit is the modal verb *may*.** On Volume 11 a pass wrote *Monday* into an added paragraph about the two ends of a week and had to take it out; **a chapter's prose about a week must not name a day of it.**
- `this year`, `this volume`, `this novel`: zero.
- **Bold markers even in every file. Measure them rather than take a prompt's word for it** — `python3 tools/measure.py markers --volume 08` if it will take the flag, and the raw `grep -o '\*\*' | wc -l` per file if it will not.
- **Report the named-form rate before and after with the method printed whole, not described.** Use `m.words_in_file` for every word figure — **and note that it takes a path, so reading the working tree while claiming to read a commit is how a record printed one figure three times; for a committed blob apply the same definition, `sum(len(line.rstrip().split()) for line in handle)`, to the text `git show` returns.** And check that the per-chapter columns sum to the totals printed beside them.
- **Print the count as well as the rate, and judge the range on the count.** A repair that lengthens prose without cutting the construction lowers the rate and raises the count at the same time.

## Three instrument findings this prompt inherits, and the first two have changed an outcome on the range before this one

**These are the second half of the `body()` finding in the section above, and both of them are about a certificate rather than a sentence, which is the class of defect no command in this repository can currently see.**

- **Count a run's holders on the exact string you are about to print beside it, and take both from the same measurement.** A record on the range before this one justified leaving five nine-word runs standing by counting their holders, **and three of the five counts were measured on a shorter string than the run they were printed beside — in every case a string with the larger count, which is what makes the conclusion look safe.** *for about as long as it takes to square a sheet* is held by 10 chapters across 3 volumes and was certified at 21/4, which is the count of *as long as it takes to square*; *be able to do one single thing with it* is 3 across 3 and was certified at 45/8, which is the count of *one single thing*; *and that is the whole of the protection a* is 4 across 4 and was certified at 16/8, which is the count of *whole of the protection*. **On the corrected counts two of the four are held by two or three chapters, are not the register's stock connective, and had to be revoiced.** A holder count of ninety-nine against a two-word tail is not a holder count of the thing you are reporting about.

- **Run the added-against-added index at six words as well as seven on a range where one object appears in more than one chapter.** **The same sentence appeared word for word in `chapter-0508.md` and `chapter-0509.md` about the same book in the same building, six words verbatim, and the seven-word index did not return it** because the two sentences diverge before and after those six words. The threshold is a floor and a six-word duplication of a whole clause sits under it.

- **Print both body figures whenever a chapter heading can carry a demonstrative-plus-noun, and on Volume 08 it can on all ten files**, which is the second half of the item 173Q finding and it is stated above. **On the range before this one the two methods agreed on all three named lists and disagreed on the sweep by four, 298 on the page and 302 through the strip, and the four were chapter headings.**

## State and the next phase

Append one section to `state/batch-summary.md` with the measured record, the method beside every figure, **and any regression this phase introduced and fixed**. Add an item in `state/open-threads.md` for what remains, and keep `state/current.md` short; it has been trimmed once already for bloat and its own complaint is at its head. **Update the Volume 08 row and the manuscript total in the table at the head of `state/current.md`, and print the command in the row.** The repaired-range means list in that file gains its thirteenth entry, and it gains it honestly: **the ranges do not agree with one another and the gap between the shortest and the longest is the size of what is still owed.**

**Then create exactly one next phase prompt** and no more, at `workspace/prose-repair-0014/`, for the same work on the next ten chapters of Volume 08, `chapter-0361.md` to `chapter-0370.md`, **still `--volume 08`**. **Measure that range's concentration before you name it, because the leaders have changed on twelve ranges running and `that room` at nineteen leading with `that counter` at twelve second is a first reading of Volume 08 and the next range will not repeat it.**

**And say in that prompt's own words that Volume 11 is repaired in full and Volumes 08, 09 and 10 are the only untouched chapters left in the manuscript, that a hundred and forty chapters is twenty-eight per cent of what is left, and that the remaining scope is still most of it.**
