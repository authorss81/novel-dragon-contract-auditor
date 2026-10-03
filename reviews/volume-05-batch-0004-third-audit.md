# THIRD AUDIT: THE PAID SECOND READING OF VOLUME 05, BATCH 0004, CHAPTERS 0231 TO 0240 — TWO PROSE FAULTS NO PASS REPORTED, AND THE HEADLINE FINDING SHRUNK FROM NINETEEN TOKENS TO SIX

**Who wrote this, and what it is not.** This is an audit of a review, not a second review and not a third reading claimed as independent. It was written by an agent that wrote no prose, and **nothing in this repository's review gate is independent** — the gate has fallen back to the writing agent every time it has been asked, `NOVEL_SPEC.md` and `state/open-threads.md` item 171 both say so in terms, and **no sentence in this file, and no sentence in either file it audits, may be cited as an independent finding.** What it has that a re-run of the two earlier passes' own scripts does not have is that all ten chapters were read end to end a fifth time, that every figure printed below was re-derived from the page rather than checked against the files that printed it, and that one of the paid review's two prose findings was re-measured by **residual subtraction** rather than by similarity — which is the one method in this file that a run using `SequenceMatcher` alone cannot reach, and which changed the finding.

**Why this file exists, and why it is not `volume-05-batch-0004.md` and not `volume-05-batch-0004-verification.md`.** Both are on disk. `reviews/volume-05-batch-0004.md` is at commit **`5316a4f`**, *review: the owed second reading of Volume 05 Batch 0004, chapters 0231 to 0240*, recorded PAID at **item 270A**. `reviews/volume-05-batch-0004-verification.md` is at **`5716598`**, recorded at **item 276**. **This run was handed the prompt for that same review — `workspace/review-debt-0002/PROMPT.md`, which does not exist — and found the work done twice over.** It is the **fourth** duplicate dispatch in this repository's record (items 275, 276, 277, this one) and the **fifth** pass over the page. **Per item 275A's standing, followed here as at item 276A and item 277A: it wrote no second review, amended no paid file, amended no earlier verification, and marked no prompt**, on `PHASE_SYSTEM.md` line 216, and a phase that marks its own directory has certified itself. **A second reading that overwrites the first reading is not a reading; a third that reprints it is a third copy of a claim.**

**What this phase did not do, and it is the important half.** It opened no chapter for edit. Volume 05 is a closed volume, every prose finding below is in text only a phase with delete or substitute authority can touch, and **this run had none and did not take any.** It edited no outline, so the record defects in `outline/batches/volume-05-batch-0004.md` are reported and not repaired. It planned no volume, opened no `outline/ending.md`, added no Volume 13, repaired no prose, wrote no `state/complete.md`, edited no controller file, **and created no prompt**, for the reason in section five. `tools/measure.py` is an instrument and was not changed.

**The base, resolved and asserted before a single figure was taken from it.** `git log --oneline -1 -- chapters/volume-05/chapter-023[1-9].md chapters/volume-05/chapter-0240.md` returns **`65abf1d`**, *novel: save review fixes batch-0004*, which is the base this run's prompt expected. `git diff --numstat 65abf1d -- chapters/volume-05/` returns **nothing for these ten files** and **1,224 insertions across `chapter-0241.md` to `chapter-0250.md`** — the trap item 203 names, read from the wrong end: a reader who runs the volume-wide command sees output and concludes the volume has moved, and the ten files this audit owns have not moved by a line. **The ten were asserted non-empty at that commit before any measurement**, on item 265E's rule that a silent 0 from a `git show` piped into a counter is a missing base and not a measurement: `git show 65abf1d:chapters/volume-05/chapter-<each of the ten> | wc -c` returns **13898, 13582, 12949, 13678, 13753, 13246, 13252, 13415, 11874 and 13163 bytes, ten out of ten**. `git log --oneline --grep="prose-repair" -- chapters/volume-05/` returns **nothing**, so Volume 05 has never been through the prose repair — with the caveat both earlier files print, that `65abf1d` is a *review fixes* commit that **did** edit prose in all ten files, **so every line number below is the tree's line number and is a citation of a text and not of a position.**

