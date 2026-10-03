# THIRD AUDIT: THE PAID SECOND READING OF VOLUME 05, BATCH 0003, CHAPTERS 0221 TO 0230 — THE SIXTH DISPATCH, WHICH FOUND TWO PROSE DEFECTS THE PAID REVIEW AND BOTH AUDITS BEFORE IT DID NOT REPORT

**Who wrote this, and what it is not.** This is an audit of an audit, not a review. `reviews/volume-05-batch-0003.md` was written at `2359f84` and paid at item 268; it was audited at item 275, verified at item 279 in `reviews/volume-05-batch-0003-verification.md`, and confirmed at item 280. **This run was handed the prompt for that same work for the sixth time and found the work done three times over.** It therefore wrote **no review, amended no paid file, and marked no prompt** — `workspace/review-debt-0001/PROMPT.md` carries no `.done`, `.blocked` or `.retired` from this run, on `PHASE_SYSTEM.md` line 216, and a phase that marks its own directory has certified itself. **Nothing in this repository's review gate is independent:** the gate has fallen back to the writing agent every time it has been asked, `NOVEL_SPEC.md` and `state/open-threads.md` item 171 both say so in terms, and **no sentence in this file may be cited as an independent finding either.** What it has that a scan does not have is that all ten chapters were read end to end a fourth time, and that every figure in both paid files was re-derived from the page rather than carried.

**Why this range.** `outline/volume-12.md`, at its close, names four owed reviews, and this is the second of them: the owed second reading of Volume 05's Batch 0003.

**Base, resolved and asserted before any figure was taken from it.** `git log --oneline -- chapters/volume-05/chapter-022[1-9].md chapters/volume-05/chapter-0230.md` returns `18e57c8` (*save review fixes batch-0003*) and `7a54b16` (*save writer work batch-0003*) and nothing else, so **`18e57c8` is the base**. `git show 18e57c8:chapters/volume-05/chapter-<each of the ten> | wc -c` returns **14465, 13200, 12889, 14056, 14323, 14960, 13221, 13046, 13878 and 14020 bytes, ten out of ten non-empty** — item 265E's check, and the reason a counter piped off a missing base was not believed. `git diff --numstat 18e57c8 -- <the ten files>` returns **nothing**: worktree and base are byte-identical on all ten. `git log --oneline --grep="prose-repair" -- chapters/volume-05/` returns **nothing**, so Volume 05 has never been through the prose repair and **every line number below is a citation of a text and not of a position.**

**What this run did not do.** It opened no chapter for edit, edited no outline, repaired no prose, planned no volume, opened no `outline/ending.md`, created no Volume 13, wrote no `state/complete.md`, edited no controller file, and did not change `tools/measure.py`.

---

## Section one — two prose defects that no earlier pass on this range reported

Both were found by reading, and both are located in base text. **Both need delete or substitute authority in a closed volume, which this run does not have and did not take, so both are reported and neither is fixed.**

### One. `chapter-0225.md:132` and `chapter-0225.md:134` give the same count as eleven and as thirteen, three lines apart

Line 132, narration:

> "...and at the bottom she put the reason, which is the reason she has written **eleven times** in nine years and which has not got any better:"

Line 134, the entry she is writing, in bold:

> "**A hand of mine is the only hand anybody is going to be able to put side by side in about four years, and I have now done this for the thirteenth time** and I have not stopped and I am not going to."

Both numbers count writes of the same sentence — the narrative calls it *the reason she has written* eleven times, and the entry calls the same sentence *this* and says she has now done it for the thirteenth time. **The gap is two, and that is what closes the only reading that would reconcile them.** The natural reconciliation in a manuscript where a count is narrated before the counted act is *eleven before today, so today is the twelfth* — and **eleven plus one is twelve, not thirteen**, so that reading is unavailable. A third reading, that the first two entries carried no reason, would make the reason count eleven and the entry count thirteen, and **the text says the reason is written every time at the bottom of an entry** (line 132: *at the bottom she put the reason*), so there is no entry without one.

Method: `sed -n '132p;134p' chapters/volume-05/chapter-0225.md`, and `grep -rn "thirteenth\|eleven times" reviews/ state/` returns **nothing** — the defect is in no review and no state file in this repository.

