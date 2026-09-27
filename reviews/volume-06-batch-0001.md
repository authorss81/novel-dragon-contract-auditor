# Review: Volume 06, Batch 0001, Chapters 251 to 260

Phase reviewed: the writing run that took `workspace/volume-06/batch-0001/PROMPT.md`, commit `9ae089f`.
Reviewed: 2026-09-27, against the committed phase changes.
Repair phase: the run that read `logs/batch-0001.review.log` and applied what it could. Its record is the newest section of `state/current.md`.

This file is persisted here because `logs/` is gitignored. The reviewer's own output was never committed, and a review that exists only in an untracked log is a review the next run cannot inherit.

## The finding that governs every other finding here

**The review gate is not running an independent reviewer, and this review is not independent.**

`scripts/novel_runner.sh:273` dispatches the gate with `opencode run --agent novel-reviewer`. `.opencode/agent/novel-reviewer.md` declares `mode: subagent`. The runtime refuses a subagent for a top-level `run` and falls back to the default agent, which is the writing agent. The fallback warning is the first line of `logs/batch-0001.review.log`, and it appears nine times in that file.

Four consequences, all verified rather than argued:

1. The agent grading the writing is the writing. The reviewer's own frontmatter sets `edit: deny` and `bash: deny`; the fallback runs with both allowed, so "do not edit files" is prompt text and not a permission.
2. This is the project's own named failure mode, and it is now produced structurally on every batch regardless of writer discipline. `state/current.md` and `state/continuity.md` both carry the standing line that a self-audit reported as a review makes a debt look discharged when it is not. The runner now generates that artefact on every pass.
3. The gate that consumes the review is a keyword match on the reviewer's prose, `grep -qiE 'finding|problem|issue|contradiction|repetition|outline-like|meta'`. It is near-always true, and it also fires on a passing review that merely discusses findings. Whether the repair phase runs is arbitrary.
4. The model probe at `.github/workflows/novels.yml:64` uses the same `--agent novel-reviewer` and so falls back silently too, which is why the model probe did not catch it.
5. `logs/batch-0001.review.log` is a concatenation and not one run: the fallback warning is repeated and the dispatch line appears at both line 1199 and line 1261. There is no single authoritative review transcript, and only one `## Review:` heading is present, at line 1298.

**The fix is one line of frontmatter, `mode: primary` on `novel-reviewer`, or dispatching it as a real subagent. Both `.opencode/agent/` and `scripts/` are controller-owned and neither was edited. This needs a controller owner. No review in this project is to be called independent until then, and every second reading owed in the state files is owed for the same reason.**

## Discharged by the repair phase

**`NOVEL_SPEC.md` was seventy chapters stale and actively misdirecting.** `AGENTS.md` puts that file first in reading order for every run. It claimed one hundred and ninety chapters and 680,492 words, Volume 04 open and forty chapters in, and named Volume 04 Batch 0005 as the live next phase. The truth is two hundred and sixty chapters and 881,832 words, Volumes 01 to 05 closed, Volume 06 open and ten in, and Volume 06 Batch 0002 at `workspace/volume-06/batch-0002/PROMPT.md` as the one next phase. The Status block is corrected; the premise, the ending, the length target, the relationship policy and the power rule are untouched, because none of them was wrong.

This is the second time this file has drifted and the second time it has been corrected in place. It is on no refresh path, so it will drift again, and the next run that reads it first should check its chapter count against `find chapters -name 'chapter-*.md' | wc -l` before trusting it.

**Review output was not persisted anywhere in the repository.** `reviews/README.md` is tracked and says review files will be created after the first batch, and no such file existed. This file is that file.

## Carried, controller-owned, not fixed

`state/phase-ledger.json` still reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0`, with one entry, at more than twenty phases out of date. It is controller-owned and is flagged only. The novel-reviewer defect above and the concatenated review log are in the same category and travel together: all three are in the runner and the agent definition, and no writing phase can reach any of them.

## Recorded, measured, and not applied

**The sentence bound's headroom rests on one clause of its own pinned method, and this is now verified rather than reported.** Reading A splits on a terminator plus a space plus a capital, quotation mark or asterisk, and on a terminator immediately followed by a closing quotation mark or asterisk. The second clause is load-bearing because the prose sets `**bold**` on most paragraph openings, so a sentence ending in emphasis is split by it and by nothing else. Re-run on the ten files: with the clause, the longest unit in the batch is 88 words in Chapter 0258 and nothing anywhere reaches a hundred; without it, the longest unit in Chapter 0258 is 127 words and exactly four chapters breach, 0251, 0252, 0254 and 0258. The reviewer's figure reproduced to the word and to the file.

**One figure in the batch record did not reproduce, and it is left standing because two measurements agree against one.** The record gives 1,104 sentences under Reading A. A re-implementation of the pinned definition returned 964 while returning the maximum, 88 in Chapter 0258, exactly. The maximum is therefore robust across the details varied and the total is not, which is the more useful half of the answer and the reason the method's remaining loose joint, how lines inside a paragraph are joined and whether emphasis markers are stripped before counting, is now written down. This is a defect in the method's specification and not in the prose, and the bound stands and is not revised by it.

**Chapter titles run 87 to 121 characters and are declarative summaries that pre-tell the chapter's outcome.** They read as plot blurbs in a table of contents. Not applied, for a reason worth stating rather than leaving implicit: the pattern runs the length of the manuscript, two hundred and fifty chapters of closed prose are sealed and may not be reopened, and retitling only Volume 06's ten would replace one inconsistency with a sharper one. It is carried as a craft item for a decision that is not a batch's to take.

**The state layer is no longer compact.** Six files, just under 5 MB as last measured, and `state/continuity.md` is 1.46 MB, which is roughly 5.6 KB of state per chapter, with the newest sections running long and heavily marked up. `AGENTS.md` asks for compact and useful. The `grep -n` and read-range cap does work and nothing is breaking, so the archive was not rewritten: these files are the project's memory, they are append-only by design, and a compaction would destroy the record that lets a run say what it inherited and what it changed. What the repair can control is the size of what it adds, and this repair adds a short record rather than a long one.

**The retired `workspace/volume-06/volume-06-outline/PROMPT.md` contradicts itself** on whether the outline phase may create a batch directory, one line forbidding it against three requiring it. Already recorded as an open thread by the outline repair and correctly left unedited, since that file is the record of a phase that has run.

## What was checked and found correct

Every measured figure in the new state record was re-run rather than trusted, and the batch's self-audit is clean. Volumes 01 to 05 read 202,117, 184,039, 176,097, 148,821 and 144,248, Volume 06 reads 26,510, and the manuscript reads 881,832, which is 855,322 across the five closed volumes plus the open one. Under Reading A there is no sentence of a hundred words or more in the batch and the longest is 88 in Chapter 0258. Emphasis runs 8.3 to 12.5 per cent of text with a median near 10.1, inside the fifth-of-a-chapter bound. The phrase `this year` returns zero across the ten files. Five whole-word month names occur and all five are the modal verb *may*. The count of askings is six and the numeral appears only on the page of Chapter 0258 and twice in Chapter 0259, with `seven` absent from the volume, which is what the outline requires.

Phase mechanics hold. Exactly one next phase exists and `batch-0001/` carries `.retired`. The card file was written before the prose. No closed volume was touched, no post, commission, warrant or new heading was opened, and the owed reviews, being Volume 04's Batch 0005 and second readings of Volume 05's Batches 0003, 0004 and 0005, are carried and not falsely discharged. Batch 0002's ten week-anchors progress from Chapter 0260 with no year slip, which is the exact defect class the Volume 06 outline repair fixed.