---

## Section one — both earlier passes hold, and this run confirms them against the page

Stated first, because a verification that opens with its disagreements is a review wearing a hat. **`reviews/volume-05-batch-0004.md` and `reviews/volume-05-batch-0004-verification.md` are sound, and every figure either of them printed that this run re-derived reproduced exactly — with five exceptions, four of which the verification found itself and one of which is new.**

| Claim, from whichever file printed it | Reproduces | Command run here |
|---|---|---|
| `about nine`, card's own method, raw minus `about nine hundred` | **1, 5, 6, 8, 4, 7, 7, 7, 5, 6 = 56** against the card's 60; **five of ten cells wrong** | `re.findall(r"\babout nine\b", t, re.I)` less `re.findall(r"\babout nine hundred\b", t, re.I)`, per file |
| Batch word total and per-file list | **2911 / 2856 / 2736 / 2906 / 2910 / 2836 / 2810 / 2844 / 2521 / 2788 = 28,118**, `chapter-0240.md` at **2,788** and not the card's 2,791 | `m.words_in_file` per file |
| Question marks | **1, 3, 3, 2, 1, 4, 3, 4, 8, 1 = 30**, card item 42's distribution to the digit | `T[p].count("?")` per file |
| Whole-word `may` | **5 hits on 5 lines in 4 chapters**, every one read in place the modal verb — `0231:126`, `0232:99`, `0234:51`, `0238:37`, `0238:71`. Month and weekday names **0 and 0** | `grep -n -i "\bmay\b"`; `grep -on -iE "\b(january\|…\|sunday)\b"` |
| Distances | `four hundred and thirty` **47**, `four hundred miles` **0**, `four hundred and forty` **6** | `grep -o -i` per string |
| Sentence hard bound | longest **90 whitespace-words at `chapter-0232.md:118`**, **1** at ninety or over, **0** at a hundred | per-paragraph, `m.SPLIT` |
| `the book` | **six** standalone singular, **two** plural, **three** compounds at `0233:31`, `:107`, `:111` (two capitalised), **raw 11**; all six singular are objects in a room or a building, manuscript sense zero | `grep -on -iE "\bthe book"` read line by line |
| Locked absences | `exception` **0**, `precedent` **0**, `Mosswake` **0**, `thirty-one` **0**, `fourteen months` **0**, `Venn` **0**, `schedule` **0**, `ruling` **0**, `Ashfall` **0** | per-term `grep -o -i` |
| Standing locks that hold | Lowcross bill **4** mentions at nineteen pounds three and fourpence, unpaid, nobody liable; guarantee **4** mentions, word for word, none answered; `certif` **2** and both negative (`0234:5`, `0236:80`); **the count of askings is four in every chapter that prints it** — `0231:136`, `0234:121`, `0235:105` (*Four in about a hundred and forty years*), `0237:111`, `0239:123`, `0240:97` — and **no chapter of this range makes it five**; the reader of seventeen unnamed, unthanked, unsent anybody | read, plus `grep -n -o -E` per string |
| Card item 41 frames | *there is no form anywhere in this empire* **15**, *there is no form in this empire* **9**; the two frames the card lists **once** return **0**; the bare tail **25** against the card's *sixteen* | `grep -o -i` per frame |
| Card item 45, protagonist on the page | **nine** of ten; `chapter-0238.md` is the miss | `grep -l -E "Kest\|no office and no fund\|man with no office\|thirty-eight with no office"` |
| Five doubled blank lines | `0232:116,117`; `0236:103,104`; `0238:128,129`; **`0239:112,113` then `---` at `:114`**; `0239:119,120`. Consecutive `---` **0** | line-by-line scan, `prev=="" and $0==""` |
| `thank` | **15 lines**, **20 occurrences across 8 files**, every line a negation or a refusal, the single actual thank `0236:82` from **a man of about forty** | `grep -n -i "thank" \| wc -l`; `grep -io` |
| `about four words` at `0234.md:59` | referent **15 tokens** for the first clause, **16** for the second | `m.TOKEN.findall` |

