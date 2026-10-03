# REVIEW: VOLUME 05, BATCH 0004, CHAPTERS 0231 TO 0240 — THE THIRD OF THE FOUR OWED REVIEWS

**Who wrote this, and what it is not.** This is a review of ten finished chapters in a closed volume. It was written by the same agent that wrote the state files this run, and **nothing in this repository's review gate is independent** — the gate has fallen back to the writing agent every time it has been asked, and `NOVEL_SPEC.md` and `state/open-threads.md` item 171 both say so in terms. **No sentence in this file may be cited as an independent finding.** What it has that a scan does not have is that all ten chapters were read end to end, and that every claim in `outline/batches/volume-05-batch-0004.md` tested here was tested against the page with the method printed beside the figure.

**Why this range.** `outline/volume-12.md`, at its close, names four owed reviews and says *which is four and not three*: one owed review of Volume 04's Batch 0005, and owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003. The first is paid at `reviews/volume-04-batch-0005.md` and the second at `reviews/volume-05-batch-0003.md`. This is the third. Volume 05 has never been through the prose repair — `git log --oneline --grep="prose-repair" -- chapters/volume-05/` returns nothing — and none of these ten files has been edited since `65abf1d` (*save review fixes batch-0004*), verified with `git log --oneline -1 -- chapters/volume-05/chapter-023[1-9].md chapters/volume-05/chapter-0240.md` returning `65abf1d` and `git cat-file -e 65abf1d:chapters/volume-05/chapter-<each of the ten>` returning PRESENT ten times out of ten, so **every line number below resolves**.

**The precheck, and the trap in it.** `git diff --numstat 65abf1d -- chapters/volume-05/` returns **nothing for these ten files** and **1,224 insertions and 0 deletions for `chapter-0241.md` to `chapter-0250.md`**. A reader who runs the volume-wide command and sees output concludes the volume has moved; the ten files this review owns have not moved by a line. That is item 203's standing read from the wrong end, and the same command run over the ten files alone returns nothing and is the one that settles it. **`65abf1d` is Batch 0004's base and is not Batch 0005's**, which is a fact the next owed review needs and which is recorded in its prompt.

**What this phase did not do, and it is the important half.** It opened no chapter for edit. Volume 05 is a closed volume, every prose finding below is in text only a phase with delete or substitute authority can touch, and **this run had none and did not take any.** It edited no outline, and `outline/batches/volume-05-batch-0004.md` is an outline file, so the eight record defects in section two are reported and not repaired. It planned no volume, opened no `outline/ending.md`, added no Volume 13, wrote no chapter prose, repaired no prose, and wrote no `state/complete.md`.

---

## Section one — four prose defects, all located, all needing authority this run does not have

### One. `chapter-0238.md:125` is a nineteen-token lift of `chapter-0236.md:102` and an eighteen-token repeat of its own line sixty lines earlier

> **chapter-0238.md:65**, in Halla Wray's mouth, in a bay on the Slade bank: *"I have watched about nine people in this empire make a habit into a thing and every single one of them ended up with a heading over it."*

> **chapter-0238.md:125**, in narration, at the end of her walk back down the road: *"**And he did not ask, and that is the arrangement, and it is a habit, and I have watched about nine people in this empire make a habit into a thing and every single one of them ended up with a heading over it.**"*

> **chapter-0236.md:102**, in Tamsin Rook's mouth, at the fourth counter of the Notaries' Table in Auremar: *"About nine people in this city have made a thing out of a habit in my time in these bays and every single one of them ended up with a heading over it."*

Measured on `m.TOKEN` with `difflib.SequenceMatcher(autojunk=False)` over the two lines, printing the longest shared contiguous token run:

| Pair | Longest shared run | The run |
|---|---|---|
| `0238:125` vs `0236:102` | **19 tokens** | *in my time in these bays and every single one of them ended up with a heading over it* |
| `0238:125` vs `0238:65` | **18 tokens** | *a habit and I have watched about nine people in this empire make a habit into a thing* |
| `0236:102` vs `0238:65` | **13 tokens** | *and every single one of them ended up with a heading over it* |

Three things are wrong at once and they are one fault. **The narration at `:125` re-performs a sentence the same chapter's point of view has already said, verbatim from *I have watched* onward, sixty lines earlier** — the chapter says the same thing twice about the same decision, once as speech and once as narration, and the narration is the weaker of the two because it adds *and it is a habit* and a clause about the arrangement that the speech already carried. **And the sentence it re-performs is lifted across four hundred and thirty miles and a change of person**: *in my time in these bays* belongs to a clerk standing at a counter in Auremar, and it now stands in the mouth — or the narration — of a foreman on a bank in a different city, in a room the volume has spent five chapters calling a bay. The nine-token run *in my time in these bays* is the whole of the transplant, and the chapter's own geography is what it breaks.

