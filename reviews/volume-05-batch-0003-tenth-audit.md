# TENTH AUDIT OF THE PAID SECOND READING OF VOLUME 05'S BATCH 0003, `chapter-0221.md` TO `chapter-0230.md`, AND A FAULT IN `tools/measure.py` THAT NO PASS ON THIS RANGE HAS FOUND

**Who wrote this, and what it is not.** This is an audit of a paid review, written by the same agent that wrote the state sections this run, and **nothing in this repository's review gate is independent** — the gate has fallen back to the writing agent every time it has been asked, `NOVEL_SPEC.md` and `state/open-threads.md` item 171 both say so in terms, and **no sentence in this file, and no sentence in any of the eleven files it audits, may be cited as an independent finding.** What it has that a re-run of the paid review's own scripts does not have is that all ten chapters were read end to end, a twelfth pass over the page, and that every figure below was re-derived on this tree with the command printed beside it rather than carried from any of the eleven earlier passes.

**Why this file exists instead of a review, and why it is not `volume-05-batch-0003.md`.** This run was handed `workspace/review-debt-0001/PROMPT.md` verbatim and found its work paid ten times over: `reviews/volume-05-batch-0003.md` on disk at **`2359f84`** (item 268), **never modified since** — `git log --oneline -- reviews/volume-05-batch-0003.md` returns that one commit and no other — with siblings at items 275, 279 (`-verification`), 283 (`-third-audit`), 290 (`-fourth-audit`), 291 (`-fifth-audit`), 294 (`-sixth-audit`), 295 (`-seventh-audit`), 302 (`-eighth-audit`) and 303 (`-ninth-audit`). **The prompt's two destructive instructions were not carried out.** It directed this run to write `reviews/volume-05-batch-0003.md`, which would have destroyed the second of the four owed reviews and the file that nine audits cite by name; and it directed this run to create `workspace/review-debt-0002/PROMPT.md`, which **already exists** (9,722 bytes, written at `df6a8e0`, for Volume 05's Batch 0004 at base `65abf1d`) and whose review is **paid** at `5316a4f` (item 270A) and audited four times. Neither was done, per items 275A, 283F, 290H, 294H, 299A and 302F. **It wrote no marker in its own directory** — `PHASE_SYSTEM.md` line 216 bars a writing phase from phase selection, and a phase that marks its own directory has certified itself. **It opened no chapter for edit, amended no paid file, planned no volume, wrote no `state/complete.md`, and created no prompt.**

**Base, asserted before any figure was taken from it.** `git log --oneline -- chapters/volume-05/chapter-022[1-9].md chapters/volume-05/chapter-0230.md` returns `18e57c8` (*save review fixes batch-0003*) and `7a54b16` (*save writer work batch-0003*) and nothing else. `git show 18e57c8:chapters/volume-05/chapter-<each of the ten> | wc -c` returns **14465, 13200, 12889, 14056, 14323, 14960, 13221, 13046, 13878, 14020** — ten of ten non-empty, which is item 265E's check. `git diff --numstat 18e57c8 --` over the ten returns empty, so none of these ten has moved by a line and **every line number below is a citation of a text and not of a position.** `git log --oneline --grep="prose-repair" -- chapters/volume-05/` returns nothing: **Volume 05 has never been through the prose repair.** `python3 tools/measure.py selftest` returns **PASS**.

**And the prompt's own counter-example does not reproduce, which is the first finding and the cheapest one to check.** The prompt states that `git show 9ae089f:chapters/volume-05/chapter-0221.md` *will exit 128 and every structural counter piped from it will come back exactly zero*. **It does not.** `git cat-file -e 9ae089f:chapters/volume-05/chapter-0221.md` returns PRESENT, `git cat-file -t` returns `blob`, and `git show 9ae089f:chapters/volume-05/chapter-0221.md | wc -c` returns **14465** — a real blob, and **byte-identical to the base**: `git diff --numstat 9ae089f 18e57c8 --` over the ten returns empty. `9ae089f` is *save writer work batch-0001* and it carries all ten of this range's files unchanged. **Item 265E's check is sound and this run used it; the instance of it printed in the dispatching prompt is not, and a prompt that hands a phase a counter-example which is not there teaches it that exit 128 is an ordinary outcome of this range instead of an alarm about its base.** Named because the prompt is the artifact and the check is the standing, and a check cited with a false instance is a check a later phase will distrust.

