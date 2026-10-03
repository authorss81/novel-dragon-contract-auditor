# SIXTH AUDIT: THE PAID SECOND READING OF VOLUME 05, BATCH 0003, CHAPTERS 0221 TO 0230 — THE TENTH DISPATCH ON THIS RANGE AND THE EIGHTH PASS OVER THE PAGE, WHICH FOUND ONE PROSE DEFECT THAT NINE PASSES DID NOT REPORT, AND FOUND THE PROMPT THAT SUMMONED IT TO BE PAID WORK RE-DISPATCHED A TENTH TIME

## Who wrote this, and the statement that it is not independent

This is a writing phase, not a reviewer and not a controller. It read ten chapters end to end and reported on them. **It is not independent, and no sentence in this file may be quoted as though it were.** The review gate itself is a controller-owned defect recorded at `state/open-threads.md` item 171, and a phase that writes its own review cannot also certify that the gate which called for it is sound. What this file is: *the sixth review document, and the eighth pass, over one range of ten chapters.*

It is item **294**, taken from the high-water mark of 293 in `state/open-threads.md` and read off that file and off nothing else. **Nothing above that mark was renumbered, because renumbering a ledger renumbers every cross-reference to it.**

---

## Section one — the prompt that dispatched this run is paid work, and this is the tenth time it has said so

**The prompt handed to this phase is `workspace/review-debt-0001/PROMPT.md`, and its work has been done nine times over. Its own closing line is false on the tree.** Method:

```
head -1 workspace/review-debt-0001/PROMPT.md
head -1 workspace/review-debt-0002/PROMPT.md
head -1 workspace/review-debt-0003/PROMPT.md
head -1 workspace/review-debt-0004/PROMPT.md
```

| directory | first line | state of its work |
|---|---|---|
| `workspace/review-debt-0001` | *OWED SECOND READING: VOLUME 05, BATCH 0003 … THE SECOND OF THE FOUR OWED REVIEWS* — **this is the prompt that summoned this run** | **paid nine times over** |
| `workspace/review-debt-0002` | *OWED SECOND READING: VOLUME 05, BATCH 0004 … THE THIRD OF THE FOUR OWED REVIEWS* | **paid**, `reviews/volume-05-batch-0004.md` |
| `workspace/review-debt-0003` | *OWED SECOND READING: VOLUME 05, BATCH 0005 … THE FOURTH OF THE FOUR OWED REVIEWS* | unpaid — **the live frontier** |
| `workspace/review-debt-0004` | *OWED REVIEW: VOLUME 06, BATCH 0003* | unpaid |

```
git log --oneline -- reviews/volume-05-batch-0003.md \
  reviews/volume-05-batch-0003-verification.md \
  reviews/volume-05-batch-0003-third-audit.md \
  reviews/volume-05-batch-0003-fourth-audit.md \
  reviews/volume-05-batch-0003-fifth-audit.md
```

```
2359f84 review: the owed second reading of Volume 05 Batch 0003, chapters 0221 to 0230, the second of four named at Volume 12 close, finds four prose defects needing authority it does not take and two record clearances that do not reproduce
a826345 review: verify the paid second reading of Volume 05 Batch 0003 instead of rewriting it, find five record faults it did not report, and close an elapsed-span contradiction without needing a month length
839f5e6 review: the third audit of the paid second reading of Volume 05 Batch 0003, the sixth dispatch on it, which found two prose defects the three earlier passes did not report and one record derivation that is wrong while its conclusion survives
8de8810 review: the fourth audit of the paid second reading of Volume 05 Batch 0003, the eighth dispatch on it, which found a prose defect no pass reported and corrected the third audit's year-term marginal to the wrong term
30c04cd audit: fifth audit of paid second reading of Volume 05 Batch 0003, item 291, nothing new
```

**So the prompt's line — *Three owed reviews remain after this one: Volume 05's Batch 0004, Volume 05's Batch 0005, and Volume 06's own Batch 0003* — is false on this tree.** Batch 0004's review exists at `5316a4f` and has been verified and audited four times since. **Two remain, not three.**