**Why every standing instrument in this repository returned clean on it, and the standing that follows.** Card item 42's test seven is *"a sliding sixty-word window over the ten files, compared across every position and not across paragraphs, must not return the same sixty words twice"*, and it returns **zero** on these ten files, as the card says. **A sixty-word window requires sixty identical tokens, so it cannot see a nineteen-token duplication — and its window is its own detection threshold, not a description of the damage.** It found the Chapter 0239 fault because that fault was about sixty words long, and it reports a batch clean because this fault is nineteen. That is the fourth time this repository has demonstrated the same shape, and `outline/batches/volume-05-batch-0004.md` item 61 names two of the earlier three. **The standing this adds: a sliding-window duplicate test detects a duplication of its own window length and nothing shorter, so a zero from it is evidence about that length only, and it must never be reported as a batch-level clearance.** A paragraph-level duplicate audit is also blind to it, for the reason item 56 gives in its own words. What found it was reading `:65` and then reading `:125`, which is the cheapest method in this file and the one that found the two earlier faults.

Item 59 of the card records that this exact sentence pair was touched by the second repair — *"`make a habit out of a habit` is now `make a habit into a thing`, which is what Chapter 0238's own foreman says two hundred lines earlier"* — so the repair **made the two lines identical in order to make them agree, and the agreement is the defect.** A repair that harmonises a lift removes the evidence of the lift. Left, recorded; it needs delete or substitute authority.

### Two. `chapter-0236.md:105` names the wrong man as the one person who has thanked Tamsin Rook, and says the same thing twice in one clause

> **chapter-0236.md:105**: *"And a man of thirty-eight with no office and no fund has a sheet of paper in his own hand that **is now in his own hand** and not in a book of hers and not in a drawer and not in a room… I have never once been one of the four. I have said the price of that out loud four times this year and **been thanked once by a man of about thirty** who is not in the matter and did not know what he was thanking me for."*

Two defects in one paragraph, and the first one is a contradiction inside twenty-three lines of itself.

**The thank is attributed to the wrong man.** The only person who says thank you anywhere in this batch is at **`chapter-0236.md:82`**: *"A man of about forty came for a copy at about the fifth hour and paid fourpence and it took her about eleven minutes and she read it back to him twice and he read it back once and said thank you."* The man **of about thirty** at `:50`–`:64` is a different man, and he explicitly declines: *"I am not going to spend it"*, *"I have come about four bays to be told no by a person and I have been told no and I am going."* He puts the coin down, picks it up, says his name is not going to be in anything, and leaves. **He never thanks her.** A whole-word `thank` sweep over the ten files returns nineteen lines and **one instance of an actual thank, at `:82`, and it is the man of about forty.** The closing paragraph attributes it to the man of about thirty and adds that he did not know what he was thanking her for, which is a characterisation of a man who is not on the page.

**And the same clause says *in his own hand* twice**, *"a sheet of paper in his own hand that is now in his own hand"*, which is a tautology standing where a contrast was intended, and the contrast the paragraph wants is the one the rest of it makes: not in a book of hers, not in a drawer, not in a room. Both are substitutions against base in a closed volume. Left, recorded.

### Three. Five doubled blank lines in four of the ten chapters, and one of them stands before a section rule

`re`-scanned line by line for two consecutive blank lines, which in a file where one prose line is one paragraph is a doubled paragraph separator and renders to a reader as a paragraph break with nothing in it:

| File | Blank lines | What stands between them and the next line |
|---|---|---|
| `chapter-0232.md` | **116, 117** | the closing roll-call paragraph at `:118` |
| `chapter-0236.md` | **103, 104** | the first-person closing paragraph at `:105` (finding four below) |
| `chapter-0238.md` | **128, 129** | *She had been gone about two minutes…* at `:130` |
| `chapter-0239.md` | **112, 113** | **`---` at `:114`** — two blanks and then a scene break, which renders as an empty section |
| `chapter-0239.md` | **119, 120** | the closing roll-call paragraph at `:121` |

