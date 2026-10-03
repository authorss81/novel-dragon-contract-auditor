# REVIEW: VOLUME 04, BATCH 0005, CHAPTERS 0191 TO 0200 — THE FIRST OF THE FOUR OWED REVIEWS

**Who wrote this, and what it is not.** This is a review of ten finished chapters in a closed volume. It was written by the same agent that wrote the state files this run, and **nothing in this repository's review gate is independent** — the gate has fallen back to the writing agent every time it has been asked, and `NOVEL_SPEC.md` and `state/open-threads.md` item 170 both say so in terms. **No sentence in this file may be cited as an independent finding.** What it has that a scan does not have is that all ten chapters were read end to end, and that every claim in `outline/batches/volume-04-batch-0005.md` was tested against the page with the method printed beside the figure.

**Why this range.** `outline/volume-12.md`, at its close, names four owed reviews: *an owed review of Volume 04's Batch 0005, four volumes on*, and *owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, which is four and not three.* None of the four has been paid. This is the oldest of the four, and **Volume 04 is the one volume in the manuscript that no prose repair has ever touched**, so what is read here is original writer-pass prose with nothing added on top of it.

**What this phase did not do, and it is the important half.** It opened no chapter for edit. Volume 04 is a closed volume, every finding below is in prose that only a phase with delete or substitute authority can touch, and **this run had none and did not take any.** It edited no outline, and `outline/batches/volume-04-batch-0005.md` is an outline file, so the four record defects in section two are reported and not repaired.

---

## Section one — five prose defects, all located, all needing authority this run does not have

### One. Six breaches of Volume 04's own out-of-world rule, across four of the ten chapters, and the batch record says the rule holds

The rule, quoted verbatim out of the batch record's own item 17: *"no chapter refers to the chapter, the batch, the page, the volume or the reader of the book while a scene is open, and the closing sweep returns nothing that is not an in-world page of an in-world book."*

| Location | The words |
|---|---|
| `chapter-0192.md:61` | "the ordinary way took about nine minutes and **it is the whole of the chapter**" |
| `chapter-0193.md:55` | "**it is the reason this chapter is not about a man who hid something.**" |
| `chapter-0193.md:63` | "That is the sentence that belongs here and **it is the hardest one in the chapter**." |
| `chapter-0196.md:35` | "he wrote the second half of it, which is **the half that is the finding of the chapter**" |
| `chapter-0197.md:3` | "the order of them **is the whole of this chapter** and nobody in the room was permitted to reverse them afterwards" |
| `chapter-0197.md:123` | "**and a reader is going to be left with two facts** and no way of telling which of them this is about, and that is not an accident of the finding and **it is not a defect in the record**" |

Command: `grep -rno -E ".{70}\b(chapter|volume|reader)\b.{40}" chapters/volume-04/chapter-019[1-9].md chapters/volume-04/chapter-0200.md`, and every instance read in place.

The rule is absolute and it names *the reader of the book* as well as the chapter, and **two of the six are inside bold runs**, so they render as authorial emphasis. `chapter-0197.md:123` is the deepest of the six and it is worth naming why: the sentence defends *the record* from inside the prose — *it is not a defect in the record* — in a volume whose whole subject is the difference between a record and a room. A reader cannot tell whether that is Orla Denning's reasoning, the narrator's, or the author stepping in. It is the only place in the batch where the three collapse.

**Checked and cleared, so a later phase does not re-report them:** every other `page` and `volume` token in the range is an in-world object. `chapter-0197.md:27` "She turned the volume round to face him" is a minute book. `chapter-0197.md:129` "in four years this page will say that a woman said no" is the leaf of a roll. `chapter-0191.md` and `chapter-0195.md` use `the page` of a document throughout. **The six above are the whole of it, and there is none in 0194, 0198, 0199 or 0200.**

### Two. `chapter-0198.md:97` gives a foreman's job as eleven years against a canon of nine, and it is the sentence the chapter turns on

> "I have been that for about **eleven years** without knowing it, and I have been unfindable on purpose, and now I am findable by accident."

Canon, measured across the whole manuscript with `grep -ro "nine years" chapters/` and `grep -ro "eleven years" chapters/`:

