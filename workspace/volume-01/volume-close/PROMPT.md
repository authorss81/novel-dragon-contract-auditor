# Volume 01 Close — Manuscript Phase Prompt

## What this phase is

**Volume 01 is finished. `outline/volume-01.md` gives the chapter range as 1–50, and all fifty chapters exist as finished prose in `chapters/volume-01/`.** This phase does not write prose. It closes the volume: it measures the manuscript, builds the index a reader and a later batch need, hands continuity and open threads across into Volume 02, states the volume's question and the volume's answer, and writes a short retrospective on what the volume established and what it deliberately left open.

**This is the only phase Volume 01 gets. Do not create a Volume 02 batch directory, a Volume 02 outline, a Volume 02 batch-cards file, a Volume 02 prompt, or any further phase prompt. The Volume 02 outline is a separate phase and must not be written here.** If a prompt is dispatched that asks for Chapters 1–10, 11–20, 21–30, 31–40 or 41–50 again, or asks for Volume 02 chapters, it is a duplicate and must not be run.

## What you must not change

- **Do not rewrite, continue, trim or "improve" any chapter.** All fifty are finished prose and have been through three repair passes. If this phase finds a factual error, record it in `state/continuity.md` as an open repair item and leave the prose alone; a repair is its own phase.
- **Do not introduce a new canon rule.** Nothing in this phase may become canon unless it is recorded in `bible/` and in `state/continuity.md` in the same pass.
- Never edit `state/phase-ledger.json`, `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, or `opencode.json`.

## Read in this order

`AGENTS.md`, `NOVEL_SPEC.md`, `outline/series.md`, `outline/ending.md`, `outline/volume-01.md`, then `outline/batches/volume-01-batch-0001.md` through `volume-01-batch-0005.md` — **the batch goals and the "Notes for the next batch" sections of the five card files are the closest thing the project has to a plan history and they are worth reading whole.** Then `state/current.md`, `state/continuity.md`, `state/open-threads.md`, `state/batch-summary.md`, `state/character-state.md`, and `state/chapter-summaries.md`. Then Chapters 1, 10, 20, 30, 40 and **45 to 50 in full**, which is where the volume's last word actually is. Do not load all fifty chapters into the prompt; the summaries and the state files are the index.

## What this phase must produce

### 1. The word-count record

Measure every chapter the way the project has been measuring them, so the numbers are comparable and reproducible: `sed 's/[[:space:]]*$//' chapters/volume-01/chapter-00NN.md | wc -w`, for all fifty, plus the per-batch totals and the manuscript total. Record in a new section of `state/continuity.md`:

- the total across fifty chapters, and the per-batch totals for Batches 0001 to 0005;
- the average per chapter and the shortest and longest chapter, **named**;
- **the chapters that sit outside the band their batch was given**, named, with the reason. The honest ones are Chapter 10 (7,944) and Chapter 20 (7,007) from the two long early batches, and Chapter 46 at 4,279. **Chapter 50 is 3,933 against a 2,800–3,400 aftermath band and is over it deliberately**: the canon lock required that all five terms of the ruling be posted and the review found only the second on the page, so a five-terms block was added and the rest of the chapter compressed to pay for it. Say so, do not hide it, and do not treat it as a licence.
- a one-paragraph note on what the length profile means for Volume 02. The honest summary is that **the chapters that ran long are the ones carrying a hearing, an inventory, a signature or a batch climax, and the ones that ran short are the ones carrying one room and one decision**, and that Volume 02 should aim at 3,200–4,000 a chapter with 2,800–3,400 for aftermath and about 4,200 allowed for a hearing.

### 2. The chapter-summary index

Add a single index to `state/chapter-summaries.md`, at the top or immediately under its existing preamble: all fifty chapters as a one-line table — number, title, POV, the date span, and a three-to-eight-word description of what the chapter does. This is the file a later batch reads when it needs to know what a chapter was about without loading it. Keep the existing per-chapter entries; do not delete or rewrite them.

### 3. The continuity handover into Volume 02

Append one clearly headed section to `state/continuity.md`, and nothing that contradicts anything above it. It must carry, each with a named holder where one exists:

- **The two printed documents, still two.** The MC/FS circular (series MC/FS, Standing Office of Provincial Continuities, base issue of the second month of this year run five hundred and sixty, amendment sheet of the twenty-second of the ninth run **nine hundred and forty**, carrying the Mosswake public-necessity sentence verbatim under a note permitting a court to adopt it or any other wording) and the **First Seat quarterly return** (a permission, not a crime, whose correct use is administrative). **No document connects them. No character knows both exist except Marek Kest and Tamsin Rook.** The circular was named but **not produced and not examined** at the Cinder Court.
- **The Cinder Court's four orders**, verbatim in substance, and exactly what they bind: the first binds that court and any court taking a recognition from it and does not reach back to a district decision already made; the second records the sentence as model wording and not a decision of any court and does not withdraw it anywhere, because only the district that stated it can withdraw its own practice; the third suspends sixty-one certificates on the registrar's own authority and puts a mark in a public minute book as a mark; the fourth escalates the sealed instruction to a full sitting with jurisdiction **on the court's own motion over the applicant's objection**.
- **The entry by device**, and its operative line: where a document bears the seal of a seat and no name, the seat is entered as a respondent by its device, no person of or belonging to it is party, cited or examinable, and **no inference of any kind may be drawn from the fact that a person has not been named.**
- **The sixty households of the sixth year** whom the Mosswake court named in a minute and did not name, and which nobody has yet gone looking for.
- **The pattern of five offices**, and the sentence that matters: four can no longer do harm, the third can do it again tomorrow, and there is nobody in it and it is not a person.
- **The custody chain, unchanged:** the Venn source leaf is in the Notaries' Table's cabinet in Auremar and did not move in this volume; the provincial hold carries no office name; the First Seat's device was first named aloud in open court on the twelfth of the ninth month of last year; **the second sealed page is shut with the second recorded decision not to open it and there is no third refusal**; the counting-house mark is a mark and not a name; **the red stitch, the thread in the form's fold, and the working stitch in the Ashfall bundle are three different things and no two of them may be joined in a sentence**, and Marek's prohibition of the eighteenth of the ninth month stands.
- **The calendar**, so that Volume 02 does not re-derive it: the volume runs from the seventh of the ninth month of the ninth year to the twenty-second of the eighth month of the year after it, in five batches, with the Batch 0005 calendar already in the file and the four repair passes already recorded at the head of it.
- **The two documents-must-not-be-merged rule and the four-lines-and-sentence-have-different-ages rule**, restated for Volume 02 in one line each, because they are the two rules most likely to be broken by accident.

### 4. The open-thread handover

Rewrite `state/open-threads.md` so that every row is stated in the present tense, every payoff target is a **Volume 02 or later** target or an explicit em dash, and **no row still points at Chapters 41–46 as future work.** Keep the three sections the file already has: the thread table, what the volume answered, what it deliberately left open, and the current blockers. Every Volume 01 thread that is genuinely closed says so and is marked `—`. Do not delete a thread because it is inconvenient; a thread with no payoff target is still a thread.

### 5. The volume's question and the volume's answer

Add one section to `state/current.md` headed **Volume 01, closed.** It must state, in plain sentences and without a list of motifs:

- **The question the volume asked:** *why does the same substituted language appear in three provinces, in a broker's records, and in Ilyra Kest's private file, and what authority is behind the sealed First Seat instruction?* — taken from `outline/volume-01.md`.
- **The answer the volume gave,** which is deliberately a **narrower answer than anybody wanted**: nobody names anybody; two courts have now recorded in writing that they do not know and cannot compel; the sentence is model wording and not a decision of any court, and the district that stated it has not withdrawn it; the mechanism is a **list of five offices**, four hundred miles apart, each of which did exactly what it was required to do, and a list of offices is a route and not an answer.
- **The smaller question the volume actually answered,** which is the one that turned out to be the volume: *who is helped by quiet?* — answered in the negative, in a furnace town, by a trade, and the finding is that a document nobody can produce is not a defect in the system but the system working as designed.
- **The sentence the volume is a book about**, in the words of the closing page: *there is not one line of it that says I was right.* The volume's last image is the roll-call; the red thread is the route it ends on, and **the two are not the same thing and the divergence between the batch goal and the Chapter 50 card is already recorded in `state/continuity.md`.**

### 6. A short retrospective

Append to `state/batch-summary.md` a final section headed **Volume 01, retrospective**, of **no more than eight hundred words**, covering:

- **What the volume established**, as four or five findings in the form the volume found them in — *a district that obeyed a form is not safe, it is quiet, and quiet is the injury*; *a person must be heard and must sign before a guarantor duty attaches*; *a printed sentence is a record of a document and not a record of a law*; *a number is a fact about the book and not about the document*; *a copy of a decision is a weapon and it is a target*; *the thing that travels is a person who turns up*.
- **What it deliberately left open**, with a named holder for each, and the eight open questions already listed at the foot of `outline/batches/volume-01-batch-0005.md`.
- **What the machinery of this project turned out to be,** in one paragraph: the corpus is institutional documents, the protagonist's power is useless in the plot, the wins come from ordinary competence, and the recurring form of every volume beat is a person being asked to say a thing out loud. Name two or three things that worked and one that did not.

## The quality gate for this phase

This phase is complete only when all of the following are true.

- Fifty word counts exist, are reproducible by the stated command, and the outliers are named with reasons rather than left for a reader to find.
- The chapter-summary index covers **all fifty chapters** and every entry in it is correct against the chapter it names.
- `state/continuity.md` carries a Volume 02 handover section, and **nothing in it contradicts anything above it in the same file.**
- `state/open-threads.md` has **no row** that still points at Chapters 41–46 as future work, and every open thread has a payoff target or an explicit dash.
- `state/current.md` states the volume's question, the volume's answer, the smaller question the volume actually answered, and the volume's closing sentence.
- `state/batch-summary.md` has a Volume 01 retrospective of no more than eight hundred words.
- **No chapter file was modified.** `git status` shows changes only under `state/`, `bible/` and `workspace/`.
- **No Volume 02 directory, outline, cards file or prompt was created.** `workspace/` contains `phase-000-bootstrap`, `phase-001-outline`, `phase-002-batch-plan`, and `volume-01/batch-0001` through `volume-01/batch-0005`, plus this `volume-01/volume-close/`, and nothing else.
- A reviewer has checked the result against this list.

## If something is wrong

If the measurements, the index or the handover disagree with the manuscript, **the manuscript wins and the state file is wrong.** Correct the state file. If the disagreement is a factual error inside a chapter, do not fix the chapter: record it in `state/continuity.md` under a heading naming it an open repair item, with the chapter, the line, what it says and what canon says, and stop. A repair is a separate phase and it must not be smuggled into a close.