---

## One — an instrument fault, with the case printed, and a figure in a paid sibling review corrected by it

### One A. `shared_runs` reports the *envelope* of a cluster of overlapping runs as one contiguous run

`python3 tools/measure.py reprints --window 20 --volume 05 --show 4` prints, as the three longest prose runs in the volume:

```
[255] chapter-0225.md: she shut the window at about the fourth minute past the hour and …
[210] chapter-0218.md: at about the ninth hour for a copy of a form at fourpence and …
[195] chapter-0229.md: said the bridge is shut and has been shut since before the water came in and …
```

**All three are wrong, and the mechanism is in the merge step.** `shared_runs` (`tools/measure.py:216`) builds a window index, extends each candidate `(path, start)` against every *other* file holding the same window, and appends `(path, start, start + best)` where `best` is the longest verified extension. It then merges:

```python
for start, end in spans:
    if merged and start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
```

**A new span is merged whenever it *starts at or before* the previous span's end, and the merged result takes the outer envelope.** Two runs that overlap only partly — and that matched **different partner files** — are therefore reported as one span running from the first run's start to the second run's end, and **the tokens in between were never verified against anything.** The merge is sound only when one span contains the other or the two abut exactly; as written it also fires on any overlap, because the condition tests the start against the end and not containment.

**The case, measured.** Re-deriving the instrument's own index and its own extension loop, and taking `max(best)` over candidates **without** the envelope step, loaded through `m.load_cached` and `m.TOKEN` exactly as `cmd_reprints` loads them:

| File | `reprints` prints | true longest verified run | partner |
|---|---|---|---|
| `chapter-0225.md` | **255** | **117** | `chapter-0213.md` |
| `chapter-0218.md` | **210** | **129** | `chapter-0207.md` |
| `chapter-0229.md` | **195** | **86** | `chapter-0214.md` |

And the volume's true longest verified cross-file run is **132 words**, at `chapter-0223.md:3` ↔ `chapter-0234.md:3` — **`chapter-0225.md`, which the instrument names as the volume's worst offender at 255, is not in the true top six at all.** Worked case for the mechanism, on the 255 itself: at `chapter-0225.md` token offset 2434 the twenty-word window is held in exactly two positions, its own and `chapter-0213.md:2704`, and the verified extension against that partner is **81 words**; the instrument reports **255**.

### One B. The eighth audit's 195 is an envelope, and that audit's own table already printed the right figure

`reviews/volume-05-batch-0003-eighth-audit.md` charged the paid review's *in different words* clearance and supported it with the instrument: *"`python3 tools/measure.py reprints --window 20 --volume 05 --show 6` reports a **195-token** run in `chapter-0229.md` … **the instrument exists and it works** — and **the clearance was written without running it.**" **That audit's own table, four lines above, prints the correct figure:** `| **69** | **42 / 39** | *said the bridge is shut and has been shut since before the water came in …* |`.

**The 69 is right and the 195 is the envelope artefact.** Measuring the longest common contiguous token run between `chapter-0229.md` and `chapter-0230.md` directly returns **69 words**, beginning *said the bridge is shut and has been shut since before the water came in* — the identical span, from the identical offset, at the identical length. **So the eighth audit reported a figure nearly three times the true one, in the same document, four lines under the true one, and used the wrong one to certify that an instrument works.** The instrument has an unstated and unstated-in-the-wrong-direction convention on its headline number, and it is the *only* number `reprints` prints a reader is likely to quote.

**What survives and what does not.** **The eighth audit's substantive finding is untouched and remains correct**: the bridge-shut exchange at `chapter-0229.md:116-124` and `chapter-0230.md:77-85` *is* a deliberate verbatim reprise of 69 consecutive words, the prose says so in three characters' mouths at `chapter-0230.md:83`, `chapter-0230.md:85` and `chapter-0229.md:122`, and the paid review's clearance of it as *in different words* is still false. **What is withdrawn is the 195 and the sentence asserting the instrument works unchecked.** The Lowcross claim the clearance was supporting — nineteen pounds three and fourpence, unpaid, nobody liable, no line for a bridge in that fund in nineteen years — reproduces untouched at `chapter-0229.md:15`, `chapter-0229.md:128` and `chapter-0230.md:91` and is not affected.