**Both instructions this prompt gives that would destroy paid work, and what this run did instead, under item 275A's standing.**

1. *Write one file: `reviews/volume-05-batch-0003.md`.* That is the paid review at `2359f84`. Writing it would have destroyed the second reading and four audits on top of it, and every cross-reference to all five in `state/`. **This run did not open it for edit.** It wrote `reviews/volume-05-batch-0003-sixth-audit.md`, which is the naming this repository already uses for this case — `reviews/volume-05-batch-0003-fifth-audit.md` is item 291, so this is the sixth review document.
2. *Create exactly one next phase prompt at `workspace/review-debt-0002/PROMPT.md` for Volume 05's Batch 0004.* **That file exists at 9,722 bytes and its work is paid.** **This run created no prompt**, following items 283F, 284D, 285H, 290H and 291C, which reached that decision on this identical instruction five times before. The base was resolved anyway, as those items did, and is in section seven. The instruction's purpose — that the ladder advances past this phase — **is already satisfied on the tree**: `workspace/review-debt-0003` and `workspace/review-debt-0004` hold the two genuinely unpaid prompts.

**The mechanism, for a controller owner and not for this phase.** `.github/workflows/novels.yml` selects by `find workspace -name PROMPT.md -type f | sort`, skipping a directory holding `.done`, `.retired`, or a first line matching `Retired .*phase`:

```
sed -n '140,175p' .github/workflows/novels.yml
```

`workspace/review-debt-0001/` holds `.attempts`, `.deferred`, `.retry-after` and `.wip-conflict`, **no `.done`**, and it sorts first. **So the one directory whose work is finished is the one directory that keeps being dispatched.** This run took no marker, because writing `.done` or `.retired` is phase selection and `PHASE_SYSTEM.md` line 216 bars a writing phase from it. **The fix is a controller decision and this item does not make it.**

**The standing this produces: a review debt is discharged by a document, a prompt stays live until its directory is retired, and nothing in this repository joins the two.** Ten dispatches on one range of ten chapters is the cost. **Nine of them were spent on work already finished, and the ninth found nothing, and this tenth found a real defect — so the runs were not wasted, but they were never aimed.**

---

## Section two — the prose defect no pass on this range has reported

**`chapter-0227.md:59` carries a person-shift inside one speech turn: the speaker answers a question put to him in the second person, then refers to himself in the third, mid-sentence.**

The question is Nell Kest's at `chapter-0227.md:55`: *"**Are you the most dangerous person in this matter,**"*. The answer is `chapter-0227.md:59`, and its pronouns run:

| sentence | person |
|---|---|
| *"There is nobody who can protect **me**"* | first |
| *"There is nothing anybody can instruct **me** about, nothing anybody can pay **me** for, and nothing anybody can thank **me** for."* | first ×3 |
| *"**That is why he** is the most dangerous person in this matter and it is also the reason nobody in it can stand in front of **him**."* | **third ×2** |
| *"**A person** nobody can pay cannot be bought… **A person** nobody can thank cannot be repaid."* | generic |
| *"…and **I** have heard all three of those said out loud…"* | first |

The third sentence is the defect. **"That is why"** reaches back at three clauses naming *me*; the subject it introduces is *he*; the next sentence reverts to a generic *A person*. No second speaker, no intervening paragraph, no cue. **A reader who takes *he* at face value has been told, in one breath, that Marek Kest is not the person who cannot be paid, thanked or instructed — in a chapter whose finding at `:73` is that he is.**

**And the clause is not his, which is what settles carry-across against voice.** Method:

```
grep -rn "most dangerous person in this matter" chapters/volume-05/
grep -rc "he is the most dangerous person in this matter" \
  chapters/volume-05/chapter-0215.md chapters/volume-05/chapter-0227.md
```

```
chapters/volume-05/chapter-0207.md
chapters/volume-05/chapter-0215.md
chapters/volume-05/chapter-0227.md
chapters/volume-05/chapter-0235.md
chapters/volume-05/chapter-0246.md
1        # chapter-0215.md
1        # chapter-0227.md
```