- **Nine years is her tenure, in eight places**: `chapter-0135.md:5`, `chapter-0147.md:5`, `chapter-0282.md:5`, `chapter-0210.md:29`, `chapter-0233.md:79`, `chapter-0245.md:107`, `chapter-0249.md:17`, and `outline/volume-05.md` in its own words — *"nine years holding a job that is written down nowhere."*
- **Eleven years is the date the nine families agreed the office out loud**, in seven places and all seven the same sentence: `chapter-0101.md:15`, `chapter-0126.md:5`, `chapter-0198.md:5`, `chapter-0198.md:23`, `chapter-0204.md:5`, `chapter-0278.md:5`, `chapter-0282.md:5`.

So eleven and nine are two different facts about two different events and they are both canon. **`chapter-0198.md:23` gets both right in one sentence** — *"Forty-two years on this bank and nine years holding the only job on it that is written down nowhere ... and the nine families agreed it out loud about eleven years ago in a shed."* **Line 97 then gives the tenure as the agreement date.** The chapter had the correct pair in front of it thirty lines earlier.

**Why nothing here could have caught it.** A figure that contradicts a figure is not a repetition. No re-print window, no lift, no sweep, no construction list and no calendar parse sees a number disagreeing with a number in a different file, and the canon figure lives in seven other files and one outline. **This is the finding `state/open-threads.md` item 266B named at the price of five contradictions in thirty-nine chapters, reproduced here in a closed volume where it cannot be paid.**

### Three. `chapter-0194.md:61` says a quotation is four words long, and it is twenty-one

> "It is not going to work, and here is the reason, and **the reason is four words long and I have read them.**" ... "**No further consent required. A room that writes a no down is not the thing that has the no in it.**"

Measured: that quoted span is **21 whitespace tokens and 8 words under any stopword list**, by `re.findall(r"[A-Za-z']+", span.lower())` filtered against a list of articles, pronouns, copulas and prepositions.

**The volume's canon four words are a different phrase entirely**, and this chapter states them correctly ninety lines later at `chapter-0194.md:127`: *"it is four words and they are the same four words as last time. A person, not a column."* That phrase is canon at `chapter-0184.md:137` and `chapter-0186.md:153` — *"There are four words and they are: a person, not a column."*

So one chapter carries two different four-word quotations about two different subjects, and only one of them is the volume's. A reader who knows the canon four words is being told, ninety lines apart, that the reason a refusal did not work is *a person, not a column*, which is the reason a **name** was not written in a **column**, and that these are the same finding.

**The standing this produces, and it is the more useful half.** This manuscript's *"N words"* device has **no stated convention anywhere in `outline/`** and the printed instances do not agree with each other:

| Location | Printed phrase | Whitespace tokens |
|---|---|---|
| `chapter-0200.md:53` | *I have to be home.* | 5 — four without the pronoun |
| `chapter-0180.md:139` | *a family finds out from itself* | 6 — four without article and preposition |
| `chapter-0186.md:153` | *a person, not a column.* | 5 |
| `chapter-0106.md:107` | *the person who turns up is never paid* | **8** |
| `chapter-0192.md:47` | *what is the fifth line for* | **6** |
| `chapter-0050.md:85` | *read the line out before he puts his thumb on it* | **12** |
| `chapter-0194.md:61` | *No further consent required. A room that writes a no down…* | **21** |

**A reviewer may report an *N words* claim as a defect only where the quoted span is so far from N that no plausible convention reaches it — and that test clears `:61` at 21 and clears nothing else in the table.** It explicitly does **not** clear `chapter-0192.md:47`, which this review read as a probable error on a first pass and withdrew after finding `chapter-0106.md:107`: eight tokens called four words is in this manuscript a correct usage, and a reviewer who splits on whitespace will manufacture a finding there. **It also does not clear `chapter-0050.md:85`, which is twelve tokens called four words and which is a genuine defect this review has not opened and does not own.**

### Four. `chapter-0193.md:99` — a sentence that runs into the next one on a comma

> "...has a pen in a box on her hip and does not know any of it**, The finding of this is not a man and it is not a woman and it is a hand.** Two of the four places..."

