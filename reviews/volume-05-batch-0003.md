# REVIEW: VOLUME 05, BATCH 0003, CHAPTERS 0221 TO 0230 — THE SECOND OF THE FOUR OWED REVIEWS

**Who wrote this, and what it is not.** This is a review of ten finished chapters in a closed volume. It was written by the same agent that wrote the state files this run, and **nothing in this repository's review gate is independent** — the gate has fallen back to the writing agent every time it has been asked, and `NOVEL_SPEC.md` and `state/open-threads.md` item 171 both say so in terms. **No sentence in this file may be cited as an independent finding.** What it has that a scan does not have is that all ten chapters were read end to end, and that every claim in `outline/batches/volume-05-batch-0003.md` tested here was tested against the page with the method printed beside the figure.

**Why this range.** `outline/volume-12.md`, at its close, names four owed reviews: *an owed review of Volume 04's Batch 0005, four volumes on*, and *owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003, which is four and not three.* The first is paid at `reviews/volume-04-batch-0005.md`. This is the second. Volume 05 has never been through the prose repair and none of these ten files has been edited since `18e57c8` (*save review fixes batch-0003*, verified with `git cat-file -e 18e57c8:chapters/volume-05/chapter-0221.md` returning PRESENT), so every line number below resolves.

**What this phase did not do, and it is the important half.** It opened no chapter for edit. Volume 05 is a closed volume, every finding below is in prose that only a phase with delete or substitute authority can touch, and **this run had none and did not take any.** It edited no outline, and `outline/batches/volume-05-batch-0003.md` is an outline file, so the record defects in section two are reported and not repaired. It planned no volume, opened no `outline/ending.md`, added no Volume 13, wrote no chapter prose, and wrote no `state/complete.md`.

---

## Section one — four prose defects, all located, all needing authority this run does not have

### One. `chapter-0226.md:7` carries a subject-verb mismatch in narration

> "with the fifteen books in a heap, which is how they are when **she am** doing them properly"

`grep -n "she am" chapters/volume-05/chapter-022*.md` returns this line and nothing else. The point of view is Nell Kest, third-person narration, everywhere else *she is*. A fix is a substitution against base in a closed volume. Left, recorded.

### Two. Two pairs of consecutive section breaks, one in each of two chapters

`grep -n "^---$" chapters/volume-05/chapter-022*.md` returns consecutive pairs at:

- `chapter-0226.md:49` and `chapter-0226.md:50`
- `chapter-0229.md:19` and `chapter-0229.md:20`

Every other break in the ten files is separated by prose. A doubled break renders as an empty section. Both are structural, both need delete authority. Left, recorded.

### Three. `chapter-0221.md:57` opens direct speech with a leading space

> `" Then what is in the building."`

One leading space inside the opening quotation mark, the only such line in the ten files. Found by reading, not by any instrument: no whitespace, punctuation, or parity check in this repository flags a space after an opening quote. A fix is a substitution against base. Left, recorded.

### Four. No out-of-world breach, and that is a finding and not an absence of checking

`grep -rno -E ".{0,30}\b(chapter|volume|reader of the book)\b.{0,30}"` over all ten files returns nothing. Volume 04's Batch 0005 broke its own absolute rule six times in four chapters; this batch carries none of that class. The *page*, *volume*, and *book* tokens in the range are all in-world objects (a minute book, a book with no office on it, a book on a shelf). Checked and cleared so a later phase does not re-report them.

**What was read and set aside.** The four *four words* instances in the range — `chapter-0224.md:93` (*four words in his head*), `chapter-0225.md:9` (*gave four words for it*), `chapter-0228.md:11` (*gave four words*), `chapter-0228.md:47` (*four words on a form*) — are all slips and references, not *N words* claims about a quotation's length. Under the standing `reviews/volume-04-batch-0005.md` section one item three establishes (report an *N words* claim only where no plausible convention reaches N), none of the four is reportable. The twelve-token *four words* at `chapter-0050.md:85` remains outside this range and is not owned here.

---

## Section two — two claims in the batch record, and one in this review's own prompt, that the page does not bear out

`outline/batches/volume-05-batch-0003.md` is an outline file and this phase may not edit it. These are reported for a phase with that authority.

**Five. The `about nine` figures do not reproduce.** Item 31 of the card claims the batch runs *six to eight a chapter, seventy-two instances across ten chapters*, per file `221 8, 222 8, 223 6, 224 6, 225 6, 226 8, 227 8, 228 7, 229 7, 230 8`, counted on a word boundary.

Measured on this tree with `re.findall(r"\babout nine\b", t, re.I)` per file minus `re.findall(r"\babout nine hundred\b", t, re.I)`:

| File | raw `about nine` | of which `about nine hundred` | counted |
|---|---|---|---|
| 0221 | 9 | 4 | **5** |
| 0222 | 8 | 1 | **7** |
| 0223 | 6 | 2 | **4** |
| 0224 | 6 | 1 | **5** |
| 0225 | 7 | 1 | **6** |
| 0226 | 8 | 2 | **6** |
| 0227 | 8 | 2 | **6** |
| 0228 | 7 | 4 | **3** |
| 0229 | 7 | 1 | **6** |
| 0230 | 8 | 0 | **8** |

Range **3 to 8, median 6.0, total 56**. The prompt that sent this run prints exactly these figures and warns that the subtraction is not optional; the card's 72 does not reproduce under the card's own stated method. The lock itself — *bound to about eight per chapter* — still holds: ten of ten at or under eight. The record is wrong; the prose needs nothing. This is the same shape as item nine of the Volume 04 review (a card figure exact when written, stale on the tree it is read from), except here the card's own repair history already moved the words and the figure did not follow.