**Exactly two instances of the clause `he is the most dangerous person in this matter` exist in the whole of Volume 05, and those are them.** The first is `chapter-0215.md:85`, and it is correct:

> *"That is not a number and I will say it," said **Tamsin Rook**. "**There is nothing anybody can instruct him about, and nothing anybody can pay him for, and nothing anybody can thank him for, and that is the reason he is the most dangerous person in this matter and it is also the reason nobody in it can protect him.**"*

Tamsin Rook is speaking **about** Marek Kest; *him* and *he* are right and are sustained across both halves. The second is `chapter-0227.md:59`, where Marek Kest is speaking **about himself**, and there the first half was converted to *me* and the middle was not.

**The signature is that one half was edited and the other was not, and both halves show it:**

| | `chapter-0215.md:85` | `chapter-0227.md:59` |
|---|---|---|
| first half | *nothing anybody can instruct **him** about…* | *nothing anybody can instruct **me** about…* — **relativised** |
| second half | *…the reason **he** is the most dangerous person in this matter* | *…**why he** is the most dangerous person in this matter* — **not relativised** |
| closing clause | *nobody in it can **protect him*** | *nobody in it can **stand in front of him*** — **rewritten** |

The closing clause was rewritten, so 0227 is not a mechanical quotation of 0215: it is a revision in which the opening was correctly converted to the speaker and the middle was missed. **That is why nine passes did not see it. The two lines share no long verbatim run, and this repository's `lifts`, `reprints` and `sweeps` are blind to a clause by construction.** A vocabulary sweep finds the phrase; a reader has to decide who *he* is.

**It is charged, on this volume's own rule and not on a general preference.** The manuscript turns on the difference between a person and a document, an office, a seat and a name, and it has spent twelve volumes insisting that a thing said about persons must say *which* — `chapter-0227.md:7` itself, *"a person who is not from the office that cannot be named has to be present."* A third-person self-reference could in principle be deliberate: a man making himself a category. **It is not, here, for three reasons all on the page. One:** every other deliberate register-shift in this manuscript is *signalled* — `chapter-0227.md:21` drops into a list, `chapter-0212.md:119` announces its comparison — and this one carries no signal. **Two:** *he* cannot be the generic, because the very next sentence supplies *A person* as the generic; a generic would have read *a person*. **Three:** the same proposition, in the same volume, is delivered in the third person **by somebody else**, which establishes the clause as Tamsin Rook's possession and not as a line Marek Kest owns.

**Reported, not fixed.** Volume 05 is closed, this run holds no delete or substitute authority, and a review that edits the prose it reads cannot be cited as a reading. **The citation resolves:** `git diff --numstat 18e57c8 -- chapters/volume-05/chapter-0227.md` returns nothing.

---

## Section three — the eight defects already located, all re-seen and none re-charged

Nine passes located eight prose defects here. **This run read all ten chapters end to end, saw every one still standing, and charges none a second time.**

| # | Location | Defect | First reported by |
|---|---|---|---|
| 1 | `chapter-0226.md:7` | *which is how they are when **she am** doing them properly* — subject–verb | paid review, item 268 |
| 2 | `chapter-0226.md:49-50` | two consecutive `---` | paid review |
| 3 | `chapter-0229.md:19-20` | two consecutive `---` | paid review |
| 4 | `chapter-0221.md:57` | `" Then what is in the building."` — space inside the opening quote | paid review |
| 5 | `chapter-0228.md:108-109` | two consecutive blank lines before a `---` | verification, item 279 |
| 6 | `chapter-0225.md:132` against `:134` | *written **eleven** times* and *I have now done this for the **thirteenth** time*, two lines apart | third audit, item 283 |
| 7 | `chapter-0227.md:5` | *She was in the room **in** a rented room* — doubled locative | third audit |
| 8 | `chapter-0226.md:60` | *since **the first week of the fourth month of last year*** — knowledge 317 days before the fact | fourth audit, item 290 |
| **9** | **`chapter-0227.md:59`** | **person-shift — section two** | **this pass** |

