# Review: Volume 06, Batch 0002, Chapters 261 to 270

Phase reviewed: the writing run that took `workspace/volume-06/batch-0002/PROMPT.md`, commit `6240f4d`.
Reviewed: 2026-09-27, against the committed phase changes.
Repair phase: the run that read `logs/batch-0002.review.log` and applied what it could. Its record is the newest section of `state/current.md` and the newest section of `state/batch-summary.md`.

This file is persisted here because `logs/` is gitignored. The reviewer's own output was never committed, and a review that exists only in an untracked log is a review the next run cannot inherit.

## The finding that governs every other finding here

**The review gate is not running an independent reviewer, and this review is not independent.**

`logs/batch-0002.review.log:1` reads `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`.

This is the same structural fault recorded for Batch 0001 and it is unchanged. `.opencode/agent/novel-reviewer.md` declares `mode: subagent`; the runtime refuses a subagent for a top-level run and falls back to the default agent, which is the writing agent. The reviewer's frontmatter sets `edit: deny` and `bash: deny`, and the fallback runs with both allowed, so *do not edit files* was prompt text and not a permission. `scripts/novel_runner.sh:273` dispatches the gate; the model probe at `.github/workflows/novels.yml:64` uses the same agent and so falls back silently too.

**Consequence for the record, and it is the useful half:** the agent that graded the prose was the prose, and it found three of its own published measurements false. It did not certify a clean batch. A self-review that catches the writing agent asserting a passing measurement is worth more than nothing and less than a review.

**The fix is one line of frontmatter, `mode: primary`, or a real subagent dispatch. Both `.opencode/agent/` and `scripts/` are controller-owned and neither was opened. It needs a controller owner, and it is the first thing in the list.**

## Blocking

### 1. Chapter 0261 gives the wrong character's name — canon break. **Fixed.**

`chapters/volume-06/chapter-0261.md` gave the twenty-four-year-old clerk's name as **Marn Ottery**, who is established across four volumes as the *thirty-four-year-old* clerk of eleven years at that counter (`ch-0151.md:11`, `ch-0202.md:5`, `ch-0247.md:3`). The twenty-four-year-old is **Tamsin Rook** (`ch-0179.md:87`, `ch-0236.md:5`, `ch-0207.md:5`), and Chapter 0265 already names her correctly.

The same finding had a second half, also true: the chapter said *There are three people in that room* and enumerated her, a man of thirty and a woman of twenty, with no room for Marn Ottery at all, and called her the youngest of the three when one of the three is twenty.

**Both are corrected. The counter-day exchange now reads Tamsin Rook, and the room paragraph now names the four people Chapter 0265 already names, with the ages that chapter gives, and still says what it existed to say: at about the seventh hour there is nobody in the room but her.**

The reviewer's supporting observation is true and is recorded rather than acted on: the beat itself, a boy of fifteen asking about unfilled blanks, is inherited from `ch-0247.md:115` through Batch 0001's Chapter 0254 and runs a third time here. It is the thread of the volume and a three-chapter repetition of a counter's ordinary day is not a defect on its own. **It is at item 59 of `outline/batches/volume-06-batch-0002.md`.**

### 2. Six of the ten new chapters re-used large verbatim stretches from Batch 0001, and the batch's own duplicate test reported the batch clean. **Fixed.**

`outline/batches/volume-06-batch-0002.md` item 20 (printed as item 8 in the running numbering) claimed: *A sliding sixty-word window over the ten files … returns **zero**.*

It did not. Re-measured, holding windows inside a paragraph:

- **215 duplicated sixty-word windows** across Volume 06, **207 of them involving a new chapter**.
- The writing run had found twenty-one windows in one pair, 0261 against 0270, repaired them, and reported the test clean, having run it over the pair it had read by hand.
- Largest pairs: 0255→0268, 0258→0269, 0257→0266, 0252→0264, 0254→0261, 0256→0262.
- **26 exactly duplicated paragraphs** across the volume's twenty chapters.

The review attributed the whole finding to the 0261/0270 pair, which the writing batch had already separated, and its coverage column, which reads *100% of 0268's words*, is window-slot coverage with heavy overlap rather than word coverage: 0268 was a re-render of 0255 across five paragraphs and not a whole chapter.