**One figure this run checked and withdrew, and it is recorded so a fourth pass does not re-raise it.** The paid review prints that at `chapter-0234.md:59` "both clauses together are 32." `m.TOKEN` gives **15** and **16** for the two clauses, which is 31 — and **32 is reachable**, being 15 + 16 + the `and` that joins them in the sentence as written. **A figure is only a fault where no plausible reading reaches it, and this one is reached.** Not reported.

---

## Section two — TWO PROSE FAULTS THAT NO PASS REPORTED, both located, both needing authority this run does not have

### One. `chapter-0239.md:49` gives the same interval as "the better part of a week" against nine days on eight lines of the same chapter

> **chapter-0239.md:5**, narration: *"It is the ninth day since."*
> **:11**: *"He had spent nine days on it."*
> **:39**, in Rennick Adley's mouth: *"The other half is that nine days ago neither of us knew it was going to be read out… You have had nine days and she had about four hours."*
> **:43**: *"he had it ready and it had been ready for about nine days."*
> **:95**, Adley again: *"she did it out loud, on purpose, nine days ago."*
> **:99**: *"he has been carrying it for nine days."*
> **:103**: *"Nine days ago a foreman took it apart out loud in about four minutes."*
> **:123**, the closing line: *"and the ninth day is not finished."*
> **:49**, in the man's own mouth, in the middle of the store: *"**I have been findable by a reason of my own for the better part of a week** and it is the first thing that has ever been found about me that I did not hand over…"*

```
grep -n -E "nine day|ninth day|better part of a week" chapters/volume-05/chapter-0239.md
```
returns **nine** lines: **eight carrying nine days and one carrying "the better part of a week."**

**The arithmetic, printed.** *The better part of a week* is at most six days and at least four. **Nine days is greater than seven, so no reading of the phrase reaches nine.** The two cannot both be true of one interval on one page, and the fault is item 283C's class exactly: **a figure against its own neighbour**, which no duplicate scan, no lift index, no construction list, no re-print window and no calendar parse in this repository can see, because the two claims share no run with each other.

**And here is the part worth a paragraph, because it changes which side of item 276C is wrong.** Item 276C found `chapter-0239.md` asserting nine days on seven lines against two of its own dates that are five days apart on the seven-day week `chapter-0237.md:9` and `:95` establish, reconciling only on a thirty-two-day month Volume 05 nowhere states, and it reported that as a contradiction it could not close. **This line is the tie-breaker and it goes against the nine.** Five days *is* "the better part of a week"; nine days is not. **So the page carries eight assertions of nine against one of about five, and the single minority reading is the one the chapter's own calendar arithmetic produces.** That is the same direction as the verification's own card finding at item 276D, where two of three gaps the card calls a week are not a week — **a record in this batch has now been caught rounding one interval two different ways inside a single chapter, and the direction is the same as the card's: the recorded figure is the larger one.**

**It cannot be fixed here.** A substitution in a closed volume needs delete or substitute authority, which this run does not have. **Reported with its line numbers and left.**

### Two. `chapter-0240.md:25` and `:45` print "about nineteen weeks" and no month length reaches it

> **chapter-0240.md:3**, the chapter's own day: *"it was about the fifth hour of the morning on **the fourth day of the fourth week of the eighth month of the year after next**"* — confirmed at `:73` and `:97`, which both say the last day of that same fourth week.
> **:25**, narration: *"He had written that in **the third week of the third month of the year after next** and it is the reason for everything he was about to do and also **the reason he had not done it in about nineteen weeks**."*
> **:45**, in his own mouth: *"It is the only honest thing in there and it is the eleventh line … and **that took nineteen weeks** and this morning and about four seconds of pencil."*

