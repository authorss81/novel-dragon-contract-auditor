# FIFTH AUDIT: THE PAID SECOND READING OF VOLUME 05, BATCH 0003, CHAPTERS 0221 TO 0230 — THE NINTH DISPATCH, WHICH FOUND NOTHING NEW AND CONFIRMED EVERYTHING CHECKABLE

**Who wrote this, and what it is not.** This is an audit of a review, not a review. `reviews/volume-05-batch-0003.md` was written at `2359f84` and paid at item 268; it was audited at item 275, verified at item 279 in `reviews/volume-05-batch-0003-verification.md`, confirmed at item 280, third-audited at item 283 in `reviews/volume-05-batch-0003-third-audit.md`, and fourth-audited at item 290 in `reviews/volume-05-batch-0003-fourth-audit.md`, which found one new prose defect and corrected the third audit's year-term marginal. It was written by the same agent that writes the state sections this run, and **nothing in this file may be cited as an independent finding** — the review gate remains a controller-owned defect at item 171. What it has that a scan does not is that all ten chapters were read end to end, a seventh pass over this page, and every checkable figure was re-derived with the command beside it rather than carried.

**Why this range.** `outline/volume-12.md`, at its close, names four owed reviews, and this is the second of them: the owed second reading of Volume 05's Batch 0003. This run was handed the prompt for it at `workspace/review-debt-0001/PROMPT.md` and found it paid six times over. Per item 275A's standing it wrote no second review, amended no paid file, and marked no prompt.

**Base, resolved and asserted before any figure was taken from it.** `git log --oneline -- chapters/volume-05/chapter-022[1-9].md chapters/volume-05/chapter-0230.md` returns `18e57c8` (*save review fixes batch-0003*) and `7a54b16` (*save writer work batch-0003*) and nothing else. `git show 18e57c8:chapters/volume-05/chapter-<each of the ten> | wc -c` returns 14465, 13200, 12889, 14056, 14323, 14960, 13221, 13046, 13878 and 14020 bytes, ten out of ten non-empty, which is item 265E's check. `git diff --numstat 18e57c8 -- chapters/volume-05/` returns nothing for these ten — the only deltas under that base are Batch 0004's ten files, insertions with zero deletions. `git log --oneline --grep="prose-repair" -- chapters/volume-05/` returns nothing, so Volume 05 has never been through the prose repair and **every line number below is a citation of a text and not of a position**. All ten chapters read end to end, once each.

**What this run did not do.** It opened no chapter for edit. Volume 05 is a closed volume, every defect named below lives in prose only a phase with delete or substitute authority can touch, and **this run had none and did not take any.** It edited no outline, repaired no prose, planned no volume, opened no `outline/ending.md`, edited no `tools/measure.py`, wrote no `state/complete.md`, and created no Volume 13.

---

## Section one — nothing new, and the two candidates cleared on the page

Two candidates this run examined and withdrew, with the readings printed so a tenth pass does not re-raise them:

**One, `chapter-0224.md:123`'s *"it is nine words"* is unmeasurable and therefore not a defect.** Bess Tarrant's letter is summarised — *"it is four lines"* — and its nine words are never printed, so no span exists to count. Under the standing the first owed review establishes, an *N words* claim may be reported only where the quoted span is so far from N that no plausible convention reaches it; where there is no quoted span there is nothing to test. The letter's four lines are printed in paraphrase at `:119-:121` (a name; that Orla Denning never looked for Marek Kest; that a woman of sixty-three says the name on purpose; that the recipient should not write it down), which is consistent with four lines and four is not a count this run can falsify.

**Two, the *"five"* at `chapter-0222.md:15` is five visits and not five askings.** *"You have come four times since the first month," ... "Five." ... "And you have not asked me anything in any of the five"* — the five counts comings, each explicitly an occasion on which nothing was asked. The count of things asked out loud in this matter is four in every chapter of this range that states it (`0221:105`, `0223:121`, `0225:45`, `0225:144`, `0226:134`, `0228:114`, `0229:36`, `0230:99`), and no chapter of this batch makes it five. The Chapter 0250 turn is untouched from this side.

---

## Section two — every checkable figure re-derived, with the command beside each