**The instrument was not changed by this run.** `tools/measure.py` is not this phase's to edit. The fault is named and the case printed beside it, which is what item 302's Two C did for `lifts --base` and what it should now also be done for.

### One C. And the largest true run in the volume is the manuscript's recension formula, which `classify` calls prose

The 132-word run at `chapter-0223.md:3` ↔ `chapter-0234.md:3` is **not a defect and is withdrawn as one.** Marek Kest's recension paragraph — *a table in it and a chair and a bed that is against the wall he does not use … a bar of his own that came off him on the twelfth of the ninth month of last year* — is the volume's stock re-entry paragraph: `grep -c "a bar of his own that came off" chapters/volume-05/chapter-*.md` returns ten files carrying it (`0203`, `0215`, `0216`, `0223`, `0227`, `0231`, `0234`, `0235`, `0237`, `0246`). Tamsin Rook's carries three (`0207`, `0218`, `0222`); Ivet Sarn's door-and-duty passage carries three (`0205`, `0213`, `0225`), and `chapter-0225.md:99` and `chapter-0213.md:113` are **identical whole lines**.

**These are the volume's deliberate recension device, and `classify` returns `prose` for every one of them** — `reprints --window 20 --volume 05` prints `date formula 0 prose 457`, `terms formula 0 prose 457`, `either formula 0 prose 457`. A recension paragraph carries neither a date line nor a formula term, so the classifier has nothing to key on and files the manuscript's own stock paragraphs in the bucket meant for borrowed prose. **The consequence is that `reprints`'s headline figure in this volume is a formula paragraph, and the true worst offender — `chapter-0225.md`, 255 by the instrument's arithmetic — is a recension, not a re-print.** Any future reading that takes `reprints`'s longest run as a prose finding on this volume will be reporting the manuscript's method. Recorded so the next pass does not charge it, and so the classifier's blind spot is named where the numbers are.

---

## Two — two prose defects in this range, both located, both needing authority this run does not have

Volume 05 is a closed volume. Neither of these is repaired, and neither was.

### Two A. `chapter-0230.md:3` states the third-month mark in a form no other chapter uses, and under the reading its own siblings support it contradicts `chapter-0229.md:11` by a foot and a bit

> `chapter-0229.md:11` — *"the water was a foot and a bit **off the mark** where it had been in the third month"*
> `chapter-0230.md:3` — *"the water was **up about a foot and a bit** where it had been in the third month"*

Both clauses name **the same fixed reference** — where the water had been in the third month — and they give it opposite levels, in consecutive chapters of one batch twenty-three days apart. `grep -rn "foot and a bit" chapters/volume-05/chapter-*.md` returns five statements of that mark and **four of the five are *off***: `chapter-0229.md:11`, `chapter-0231.md:11`, `chapter-0232.md:7` (*a foot and a bit off the mark it had in the third month*) and `chapter-0242.md:3`.

**`chapter-0230.md:3` is a hybrid of the volume's two idioms and matches neither.** The level idiom needs *the mark* — every one of the four carries it. The delta idiom needs *from* — `chapter-0238.md:7` has it, *"The water was **down** a foot and a bit **from** where it had been in the sixth month"*, and that sentence is unambiguously about a change, not a level. **`chapter-0230.md:3` has `up`, which is the level idiom's verb, with `where it had been`, which is the delta idiom's complement, and it has dropped *the mark* that the level idiom requires.**

**The honest limit of this finding, stated rather than buried.** Under the level reading — the one `up` invites, and the one four sibling sentences support — `chapter-0230.md:3` says the third month stood a foot and a bit **above** the mark and `chapter-0229.md:11` says it stood a foot and a bit **below**, and no reading reconciles them. Under the delta reading it says the water has *risen* about a foot and a bit since the third month, which is consistent with `chapter-0229.md:11` and unremarkable for a river in the fifth month. **So this is charged as a malformed idiom rather than as a flat contradiction**, and it is charged at all because the delta reading requires supplying a *from* the sentence does not have while four siblings supply a *the mark* this one does not. It is **minor — an idiom, not a figure** — and it is exactly the class item 298 named for Batch 0004: *a contradiction no pass or instrument here can see because it is made of a preposition and not of a number.*

### Two B. `chapter-0225.md:144` gives a sentence to the one woman on the page who refuses it, four lines after she refuses it

> `chapter-0225.md:144` — *"**A woman of about thirty-five** in another city has said in a room that a name in a book does not go looking."*