`chapter-0239.md:112-113` is the worst of the five and the only one with a second-order effect: a blank line, another blank line, and then a scene rule is an empty section, and **an empty section is a structural fault of the class `reviews/volume-05-batch-0003.md` section one item two already reports twice in the batch behind this one**, at `chapter-0226.md:49-50` and `chapter-0229.md:19-20`. Six instances of one class across two batches of one volume, none of them seen by any of the nine mechanical tests in card item 42, because a doubled blank line is not punctuation, not a quote mark, not an emphasis mark and not a word. All five need delete authority. Left, recorded.

**And the other half of the same finding is a positive.** `grep` for consecutive `---` returns **zero** in all ten files, and this batch therefore does not carry the doubled-scene-break instance of the class that the batch behind it does. Reported so that the difference is not re-derived.

### Four. `chapter-0234.md:59` claims a figure in four words against a referent of fifteen tokens standing on the same line

> *"A labour he can be refused. That is one of the two things he is, and it is the shape of a road, and **the whole of the meaning of it in about four words** is that a man who is a labour is a man somebody can pay for a day, and a man somebody can pay for a day is a man somebody can tell to stop."*

The referent is printed immediately after the claim. Counted on `m.TOKEN`: **"a man who is a labour is a man somebody can pay for a day" is 15 tokens, and both clauses together are 32.** This is the manuscript's *"N words"* device, and the standing `reviews/volume-04-batch-0005.md` section one item three establishes is to **report one only where no plausible convention reaches N** — not at six or eight tokens, and the Volume 04 instance was reported at twenty-one. **No convention reaches four for a fifteen-token clause.** Left, recorded.

**The other four *"N words"* instances in the range were read and are not reportable**, and they are set out so a later phase does not re-derive them. `chapter-0233.md:99` (*said so in that bay this morning in about nine words*) refers to a speech that is not printed in this batch. `chapter-0236.md:50` and `chapter-0236.md:62` (*four words in his head*) are a figure for a person's unvoiced thought and are not a length claim about any text. `chapter-0236.md:24` is a self-measurement — *it was about twenty words and then about nine minutes* — and it is **nearly right and not exact**: the two sentences Tamsin Rook speaks at `:26` are **24 tokens** on `m.TOKEN`, fourteen and ten. Card item 8 calls the same answer *eleven words*, which is a third figure for one piece of text and is section two, finding six.

---

## Section two — eight claims in the batch record that the page does not bear out

`outline/batches/volume-05-batch-0004.md` is an outline file and this phase may not edit it. These are reported for a phase with that authority. **Every one of them is a figure, and in six of the eight the prose needs nothing and the record is wrong** — which is item 267's item eight and item 268's item 268B in a third batch.

### Five. The `about nine` bound reproduces, the figures do not, and this is the second batch in a row

Card item 38 claims the batch *runs three to eight a chapter, sixty instances across ten chapters*, and gives per file **231 3, 232 5, 233 6, 234 8, 235 5, 236 6, 237 8, 239 6, 240 6**.

Measured on this tree with the card's own method — `re.findall(r"\babout nine\b", t, re.I)` per file minus `re.findall(r"\babout nine hundred\b", t, re.I)`, the subtraction the card's own text makes necessary when it records *every person in this trade wants it* replacing *about nine hundred of us want it*:

| File | raw | of which `about nine hundred` | counted | card |
|---|---|---|---|---|
| 0231 | 3 | 2 | **1** | 3 |
| 0232 | 6 | 1 | **5** | 5 |
| 0233 | 6 | 0 | **6** | 6 |
| 0234 | 9 | 1 | **8** | 8 |
| 0235 | 5 | 1 | **4** | 5 |
| 0236 | 7 | 0 | **7** | 6 |
| 0237 | 7 | 0 | **7** | 7 |
| 0238 | 8 | 1 | **7** | 8 |
| 0239 | 6 | 1 | **5** | 6 |
| 0240 | 6 | 0 | **6** | 6 |
| **TOTAL** | 63 | 7 | **56** | 60 |

**Five of the ten cells are wrong and the total is four out, in both directions — two chapters above the card and three below it.** The lock still holds: ten of ten at or under eight, highest single chapter eight. **The prose needs nothing.**

**This is the identical failure on the identical method, in the adjacent batch.** `reviews/volume-05-batch-0003.md` section two item five recorded that Batch 0003's card certified *six to eight a chapter, seventy-two instances* where the same method returns **56**. Two batches, the same method, the same subtraction, the same shape of error, and the card in both cases opens by insisting that the figure was measured. **The standing travels and it is now measured twice: a per-chapter figure published beside its own method must be re-derived before it is inherited, because the subtraction of a longer sibling figure from a shorter one is the step that gets dropped, and it is dropped in the same direction — upward — in both batches.**