Method for the three structural faults, the only ones an instrument can see, and for the leading space — all Python over the line list, `L[i].strip()=="---" and L[i+1].strip()=="---"`, `L[i].strip()=="" and L[i+1].strip()==""`, and `re.match(r'^"\s', L[i])`.

**One instrument note, because the fault is in the comfortable direction.** The obvious test for defect 4 — `grep -n '"[[:space:]][[:alpha:]]'` — returns **133 lines** on the ten files, because it matches every *closing* quote followed by `, said`. It finds the real hit at `chapter-0221.md:57` and buries it. **Only `re.match(r'^"\s', line)` isolates a space inside an opening quotation, and a test returning 133 hits where one is wanted is not a weak test — it is a test that has been passed off as a clearance by any run that reported its raw count.**

---

## Section four — the record claims that hold, each measured, each with its method beside it

Every figure re-derived on this tree. **None inherited from any of the five prior files.**

| Figure | Result | Method, printed |
|---|---|---|
| Base, ten of ten | **`18e57c8` holds all ten, non-empty**: 14465, 13200, 12889, 14056, 14323, 14960, 13221, 13046, 13878, 14020 bytes | `git show 18e57c8:chapters/volume-05/chapter-0N.md \| wc -c` per file |
| Working tree against that base | **empty for all ten** — `git diff --numstat 18e57c8 -- chapters/volume-05/` prints only 0231–0250 | `git diff --numstat` |
| Prose-repair commits on Volume 05 | **none** | `git log --oneline --grep="prose-repair" -- chapters/volume-05/` |
| **`about nine`, raw minus `about nine hundred`** | **5, 7, 4, 5, 6, 6, 6, 3, 6, 8 — range 3 to 8, median 6.0, total 56**, against the card's 72 | per file: `grep -o -i "about nine\b" <f> \| wc -l` less `grep -o -i "about nine hundred" <f> \| wc -l`. **Raw is 74 and `about nine hundred` is 18 of it — `0221` 9→5, `0228` 7→3, both confirmed** |
| **Calendar lock** | **holds — 13 raw hits on 12 lines, every one the modal verb; capital `May` 0; the other eleven month names 0; all seven weekday names 0.** Lines: `0222:73` ×2, `0222:125`, `0223:23`, `0223:105`, `0224:35`, `0225:37`, `0225:45`, `0228:15`, `0228:91`, `0228:99`, `0229:13`, `0229:70` | Python `re.finditer` over all nineteen names on an explicit ten-file list, each hit printed with 55 characters either side and **read**, not matched |
| `wc -w`, per file | **3011, 2758, 2714, 2956, 3018, 3164, 2763, 2754, 2919, 2975 = 29,032** | `wc -w` over an explicit ten-file list |
| The count of things asked out loud | **four in every chapter of the range that states it** — `0221:105`, `0222:81`/`:135`, `0223:121`, `0224:111`, `0225:45`/`:144`, `0226:134`/`:138`, `0228:114`/`:116`, `0229:134`, `0230:99` — **and no chapter makes it five** | read in place; `grep -rn "count is five\|is five,"` over the ten returns nothing |
| `exception` / `precedent` | **0 / 0** | `grep -o -i -w` over the ten |
| `certif` | **2**, at `0223:5` and `0227:21`, both *nothing in this empire he could **certify** anything with*. **No certification is granted and none is held** | `grep -o -i certif`. **The word-boundary form `-w` returns 0 and is the wrong instrument; it will not match *certify*** |
| Nobody thanked | **holds — 19 lines, every one a negation or an explicit refusal**: `0222:101`, `0223:95`, `0224:63`, `0224:75`, `0225:45`, `0225:75`, `0226:25`, `0226:31`, `0226:82`, `0227:59`, `0227:97`, `0227:107`, `0227:113`, `0228:71`, `0228:114`, `0229:96`, `0229:130`, `0230:73`, `0230:101` | read line by line. **Note `0227:59` is on the list — the same line as this pass's defect, and it reads *nothing anybody can thank me for*, which is a negation and is correct** |
| Lowcross bill | **holds** — *nineteen pounds three and fourpence*, unpaid, nobody liable: `0229:15`, `0229:128`, `0230:91` | read |
| The guarantee | **holds** — *about four hundred and forty foot* of bank, *about sixty children under sixteen* inside it, offered and unanswered: `0229:130`, `0230:15`, `0230:101`. The word occurs 6 times across 2 chapters (`0229:130`; `0230:11`, `:15`, `:25`, `:73`, `:101`) and **no child is named** | read |
| The reader of seventeen | **holds** — unnamed, unthanked, not going to start, **no rate and no elapsed period printed**: `0229:96` (*at the rate the list is set at*), `0230:73` (*on the same rate as everybody else on the list*) | read at both lines |
| Distances | **`four hundred and thirty` 14 and `four hundred miles` 0** on the ten; **134 and 0** across Volume 05's fifty chapters | `grep -o` over an explicit ten-file list and over `chapters/volume-05/chapter-*.md`. **Both of the prompt's figures reproduce; the short form is absent, so the Volume 03 and Volume 04 inconsistency is not repeated here** |
| `measure.py words --volume 05` | **144,248** | run on this tree |
| `measure.py words` | **1,496,525 in 620 files** | run on this tree |
| `measure.py selftest` | **PASS** | run on this tree |