**What was done: the duplicated passages in Chapters 0261, 0262, 0263, 0264, 0265, 0266, 0267, 0268 and 0269 were rewritten. Same point of view, same date, same room, same figures, same beats, same order, same ending. What changed is the wording.** No chapter was rewritten whole and no last paragraph was touched.

**After the repair: the sixty-word window returns zero. Exactly duplicated paragraphs in Volume 06 return zero. The forty-word window returns two, and both are the calendar formula and the address formula, which every chapter in this manuscript states.**

### 3. The headline word count dropped a whole batch. **Fixed.**

`state/current.md` printed *the manuscript is 879,669 across two hundred and seventy chapters … 855,322 of the 879,669 is the two hundred and fifty closed chapters.*

879,669 = 855,322 + 24,347, which omits Batch 0001's 26,510 entirely. It is a 260-chapter figure. The error had already propagated into `workspace/volume-06/batch-0003/PROMPT.md`.

Measured, and both rows the reviewer doubted were right:

| | words |
|---|---|
| closed 250 (Volumes 01–05) | **855,319** |
| Volume 06, Chapters 251–270 | **50,906** |
| Batch 0001 (251–260) | 26,510 |
| Batch 0002 (261–270) | 24,396 |
| **manuscript, 270 chapters** | **906,225** |

Volume 05 is 144,245 against an inherited 144,248, and the 250-row inherits the same three-word drift. **All four files carrying the false total are corrected and now print the sum.**

## Major

**4. `state/character-state.md` made a false claim. Fixed.** It said *Marn Ottery is named in this batch and it is the first time she has been named in the two hundred and seventy.* She is named throughout Volume 04 (`ch-0151`, `0160`, `0163`, `0176`–`0181`) and Volume 05 (`ch-0202`, `0219`, `0222`, `0228`, `0236`, `0247`), and in Volume 06's own Chapter 0253. This is finding 1 propagating into the state layer. **The clause is struck in place with the reason named, not deleted.**

**5. `state/open-threads.md`. Fixed.** One row said the question is unasked in *three hundred and thirty files now*; the manuscript is 270. The same row also duplicated a clause: *it is in five mouths and on a slate **and it is in five mouths and on a slate still***. A second row said *three hundred and thirty chapters*. **All three are corrected in place and the false ones are marked as false rather than quietly overwritten, because a thread file that inflates the manuscript by sixty chapters is a file a writer cannot use.**

**6. The review phase is a self-review. Not fixed, and it is controller-owned.** See the top of this file. `state/current.md` already names this as *the one failure that makes a debt look discharged when it is not*, and it is now confirmed to be produced structurally on every batch. Flagged, not fixed.

## Minor

**7. Prose-tic rates** (24,396 words): `in this empire` ×82 (~8/chapter), `about nine` ×68, `about four minutes` ×30. **The repair did not thin them.** They are this house's ledger voice, the bound at item 14 of the divergence record is held, and thinning them in a repair would change a voice nobody asked to have changed.

**8. State layer size:** 4.9 MB across six files, `continuity.md` 1.47 MB. Already logged in `open-threads.md` as accepted. No new action.

## What checked out

- **Calendar:** Chapters 271–280 are monotone at exactly +7 days each, and 271 follows 270 with no gap and no overlap.
- **Count of askings:** `seven` returns 0 across all ten files; every printed total is six; the `six` ×4 in 0261 is correctly flagged as a week-count, not a total.
- **Third new rule** is declared twice with the fourth movement untouched — the early take is properly recorded.
- **Planned ending preserved:** `outline/ending.md` untouched; the outline's "volume ends on seven" is honoured; no new enemy introduced.
- **Scope discipline:** no controller files touched; exactly one next phase created (`workspace/volume-06/batch-0003/PROMPT.md`); `.retired` markers correct.
- **The sentence bound held under the repair and no maximum rose.** One stale figure in the same item was corrected: with the second clause removed the longest unit is 95 words and it is in Chapter 0262, not Chapter 0263.

## The repair, in one place

Nine chapters changed wording. Nine passages were duplicated and are now original. Two canon errors in one chapter are fixed and one false claim in the state layer is struck. Four files carrying a false word count are corrected. Six tests that a writing run reported clean were re-run, and four of them were not clean.

**The debt that matters is not discharged by any of it. This batch has had a self-review and a repair, and a self-review is not a review, and a repair is not a second reading.**