### Six. Two items in one file give two different distributions for the same thirty question marks

Card item 42's test eight gives the ten files as **1, 3, 3, 2, 1, 4, 3, 4, 8 and 1, thirty in all**. Measured: `T[p].count("?")` per file returns **exactly that, cell for cell, and the total is thirty.** Item 42 holds to the digit.

Card item 2 gives a different distribution for the same figure: *"three in Chapters 0231, 0232 and 0233, two in Chapter 0234, one in Chapter 0235, four in Chapter 0236, three in Chapter 0237, four in Chapter 0238, **seven in Chapter 0239** and one in Chapter 0240"* — while stating *there are thirty question marks in the ten files*. **Read as one each in the first three chapters it sums to 25; read as three in each of the first three it sums to 31. It is 30 on neither reading.** Two cells are wrong on the page's side: **`chapter-0231.md` carries 1 and not 3, and `chapter-0239.md` carries 8 and not 7.** A figure of thirty is printed twice in one file with two breakdowns under it, one of which cannot sum to it. **The standing: a total published more than once in one record must have one distribution, and a distribution that does not sum to the total beside it is a distribution nobody has checked.**

### Seven. Card item 41 lists two sentence frames that were never written, and undercounts the one that was written twenty-five times

The two headline figures of the item reproduce exactly: **"there is no form anywhere in this empire" runs fifteen times and "there is no form in this empire" runs nine**, twenty-four across ten files against the bound of about twenty-five. Four of the neighbouring frames reproduce: *for a fund* twice, *there is not one form in this empire* twice, *there is not one form for it* once, *that puts a street in a book* once. The six frames the item declares absent are indeed all zero.

**Three cells do not hold:**

| The card writes | The page carries |
|---|---|
| *and there is no form anywhere in this empire with no name under it* — **once** | **0.** Neither the long frame nor the fragment *with no name under it* occurs anywhere in the ten files |
| *there was no form anywhere in this empire* — **once** | **0.** The past-tense frame is not in this batch |
| *a bare "and there is no form" tail on the end of **sixteen** sentences* | **25**, listed in full below |

The twenty-five: `0231:89`, `0232:118`, `0232:122`, `0233:37`, `0233:111`, `0234:25`, `0234:51`, `0235:61`, `0236:19`, `0236:80`, `0236:102`, `0237:31`, `0237:63`, `0237:69`, `0237:111`, `0238:37`, `0238:59`, `0238:71`, `0238:123`, `0238:138`, `0239:116`, `0240:7`, `0240:63`, `0240:67`, `0240:95`.

**This item ends by warning that "a list of variations that were never written is a list a later writer will go looking for", and it then prints two of them as written.** A frame listed at zero may be cut; a frame listed at one sends a writer looking for a sentence that is not on the page. And the bare tail, which is the motif's most-used shape in the batch, is understated by nine.

### Eight. Card item 45 says the protagonist is on the page or named in ten of ten. He is in nine

`grep -n "Kest\|no office and no fund\|man with no office\|thirty-eight with no office"` over the ten files returns a hit in **nine**. The tenth is **`chapter-0238.md`, which contains no mention of Marek Kest at all** — not his name, not *a man of thirty-eight with no office*, not *the only person in this matter anybody can go looking for*. A foreman reads nineteen reasons out loud in a bay, a man of about thirty recognises his own, a second man stands up and is not stopped, and the chapter closes with the mechanism of findability and no mention of the one person in the matter who is unfindable. **That is not a fault of the prose.** It is a foreman's chapter and he does not need to be in it. **It is a fault in the record, and item 45 is a claim about presence with a figure in it.** The item's own enumeration is short in the other direction as well: it lists the point of view of two chapters plus Chapters 0232, 0233, 0235, 0237 and 0239, **six chapters, and it omits `chapter-0231.md:134`, where he is on the page in the closing roll-call.**

### Nine. Card item 8 calls an answer eleven words; the page's two sentences are twenty-four, and the prose says twenty

> **chapter-0236.md:24**: *"…and then she said the whole of her answer, standing, which is how she gives things, and **it was about twenty words** and then about nine minutes."*