---

## Section five — three claims that do not bear out, and every one of them is in this run's own prompt

**The prompt is the record under test this time**, on its own instruction: *No figure in this prompt is a figure of record. Every one is to be re-derived by your own run.* **All three faults run in the same direction — the prompt undercounts a homograph.**

1. **The prompt's `may` census is short by five.** It prints *eight raw hits, all `may`* and names `0222:73`, `0223:23`, `0225:37`, `0225:45`, `0228:15`, `0228:91`, `0228:99`, `0229:13`. **The page carries 13**; the five omitted are `0222:125`, `0223:105`, `0224:35`, `0229:70`, and a second occurrence on `0222:73`. `reviews/volume-05-batch-0004.md` already recorded this thirteen against the same eight, so the correction is not new — **what is new is that the same prompt's whole-volume figure is wrong too, and by more.**
2. **The prompt's whole-volume `may` census reproduces under no reading at all.** It prints *Across the whole of Volume 05 the same naive run returns twenty-seven raw hits*. **Volume 05 returns 46 occurrences on 40 lines** across its fifty chapters — `ls chapters/volume-05/chapter-*.md \| wc -l` = 50, Python scan over all fifty. **Not 46 occurrences, not 40 lines, and not the 33 left after this batch's own thirteen, is 27.** A prompt figure that fails all three counts it could be is not a figure of record and should not have been printed as one.
3. **The prompt's missing-base warning does not fire on this tree and should be corrected rather than left to mislead.** It states *`git show 9ae089f:chapters/volume-05/chapter-0221.md` will exit 128 and every structural counter piped from it will come back exactly zero*. **Measured: `git cat-file -e 9ae089f:chapters/volume-05/chapter-0221.md` returns PRESENT**, and `git diff --numstat 9ae089f 18e57c8 --` over the ten returns **empty**, so the two commits hold byte-identical content here and `9ae089f` is as usable as `18e57c8`. **The item 265E hazard is real and general; it is not present on this range.** The correct instruction is the one this run followed: *assert the base by content, per file, and not by `git cat-file -e` alone.*

**Two figures this prompt inherits that belong to a wider range, recorded because the prompt prints them as settled.** **`thirty-one of Mosswake` is *a figure in three places*: `grep -rlo 'thirty-one of Mosswake' chapters/` returns six files** — `chapter-0150.md`, `0180`, `0190`, `0200`, `0206`, `0217` — **and my range carries zero.** This reproduces item 284C's open marginal exactly and is not re-litigated here. **And the count of things asked out loud going from four to five once, in `chapter-0250.md:125`, is confirmed still to be outside this range**, which prints four in ten places and five in none.

---

## Section six — the standing this pass produces