The page supplies the attribution three times, and the woman it names is **on the page declining it**:

- `chapter-0212.md:107` — **Orla Denning**, the clerk of about fifty-five, says it: *"**A name in a book does not go looking.** A name in a book only goes looking when somebody goes looking…"*
- `chapter-0224.md:41` — **Bess Tarrant**, sixty-three, puts it to the woman of thirty-five: *"**Then somebody has to have told you that a name in a book does not go looking.**"*
- `chapter-0224.md:45` — **the woman of about thirty-five asks `"Who says that?"`**
- `chapter-0224.md:47` — Bess Tarrant answers and names the speaker: *"**A woman of about fifty-five in a room off the old river road said it to me** on the second day of the second week of the twelfth month of the year after, and she said it because I asked her to go and look for me in a book of about nine hundred and forty names, and she said no."*
- `chapter-0224.md:53` — Bess Tarrant says it herself, extended: *"**A name in a book does not go looking, and a name in a street does not go looking either.**"*

**So the woman of about thirty-five asked, on the page, who had said it; the page answered *a woman of about fifty-five*; and one chapter later a clerk four hundred and thirty miles away reports that the woman of about thirty-five is the one who said it.** This is the same class as the person-shift the sixth audit found at `chapter-0227.md:59` and as the thank the Batch 0004 review found given to the wrong man at `chapter-0236.md:82`, **and it is stronger than either, because here the page contains the denial and the correct attribution in the four lines immediately before the error.** The volume's whole method is that a name in a book does not go looking; an attribution that puts the sentence in the wrong mouth is the failure that method is built to prevent, and it is the failure the record has been most reliable about catching. `chapter-0225.md:144` is in this batch and is charged.

### Two C. `four bays and a corridor away` is a same-building distance, and it is used at `chapter-0223.md:123` and `chapter-0224.md:83` of two places the volume puts nine miles off

`grep -rn "four bays and a corridor away" chapters/volume-05/chapter-*.md` returns three, and only the first is that distance:

| Line | Whose position is being given | What the volume says the distance is |
|---|---|---|
| `chapter-0222.md:135` | the bay → Orla Denning's room | same building — **correct use** |
| `chapter-0223.md:123` | the bay → **Marek Kest's rented room** | **nine miles** |
| `chapter-0224.md:83` | the bay → **Bess Tarrant** | **nine miles** |

`chapter-0223.md:123` sits in Marek's rented room and reads *"a woman in a bay four bays and a corridor away did not come up a stair"*. **Thirty-two lines earlier in the same chapter, at the same door, Tamsin Rook says** (*`chapter-0223.md:91`*) *"This is a woman standing in a doorway in **a city nine miles from an office of a seat**"* — and the bay is in the building that holds the office of a seat, four bays and a corridor from Orla's room. `chapter-0224.md:83` has Bess Tarrant place Tamsin's bay *"four bays and a corridor away"* from herself, and **`chapter-0224.md:93`, ten lines later in the same chapter, puts Bess's own street *"in a city about nine miles from a building off that same road"*** — the same road the bay's building is off.

**The volume proves its own convention in a fourth sentence.** `chapter-0225.md:49` — *"I told a man of about sixty at a counter **four bays and a corridor and a river away** that he could"* — **adds *and a river* when it means distance.** The bare phrase is the short, same-building measure, and the volume has a longer form for the long one and used it three chapters after using the bare one correctly. Nine miles is not four bays and a corridor.

**And the rest of the distance record agrees on nine.** `chapter-0215.md:29`, `:33`, `:93` and `:117` and `chapter-0226.md:116` all put Marek's rented room about nine miles from the counter; `chapter-0215.md:117` has the woman of twenty record *"I walked about nine miles"* to it. **So this is a phrase borrowed from a sentence about a different pair of rooms, and it is charged as a minor prose defect in two lines of this range.** The fourth audit saw `chapter-0224.md:83` and adjudicated it — *"Not contradicted by the page… That is a craft observation and not a defect"* — but it examined only the *"in about a year"* and *"through a door"* axes, on the sound ground that no chapter in the volume carries Bess and Tamsin together. **That ground is right and it does not reach the distance**, which is a claim about geography rather than about company, and which the same chapter contradicts at `:93`.

---

## Three — five candidates raised on this pass and withdrawn, recorded so a later phase does not re-derive them

The standing requires a pass to print what it looked at and gave up. Five, all measured.