The answer she gives at `:26` is two sentences: *"The second half, no, and not one word of it in writing at all."* (14 tokens on `m.TOKEN`) and *"The first half, yes, on the day you have written."* (10 tokens). **Twenty-four.** The prose's *about twenty* is a defensible rounding of twenty-four; the card's *eleven words* is a third figure for the same two sentences and is wrong by thirteen. Reported because a card that re-measures the page's own self-measurement and gets a different number has either measured something else or has printed a figure it did not derive.

### Ten. Card item 58's per-file word list does not sum to its own batch total, and its volume figures are five batches out of date

The **batch total of 28,118 reproduces exactly** on this tree, by `m.words_in_file` per file. **The per-file list does not sum to it.** Card item 58 gives *2,911 / 2,856 / 2,736 / 2,906 / 2,910 / 2,836 / 2,810 / 2,844 / 2,521 / 2,791*, which sums to **28,121**. Measured per file: 2,911 / 2,856 / 2,736 / 2,906 / 2,910 / 2,836 / 2,810 / 2,844 / 2,521 / **2,788**. **`chapter-0240.md` is three words shorter than the card says, and every other cell is exact to the word** — so the total is right and one cell of the list that is supposed to produce it is wrong. That is the fourth time in this repository's own record that a per-file list and its own total have been printed from different trees.

Item 58 also prints *Volume 05 at 115,457 and the manuscript at 826,531*. Re-run on this tree with `python3 tools/measure.py words --volume 05` and `python3 tools/measure.py words`: **Volume 05 stands at 144,248 and the manuscript at 1,496,533 in 620 files.** Both are five batches out of date and neither is a defect of this batch; they are recorded because a writer who takes the card's volume figure as a baseline is measuring against a tree that no longer exists.

### Eleven. Card item 43's `the book` census is one short and three short, and its own enumeration names the one it missed

Card item 43 reports that *the book* as a standalone singular *occurs FIVE times* — the rent coming out of it in 0231, *put the sum in the book* in 0235, *taken out of the book* and *the book that goes down the river* in 0239, and *he shut the book* in 0240 — and that *a loose search also counts the compound the book-keeper once, so the raw string returns eight*.

Every one of the five the card names is real. **There is a sixth, and it is the one the card's own list stops short of: `chapter-0240.md:7`, *"The book with no office on it was on the table with the eleven lines in it and the twelfth empty."*** The standalone singular is therefore **six**, not five. The raw string — the singular, the two plurals at `0231:5` and `0235:5`, and the three compounds *the book-keeper* at `0233:31`, `0233:107` and `0233:111` — is **eleven**, not eight.

**The lock the item is really about holds, and it is checked here so it is not re-derived: all six singular instances are objects in a room or a building, and the manuscript sense of *the book* is zero.** The item's own last sentence, that a loose search counts the compound, is right and understates it by two.

### Twelve. Card item 40's sentence figures do not reproduce under the method the card states, and its hard bound reproduces exactly

The card states the method — counted per paragraph and not across a paragraph join, split on a full stop or question or exclamation followed by a space and a capital, a quotation mark or an emphasis marker — and then prints *958 sentences, a mean of 29.0 words, a median of 23.5, thirty-three point five per cent at forty words or more, twelve point seven at sixty or more, three point zero at eighty or more, and a longest in any chapter of 90*, and states that there is no sentence of a hundred words or more anywhere in the ten files.

Measured by that method, over `m.TOKEN`-split paragraphs per file: **879 sentences, mean 31.7, median 27.0, 36.5 per cent at forty or more, 13.9 at sixty or more, 3.2 at eighty or more, and a longest of 90 words at `chapter-0232.md:118`, with 0 at a hundred or over.**

**The hard bound holds to the digit, and it is the part the card says is the checkable part.** The distributional set does not reproduce, and — this is the finding — **it does not reproduce in the position the card says was already fixed.** Item 40 records that an earlier set (*mean 30.1, median 24, thirty-five point nine at forty, fourteen point nine at sixty, three point five at eighty*) *are not reproducible from the method this item states, and they are withdrawn and not replaced*. The replacement set is not reproducible either. **A figure that no method returns should not be printed as a measurement, and a card that declines to replace a withdrawn figure has not thereby made the new one true.** The prose needs nothing and the bound holds; the printed sentence is what is wrong.

### Thirteen. The finding this review hands forward: card item 42's test seven cannot see the fault it was written for at the size the fault occurs

This is the eighth record finding and the standing it produces, and it is section one's finding one read as an instrument question.