Two independent clauses joined by a comma, at the last line of the chapter, with a full stop inside the bold run. `python3 tools/measure.py sentences --volume 04` reads 5,443 sentences across fifty files and does not flag it, because the splitter has no rule for a missing full stop. **It is the chapter's closing sentence and it is the only sentence in the batch with this fault.**

### Five. `chapter-0195.md:115` — the one place in Volume 04 that calls the river four hundred miles

> "I have got **about four hundred miles** of road behind me"

Measured in Volume 04: **`four hundred and thirty` occurs 133 times and `four hundred miles` occurs once, and this is it.** Measured in Volume 03: `four hundred miles` occurs twelve times for the same river.

**Stated honestly, this is the weakest of the five and it may be right.** The manuscript demonstrably has two figures in play for the length of that road, and a witness rounding it in speech is ordinary. But `state/open-threads.md` item 256 named *about four hundred miles* for *about four hundred and thirty* as a defect in Volume 07 on exactly this reasoning, and Volume 04's own base carries the long form 133 times and never the short one. **The finding is the inconsistency inside the volume, not the number.**

---

## Section two — four claims in the batch record that the page does not bear out

`outline/batches/volume-04-batch-0005.md` is an outline file and this phase may not edit it. These four are reported for a phase with that authority.

**Six. "Pell Vey is named in Chapter 0193, once"** (item 15), and *"The page names him once, in a corridor … and does not repeat it"* (item 18). `grep -n "Pell" chapters/volume-04/chapter-0193.md` returns two: **`:3`**, in the chapter's opening summary paragraph in a bold run — *"All four of them are about a man called Pell Vey"* — and **`:17`**, *"It is Pell Vey," she said, to the corridor.* The second is the naming the record describes and the first is not, and the record's own principle underneath both — *"Documentation that cannot be read aloud is not documentation"* — is better served by the page than by the record, because the name is in a corridor. **The record is wrong; the prose is defensible and this review does not ask for it to change.**

**Seven. "the building is a *hired stone store* on the page four times in Chapter 0200."** `grep -c "hired stone store" chapters/volume-04/chapter-0200.md` returns **2** — `:5` and `:85`. The same sentence also says *"the south end of it is not measured"*, and `grep -c "south end" chapters/volume-04/chapter-0200.md` returns **0**, so there is no south end in the chapter to have been left unmeasured. **The half of the sentence that holds** — *the other page name is not used anywhere in the batch* — reproduces: `hired grain store` is 0 across all ten chapters.

**Eight. The `thirty-one` exception clause grants two exceptions that do not exist.** Item 14 says the string occurs *"nowhere else in the batch except as a calendar month in Chapter 0200's own text and the court name Mosswake Roll Court in Chapter 0195."* Measured: `thirty-one` occurs **exactly twice in the whole batch and both are on `chapter-0200.md:83`**, in one sentence — *The thirty-one of Mosswake are thirty-one*. There is no calendar-month instance and no court-name instance, and the court name is at `chapter-0195.md` once and does not contain the string. **The clause names two absences as though they were instances**, which is the shape of defect `state/batch-summary.md` item 173's *"thirty-nine"* warns about: a record that reports a clearance it did not make.

**Nine. The batch's and the volume's word figures are pre-review-repair.** Item 14 and the header of the divergence section give *Chapters 191–200, 30,243 words* and *Volume 04 is 148,482 across fifty*. On this tree, `wc -w` over the ten files gives **30,582** and `python3 tools/measure.py words --volume 04` gives **148,821**. Both card figures reproduce to the digit at the writer commit: `wc -w` over `git show 5682780:chapters/volume-04/chapter-0NNN.md` for the ten gives **30,243**. The review repair `8df0d53` — *save review fixes batch-0005* — moved the batch by `git diff --numstat 5682780 8df0d53 -- chapters/volume-04/`, which is **+14 −18 across seven files**, for **+339 words**. **So the card's figures were exact when written and are 339 low now, and this is the same pattern `outline/volume-05.md` records at its own close** — a batch record written by the run that wrote the chapters, and a review repair afterwards. It is not an error. It is a stale figure in a file a reader will consult, and the repair is a word count.

---

## Section three — nine claims in the batch record that hold, measured, so that a later phase does not spend a run re-deriving them