**Three A. The `next year` at `chapter-0229.md:5` and `:98` is a volume convention and not a slip.** *"since the second month of next year"* reads as a forward date in a chapter set in the fifth month of *the year after next*, and it is worth checking. `grep -rn "next year" chapters/volume-05/chapter-*.md` returns **23 lines across 14 files**, of which Rennick Adley's stock *"second month of next year"* appears **fifteen times** (`grep -rn "second month of next year"` → 15 lines): `0206:5`, `0211:5`, `0214:5`, `0229:5`, `0229:98`, `0231:5`, `:7`, `:17`, `:33`, `:79`, `:101`, `:110`, `0239:59`, `:91`, `0248:3` — **across two batches, in the same clause.** It is a repeated formula for one character's tenure, not a date error in one line. **Withdrawn.**

**Three B. `chapter-0226.md:33`'s *sixteen* is not a count error.** `chapter-0226.md:3` has fifteen books and `:5` accounts for them (eleven houses on a lane plus four in three other districts); `:45` is still *"the heap of fifteen"*; the sixteenth arrives at `:124` and `:140` is *"sixteen books"*. **But `:33` says *the sixteen* before the sixteenth has been handed over** — and at `:33` it is physically in the room, in the satchel the woman of thirty *"had been holding against her chest since she came in"* (`:45`), with the key. A count of what would go to a woman with a key, spoken while she is holding one of them, is defensible. **Withdrawn.**

**Three C. `chapter-0228.md:77`'s *nine sentences* and `chapter-0228.md:35`'s *nine sentences* can both stand.** They are forty-two lines apart in one chapter about one exchange and cannot both be a count of the same thing — but the page supports each on its own reading. Measured with `tools/measure.py`'s own `SPLIT = re.compile(r"(?<=[.!?])[\"'’”)\]]*\s+")` (`tools/measure.py:580`), the first answer run, `chapter-0228.md:25`–`:29`, is **exactly 9 sentences** (`:25`→2, `:27`→3, `:29`→4), which is what `:35` claims — *"the answer to his own question in nine sentences"* — and `:35` names its referent precisely. `:77`'s *"I have given you nine sentences"* is loose, since her quoted paragraphs across `:25`–`:79` measure **49**, but it can be read as the same claim of the answer to the one question she was asked. **Withdrawn, and the 9 and the 49 are printed so the next pass does not rebuild them.** This is the standing from `reviews/volume-04-batch-0005.md` section one item three applied in the other direction: a loose claim is not a wrong one.

**Three D. `chapter-0224.md:83`'s *"once in about a year"* is owned.** The fourth audit raised it, measured the nine-day gap to `chapter-0223.md:73`, and ruled it unstaged history on the ground that no chapter carries Bess and Tamsin together. This pass re-derived that independently — `for f in chapters/volume-*/chapter-*.md; do grep -q Bess "$f" && grep -q Tamsin "$f"; done` returns **nothing across all twelve volumes**, which is a stronger form of the same result — and **agrees with the ruling. Not re-charged.** What the fourth audit did not examine is section Two C above, and that is charged there.

**Three E. The three longest cross-file runs in the volume are the recension formula.** `chapter-0223.md:3`↔`chapter-0234.md:3` at 132 words, `chapter-0222.md:5`↔`chapter-0207.md:5` at 129, `chapter-0225.md:99`↔`chapter-0213.md:113` at 117 — **all three are stock character or scene paragraphs carried in three to ten chapters apiece**, and none is a re-print. **Withdrawn as prose defects** and the reason recorded in One C, because the instrument files them as prose.

**And this file's own errors, printed beside its findings, because a register that prints only its corrections is a list of numbers.** The first draft of section Two C said *eleven lines earlier* for `chapter-0223.md:91` against `:123` and *ninety lines later* for `chapter-0224.md:93` against `:83`. **Both are wrong and both were caught by re-running the subtraction rather than the reading: the gaps are thirty-two and ten.** The first draft of Three A said *twenty-eight lines* for `next year` and *fifteen files* where the command gives **23 lines across 14 files**. **Three figures wrong in the reading on a pass whose whole argument is that a figure printed without a command beside it cannot be checked** — and the reason each was caught is that each had a command next to it to disagree with. That is the standing working, and it is also the standing's limit: it catches a number that has a command and not a judgement that does not, which is why Two C is charged as a malformed idiom and not as a contradiction.