The batch states its own week convention in the only place it can be read off: `chapter-0237.md:9` dates the discovery *"on the fourth day of the third week of the seventh month"* and `chapter-0237.md:95` dates the weigh-house's word *"on the fourth day of the fourth week of the seventh month"* — **fourth day to fourth day, third week to fourth week, which is one week.** So weeks are seven days numbered from day one of a month, and the fourth day of the fourth week is **day 25** whatever the month is, and the third week is **days 15 to 21**.

Taking the start as late as the sentence allows — the last day of the third week of the third month — and counting whole intervening months:

| Length of months 4 to 7 | Shortest possible gap | In weeks |
|---|---|---|
| 28 (four weeks exactly) | (28 − 21) + 4×28 + 25 = **144 days** | **20.57** |
| 29 | (29 − 21) + 4×29 + 25 = **149 days** | **21.29** |
| 30 | (30 − 21) + 4×30 + 25 = **154 days** | **22.00** |
| 31 | (31 − 21) + 4×31 + 25 = **159 days** | **22.71** |

**Nineteen weeks is 133 days.** Solving `(L − 21) + 4L + 25 = 133` gives **L ≈ 25.8 — a month of about twenty-six days.** **No calendar in the world has that, and Volume 05 states no month length at all**, so this is the same position item 276C reached: *the contradiction cannot be closed from the page.* **The difference is that here it cannot be closed by any month length, where the nine-day fault could be closed by a thirty-two-day month.** Nineteen weeks is wrong at 28, 29, 30 and 31 days alike.

**And the other reading of "that" is worse, so the finding does not depend on which antecedent is meant.** If `:45`'s *"that took nineteen weeks"* measures from the **eleventh line**, which `:45` dates in the same sentence to *"the fourth week of the ninth month of the year after"* — a year earlier than the chapter's own day — the gap is **311 days at 28-day months, which is 44.4 weeks.** So: **twenty-one weeks under the reading that favours the figure, forty-four under the other, and nineteen printed twice.**

**Why every instrument missed it, and this is the standing.** `python3 tools/measure.py calendar --volume 05` returns **"files read: 50; chapters with a parsed date line: 1"** and lists the other forty-nine as `no date line` — item 276C's instrument fault, re-derived on this tree, so **the instrument built for the calendar parses one chapter in fifty of the one volume whose spine is counted days and weeks.** `DATE_LINE` admits only `It is the` and `The date is the`, and `chapter-0240.md:3` opens *"He is in the same room"*. **This is item 170's standing — *this project measures sentence length, emphasis, word counts and lifted phrases, and has never once measured an interval against a calendar* — for the second time in this batch, and the two faults it has now produced are in the two chapters the instrument skipped.**

---

## Section three — a fifth figure in the paid review that does not reproduce, and it is a citation that does not resolve

The verification at item 276B found four figures in the paid review that do not reproduce and that all run upward. **This run found a fifth, of a class the other four are not.**

Section three of the paid review's cleared table reads: *"The count of askings is four and did not move (card item 1, standing lock) — **holds** — the count printed at 0231:136, 0234:121, 0235:105, 0237:111, **0239:121**, 0240:97."*

```
sed -n '121p' chapters/volume-05/chapter-0239.md
```
> *And about four hundred and thirty miles down this river there is a man of thirty-eight with no office and no fund, and the only person in this matter anybody can go looking for and come back from with nothing…*

**That line carries no count of anything.** The count is printed **two lines later**, at `chapter-0239.md:123` — *"There are four people in this empire who have asked a person out loud what a word on a form means, the third of the four was the first one anybody did on purpose, and the count has not moved…"* — and the five other locations are exact, `0235:105` defensibly so since it reads *Four in about a hundred and forty years*.

**The lock is unaffected and the row is not.** The count is four in all six places it is printed, and no chapter of this range makes it five. **What is wrong is a citation in a table whose purpose is to certify a clearance.** Item 276B's standing was that *a row asserting a count is a measurement claim whether it sits in an outline or in a review*; **this is the same thing one step further out, because a row asserting a line number is a claim about where something is, and it is the row's own method to name a line.** The other four errors were counts that were high. **This one is a location that is wrong, and a location is the one thing in this repository's state layer that other phases cite without re-deriving it** — which is why it is reported even though nothing about the lock moves.