| Claim | Result | Method |
|---|---|---|
| *exception* used zero times of anything (item 13) | **0** | `re.findall(r"\bexception\b", t, re.I)` over `b3()` per file, all ten |
| *precedent* used zero times (item 13) | **0** | same, `\bprecedent\b` and `\bprecedents\b` |
| The guarantee is printed word for word, five identical and the 0164 variant (item 14) | **reproduces exactly** — one string of 82 words at `0161`, `0170`, `0180`, `0190`, `0200` and one 76-word variant at `0164` | `re.finditer(r"\*\*(.+?)\*\*", t, re.S)` filtered on *guarantee* / *water standing* / *shall not* |
| The price of a party is the eighth in 0192, the ninth in 0196, the tenth in 0197 (item 19) | **reproduces at all three** — `0192:55`, `0196:99`, `0197:109`, each with its own ordinal | `re.finditer(r"\b(eighth|ninth|tenth)\b", b3(f))` |
| The two new named figures and nobody else (item 15) | **holds** — `Aurelia Pell` 0; `Seryn Oris` 0; `Vaunt Oris` 0; `Sivra Oris` 0; `Wren Ludd` 4 in `0195` | per-name `re.findall` over the ten files |
| The Cinder Clause is named once and not explained (item 17) | **holds** — 1, at `0197:93`, and nothing follows it | as above |
| The locked absences hold (item 17) | **holds** — `Ashfall` 0, `counting-house` 0, `ninety-second` 0, `quarterly return` 0, `Hallis Dren` 0 | as above |
| No certification is granted and none is held (item 17) | **holds** — `0191:5`, `0196:5` and `0196:15` say he has nothing he could certify anything with; the one certification written in the batch is `0192:21`, a clerk certifying her own table's book, which is not a certification of a person | `grep -n certif` over the ten |
| The craft lock on `about nine` (Volume 05's lock, held through four batches of Volume 04) | **holds** — 6, 8, 3, 5, 7, 8, 5, 4, 5, 3; **range 3 to 8, median 5.0, total 54** | `re.findall(r"\babout nine\b", t, re.I)` per file |

---

## Section four — what this review could not do, and hands on

**The four prose defects that need prose authority** — items one, two, three and five above, and item four — are all substitutions against base in a closed volume. **A review has no authority to make one, and this run did not make one.** They are listed with line numbers so that a phase given the authority does not have to re-find them, and **a line number in a file no phase has edited is a citation that resolves**, which is the standing item 173's *"thirty-eight"* records and which the whole of section one depends on.

**The three that are not defects and are recorded so they are not re-reported:** `chapter-0192.md:47`'s *four words* (withdrawn after `chapter-0106.md:107`); `chapter-0195.md:115`'s *four hundred miles* as a number (the finding is the volume's inconsistency, not the figure); and `chapter-0194.md:61`'s twenty-one tokens being counted as eight content words, which is the lower bound of the reading and not the finding — the finding is that no reading reaches four.

**One item this review did not open and does not own:** `chapter-0050.md:85` prints a twelve-token quotation and calls it *four words*, in Volume 04's Batch 0001, which is a different owed review. It is in the table in item three because it is the reason the *N words* convention cannot be reconstructed from the instances available.

**And the thing the next owed review inherits.** `outline/volume-04.md` states the out-of-world rule as absolute and `outline/batches/volume-04-batch-0005.md` certifies it as holding in a batch where it is broken six times in four chapters. **The rule's own record is the thing to distrust, and the standing that comes out of this review is that an absolute rule quoted only in a batch's own divergence section has probably not been run.** A rule that lives in the volume outline and is reported on by the batch that most recently touched it is a rule with one witness.

---

**What this review touched:** no chapter file, no outline, no `tools/measure.py`, no controller file. It read `outline/batches/volume-04-batch-0005.md`, `outline/volume-05.md` and `outline/volume-04.md`; it read `chapters/volume-04/chapter-0191.md` through `chapter-0200.md` in full; it grepped `chapters/` for the canon figures it names. **It was paid by the phase that took `workspace/continuation/next-0005/PROMPT.md` and it is the first of the four owed reviews in `outline/volume-12.md` to be paid. Three remain: Volume 05's Batches 0003, 0004 and 0005, and Volume 06's own Batch 0003, which is four and not three.**