---

## Four — every checkable figure, re-derived on this tree, with the command beside it

Nothing in this section is new. It is here so that a later phase does not spend a run on it, and so that the claims this file *does* make are visibly sitting on a base that holds.

| Claim | Result | Method |
|---|---|---|
| **No month name and no weekday name in the prose** | **holds — 0 and 0** | `grep -n -o -i -w -E "january\|…\|december\|monday\|…\|sunday"` over the ten returns **13 hits on 12 lines, every one of them `may`**: `0222:73` (twice), `0222:125`, `0223:23`, `0223:105`, `0224:35`, `0225:37`, `0225:45`, `0228:15`, `0228:91`, `0228:99`, `0229:13`, `0229:70`. Each read in place and every one is the modal verb. `grep -rn "\bMay\b" chapters/volume-05/chapter-*.md \| wc -l` returns **0** |
| **The count of things asked out loud is four, and no chapter makes it five** | **holds** | every statement of it at `0221:105`, `0222:81`/`:135`, `0223:121`, `0224:111`, `0225:45`/`:144`, `0226:134`, `0228:114`/`:116`, `0229:36`/`:134`, `0230:99` — **four in all thirteen, five in none** |
| **`about nine` bound holds; the card's figure does not** | **3 to 8, median 6.0, total 56** | `re.findall(r"\babout nine\b", t, re.I)` less `re.findall(r"\babout nine hundred\b", t, re.I)`, per file: **5, 7, 4, 5, 6, 6, 6, 3, 6, 8**. The subtraction removes **18** instances and is not optional — a raw count inflates `0221` from 5 to 9 and `0228` from 3 to 7. Card item 31's *six to eight, seventy-two* still does not reproduce |
| **`exception` and `precedent` absent** | **holds — 0 and 0** | `grep -c -i -w exception` and `grep -c -i precedent` over the ten, per file |
| **No certification granted and none held** | **holds** | `grep -n -i certif` returns 2, at `0223:5` and `0227:21`, both *"nothing in this empire he could certify anything with"* |
| **Nobody thanked** | **holds** | `grep -o -i thank` returns **25 occurrences on 19 lines**; every one read in place is a negation or an explicit refusal (*not going to be thanked, nobody has thanked her, nobody is going to thank you, if you thank me I will not take it*) |
| **`four hundred miles` absent; `four hundred and thirty` the long form** | **holds — 0 and 14** | `grep -o` both over the ten |
| **Volume-wide `four hundred and thirty`** | **134 case-sensitive, 135 with `-i`** | the delta is one sentence-initial capital at `chapter-0209.md:95`, the only capitalised instance in the volume. **Item 302's Two B reproduces: the recorded 134 is reproducible only under a case flag no record prints** |
| **Lowcross bill: nineteen pounds three and fourpence, unpaid, nobody liable** | **holds** | `0229:15`, `0229:128`, `0230:91`, each with *no line for a bridge in that fund in nineteen years* or *no line against it in nineteen years* |
| **The guarantee stands offered and unanswered, word for word, no child named** | **holds** | *four hundred and forty foot* at `0229:130`, `0230:15`, `0230:101`; *about sixty children under sixteen* at `0229:130`, `0230:15`, `0230:73`, `0230:101` |
| **The reader of seventeen is unnamed, unthanked, not going to start, no elapsed period computable** | **holds** | *written engagement* at `0229:96`, `0230:73`, `0230:101`; **`forty-five pence` 0 and `four days a week` 0** — the rate is deliberately unprinted, at *the rate the list is set at* and *on the same rate as everybody else on the list* |
| **The Venn ruling's five operative terms never miscounted** | **holds, vacuously** | `Venn` 0 and `ruling` 0 over the ten — the ruling is not mentioned in this batch, so its terms are neither given nor miscounted |
| **Mosswake and thirty-one** | **holds — 0 and 0** | `grep -c -i -w Mosswake` and `grep -c -i thirty-one` over the ten |
| **No out-of-world breach** | **holds** | `grep -rno -E ".{0,30}\b(chapter\|volume\|reader of the book)\b.{0,30}"` over the ten returns nothing |
| **Structural gates** | **all clean** | punctuation-then-two-spaces 0; full-stop-then-lowercase 0; `[A-Za-z]\*\*[A-Za-z]` 0 |
| **Word figures** | **29,032** | `wc -w` per file: 3011, 2758, 2714, 2956, 3018, 3164, 2763, 2754, 2919, 2975 |
| **No added prose against the base** | **ADDED 0 / BASELINE 532, mean 12.98** | `python3 tools/measure.py lifts --first 0221 --last 0230 --base 18e57c8`. **Run without `--base` the same command prints `ADDED 532 / BASELINE 0` on this unrepaired range — item 302's Two C, unchanged, and still untested by the eleven selftest plants** |