| Figure | Result | Command |
|---|---|---|
| `about nine` per file, card's own word-boundary-minus-`about nine hundred` method | **5, 7, 4, 5, 6, 6, 6, 3, 6, 8 = 56, range 3–8, median 6.0**, against the card's 72 | `grep -o -i "about nine\b" <file> \| wc -l` less `grep -o -i "about nine hundred" <file> \| wc -l`, one file at a time; raw per file 9, 8, 6, 6, 7, 8, 8, 7, 7, 8, subtractions 4, 1, 2, 1, 1, 2, 2, 4, 1, 0 |
| Month/weekday lock | **0 month names, 0 weekday names**; whole-word `may` **13 hits on 12 lines across six chapters** (0222, 0223, 0224, 0225, 0228, 0229), every one read in place the modal verb, capital `May` 0 | `grep -n -i -w "january\|february\|march\|april\|june\|july\|august\|september\|october\|november\|december\|monday\|tuesday\|wednesday\|thursday\|friday\|saturday\|sunday" <the ten>` returns nothing; `grep -n -w -i "may" <the ten>` returns the 12 lines, `0222:73` carrying two |
| Words per file | **3011, 2758, 2714, 2956, 3018, 3164, 2763, 2754, 2919, 2975 = 29,032** | `wc -w <file>`, one file at a time |
| Volume 05 / manuscript | **144,248 / 1,496,548 in 620 files**, unchanged | `python3 tools/measure.py words --volume 05`; full `words` run; `selftest` PASS |
| The five located prose defects | all seen on the page: `0226:7` *she am*; doubled `---` at `0226:49-50` and `0229:19-20`; leading space inside the opening quote at `0221:57`; doubled blank at `0228:108-109` | `sed -n '7p'`, `grep -n "^---$"`, `sed -n '57p'`, consecutive-blank scan returning exactly the one hit at 108–109 |
| `certif` / `exception` / `precedent` | **2 / 0 / 0**; both `certif` hits (`0223:5`, `0227:21`) are negations — *nothing he could certify anything with* | `grep -n -i "certif"`, `grep -n -i "exception\|precedent"` over the ten |
| `four hundred and thirty` / `four hundred miles` | **14 occurrences** (1, 1, 2, 5, 2, 1, 1, 1 across 0223–0230; 0226 carries 5 on 3 lines) / **0** | `grep -o "four hundred and thirty" <the ten> \| wc -l`; `grep -n "four hundred miles" <the ten>` returns nothing |
| Lowcross bill | **nineteen pounds three and fourpence, unpaid, nobody liable**, at `0229:15`; repeated without the place-name at `0229:128` and `0230:91` | `grep -n "nineteen pounds" <the ten>` |
| Guarantee | standing offered and unanswered, **word `guarantee` 6 hits in 2 chapters** (`0229:130`, `0230:11`, `:15`, `:25`, `:73`, `:101`), bank about four hundred and forty foot, about sixty children under sixteen | `grep -n -i "guarantee" <the ten>` |
| Rate language | reader of seventeen on a written engagement, unnamed, unthanked, not starting, at `0229:96` and `0229:130`; no elapsed period computed from it here | `grep -n "seventeen" <the ten>` |
| `the book` / `the books` | **18 / 3** (books at `0226:5`, `0226:11`, `0229:5`); the card's twenty-one requires both counted together | `grep -o -i "the books\?" <the ten> \| sort \| uniq -c` |
| `thirty-one` | **0** in this range; the Mosswake figure is not contradicted here | `grep -n -i "thirty-one" <the ten>` returns nothing |
| Dated askings | itemised at **`0223:121`, `0224:111`, `0226:134`, `0228:114`**, and not in the chapters the card names — item 279's fault D, confirmed | read in place |

The fourth audit's prose defect (`0226:60`, knowledge 317 days before the fact) and its year-term correction were both read on the page and stand unaltered; the page has not moved since `18e57c8`. Items 279's faults A–E and 290's marginal at `0226:82` (the woman of about sixty-four, sole holder of that age in Volume 05) are recorded and untouched.

---

## Section three — state of the frontier, and no prompt created

The prompt this run was handed directs it to write `workspace/review-debt-0002/PROMPT.md` for Volume 05's Batch 0004 at base `65abf1d`. **That file exists at 9,722 bytes and its work is paid** — `reviews/volume-05-batch-0004.md` at `5316a4f` (item 270A), verified at items 276 and 277 — and rewriting it would overwrite a paid prompt with a duplicate of itself, per items 275C, 276E, 277C, 279D and 280C. **No prompt was created and no marker was written**, on `PHASE_SYSTEM.md` line 216.

The frontier as this run read it: `workspace/review-debt-0001/` (this range, paid at 268, audited at 275, 279, 280, 283, 284 and here); `workspace/review-debt-0002/` (Batch 0004, paid at 270A); `workspace/review-debt-0003/` (Batch 0005 at base `dedc831`, live, `reviews/volume-05-batch-0005.md` not existing); `workspace/review-debt-0004/` (Volume 06's Batch 0003, now prompted, no review file on disk). **This run moved none of the four.** `state/complete.md` does not exist and this run did not write it; `state/phase-ledger.json` is a controller file, was not edited. No chapter was opened for edit, no outline was opened for edit, `outline/ending.md` was not opened, `tools/measure.py` was not edited, no paid review was amended, no volume was planned and no Volume 13 was created.

**THE ITEM IS 291.**