**Why no instrument in this repository can see it.** It is not a repetition: *eleven* and *thirteenth* share no run. It is not a wrong canon figure, because eleven and thirteen are not canon for this sentence anywhere. It is a **count disagreeing with a count about the same object two lines apart**, which is a different shape from item 266B's *figure contradicting a canon figure in seven other files* and is closer to item 170's standing: **this project measures sentence length, emphasis, word counts and lifted phrases, and has never once measured whether a number agrees with the number beside it.**

### Two. `chapter-0227.md:5` carries a doubled locative, unique in the volume

> "Nell Kest is twenty. She is a dye-house worker and her wage is held and there are now sixteen books in a room two streets off a street that goes down to the river road and not one of them has an office on it. **She was in the room in a rented room** about nine miles from a building off that road."

The preceding sentence ends in *a room* and the next clause opens *in the room*, so the line reads *was in the room in a rented room* — two locatives in a row, the first with no antecedent that is not the room she has just finished describing and which is on a different street. It reads as a botched join between the summary of the room two streets off (which is `chapter-0226.md`'s room and is where she was in that chapter) and this chapter's rented room nine miles away. **Method: `grep -rn "in the room in a" chapters/volume-05/` returns this line and no other in fifty files**, so it is not a house idiom of the volume and it is unique to this line. A duplicate-word or doubled-preposition sweep keyed on an adjacent repeated token would not reach it, because *room* and *room* are not adjacent and *in* and *in* are separated by a noun phrase.

---

## Section two — two record faults in the record of this range, and one gap in a clearance

### Fault A. The inter-chapter gap sequence printed in the verification is wrong on three of eight

`reviews/volume-05-batch-0003-verification.md` section two, fault B, states that the batch's gaps are *9, 5, 9, 5, 9, 5, 9, 5, no remainder* and uses that sequence to force a 28-day month. Re-derived from each chapter's own date line, quoted beside each:

| Chapter | Its own date line | Month, day | Gap |
|---|---|---|---|
| 0221 | `chapter-0221.md:137` *second day of the first week of the third month* | m3 d2 | — |
| 0222 | `chapter-0222.md:3` *fourth day of the second week of the third month* | m3 d11 | **+9** |
| 0223 | `chapter-0223.md:7` *second day of the third week of the third month* | m3 d16 | **+5** |
| 0224 | `chapter-0224.md:11` *fourth day of the fourth week of the third month* | m3 d25 | **+9** |
| 0225 | `chapter-0225.md:7` *second day of the first week of the fourth month* | m4 d2 | **+5** |
| 0226 | `chapter-0226.md:7` *second day of the second week of the fourth month* | m4 d9 | **+7** |
| 0227 | `chapter-0227.md:3` *fourth day of the third week of the fourth month* | m4 d18 | **+9** |
| 0228 | `chapter-0228.md:77` *fourth day of the fourth week of the fourth month* | m4 d25 | **+7** |
| 0229 | `chapter-0229.md:3` *second day of the first week of the fifth month* | m5 d2 | **+5** |
| 0230 | `chapter-0230.md:3` *fourth day of the fourth week of the fifth month* | m5 d25 | **+23** |

The true sequence is **9, 5, 9, 5, 7, 9, 7, 5, 23**. **Three of the eight inter-chapter gaps disagree with the printed sequence**, at positions five, six and seven. The last is not *no remainder* but twenty-three days.

**The verification's conclusion survives and is in fact better supported than the evidence it printed.** The origin of the fourth asking is *the first week of the first month of the year after next* at `chapter-0222.md:81` and `chapter-0223.md:121`; measured from that origin, `chapter-0223.md:121`'s *"in the ten weeks since"* is **exactly seventy days** provided months one and two are both twenty-eight, and `chapter-0222.md:81` and `:85`'s *"ten weeks"* is **sixty-five days**, or nine weeks and two days. **So the page itself forces a 28-day month and the "ten weeks" fault B records is real and stands unaltered.** What does not stand is the gap table that was the stated route to it, and the standing is item 267's: **a total can hold while the citations beneath it are wrong, and here a correct conclusion rests on an incorrect derivation.**

### Fault B. The paid review's "read and set aside" list does not contain the range's only *N words* claim

`reviews/volume-05-batch-0003.md` line 38 sets aside four *four words* instances as slips and references rather than quotations with a length. **A whole-range sweep for the device returns one more instance, and it is the only true one:**

> `chapter-0224.md:123` — "She put the day against it in her own hand and read it back to herself out loud, once, and **it is nine words** and she got all of them right the first time."

Method: `grep -n -o -E ".{70}\b(one|two|…|twelve) words?\b.{40}" <the ten>` returns `0223:79` (*one word of it*), `0224:93`, `0224:123`, `0228:11`, `0228:47`. Three of the five are a reference or a slip and are correctly set aside; `0223:79` is a different construction; **`0224:123` is a count of words and is not in the paid review's list.**

**It is not charged as a defect, and the reason is the standing in `reviews/volume-04-batch-0005.md` section one item three** — an *N words* claim may be reported only where the quoted span is so far from N that no plausible convention reaches it. **No span is quoted here at all**, so that test cannot be run: the referent of *it* is unresolvable from the page, being either the letter's four lines (about 140 words) or the day written against them. **It is recorded as an unresolvable claim and not as a counted defect**, and it is reported here because a clearance list that enumerates the device in a range and misses the one instance of it is a clearance that cannot be relied on.

**And it sits against a stated incapacity, which is why it is worth a line and not a word.** `chapter-0224.md:5` — *"She can write and she cannot read a paragraph"* — and `chapter-0224.md:117` — *"She cannot read a paragraph"* — and `chapter-0224.md:123` — *"read it back to herself out loud, once, and it is nine words and she got all of them right the first time."* A woman established twice in one chapter as unable to read a paragraph does not read a sheet back to herself and get every word right the first time. **The claim needs authority to resolve and this run has none.**

### Marginal, and named so it is not lost — `chapter-0229.md:5` and `:98` place a past event in *next year*

`chapter-0229` is dated *the second day of the first week of the fifth month of the year after next* at `:3`. At `:5` and `:98` Rennick Adley has kept the Slade Cut books *"since the second month of next year"*, and at `:98` the book already holds *"four hundred and some"* entries made since. **`chapter-0226.md:23`, twenty-one days earlier, puts a past event in *the first week of the second month of this year***, so the volume uses **this year** for the current year, and *next year* at 0229 is a year ahead of it.

**This is reported as marginal and not as a defect of this range, for a reason this run checked:** the identical phrase *the second month of next year* attaches to the same book-keeper's start at `chapter-0206.md:5`, `chapter-0211.md:5`, `chapter-0214.md:5`, `chapter-0231.md:7` and `:79` and `:101`, and `chapter-0248.md:3` — **five chapters outside this range and two other batches**, and Volume 05 dates **36 of its 50 chapters** *the year after next* and the rest variously *the year after*. The year-relative naming is therefore a **volume-wide** property and not a slip at 0229. **It cannot be closed from the page, and adjudicating it belongs with whoever reads Volume 05 whole.** `python3 tools/measure.py calendar --volume 05` returns *files read: 50; chapters with a parsed date line: 1*, item 276C's instrument fault, so no instrument in this repository sees any of this.

---

## Section three — every checkable figure reproduces both paid files, re-derived from the page

| Figure | Result | Method, printed |
|---|---|---|
| `about nine`, per file, raw minus `about nine hundred` | **5, 7, 4, 5, 6, 6, 6, 3, 6, 8 — range 3 to 8, median 6.0, total 56**, against the card's 72 | `re.findall(r"\babout nine\b", t, re.I)` less `re.findall(r"\babout nine hundred\b", t, re.I)`, per file. Raw `about nine` is 9, 8, 6, 6, 7, 8, 8, 7, 7, 8 = 74, and **`about nine hundred` is 18 of those**, so **the subtraction is 18 instances and not optional**: 0221 goes 9→5 and 0228 goes 7→3 |
| Whole-word `may` | **13 hits on 12 lines across six chapters**, every one read in place the modal verb; **capital `May` 0**; all nineteen calendar names return only those 13 | `grep -o -w -i may <the ten>` = 13; `grep -w -i may <the ten>` = 12 lines. The month/weekday lock **holds** and the dispatching prompt's census of eight is short by five |
| `wc -w`, per file | **3011, 2758, 2714, 2956, 3018, 3164, 2763, 2754, 2919, 2975 = 29,032** | `wc -w` over an explicit ten-file list. The card's repaired 29,032 reproduces |
| The five located prose defects | **all five seen on the page**: `0226:7` *she am*, doubled `---` at `0226:49-50` and `0229:19-20`, leading space inside the opening quote at `0221:57`, doubled blank at `0228:108-109` | read; the three structural ones also by scan on `lines[i].strip()=="---" and lines[i-1].strip()=="---"` and `lines[i]=="" and lines[i-1]==""` |
| `certif` | **2**, at `0223:5` and `0227:21`, both *nothing he could certify anything with* | `grep -n -i certif` |
| Nobody thanked | **holds — 25 occurrences on 19 lines**, every one a negation or an explicit refusal to thank | `grep -o -i thank <the ten>` = 25 occurrences; `grep -i thank <the ten>` = 19 lines. **This is the paid review's line-count/occurrence confusion, and its number is right while its printed command returns 19** |
| `exception` / `precedent(s)` | **0 and 0** | `grep -o -i -w` over the ten |
| `four hundred and thirty` / `four hundred miles` | **14 and 0** | `grep -o -i` over the ten. **The short form is absent, so the Volume 03 and Volume 04 inconsistency is not repeated in this range** |
| The guarantee | **6 occurrences in 2 chapters**, `0229:130` and `0230`, at *about four hundred and forty foot* and *about sixty children under sixteen* — word for word at both prose instances | `grep -n -i guarantee` |
| The reader of seventeen | **no rate printed**: `0229:96` says *at the rate the list is set at* and `0230:73` says *on the same rate as everybody else on the list*, so **no elapsed period can be computed from her engagement**, as canon requires | read at both lines |
| Lowcross bill | **holds** — *nineteen pounds three and fourpence*, unpaid, nobody liable, at `0229:15` and `0229:128` and `0230:91` | read |
| `the book` / `the books` | **21 raw, 3 of them `the books`, so 18** — the card's twenty-one requires the subtraction | `grep -o -i "the book"` and `grep -o -i "the books"` |
| `python3 tools/measure.py selftest` | **PASS** | run on this tree |

**No new prose defect was found in the recorded set, nothing recorded was amended, and the five located defects plus the two in section one all stand.** The two record faults and the marginal item in section two are recorded here and **corrected nowhere**, per item 275A's standing that a duplicate dispatch does not amend a paid record.

---

## Section four — the standing this audit produces

**A number that disagrees with the number beside it is a third class, and it is the one no instrument here is looking for.** Item 266B named figures that contradict a canon figure in other files. Item 279B named an elapsed span that contradicts a date line in another chapter. **`chapter-0225.md:132` and `:134` are a count that contradicts a count about the same object two lines apart, inside one paragraph pair, in one file** — and it is invisible to every mechanism this project owns, because it is not a repetition, not a lift, not a sweep, and not a calendar parse. **The extension: a reviewer who checks every number against the canon and every span against the calendar has still left the cheapest class of all unchecked, which is a figure against its own neighbour.**

**And a clearance list is only as good as its longest list.** The paid review set aside four instances of the *N words* device in this range and named them, and the fifth instance is the one that is the device. **Item 267's standing — that a record which certifies something clean is worse than a record which is silent — applies to a review's own read-and-set-aside paragraph as squarely as it applies to an outline's cleared-claims table,** and this is the fourth time in three batches that an enumerated clearance has been the place its own error lives (items 276B's 19 against 15, 279B's 25 against 19, 280B's prefix glob, and this).

---

## Section five — what this audit could not do, and hands on

**The two prose defects in section one need substitute authority in a closed volume, which no prompt in this repository grants.** They are reported with line numbers so a phase given that authority need not re-find them, and **a line number in a file no phase has edited is a citation that resolves**, which is item 267's standing and which the whole of section one rests on.

**Two things this audit did not open and does not own:** `chapter-0050.md:85`, twelve tokens called four words, in Volume 04; and `chapter-0250.md`, the `about nine` count at 1 against a card claiming 3 to 8. **Both are named in `outline/volume-12.md`'s frontier and neither is counted here.**

**What was touched.** No chapter file, no outline, no `tools/measure.py`, no controller file. It read `outline/batches/volume-05-batch-0003.md`, `outline/volume-05.md`, `reviews/volume-04-batch-0005.md` and both paid files on this range; it read all ten chapters in full; it grepped `chapters/` for every canon figure it names. **It is the sixth dispatch on this range and the fourth pass over the page, and it is the first that found a prose defect.**