Card item 42's test seven is *"a sliding sixty-word window over the ten files, compared across every position and not across paragraphs, must not return the same sixty words twice"*, added by the review repair, and item 61 calls it the check added in consequence of the Chapter 0239 duplication. **Run on the ten files it returns 0 pairs, exactly as the card reports.** It cannot see the nineteen-token duplication at `chapter-0238.md:125` against `chapter-0236.md:102`, because a sixty-word window requires sixty identical tokens and this fault is nineteen.

**The window is the detection threshold, and a threshold is not a bound on the damage.** The Chapter 0239 fault was about sixty words and the test was sized to it; the next fault in the same batch is nineteen words and the test is invisible to it. The test also cannot see a paragraph that repeats with its interior changed, which is the class item 56 names and which `chapter-0238.md:125` is an instance of — it re-performs `0238:65` with a clause added at the head.

**The standing this adds, and it is the fourth statement of this shape in the card and the sixth in the state layer:** *a test that returns zero is evidence of nothing until you have checked what shape of damage it is blind to* is already in item 42 and item 57. This review states the corollary it has been missing: **a test with a numeric parameter reports on that parameter and not on the class, so a duplicate scan must be run at a floor well below the size of the fault it is standing in for — four words is the floor that item 258 and item 260 found by saturation, and a sliding window is the wrong instrument because its floor and its threshold are the same number.**

---

## Section three — the claims that hold, measured, so that a later phase does not spend a run re-deriving them