**The nine prose defects already located on this range all re-seen at their line numbers and none re-charged:** `chapter-0226.md:7` (*she am*), the doubled breaks at `chapter-0226.md:49-50` and `chapter-0229.md:19-20` (my `awk` reports the second line of each pair, `:50` and `:20`), and `chapter-0221.md:57` (*`" Then what is in the building.`*), the last confirmed by `grep -rn '^" ' ` over the ten, which returns that line alone.

---

## Five — what this pass could not do, and the frontier, unmoved

**The defects in section two need prose authority** — one substitution in `chapter-0230.md:3`, one attribution in `chapter-0225.md:144`, one phrase in each of `chapter-0223.md:123` and `chapter-0224.md:83`, in a closed volume. **A review has no authority to make one and this run took none.** They are listed with line numbers so a phase given the authority need not re-find them, and **a line number in a file no phase has edited is a citation that resolves**, which is the standing item 267's record establishes and which all of section two depends on: `git diff --numstat 18e57c8 --` over the ten is empty.

**The instrument fault in section one is not this phase's to fix.** `tools/measure.py` is named in the phase rules among the files a writing phase may not edit, so One A is a report and a printed case. **The correction that matters most is small and one line**: the merge in `shared_runs` should extend the previous span only when the new span is contained in it or abuts it exactly, and a caller who needs the true longest run wants `max(best)` over candidates with no envelope at all. Until then **any figure quoted from `reprints`'s longest run on this volume is an upper bound and not a measurement**, and item 302's Two B and this section are the same standing applied twice: *a figure that is only reproducible under an unstated convention is a figure nobody can check.*

**And what this pass did not find, which is the honest half.** Twelve passes have now read these ten chapters. This one found two prose defects and an instrument fault and withdrew five candidates. **It read all ten chapters end to end and re-seen all nine previously located defects without charging any of them**, which is the ninth audit's own recorded experience at four of nine invisible to an eleventh full reading. **A range that has produced two live prose defects on its twelfth pass has not been exhausted**, and the standing that requires every claim tested against the page with the method printed beside the figure is the only reason this one produced anything at all.

**The frontier, unmoved.** Volume 05's Batch 0003 is paid at `2359f84` and audited **ten** times over. Volume 05's Batch 0004 is paid at `5316a4f` and audited four times. **Volume 05's Batch 0005 and Volume 06's own Batch 0003 are the two that remain owed, and both already hold correct current prompts** — `workspace/review-debt-0003/PROMPT.md` at base `dedc831` and `workspace/review-debt-0004/PROMPT.md`. **So this run created no prompt and overwrote none**, and the prompt it was handed told it to create one at `workspace/review-debt-0002/PROMPT.md`, which exists, is paid at item 270A, and has itself been deferred three times. `workspace/review-debt-0001/` holds a finished phase's prompt with no `.done`, sorts first in the walk, and **this is at least the fourteenth dispatch of paid work from it**; writing a marker is phase selection and `PHASE_SYSTEM.md` line 216 bars a writing phase from it, so **this run took none and the fix belongs to a controller owner.** Nothing was amended, no paid review touched, no chapter opened for edit, no outline opened for edit, no prose repaired, no volume planned, no Volume 13, no `state/complete.md` written, no controller file edited, `tools/measure.py` unchanged, and **no review here described as independent** — item 171 holds that until a controller owner changes it.

**One lead carried forward, and it belongs to the fourth owed review.** Section One C establishes that `classify` in `tools/measure.py` returns `prose` for the manuscript's stock recension paragraphs, and that the volume's longest reported run is one of them. **`workspace/review-debt-0004/PROMPT.md` reviews Volume 06's Batch 0003, `chapter-0261.md` to `chapter-0270.md`, a range already through the prose repair.** A repaired range is where a recension paragraph and a genuine re-print are hardest to tell apart, and **the lead is named here so it is not lost and it is not counted here.**