**A quotation carried across speakers must be relativised in every pronoun, and a revision that rewrites the *end* of a sentence while converting its *beginning* is precisely the edit in which the middle is missed.** `chapter-0215.md:85` → `chapter-0227.md:59` is the worked instance. Its diagnostic is general and cheap: **find a clause that occurs in two chapters of the volume, establish who owns it in each, and check whether the owners differ.** That is one `grep -c` and one read. It is absent from this repository's instrument set because a shared clause reads as evidence of *repetition*, which every tool here hunts, and never as evidence of a *referent*, which is the thing that broke.

**The class item 283 named now has five instances in one range of ten chapters, and not one is a repetition.** Item 266B: figures contradicting canon elsewhere. Item 279B: an elapsed span contradicting a date line elsewhere. Item 283: a count contradicting a count two lines apart. Item 290: a year-term contradicting a date line in its own chapter. **This pass: a clause contradicting its own referent across two chapters.** Four are invisible because the two statements share no string. **The fifth shares one and was still missed nine times, because the string is correct in one file and wrong in the other, and no instrument in this repository reads a word's referent.**

**And on the ladder: two owed reviews remain, not three, and both already have correct live prompts.** Volume 05's Batch 0005 at `workspace/review-debt-0003/PROMPT.md` is the next. **What is owed to neither is a controller decision on the ladder, and no writing phase may take it.**

---

## Section seven — what this pass could not do, and hands on

**It wrote no prose.** Volume 05 is closed. No chapter was opened for edit — not `chapter-0227.md`, not `chapter-0221.md`, not `chapter-0250.md`, not `chapter-0620.md`. No review was rewritten or amended. No outline was opened for edit, including `outline/batches/volume-05-batch-0003.md`. `state/complete.md` was not written. `state/phase-ledger.json` was not edited. No volume was planned and there is no Volume 13. `tools/measure.py` was run and not changed.

**The nine prose defects need authority no prompt in this repository grants.** Against base `18e57c8`: one subject–verb agreement, two doubled section rules, one doubled blank line, one leading space, two count disagreements, one doubled locative, one year-term, one person-shift. **A phase given that authority does not have to re-find any of them.**

**Batch 0005's base, resolved and asserted here for the next phase, though it is not this phase's to use.** `git log --oneline -1 -- chapters/volume-05/chapter-023[1-9].md chapters/volume-05/chapter-0240.md` returns **`65abf1d`** (*save review fixes batch-0004*); `git show 65abf1d:chapters/volume-05/chapter-0N.md | wc -c` returns 13898, 13582, 12949, 13678, 13753, 13246, 13252, 13415, 11874, 13163 — **ten of ten non-empty**, item 265E's check; `git diff --numstat 65abf1d --` over those ten returns empty. For Batch 0005 the base is **`dedc831`** by the same command.

**One lead handed on, and it is three chapters wide where the prompt hands it forward as one.** The prompt's lead is `chapter-0250.md` at 1. **A full per-chapter sweep of all fifty chapters of Volume 05, raw minus `about nine hundred`, reads:**

```
4 2 6 4 5 4 3 4 7 4 6 4 7 5 5 8 7 3 5 4 5 7 4 5 6 6 6 3 6 8 1 5 6 8 4 7 7 7 5 6 7 6 3 3 8 7 8 6 7 1
```

**Maximum 8, minimum 1, median 5.5, mean 5.3 — and not one chapter above eight, so the `about nine` lock holds across all fifty chapters of the volume and not only across this batch.** Three chapters sit at or under two: **`chapter-0231.md` at 1** (raw 3 less 2), **`chapter-0250.md` at 1** (raw 4 less 3), and **`chapter-0202.md` at 2** (raw 3 less 1). Item 290 named the first two; **this run names the third.** A reviewer of Batch 0005 who checks only the chapter the lead names will miss two.

**`chapter-0262.md:109` and the base defects at items 292 and 293 are not this range's and are untouched.**

**The frontier, as the tree stands.** Volume 05 Batch 0003: paid and audited five times over, this pass the sixth document and the eighth pass. Volume 05 Batch 0004: paid and audited four times. **Volume 05 Batch 0005 and Volume 06 Batch 0003: owed, unpaid, and both already correctly prompted on disk.**