| Claim | Result | Method |
|---|---|---|
| Emphasis, the governing text measure (card item 37) | **holds, all ten cells to one decimal** | prose characters inside paired `**` over prose characters, headings and blockquotes excluded, runs paired per file; per file 8.4 / 10.8 / 9.2 / 10.0 / 11.1 / 9.2 / 9.0 / 12.7 / 13.9 / 11.1, range 8.4–13.9, median 10.4 |
| Emphasis, the reported line measure (card item 37) | **holds, all ten cells to one decimal** | non-blank prose lines carrying at least one mark over non-blank prose lines; 13.2 / 13.3 / 18.2 / 16.7 / 10.9 / 18.4 / 12.7 / 11.8 / 13.3 / 12.5, range 10.9–18.4, median 13.3 |
| Emphasis parity (card item 42 test four) | **holds — 0 odd blocks, even mark count in all ten files** | per-paragraph `**` parity over non-blank non-blockquote paragraphs |
| `this year` occurs seventeen times and every one is an elapsed span (card item 32) | **holds — 17 exactly**, at 0231 ×1, 0232 ×2, 0233 ×2, 0234 ×1, 0235 ×4, 0236 ×4, 0238 ×1, 0239 ×2 | `re.findall(r"\bthis year\b")` per file; 0237 and 0240 carry none |
| The bar sentence is verbatim in five chapters with no variant (card items 32 and 59) | **holds — verbatim at 0231:134, 0234:5, 0235:117, 0237:107, 0240:5, one each** | literal search for *came off him on the twelfth of the ninth month of last year on an application of one line which he wrote himself*; every other `came off` in the range is unrelated (a gate, buildings) |
| No month name and no weekday name (card item 33, standing lock) | **holds — 0 and 0** | whole-word search for the twelve month names and seven day names. **The string `may` returns 5 hits on 5 lines in 4 chapters (0231:126, 0232:99, 0234:51, 0238:37, 0238:71) and every one is the modal verb**, so the card's *four chapters* holds and its *the only instance of the string may anywhere in the batch is the modal verb* holds. Read in context, all five. **Item 268B's prompt warned against inheriting an eight-hit list as a clearance; the true census is five on this range and it is modal five times out of five** |
| Every question mark is bare, short, and in the mouth of a person; none is about a word on a form (card item 2) | **holds — all thirty**, located at 0231:69; 0232:21, 45, 75; 0233:21, 43, 45; 0234:81, 89; 0235:83; 0236:40, 56, 58, 94; 0237:27, 57, 87; 0238:25, 31, 47, 67; 0239:17, 27, 63, 71, 77, 85, 89, 93; 0240:57. Every one is a short line opening with a quotation mark; `0236:58` is marked as not about a word on a form **in its own mouth** | every hit printed in full and read |
| `exception`, `precedent`, `schedule`, `Venn`, `ruling`, `Ashfall`, `counting-house mark`, `ninety-second`, `Oris`, `Mosswake`, `present holder` (card items 35 and 46) | **holds — all 0** | per-term `re.findall` over the ten files |
| `four hundred miles` absent; `four hundred and thirty` the long form (card item 35) | **holds — 0 short, 47 long** | both strings searched over the ten; *four hundred and forty* separately 6, all the bank |
| `fourteen months` and no duration counted in months (card items 34 and 39) | **holds — 0** | literal search |
| Tests one to six (card item 42) | **all zero** | punctuation + two spaces 0; full stop + lowercase 0; `[A-Za-z]\*\*[A-Za-z]` 0; odd `**` block 0; any non-blank prose line with an odd quotation-mark count 0, which covers test five and the blunt test together; a prose line opening with a quotation mark and carrying an odd count 0 |
| No card language in the narration (card item 43) | **holds — all fifteen patterns 0** | *on the page, on this page, this page, in this chapter, this chapter, the chapter, in this batch, this batch, the volume, the reader of, is not a device, is not a symbol, is owed nothing, this is not this girl, is the ordinary way this matter works, nobody has named it in a room yet* |
| Named figures (card item 44, as corrected) | **holds** | every capitalised two-word name extracted: **Halla Wray, Marek Kest, Nell Kest, Rennick Adley, Tamsin Rook** and *Slade Cut*, which is a cut and not a person. **Auremar** is the single-word place the card itself added, and it is at `0236:3` and `0237:5`. **No new named person in the batch** |
| No out-of-world breach | **holds — none** | as in Batch 0003, no chapter, volume, page or reader token is out of world; *the book* and *the books* are all objects in a room or a building |
| The count of askings is four and did not move (card item 1, standing lock) | **holds** | the count printed at 0231:136, 0234:121, 0235:105, 0237:111, 0239:121, 0240:97, always four, with *the third of the four was the first one anybody did on purpose* at 0231:136, 0234:121, 0240:97. **All twenty occurrences of `fifth` in the range were printed and read: nineteen are *the fifth month* or *the fifth hour*, one is *about a fifth of the way*, one is *I have said it five times and the fifth one was to a boy of nine*, one is *not going to hand you a fifth in a bay* and one is *work out a fifth from a chair*. **None of them makes it five |
| The reader of seventeen is unnamed, unthanked, unsent anybody, and not asked (standing lock) | **holds** | nine mentions; `grep -n -i thank` returns nineteen lines across the ten files and **every one is a negative or a refusal**, the single actual thank being `0236:82` and belonging to a man of about forty (finding two). `forty-five pence a day and four days a week` appears once, at `0234:61`, and is not varied |
| The Lowcross bill at nineteen pounds three and fourpence, unpaid, nobody liable, no line in nineteen years (standing lock) | **holds** | four mentions, at 0231:128, 0232:101, 0235:127, 0239:111, each carrying the sum and the unpaid state; **no chapter funds, pays or forgives it** |
| The guarantee standing and unanswered, about sixty children (standing lock) | **holds** | four mentions, 0231:130, 0237:109, 0239:111, plus 0239:107; **no chapter answers it** |
| No hearing, no arrangement of one, no commission, no warrant, no appointment, no new heading, no new form (card items 28 and 46) | **holds** | `commission`, `warrant`, `appointment`, `appointed` return **0 across all ten files**. `post` returns five and four are *no post anywhere in this empire whose job is to ask* or *no form and no post*; the fifth is `0240:93`, *He put the sheet in the post*, which is the mail. `hearing` and `court room` return one line, `0235:105`, inside the recital of the four askings and in the past |
| No certification granted and none held (card item 35) | **holds — 2, both negative** | `0234:5`, *nothing in this empire he could certify anything with*; `0236:80`, *A certificate is four shillings, and she has never issued one* |
| The four who cannot read a paragraph are unasked and all four decisions stand (card item 21) | **holds** | the finding at `0233:69` and `0239:79` refers to the entry of the second week of the tenth month of the year after and is not re-argued; **no chapter asks any of the four anything about the hold** |
| Nobody is thanked in the matter (standing lock) | **holds for the reader of seventeen and for every person in the roll-call** | see above. **The one exception on the page is finding two, and it is an attribution error and not a broken lock** |

---

## Section four — the live lead this review was handed, answered

The prompt for this run carried one lead from `workspace/review-debt-0001/PROMPT.md`: *"the same word-boundary method on Batch 0005's `chapter-0250.md` returns **1** against a card claiming* 3 to 8*. That card figure does not reproduce."*

**The lead is half right and it is worth correcting, because a lead handed on uncorrected becomes the next review's premise.**