**Taken with item 276B, five figures in the paid review do not reproduce, and the pattern is now five for five in one direction** — `thank` at 15 against a printed 19, a `fifth` enumeration describing 23 in a sentence claiming 20, seven chapters named against a stated eight, a guarantee cited at a line that does not contain the word, and now a count cited at a line that does not contain it. **72 against 56, 60 against 56, 19 against 15, and now a wrong line — four records in two batches of one volume, and every one of them high or wrong, and none of the five in the same direction as the work rather than against it.**

---

## Section four — THE CORRECTION, and it is to the paid review's headline finding, and it makes the finding smaller and sharper

The paid review's finding one is the batch's best prose finding and it stands. **It is also measured wrong, and measured by the one method in this file that changes the answer.**

The paid review reports, on `difflib.SequenceMatcher(None, A, B, autojunk=False)` over `m.TOKEN.findall(line)`, a **19-token** longest shared run between `chapter-0238.md:125` and `chapter-0236.md:102`, an **18-token** run against its own `chapter-0238.md:65`, and a **13-token** run between `:102` and `:65`, and concludes that `:125` *"re-performs a sentence the same chapter's point of view has already said, verbatim from `I have watched` onward"* **and** that the sentence *"is lifted across four hundred and thirty miles and a change of person."*

**Both runs reproduce. The conclusion drawn from the 19 does not follow from it.** Run the same comparison as a **difference** rather than a similarity — the opcodes, printing every non-`equal` block:

> **`chapter-0238.md:125` against `chapter-0238.md:65` — one operation, and it is an insertion:**
> `insert 'in my time in these bays'`
> *(everything else is a `replace` of this chapter's own words: `Nineteen reasons in a column` → `And he did not ask`; `nine men in a bay` → `that`; `starts being` → `is`; and one `delete` of `I am not going to be the one that puts it over about forty-one people`.)*

> **`chapter-0238.md:125` against `chapter-0236.md:102` — six operations, all `replace` or `delete`, and no insertion.**

**So `:125` is `:65` with a six-token phrase put into it, and that phrase is the whole of the cross-chapter fault.** The 19-token run is an artefact: `:65` and `:102` *already* shared 13 tokens before `:125` existed — both end in *"and every single one of them ended up with a heading over it"* — so a longest-run measure over `:102`×`:125` necessarily returns those 13 plus the 6 inserted ones, **and reports a nineteen-token lift where the actual transplant is six tokens.**

**And the eighteen-token intra-chapter echo is not a defect at all. It is this batch's house device, and it has four other instances.** Taking every pair of lines in the batch, one opening with a quotation mark and one not, and printing every shared run of twelve tokens or more:

| Pair | Run | What it is |
|---|---|---|
| `0232:47` → `0232:122` | **19** | speech, then the closing roll-call restating it — *heard it and did not ask and did not write it down and it cannot be got back* |
| `0236:5` → `0236:96` | **19** | narration, then her own mouth — *person who is safe because nobody can instruct her and useful because somebody needs her standing in a room* |
| `0238:37` → `0238:71` | **16** | speech, then narration — *and there is no form anywhere in this empire that says a man may not say* |
| **`0238:65` → `0238:125`** | **18** | **the one charged** |
| `0232:17` → `0232:105` | **12** | speech, then the roll-call — *a piece of paper with a name at the foot of it* |

**Five instances, twelve to nineteen tokens, all inside one chapter, all a restatement and not a transplantation.** A chapter that restates a line in a different voice later is doing what four other chapters in the same ten do. **The echo is not the fault and the paid review is right that the narration at `:125` is the weaker of the two** — it adds *and it is a habit* and a clause about the arrangement — **but that is a judgement about a device the batch uses five times, and charging it as a defect charges the device.**

**What is left after the echo is subtracted is one fault, and it is a fault of a kind no pass in this batch has named: a character's idiolect, carried into another character's chapter, in a first person that is not hers.**

> **chapter-0223.md:83**, Tamsin Rook, at the counter in Auremar: *"**…and I have watched about nine people make a thing out of a habit in my time in these bays and every single one of them ended up with a heading over it.**"*
> **chapter-0236.md:102**, Tamsin Rook, at the same counter: *"**About nine people in this city have made a thing out of a habit in my time in these bays and every single one of them ended up with a heading over it**…"*
> **chapter-0238.md:125**, narration, in Halla Wray's chapter, on the Slade bank: *"…I have watched about nine people in this empire make a habit into a thing **in my time in these bays** and every single one of them ended up with a heading over it."*

**"These bays" are the four bays of the Notaries' Table in Auremar** — `chapter-0236.md:3` — **and the phrase is hers at both of its other two occurrences, twenty-two chapters and two chapters apart.** `grep -rc "in my time in these" chapters/volume-05/` returns it in **exactly three files: `0223`, `0236`, `0238`**, and it belongs to the woman at the counter in two of them. **At `:125` it stands in a chapter whose bay is a bay on a different bank four hundred yards from a hired stone store, in a sentence about a man on that bank, in a first person that belongs to neither Halla Wray nor the narration around it.**

**So the finding is: not a nineteen-token duplication, but a six-token voice transplant, and it is measurable as the residual of two similarity measures rather than as either of them.** The paid review's charge and its consequence are right — it needs substitute authority in a closed volume and it is left — **and its size is wrong by a factor of three, and the thing that makes it wrong is the very coincidence of wording that made `:65` and `:102` look like a pair.** A repair that fixed this by replacing nineteen tokens would have rewritten a house device.

**And this bears directly on the question the paid review left open at its section five and did not answer**, which is whether first-person interior narration inside a third-person chapter is an unwritten house device of Volume 05 or a fault standing in five chapters. **It is a third question inside the same finding, and it is the sharper one: at `chapter-0238.md:125` the first person is not a point of view at all, it is a borrowed one**, which is a different defect from the one eight chapters of Volume 05 share, and it does not bear on that count. **The class the paid review measured is unchanged at eight chapters wide; the eighth instance is not one of them.**

---

## Section five — what this audit could not do, and hands on

**The two prose faults in section two need prose authority this run does not have.** Each is a substitution in a closed volume. **A review has no authority to make one, an audit less than a review, and this run made none.** They are written down with their line numbers so that a phase given the authority does not have to re-find them. **A line number in a file no phase has edited is a citation that resolves** — with the caveat both earlier files print, that `65abf1d` is a review-fixes commit that moved prose in all ten files, so these are the tree's line numbers and not the base's.

**The five figures in sections three and four are not repaired either, and cannot be.** They are in `reviews/volume-05-batch-0004.md`, which is a review and not an outline, and item 275A's standing — which this run is following, as items 276A and 277A did — is that a duplicate dispatch **does not amend a paid review.** The correction to finding one is the largest of them and it is **not** applied to the paid file. **It is recorded here and in the state layer and nowhere else, and that is the whole of what a phase without authority over a paid review can do about it.**

**One prompt this run was told to create and did not create.** `workspace/review-debt-0003/PROMPT.md` **already exists at 14,688 bytes**, for **Volume 05's Batch 0005, `chapter-0241.md` to `chapter-0250.md`**, base **`dedc831`** (*save review fixes batch-0005*), verified present here with `git cat-file -e dedc831:chapters/volume-05/chapter-0241.md` returning PRESENT. It is recorded at item 270E and it already carries the paid review's correction of the `about nine` lead and its instrument standing. **Writing it again would overwrite a live prompt with a duplicate of itself, which is item 275C's judgement and which this state layer has logged against prose-repair prompts eleven times: *writing the file this dispatch was told to write would have destroyed the prompt.*** And the prompt this run actually inherited is `workspace/review-debt-0002/PROMPT.md`, **which does not exist**, so the dispatch named a range that has been paid, verified and re-derived and left two prompts behind it. **No prompt was created.**

**The state of the frontier, and it is better than it was at item 276E.** All four reviews named at `outline/volume-12.md`'s close now stand accounted for: **Volume 04's Batch 0005 paid** at `reviews/volume-04-batch-0005.md`; **Volume 05's Batch 0003 paid and audited six times** (items 268, 275, 279, 280, 283, 284); **Volume 05's Batch 0004 paid and audited twice** (items 270A, 276, and this one at 285); **Volume 06's own Batch 0003 written as a prompt at `workspace/review-debt-0004/PROMPT.md`** (item 283F) **and still unpaid.** **Two owed reviews remain — Volume 05's Batch 0005 and Volume 06's Batch 0003 — and both now have a live prompt, which is a state neither of them was in at any earlier item.** **The review gate itself remains a controller-owned defect and is not among them** — item 171 records it, and **no review any phase writes may be described as independent until a controller owner changes it.**

**And the standing this audit produces, which is the standing its own method is for.**

**One. A similarity measure and a difference measure disagree about a fault's size, and only the difference measure can be used to repair it.** The paid review measured `:125` against `:102` and got 19; the opcodes say the cross-chapter transplant is **six tokens** and the rest of the run is pre-existing agreement between two lines that were already alike. **The cheapest consequence of this is that a duplication finding reported as a run length cannot be actioned: a repair that removed nineteen tokens would have destroyed a house device that five places in the batch use.** The extension, and it is cheap to run: **after a duplicate finding, subtract the two lines from each other and print what is left. If the residue is an insertion, the finding is about the insertion and not about the run.**

**Two. A repeated phrase is a character's, and the way to know whose is to count the chapters it appears in.** *In my time in these bays* occurs in three files of Volume 05 and belongs to the woman at the counter in two of them. **A phrase that recurs across a volume is not a motif of the volume until somebody checks whose mouth it is in each place, and a phrase in narration is the place a borrowed one is hardest to see** — because narration has no owner to be wrong about. This is the paid review's open question about first-person narration turned into a method, and it is the first finding in this range that is about **voice** rather than about a measurement.

**Three. A figure and the figure it contradicts can be in the same sentence, the same chapter, or the same paragraph, and the batch now has one of each.** Item 266B found figures contradicting canon figures in seven other files; item 279B found an elapsed span contradicting a date line in another chapter; item 283C found a count contradicting a count three lines apart. **This run adds an interval contradicting an interval eight lines apart in one chapter (`0239:49` against eight lines), and a figure that is unreachable from the chapter's own two dates under every month length (`0240:25`, `:45`).** Neither is visible to any instrument here, and **the second is invisible to `measure.py calendar` for the specific and checkable reason that the instrument parses 1 chapter of 50 in this volume** — so the class has now produced a finding on the one volume where the calendar instrument fails.

---

**What this file touched:** no chapter file, no outline, no `tools/measure.py`, no controller file. It read `outline/batches/volume-05-batch-0004.md` in full, `outline/volume-12.md`'s close, `reviews/volume-04-batch-0005.md`, `reviews/volume-05-batch-0003.md`, `reviews/volume-05-batch-0004.md` and `reviews/volume-05-batch-0004-verification.md`; it read `chapters/volume-05/chapter-0231.md` through `chapter-0240.md` end to end, a fifth time; it swept `chapter-0223.md` for the ownership of one phrase, which is the only figure of a file outside its range this audit prints; and it read `chapter-0250.md` not at all, item 270E's lead having been closed by item 270's section four and by items 276 and 277. **It amended nothing. It wrote `reviews/volume-05-batch-0004-third-audit.md` and not `reviews/volume-05-batch-0004.md`, because the second is paid at `5316a4f` and item 270A, and a second reading that overwrites the first reading is not a reading.** Its state record is item 285, and it created no prompt.