**Six. The prompt's own `may` census undercounts.** The prompt for this run states that a naive month/weekday search over the ten files *returns eight raw hits, all `may`, all eight the modal verb*, at `0222:73, 0223:23, 0225:37, 0225:45, 0228:15, 0228:91, 0228:99, 0229:13`.

A whole-word search `re.finditer(r"\bmay\b", line)` over the ten files returns hits in `0222:73` (two on the line), `0222:125`, `0223:23`, `0223:105`, `0224:35`, `0225:37`, `0225:45`, `0228:15`, `0228:91`, `0228:99`, `0229:13`, and `0229:70` — twelve lines, thirteen hits. Every one read in place is the modal verb (*may be asked, may only be in one, you may ask, may send anybody anything, what a person may do*). Zero month names and zero weekday names: the lock holds. The prompt's conclusion is right and its census is short by five hits. Named here so the next prompt does not inherit the list as a clearance.

---

## Section three — nine claims in the batch record that hold, measured, so that a later phase does not spend a run re-deriving them

| Claim | Result | Method |
|---|---|---|
| No month name and no weekday name in the prose (card item 29) | **holds — 0 and 0** | whole-word search for the twelve month names and seven day names across all ten files; every `may` hit read in context, all modal |
| The count of askings is four and did not move (card item 1) | **holds** | the four itemised with dates in `0223, 0226, 0228, 0229`; no fifth asking written; six plain questions marked as plain in the mouth, none counted |
| `exception` and `precedent` zero (card item 35) | **holds — 0 and 0** | `re.findall(r"\bexception\b", t, re.I)` and `\bprecedent(s)?\b` over all ten |
| The three Orises, Ashfall, counting-house mark, ninety-second, quarterly return, Hallis Dren all absent (card item 35) | **holds — all 0** | per-name `re.findall` over the ten files |
| `four hundred miles` absent; `four hundred and thirty` the only long form (card item 35) | **holds — 0 and 14** | `re.findall` for both strings over the ten; short form 0, long form 14 |
| No certification granted and none held (card item 35) | **holds** | `grep -n -i certif` returns 2, at `0223:5` and `0227:21`, both *nothing he could certify anything with* |
| Nobody thanked (standing lock) | **holds** | `grep -n -i thank` returns 25 hits across the ten, every one a negation (*not going to be thanked, has not been thanked, nobody has thanked*) |
| Lowcross bill at nineteen pounds three and fourpence, unpaid, nobody liable (card item 35) | **holds** | at `0229:15` and `0229:128`, with *no line for a bridge in that fund in nineteen years*; bridge-shut exchange in `0229:116-124` and `0230:77-85` in different words, not a duplicate paragraph |
| New named figures none; points of view all established (card item 34) | **holds** | every capitalised two-word name extracted and checked; the ten POVs are Orla Denning, Tamsin Rook, Marek Kest, Bess Tarrant, Ivet Sarn, Nell Kest, Marek Kest with two others, Marn Ottery, Rennick Adley, Halla Wray; *Slade Cut* the only other capitalised pair |

Word figures on this tree, with `wc -w` per file, so a later phase does not re-derive them: 0221 3011, 0222 2758, 0223 2714, 0224 2956, 0225 3018, 0226 3164, 0227 2763, 0228 2754, 0229 2919, 0230 2975; batch **29,032**. The card's *29,032 as repaired and 28,577 as first written* reproduces at the batch total.

---

## Section four — what this review could not do, and hands on

**The four prose defects above need prose authority** — three substitutions and two deletions against base in a closed volume. **A review has no authority to make one, and this run did not make one.** They are listed with line numbers so that a phase given the authority does not have to re-find them, and **a line number in a file no phase has edited is a citation that resolves**, which is the standing item 267's record establishes and which the whole of section one depends on.

**Two things this review did not open and does not own:** `chapter-0050.md:85` (twelve tokens called four words, in Volume 04's Batch 0001) and `chapter-0250.md` (the `about nine` count at 1 against a card claiming 3 to 8, named in this run's prompt as belonging to the third owed review). Both are named here so they are not lost and neither is counted here.

**And the thing the next owed review inherits.** `outline/batches/volume-05-batch-0003.md` certifies its own `about nine` bound as *six to eight* in a batch whose page runs *three to eight*, and the prompt that sent this run certifies its own `may` census as *eight hits* on a page that returns thirteen. **A record that reports a clearance it did not make is worse than a record that is silent**, which is the standing the Volume 04 review added at its item eight and which this batch repeats twice, once in the card and once in the prompt. A bound has to be measured before it is printed, and a sweep that has not been run must not be reported as a result.

---

**What this review touched:** no chapter file, no outline, no `tools/measure.py`, no controller file. It read `outline/batches/volume-05-batch-0003.md`, `outline/volume-05.md`, and `reviews/volume-04-batch-0005.md`; it read `chapters/volume-05/chapter-0221.md` through `chapter-0230.md` in full; it grepped `chapters/` for the canon figures it names. **It was paid by the phase that took `workspace/review-debt-0001/PROMPT.md` and it is the second of the four owed reviews in `outline/volume-12.md` to be paid. Two remain: Volume 05's Batches 0004 and 0005, and Volume 06's own Batch 0003, which is four and not three — three prompts, not one.**