**The figure reproduces exactly.** `re.findall(r"\babout nine\b", t, re.I)` minus `re.findall(r"\babout nine hundred\b", t, re.I)` over `chapters/volume-05/chapter-0250.md` returns **1**. `chapter-0250.md` has been on disk, unedited, since `dedc831`.

**What does not hold is the bound, not the figure.** Batch 0005's card claims the batch *ran 3 to 8*. Measured across all ten of Batch 0005 on the same method: **241 7, 242 6, 243 3, 244 3, 245 8, 246 7, 247 8, 248 6, 249 7, 250 1** — a range of **1 to 8**, with `chapter-0250.md` alone below the floor and `chapter-0243.md` and `chapter-0244.md` sitting on it. **The defect the lead points at is real and it is in the card's bound, and the next review should test the bound and not re-derive the single file.** This is the same distinction finding five makes about Batch 0004 — *the lock holds, the figures do not* — turned the other way round: here the figure holds and the lock does not.

---

## Section five — what this review could not do, and hands on

**The four prose defects above need prose authority**: three deletions against base and one substitution in a closed volume. **A review has no authority to make one, and this run did not make one.** They are listed with line numbers so that a phase given the authority does not have to re-find them, and **a line number in a file no phase has edited is a citation that resolves.**

**One thing this review did not settle and will not settle.** Two paragraphs in this range carry first-person narration inside a third-person chapter: `chapter-0236.md:105` (*I have never once been one of the four*) and `chapter-0238.md:125` (*I have watched … in my time in these bays*). Scanned across all fifty chapters of Volume 05, excluding headings, blockquotes and pure speech turns, **first-person narration appears in eight chapters: 0205, 0213, 0217, 0223, 0225 and these two.** Three of the five outside this range are the same bolded sentence in three chapters — *A hand of mine is the only hand anybody is going to be able to put side by side in about four years, and I have now done this for the eleventh / twelfth / thirteenth time* at `0205:109`, `0213:145` and `0225:134`. Two more sit inside a third-person chapter that has already used the third person in the same breath: `0217:81` reads *Four, she thought* and then, eleven words later, *and **I** have not been told her name*; `0223:121` reads *because **I** am a person who counts* in a chapter whose next paragraph opens *He shut the book*.

**Volume 12 is written in the first person throughout**, which is a volume-level decision and not a fault. **So either first-person interior narration is a house device of Volume 05 that no outline and no card has ever written down, in which case eight chapters are carrying an unwritten rule; or it is a fault that has stood in five chapters across two batches and that two reviews, including one that read `0217` and `0223` in full, did not report.** **This review does not decide it and does not report it as a defect of this batch**, because it is not one. It is recorded here and in `state/open-threads.md` so that the next owed review does not have to find it again, and so that the question is put once in a place somebody with authority can answer.

**And the thing the next owed review inherits.** This batch's card certifies four figures that do not survive checking (`about nine` at 60, the question-mark distribution in item 2, two sentence frames in item 41, the protagonist at ten of ten), one per-file cell that does not sum to its own total, one sentence-census that no method returns, and one duplicate test whose zero is a statement about sixty tokens and not about the batch. **A record that reports a clearance it did not make is worse than a record that is silent**, which is the standing the Volume 04 review added at its item eight and which Batch 0003 repeated twice, once in the card and once in the prompt. **This is the third batch in a row, and the third batch in a row in which the error runs upward** — 72 claimed against 56 measured, 60 against 56, and now a card that lists two sentence frames as written which were never written at all. **The standing does not need restating; it needs applying to the file that wrote it, which is the only part of this paragraph that is new: the next owed review's prompt should carry the count of card claims that failed for the batch behind it, because a reviewer who knows the previous card failed in five places reads every figure in the next card as a claim rather than as a fact, and that is the whole difference between this review and a scan.**

---

**What this review touched:** no chapter file, no outline, no `tools/measure.py`, no controller file. It read `outline/batches/volume-05-batch-0004.md`, `outline/volume-05.md`, `reviews/volume-04-batch-0005.md` and `reviews/volume-05-batch-0003.md`; it read `chapters/volume-05/chapter-0231.md` through `chapter-0240.md` in full; it measured `chapter-0250.md` once for the lead section, which is the one figure of another batch's file this review prints. **It was paid by the phase that took `workspace/review-debt-0002/PROMPT.md` and it is the third of the four owed reviews in `outline/volume-12.md` to be paid. Two remain: Volume 05's Batch 0005, and Volume 06's own Batch 0003 — which is two prompts, not one, and Volume 05's Batch 0005 is the nearer of them.**