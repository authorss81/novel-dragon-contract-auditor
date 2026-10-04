# REVIEW: VOLUME 05, BATCH 0005, CHAPTERS 0241 TO 0250 — THE FOURTH OF THE FOUR OWED REVIEWS

**Who wrote this, and what it is not.** This is a review of ten finished chapters in a closed volume. It was written by the same agent that wrote the state files this run, and **nothing in this repository's review gate is independent** — the gate has fallen back to the writing agent every time it has been asked, and `NOVEL_SPEC.md` and `state/open-threads.md` item 171 both say so in terms. **No sentence in this file may be cited as an independent finding.** What it has that a scan does not have is that all ten chapters were read end to end, and that every claim in `outline/batches/volume-05-batch-0005.md` tested here was tested against the page with the method printed beside the figure.

**Why this range.** `outline/volume-12.md`, at its close, names four owed reviews and says *which is four and not three*: one owed review of Volume 04's Batch 0005, and owed second readings of Volume 05's Batches 0003, 0004 and 0005 and of Volume 06's own Batch 0003. The first is paid at `reviews/volume-04-batch-0005.md`, the second at `reviews/volume-05-batch-0003.md`, the third at `reviews/volume-05-batch-0004.md`. **This is the fourth, and it is the last of the four on Volume 05.** Volume 05 has never been through the prose repair — `git log --oneline --grep="prose-repair" -- chapters/volume-05/` returns nothing and `git log --oneline --grep="prose repair" -- chapters/volume-05/` returns nothing — and none of these ten files has been edited since `dedc831` (*save review fixes batch-0005*), so **every line number below resolves**.

**The precheck, and the trap in it.** `git log --oneline -1 -- chapters/volume-05/chapter-024[1-9].md chapters/volume-05/chapter-0250.md` returns `dedc831`; `git cat-file -e dedc831:chapters/volume-05/chapter-<each of the ten>` returns **PRESENT ten times out of ten**; `git diff --numstat dedc831 -- <the ten files>` returns **nothing**.

`python3 tools/measure.py lifts --volume 05 --first 241 --last 250 --base dedc831 --min 8` returns **`ADDED 0 prose lines`** against a `BASELINE` of 481, which is a second and independent confirmation that these ten files carry no repair-added prose.

**The trap, and it is the same trap the third of these reviews walked into in reverse.** `git diff --numstat 65abf1d -- chapters/volume-05/` returns **1,226 insertions and 2 deletions over thirteen files**, of which **1,224 insertions and 0 deletions are on `chapter-0241.md` to `chapter-0250.md`** and the remaining `1 −1` twice are on `chapter-0224.md` and `chapter-0228.md`. `65abf1d` is Batch 0004's base and **is not this review's base.** A reader who runs the volume-wide command sees 1,226 lines of movement and concludes the volume has moved; the ten files this review owns have not moved by a line, and the command that settles it is the one run over the ten files alone. **Item 203's standing, read from the wrong end, has now caught a prompt as well as a phase** — and note that the prompt that commissioned this run printed the volume-wide figure as *1,224 insertions and 0 deletions*, which is the figure for the ten and not for the volume, so the prompt and the review disagree by two insertions and two deletions and **both are wrong about what they measured.** The correct statement is the one in this paragraph: **1,224 insertions on the ten, 1,226 on the volume.**

**What this phase did not do, and it is the important half.** It opened no chapter for edit. Volume 05 is a closed volume, every prose finding below is in text only a phase with delete or substitute authority can touch, and **this run had none and did not take any.** It edited no outline, and `outline/batches/volume-05-batch-0005.md` is an outline file, so the nine record defects in section two are reported and not repaired. It planned no volume, opened no `outline/ending.md`, added no Volume 13, wrote no chapter prose, repaired no prose, wrote no `state/complete.md`, edited no controller file, and did not change `tools/measure.py`.

---

## Section one — sixteen prose defects, all located, all needing authority this run does not have

**Every finding below is a figure against another figure, and not one of them is a repetition.** That is the class `reviews/volume-05-batch-0004.md` section one and `reviews/volume-05-batch-0003.md` section two both record as invisible to this repository's instruments, because a contradiction shares no run with the line it contradicts. **Sixteen in ten chapters, in a batch whose own card reports at item 33 that six of its nine mechanical tests returned zero on a batch that had six kinds of real damage in it, is the largest per-chapter rate of located prose defect in the four reviews paid so far.**

### One. The same room is four hundred and thirty miles UP this river in three chapters and four hundred and thirty miles DOWN it in the fourth

> **chapter-0242.md:103** — "**So a woman of twenty is four hundred and thirty miles up this river in a room two streets off a street that goes down to the river road with sixteen books on a table**"
> **chapter-0248.md:145** — "**And a woman of twenty is about four hundred and thirty miles up that river with sixteen books**"
> **chapter-0250.md:83** — "**The other one is still in one too.** She is about four hundred and thirty miles up this river in a room two streets off a street that goes down to the river road, with sixteen books on a table"
> **chapter-0244.md:53** — "And I have worked out, **in a rented room in a city about four hundred and thirty miles down this river**, in about nine minutes, that a person who knows what a document says is a person who can be served with it"

It is one room and it is identified three times over: *rented by the week*, *two streets off a street that goes down to the river road*, *sixteen books on a table* — `chapter-0244.md:3`, `chapter-0242.md:103` and `chapter-0250.md:83` give the same three particulars. **Three chapters put it up the river and one puts it down, and the one is `chapter-0244.md`, which is the chapter that opens it.**

The direction is not left in doubt by the batch itself. `chapter-0244.md:115` places *a foreman off a dye end in this city* — this city, the city of the room — and `chapter-0249.md:57` puts the dye end *"in a room in a lane in a furnace town about four hundred and thirty miles up this river from Auremar"*. **So the room is in the furnace town, the furnace town is up the river, and `chapter-0244.md:53` is the single line in the batch that says otherwise.** It needs one word changed. Left, recorded.

Command: `grep -n -o -E ".{0,60}four hundred and thirty miles (up|down|up that) this river.{0,60}" chapters/volume-05/chapter-024[1-9].md chapters/volume-05/chapter-0250.md`, and the two rooms read against each other.

### Two. `chapter-0244.md:115` gives a second book-keeper the first book-keeper's inventory

> **chapter-0244.md:5** — "Nell Kest is twenty. She is a dye-house worker … and **she keeps the books of eleven houses on a lane in this town and of four other houses in three other districts**"
> **chapter-0244.md:115** — "**A book-keeper about four hundred and thirty miles down this river keeps the numbers of eleven houses on a lane and of four houses in three other districts**, and is not on the list of works and has never been on it."

Eleven houses on a lane plus four houses in three other districts is Nell Kest's inventory, and it is fifteen of her sixteen books — `chapter-0244.md:3` and `:65` both give sixteen books with fifteen somebody else's. The book-keeper of `chapter-0244.md:115` is a **different person**: `chapter-0244.md:31` introduces him as *"A book-keeper about four hundred and thirty miles down this river worked out before the year turned that the days **he** spends on other people's numbers are not paid … and **he** has been on that bank two years"*. A woman of twenty in a rented room and a man on a bank two years are two people, and the closing roll-call has handed the first one's eleven and four to the second.

**The three-part phrase the roll-call shares with line 31 is verbatim** — *"A book-keeper about four hundred and thirty miles down this river"* and *"is not on the list of works and has never been on it"* — so what is new at `:115` is exactly the clause that is wrong. Measured: `difflib.SequenceMatcher(None, tokens(0244:31), tokens(0244:115), autojunk=False)` returns a longest shared run of **29 tokens**, and the inventory clause sits outside it.

### Three. `chapter-0241.md` states that the four cannot be written down, and then has them written down twenty-four lines later

> **chapter-0241.md:29** — "**You cannot write them down and you cannot have them written down, and if anybody writes them down then the first thing that goes on the paper is a heading**, and a heading over four things turns four things into a practice."
> **chapter-0241.md:79** — "**What you cannot write down is the four, and I am not being careful, I am being exact**"
> **chapter-0241.md:81** — "**Write the number. Keep the four in your head.**"
> **chapter-0241.md:103** — "**The man of about thirty-four wrote the four on the inside of his own hat**, and that is the only place any of them has ever been."
> **chapter-0241.md:105** — "…because **a man who has only had it in his head for twenty minutes** is not going to get it right a second time either…"
> **chapter-0241.md:129** — "…with a number on the back of his own hand and **four things in his head** that are in no document in this empire"

Five statements and they do not agree. The four are **in his head** at `:105` and `:129` and **on the inside of his hat** at `:103`, and `:103` sits twenty-four lines after the rule that forbids it and eight lines after the instruction to keep them in his head.

**This is the chapter's whole subject and it is the batch's longest sentence.** `chapter-0241.md:79` is the longest sentence in the batch at **89 words** on the card's own method and on mine, and it is the sentence that states the rule the chapter then breaks — a batch that spent a repair pass splitting sentences to get under ninety left its load-bearing prohibition in the longest sentence in the batch and then contradicted it in the next scene. Left, recorded.

**One thing in the chapter's favour and it is not nothing:** a hat is not a document, so `:129`'s *"in no document in this empire"* survives `:103` on its own terms, and a reader can reconcile the pair that way. **What cannot be reconciled is `:105`**, where the man has them *in his head for twenty minutes* and has therefore read them back off his head, in the same paragraph in which he has written them on a hat and read them back off the hat. That is one sentence holding both readings.

### Four. `chapter-0241.md` gives the count of the two men's questions three incompatible ways

The chapter is two men in a bay counting, and it cannot agree on what it counted.

| Line | Speaker | The words |
|---|---|---|
| `:111` | man with the chain | "You have not asked me **the second question** yet." |
| `:113` | man of about thirty-four | "I have not asked you any question, **you have asked me three**." |
| `:115` | man with the chain | "**You asked me whether it costs anything, which was the second question**, and you did it in a bay…" |
| `:119` | man of about thirty-four | "You have not been asked anything in nine years and **I have just asked you three things**." |
| `:121` | man with the chain | "**You have asked me one thing and I have asked you two**, and we are both of us standing in a bay…" |

Two contradictions, both inside one scene and both inside one or two mouths. **At `:111` the second question has not been asked; at `:115` the second question is the cost question and has been asked** — four lines apart, same mouth. **At `:113` the man with the chain has asked three questions; at `:121` he says he has asked two** — eight lines apart, and `:119` has the other man agreeing with `:113` and not with `:121`.

**The page supports two of the three and cannot choose, and the choice is load-bearing:** the narration at `:7` and `:97` records exactly two questions from the man of about thirty-four (whether anybody had ever asked, and whether it costs anything), which makes the chain man's *two* at `:121` the reading the narration supports and `:113`'s *three* the one it does not. **But the chapter's own device is that the man who cannot read a paragraph is the only person who can hold a number in his head without writing it down, and this is the one number in the chapter he is not trusted to hold.** Left, recorded.

### Five. `chapter-0243.md` counts nine hundred entries in nineteen years five times and then says nine hundred entries a year

> **chapter-0243.md:15** — "…eleven books on a shelf in a room with a pane out of the window, and **about nine hundred entries in nineteen years**"
> **chapter-0243.md:37** — "**About nine hundred people** were entered in a box in this office before the year turned, and that figure is a clerk's own count off the back of **about nine hundred entries**"
> **chapter-0243.md:55** — "**About nine hundred entries** came in on about nine hundred sheets"
> **chapter-0243.md:67** — "**About nine hundred entries in nineteen years** came in on about nine hundred sheets"
> **chapter-0243.md:91** — "…there are **about nine hundred entries** in that book"
> **chapter-0243.md:117** — "She has read the second of those lines about nine hundred times … and **about nine hundred entries a year** would be very easy to stop."

Six statements of one figure. **Five of them are nine hundred in nineteen years, which is about forty-seven a year. The sixth, at `:117`, is nine hundred a year**, and it is a hundred and two lines later in the same chapter.

`:117` can be read as a counterfactual — *at a rate of nine hundred a year this would be easy to stop* — and if it is, the chapter needs a clause saying so, because the numeral is the same numeral the chapter has used five times for the actual count and a reader has no way to tell the two apart. **What no reading closes is the arithmetic**: the sentence is about the rate that would make the clerk's silence detectable, and the rate the chapter has established is forty-seven a year, so on the chapter's own figure the practice has been invisible for nineteen years for a reason the sentence does not give. Left, recorded.

### Six. Chapter 0249 raises the number of people who cannot read a paragraph from four to nine

The canon, and the volume's own lock, is **about four people in a bay who cannot read a paragraph and have never been asked once** (`outline/volume-05.md`, *the river, still running*). Three places in this batch hold it:

> **chapter-0241.md:129** — "and **the four who cannot read a paragraph** in that bay have still never been asked one question."
> **chapter-0250.md:103** — "**About four people in this bay cannot read a paragraph** and have never been asked what the hold is"
> **chapter-0250.md:125** — "**The four who cannot read a paragraph** have still never been asked one question"

Two places in one chapter raise it to nine, and the chapter's own title raises it to everybody:

> **chapter-0249.md:93** — "**Why is that worth saying to nine men who cannot read a paragraph?**"
> **chapter-0249.md:123** — "…has said one true thing out loud four times over to **nine men who cannot read a paragraph** and is not thanked and is not going to be."
> **chapter-0249.md:71** — "…the whole of why I have said this out loud four times **in a room where nobody can read a paragraph**."
> **chapter-0249.md:1** — the title: *"…In A Room Where Nobody Can Read It"*

**Eleven occurrences of the phrase in the batch**, at `0241:3`, `:97`, `:115`, `:129`, `0242:71`, `0249:35`, `:83`, `:93`, `:123`, `0250:103`, `:125`. Command: `grep -n -o -E ".{0,110}cannot read a paragraph.{0,60}"` over the ten files; `grep -c "cannot read a paragraph"` gives the per-file split **4 / 1 / 0 / 0 / 0 / 0 / 0 / 0 / 4 / 2**.

**And the chapter compounds it.** `chapter-0249.md:7` says its foreman *"is one of about four people in this matter who cannot be asked"*, which makes him the fourth; the same chapter then puts nine men in his dye end who cannot read. **The batch uses *cannot be asked* and *cannot read a paragraph* interchangeably — `chapter-0249.md:7` for the first and `:35`, `:83` for the second, in the same seven lines — and in this manuscript they are different things:** a person who cannot be *asked* is unfindable, and a person who cannot read a paragraph is one of a named four in a named bay. Nine men who cannot read in a furnace town is a count of nine in a batch whose canon is four, and one of the four is in a different room four hundred and thirty miles away. Left, recorded.

### Seven. `chapter-0249.md` dates one telling to the fourth month and the same telling to the third

> **chapter-0249.md:7** — "She told him **on a stair in about four seconds in the second day of the second week of the fourth month of the year after next**"
> **chapter-0249.md:107** — "…**a woman of twenty told me in a rented room in the second week of the third month of the year after next** to write it. Keep it and not send it … and **she made that reason up in about four seconds** and told me it was not a good one."

One telling, by one woman of twenty, on a stair outside a rented room, **in about four seconds** — and a hundred lines apart the chapter gives it two different months and puts it in two different rooms. `chapter-0244.md:3` establishes that the room *is* rented by the week and `:53` that it has a stair, so **the two accounts are of one occasion and differ by a month**, which on this volume's own calendar is four weeks. Left, recorded.

### Eight. The volume's last line counts five mouths and does not count the one it names as the first

> **chapter-0249.md:75** — "**A foreman of fifty-one said this exact question out loud in a shed in the fifth month of the year after next, and every man in that shed heard it** … And **for about four years that question has been in exactly one mouth.**"
> **chapter-0249.md:79** — "**I have said it in five**, and you have all of them … and now **there are five mouths** and none of them can be stopped and none of them can be written down."
> **chapter-0250.md:127** — "**And the largest thing anybody has said out loud in this matter is in five mouths and in no book at all**"

The volume's final line rests on a count, and the count does not include the mouth the same chapter names as the first. **One plus five is six.** Under the other reading — five *men* in the dye end, excluding the foreman and Halla Wray — the figure is seven, not five, because `chapter-0249.md:19` has four men told directly and `:21` a fifth who *"had heard it four times"* from them.

**And the chapter cannot agree with itself on the number of tellings either.** `chapter-0249.md:19` — *"he said it four times over about half an hour"*; `:23` — *"I am not asking you a fifth time because I have said it four times"*; `:71` — *"the whole of why I have said this out loud four times"*; `:123` — *"has said one true thing out loud four times over"*; and `:79` — *"I have said it in five."* **Four at four places and five at the one that carries the volume's closing figure.** Left, recorded.

### Nine. A number on the back of a hand lasts about a week, six weeks and seven weeks

The man of about thirty-four writes the count on his own hand. Four figures for how long it stays there, in two chapters:

| Where | The words | What it gives |
|---|---|---|
| `chapter-0241.md:87` | "**That is going to be on me for about a week** and then it will be gone" | **about a week** |
| `chapter-0248.md:7` | "…on the second day of the first week of the ninth month … **and by the fourth day of the fourth week of the tenth month it was not there any more**" | **about seven weeks** |
| `chapter-0248.md:45` | "**I have had the number on my own hand for six weeks** and it is gone" | **six weeks** |
| `outline/batches/volume-05-batch-0005.md` item 3 | "the number is gone in **about four weeks**" | **about four weeks** |

`:7` and `:45` are **in one scene** ninety-eight lines apart: the kitchen evening is the fourth day of the fourth week of the tenth month (`chapter-0248.md:23`), so `:7` has the mark surviving to that very day and `:45` has it gone six weeks earlier, which is the third week of the ninth month — a week *after* the man wrote it, not before. **And `:87`'s week is off by a factor of seven against the batch's own calendar**, which runs in counted weeks from the ninth month to the eleventh.

The card's *about four weeks* is a fourth figure and is not a rounding of any of the three. Left, recorded.

### Ten. `chapter-0248.md` tallies how many times he said the word three ways inside one scene and once more in Chapter 0250

> **chapter-0248.md:23** — "…he had said it out loud **to a door twice and to a wall once** and had got further with the wall."
> **chapter-0248.md:105** — "I do not know," he said. "And that is not a brave thing to say and **I have been not saying it for about six weeks**."
> **chapter-0248.md:125** — "…**I have said it to a wall** about nine miles from a forge **twice**."
> **chapter-0250.md:55** — "…he had said it **once in a kitchen** to a woman with a plate in her hand and **twice to a wall** nine miles from a forge"

`:23` and `:125` are the same evening and are three sentences and two hundred lines apart on the page. `:23` gives a door twice and a wall once; `:125` gives a wall twice and no door. **The two distributions have the same total and different shapes**, and the wall cannot have gone from once to twice because `:105`, between them, says he has *not* been saying it. `:55` then gives a third distribution — a kitchen once and a wall twice — which is the shape `:125` implies and not the one `:23` states. Left, recorded.

### Eleven. `chapter-0250.md:43` dates a September scene to the sixth month and calls it two months ago in the same breath

> **chapter-0250.md:43** — "A man of about fifty-five with a chain gave a better reason than that **in a yard in the third week of the sixth month of the year after next and he gave it two months before** you worked yours out … **And it is not better, and I have had about two months to be sure of that**…"

Chapter 0250 is the fourth day of the fourth week of the eleventh month. **Two months before is the ninth month**, and the yard in the ninth month is `chapter-0241.md`, whose date line is *the second day of the first week of the ninth month*. The third week of the sixth month is a **different yard** — `chapter-0241.md:121` names it, *"I said that to a book-keeper in a yard in the third week of the sixth month of the year after next"*, which is Batch 0004's scene and not the one the man of about thirty-four was in.

So the sentence carries two dates for one event, and **its own second clause settles which is meant**: two months, that is, the ninth month. The chapter has merged the sixth-month yard and the ninth-month yard. Left, recorded.

### Twelve. `chapter-0244.md:35` reports the fifth telling two months before Chapter 0249 stages it

> **chapter-0244.md:35** — "**And a foreman off a dye end in this city has said one true thing about himself out loud five times**, and **the fifth of them was to a boy of about nine with a slate**, and it is on a slate…"

Chapter 0244 is the fourth day of the fourth week of the **ninth** month. The only slate scene in the batch is `chapter-0249.md:43` — *"And the last thing in that end that week was a boy of about nine with a slate"* — and Chapter 0249 is the second day of the first week of the **eleventh** month. **A woman of twenty reports, in the ninth month and in her own mouth, that a telling has already happened which the volume stages in the eleventh month.**

This also puts the card's item 32 — *"a boy of about nine with a slate appears twice in the volume, and the page gives him a second one … six weeks later"* — in doubt: the first of the two cannot be in the ninth month, because the only slate scene in the batch is in the eleventh, and a telling cannot both be already reported in the ninth and be the fifth in the eleventh. **The card's own six weeks does not fit either**, since the ninth month to the eleventh month is about eight. Left, recorded.

### Thirteen. Nine hundred box-entries are dated three ways across three chapters

> **chapter-0242.md:39** — "I am not going to do it to **about nine hundred people in this empire who have been entered in one since the seventh month of the year after** by a class."
> **chapter-0243.md:37** — "**About nine hundred people were entered in a box in this office before the year turned**, and that figure is a clerk's own count off the back of about nine hundred entries"
> **chapter-0250.md:73** — "**About nine hundred of you since the year turned**, by a class, and that is roughly right because that is what a class does."

The same figure, the same agent — *a class* — and three spans. **Under this volume's own year convention** (`outline/batches/volume-05-batch-0005.md` item 15: *this year* is the year after, *last year* the year before it, *next year* the year after next) — *since the seventh month of the year after* and *since the year turned* are both **after** the turn and *before the year turned* is **before** it. **Two against one, and `chapter-0243.md:37` is the odd one** — and it is the odd one in the clerk's own mouth, as a count off the back of her own books, which is the one place in the batch where the figure would be knowable. It is also the sentence that `chapter-0250.md:73` has Halla Wray summarise, and she gets it the other way. Left, recorded.

### Fourteen. `chapter-0247.md:85` calls a nine-word question eleven words

> **chapter-0247.md:75** — `"What is the fourth thing on that board for?"`
> **chapter-0247.md:85** — "…**and you did it in eleven words** and you did not charge me a shilling for it…"

`m.TOKEN.findall` on line 75 returns `['What','is','the','fourth','thing','on','that','board','for']` — **nine tokens**, and nine on a whitespace split as well, so no convention reaches eleven.

**This is reported and it is below the threshold, and the standing says so.** `reviews/volume-04-batch-0005.md` section one item three establishes that an *N words* claim is reportable *only where no plausible convention reaches N*, and clears the device at 6 and 8 tokens and reports it at 21; `reviews/volume-05-batch-0004.md` section one item four reports it at 15. **Nine against eleven is a gap of two and is inside the band the two prior reviews set aside.** It is recorded here for two reasons and neither is that it is a large fault: it is a **self-measurement of a question printed ten lines earlier in the same chapter**, which is the class `reviews/volume-05-batch-0004.md` section two item nine did report, and **a gap of two on a printed self-measurement is the cheapest fault in this manuscript to fix and the easiest to let stand.** Left, recorded.

### Fifteen. A forty-nine-token run from Chapter 0242's closing paragraph into Chapter 0250's dialogue, and the batch is clean only above it

> **chapter-0242.md:103** — "…**four hundred and thirty miles up this river in a room two streets off a street that goes down to the river road with sixteen books on a table** and a wage that has been held since the second week of the third month of the year after."
> **chapter-0250.md:83** — "…**four hundred and thirty miles up this river in a room two streets off a street that goes down to the river road, with sixteen books on a table and a wage that has been held** since the second week of the third month of the year after."

Measured with `difflib.SequenceMatcher(None, tokens(a), tokens(b), autojunk=False)` over `m.prose_lines` for every one of the forty-five chapter pairs: **the longest shared contiguous run in the batch is 49 tokens, and it is this one.** The next four are 36, 26, 24 and 22. **A sliding 40-word window over the ten files, compared at every starting position across every pair, returns 10 duplicated windows — and all ten are the same run, because a 49-token run holds forty-word windows at ten separate offsets, so it is one region and not ten faults.** At 30 words the same scan returns 37, at 24 words 59, at 20 words 98 and at 16 words 216, all counted at every position. **At 60 words it returns 0, which is the card's test eight and is also true, and which is why the card is clean.** *Both counts are printed because a duplicate figure without its counting rule beside it is a figure nobody can check: at every position the forty-word figure is 10 and de-duplicated by non-overlapping region it is 1.*

**The card anticipates the inventory and does not record the run.** Item 41 says *"Chapter 0250 keeps the full inventory, because it is the last page of the volume and the one place it belongs."* That sanctions the inventory's presence. It does not record that Chapter 0242's **closing paragraph** is reproduced at forty-nine tokens inside a speech eight chapters later, and **a closing paragraph reproduced inside a speech is not a refrain** — the batch's refrains are counted separately at section three below, and this one is not one of them. Left, recorded; it needs delete or substitute authority.

### Sixteen. A thirty-two-token run between Chapter 0236 and Chapter 0247, and the refrain has now spread to seven instances

> **chapter-0236.md:82** — "A man of about forty came for a copy at about the fifth hour and paid fourpence and it took her about eleven minutes and she read it back to him twice and he read it back once and said thank you and she said that is the ordinary way and it is not a favour"
> **chapter-0247.md:109** — "Then a man of about forty came for a copy and paid fourpence and it took her about eleven minutes and she read it back to him twice and he read it back once and said thank you and she said that that was the ordinary way and not a favour"

**Longest shared run 32 tokens**, from *and paid fourpence* to *and she said that*. **The card's item 40 claims *"One beat was staged as fresh in three chapters and is now in two"* and repairs the *ordinary thing* beat across Chapters 0242, 0245 and 0250. It does not record this pair**, which is eleven chapters apart, in two different volumes' batches, and which is the **only actual thank in this batch** — the man of about forty at `chapter-0247.md:109`, against a lock that runs *nobody is thanked*. The lock holds for the matter and this is an ordinary copy service, exactly as `reviews/volume-05-batch-0004.md` section three recorded for the same beat at `chapter-0236.md:82`; **but the beat is now in two chapters word for word and the repair pass that reduced one refrain did not touch it.**

**And the refrain `reviews/volume-05-batch-0004.md` section one item one reported has grown.** That review found a nineteen-token duplication at `chapter-0238.md:125` against `chapter-0236.md:102`, and recorded that *the repair made the two lines identical in order to make them agree, and the agreement is the defect*. Measured on this tree, the sentence now stands **seven times in Volume 05** — `0223:83`, `0236:102`, `0238:65`, `0238:125`, `0243:107`, `0247:67`, `0248:83` — and **the batch before this one carried four of them and this batch carries three.** The repair has also split it: **the four earlier instances all read *every single one of them* and all three of this batch's read *every one of them***, with the frame varying between *in this empire*, *in this city* and *in these bays / at these counters / at this counter / in their time*. Longest shared run between this batch's own two, `0247:67` and `0248:83`, is **12 tokens**; between `0243:107` and `0248:83` it is **14**, and against `0236:102` it is **15**. **The repair reduced the duplication it was sent to reduce and the sentence has since been written three more times in a neighbouring batch, in a new variant, and the neighbour was never checked for it.** Left, recorded.

---

## Section two — nine claims in the batch record that the page does not bear out

`outline/batches/volume-05-batch-0005.md` is an outline file and this phase may not edit it. These are reported for a phase with that authority. **Every one of the first eight is a figure, and in six of the eight the prose needs nothing and the record is wrong** — which is `reviews/volume-05-batch-0004.md` section two item nine's standing in a fourth batch, and `reviews/volume-05-batch-0003.md` section two in the one before it.

### Seventeen. The `about nine` list is wrong in four cells, the total is three low, and the card's stated floor is wrong — but the lock holds

Card item 22 claims the batch *runs **two to eight** a chapter, **fifty-nine** instances across ten chapters, ten of ten at or under the bound*, and gives per file **241 7, 242 8, 243 2, 244 3, 245 8, 246 7, 247 8, 248 6, 249 8, 250 2**.

Measured on this tree with the card's own method — `re.findall(r"\babout nine\b", t, re.I)` per file minus `re.findall(r"\babout nine hundred\b", t, re.I)`, the subtraction the card's own text makes necessary and the prompt for this run says is not optional:

| File | raw | of which `about nine hundred` | **counted** | card | diff |
|---|---|---|---|---|---|
| 0241 | 7 | 0 | **7** | 7 | 0 |
| 0242 | 7 | 1 | **6** | 8 | **−2** |
| 0243 | 16 | 13 | **3** | 2 | **+1** |
| 0244 | 3 | 0 | **3** | 3 | 0 |
| 0245 | 10 | 2 | **8** | 8 | 0 |
| 0246 | 7 | 0 | **7** | 7 | 0 |
| 0247 | 12 | 4 | **8** | 8 | 0 |
| 0248 | 7 | 1 | **6** | 6 | 0 |
| 0249 | 7 | 0 | **7** | 8 | **−1** |
| 0250 | 4 | 3 | **1** | 2 | **−1** |
| **TOTAL** | 80 | 24 | **56** | 59 | **−3** |

**Four of the ten cells are wrong and the total is three out.** The subtraction removes **24** instances and is the step that gets dropped; `chapter-0243.md` is the extreme case, sixteen raw and three counted.

**The lock holds.** Ten of ten at or under eight, highest single chapter eight, median 6.5. **The prose needs nothing.**

**And the lead this run was handed is confirmed and corrected in the same breath, as section four below sets out.** The prompt said the figure for `chapter-0250.md` reproduces at 1 and that what fails is the bound. **Both halves are right and the second half is the finding:** `chapter-0250.md` is 1, and the batch's true range is **1 to 8**, so `chapter-0250.md` is below the card's stated floor of *two* and the card's own *two to eight* does not describe the batch.

**One methodological note the card half-gives and should finish.** The card warns that this method counts *about nineteen* as an instance of *about nine*, because the look-ahead excludes only *hundred*, and names **one** such instance — *Chapter 0249 carries one about nineteen in a man's age*. **There are five**, at `0242:85`, `0242:97`, `0249:5`, `0249:119` and `0250:125`, and only the one at `0249:5` is an age; **the other four are the page figure for the nineteen people behind the bank**, which is on the card's own list of page figures that are left standing. Excluding them as the card's principle requires gives **51**, a range of **0 to 8**, and puts `chapter-0250.md` at **zero**. **The lock survives either way — ten of ten at or under eight on the card's method and on the stricter one — and the figure is not the finding. The finding is that a method with a stated look-ahead, printed beside a per-file list, is off in four cells in a batch whose card opens by insisting the figure was measured.** Fourth batch in a row, and the third in a row in which at least one cell runs **downward** rather than up.

### Eighteen. Card item 16 reports `may` six times; the instance count is eight on six lines

> "The one false positive a later writer will meet is *may*, which **occurs six times** and is the modal verb every time" — followed by six glosses.

`re.finditer(r"\bmay\b", line)` over the ten files returns **8 hits on 6 lines**, at `0241:29`, `0243:73`, `0243:77` ×3, `0245:37`, `0247:9`, `0250:39`. **All eight are the modal verb** — *a person may not make one*, *a thing a clerk may do*, *may be un-filled / if it may not / if it may*, *a person who may be served*, *she may keep them*, *she may refuse to have said it* — and **the month and weekday locks hold at zero each.**

**The card counted lines and printed them as instances.** The six glosses are six sentences; the seventh, eighth and ninth occurrences are the second and third *may* on `chapter-0243.md:77`, inside the minute-book entry the card prints in full at item 30 and does not gloss. **The lock holds, the count is wrong, and the shape is the one `reviews/volume-05-batch-0004.md` section three recorded for the batch behind this one** — five hits on five lines there, eight on six here. A homograph census reported as an instance count will be short by the number of lines that carry more than one.

### Nineteen. Card item 41's twelve-word-shingle figure does not reproduce under either reading of its own metric

> "Twelve-word shingles repeated across chapters fell from **378 to 285**."

Measured on `m.prose_lines` tokens with `m.TOKEN`, counting twelve-word shingles held by more than one of the ten files: **360** distinct shingles held by two or more chapters, and **542** on the pair-count reading, summed over all forty-five pairs. **Neither is 285, and the two natural readings of the metric differ from each other by 182**, which is itself the finding: a metric named in words and not in a method is not a figure.

The repair's claim of *direction* is not supported either — **the batch carries 360 shared twelve-grams, and section one findings fifteen and sixteen are two runs of forty-nine and thirty-two tokens inside that count**, so the reduction the card reports is either measured on a different tree or on a different definition. **The prose needs nothing and the record is wrong**, and the standing is the one item 33 of the same card already states: *a check that returns a surprising number is not evidence either, and neither is one that returns the expected one.*

### Twenty. Card item 20's per-file emphasis figures reproduce to the decimal, and its own two summary halves cannot both be true

**Twenty of twenty cells reproduce.** Text measure, per file: **9.35 / 9.86 / 8.87 / 7.13 / 7.38 / 6.90 / 8.27 / 10.73 / 7.90 / 7.68** against the card's 9.3 / 9.9 / 8.9 / 7.1 / 7.4 / 6.9 / 8.3 / 10.7 / 7.9 / 7.7. Lines measure: **18.37 / 20.00 / 23.40 / 19.15 / 21.74 / 22.92 / 23.91 / 18.33 / 21.57 / 25.53** against 18.4 / 20.0 / 23.4 / 19.1 / 21.7 / 22.9 / 23.9 / 18.3 / 21.6 / 25.5. Range and median both reproduce: **6.9–10.7, median 8.1** and **18.3–25.5, median 21.7**. Method: prose is every non-blank line that is not a heading, not `---` and **not a blockquote**, per `outline/volume-05.md` lock 1 and its third named trap; the inner text of paired `**` over prose characters for the text measure, marked lines over prose lines for the lines measure. **Withholding the blockquote exclusion moves `chapter-0243.md` to 8.7 and 22.9 and no other cell, so the card measured on the method its own lock names and the trap is real and was avoided.**

**But the item's two summary sentences do not reconcile.** It says *"three of ten under a fifth"* on the lines measure and *"on this item's own stated denominator seven of the ten chapters exceed a fifth."* Measured: **three under** (0241, 0244, 0248), **six strictly over**, and **`chapter-0242.md` at exactly 20.00** — which is a fifth and is not over it. **Three under and seven over cannot both be true of ten chapters, and the seven counts a chapter that is at the line and not past it.** The bound the batch misses is the same bound either way and the prose needs nothing.

### Twenty-one. Card item 87 puts the reader's canon pay on the page in Chapters 0242 and 0250, and it is not in this batch

> "**Forty-five pence a day and four days a week for the reader, on the page in Chapters 0242 and 0250** and not computed from."

`grep -c "forty-five pence"` over `chapters/volume-05/chapter-02{41,42,43,44,45,46,47,48,49,50}.md` returns **0 in all ten**. The only two files in the whole of Volume 05 carrying the string are `chapter-0206.md` and `chapter-0234.md`, and neither is in this batch.

The reader appears four times in this batch and **all four give the rate by reference instead of by figure**: `written engagement` ×4 and *at the rate the list is set at* ×4, at `chapter-0241.md:127`, `chapter-0242.md:45`, `chapter-0250.md:5` and `:39`. **The only *four days a week* in the batch is `chapter-0244.md:21`** — *"she had been doing about four days a week of work that nobody knew about"* — which is Nell Kest's unpaid book-keeping and has nothing to do with the reader. `chapter-0246.md:11`'s *"on four days in a week"* is the bread woman.

**So the figure the lock exists to protect is not on the page in this batch, and the card says it is.** The prose needs nothing and is arguably better for it — *the rate the list is set at* keeps the reader unnamed and unpriced, which is the lock's own shape. **The record is wrong and a writer handed this item would look for a figure that is not there.**

### Twenty-two. Card item 24's sentence census is three out and every distribution figure reproduces

Card item 24 claims **838 sentences, mean 33.9, median 33, 42.4 per cent at forty or more, 17.3 at sixty, 3.8 at eighty, a longest of 89, and nothing at a hundred or over.** Measured by the method the item states — per paragraph, split on a full stop, question mark or exclamation mark followed by a space, with an emphasis marker acting as a boundary, over `m.prose_lines` tokens: **841 sentences, mean 33.8, median 33, 42.2 per cent at forty or more, 17.2 at sixty, 3.8 at eighty, longest 89 words at `chapter-0241.md:79`, and 0 at a hundred or over.**

**The hard bound holds to the digit and the distributions agree to a tenth; the total is three out and the method is stated in prose rather than in code, which is why.** This is recorded because it is the *shape* of the Batch 0004 review's item twelve — *a figure that no method returns should not be printed as a measurement* — **and the difference is that here a method does return it, within three.** A card that states its method in prose and gets within three is behaving correctly; one that states a per-cell list and misses four cells is not.

### Twenty-three. Card item 4 names six chapters as printing the count of the four; two readings give two different lists

> "Chapters **0241, 0242, 0246, 0247, 0248 and 0249** print the number of the first four, and Chapter 0250 prints it once as four…"

On the batch's own formula, `grep -c "hundred and forty years"`: **0241 ×2, 0242 ×2, 0246 ×1, 0247 ×0, 0248 ×1, 0249 ×0, 0250 ×2** — and the card's list is wrong in two chapters on this reading. On the wider reading, *any* printing of the count of the askings, **`chapter-0247.md:119`** does print it — *"there are four people in this empire who have asked a person out loud what a word on a form means"* — **and `chapter-0249.md` does not**, at any line: its four occurrences of *four people* are the unread at `:7`, `:29` and `:111` and a foreman's four reasons at `:29`.

**The card's list is right about 0247 and wrong about 0249**, on the reading a reader would take. `chapter-0249.md` prints the count of the *five mouths* and the count of the *unread* and never the count of the askings. Reported for the same reason item twenty-one is: **a list of chapters that a later writer will go looking in is a list that has to be right.**

### Twenty-four. Card item 3's "about four weeks" is a fourth figure for the mark on the hand, and it matches nothing

Card item 3: *"the number is gone in about four weeks."* The page gives **about a week** at `chapter-0241.md:87`, **about seven weeks** by the span at `chapter-0248.md:7`, and **six weeks** at `chapter-0248.md:45`. **Four weeks is a fifth figure and is the arithmetic mean of two of the others**, which is what a summary reaches for when nobody has picked. The prose finding is section one item nine; this is the record half, and the two are not the same fault: the prose contradicts itself, and the card contradicts the prose and its own two neighbours.

### Twenty-five. This run's own prompt misreports the volume-wide diff by two insertions and two deletions

The prompt for this run states that `git diff --numstat 65abf1d -- chapters/volume-05/` returns *1,224 insertions and 0 deletions, and every one of them is on `chapter-0241.md` to `chapter-0250.md`*. Measured: **1,226 insertions and 2 deletions over thirteen files**, of which **1,224 and 0 are on the ten** and `chapter-0224.md` and `chapter-0228.md` carry `1 −1` each. **The prompt's figure is the ten's figure and it is attached to the volume's command**, which is item 203's standing reproducing inside the prompt rather than inside a phase, and the two lines that differ are the two lines a reader would not look at. Recorded because the next prompt in this chain will copy this one, and because the prompt was right about the thing that mattered — that the ten have not moved — and wrong about the number attached to it.

---

## Section three — the claims that hold, measured, so that a later phase does not spend a run re-deriving them

| Claim | Result | Method |
|---|---|---|
| No calendar month name and no weekday name in the prose (card item 16, standing lock) | **holds — 0 and 0** | whole-word search for the twelve month names and seven day names over all ten files. **`\bmay\b` returns 8 hits on 6 lines — `0241:29`, `0243:73`, `0243:77` ×3, `0245:37`, `0247:9`, `0250:39` — and all eight are the modal verb**, read in place. Item 268B's warning not to inherit a clearance list is right for this range too: the card's own figure of six is a line count (finding eighteen) |
| `about nine` is bound to about eight per chapter (card item 22, craft lock) | **holds — ten of ten at or under eight, highest 8, median 6.5** | card's own method; see finding seventeen for the cells and the total |
| The question-mark distribution, per file (card item 19) | **holds exactly — 5 / 5 / 1 / 2 / 1 / 6 / 3 / 6 / 3 / 2, thirty-four in all** | `T[p].count("?")` per file |
| Emphasis, both measures, per file (card item 20) | **holds — twenty of twenty cells to the decimal**, text 6.9–10.7 median 8.1, lines 18.3–25.5 median 21.7 | prose excludes headings, `---` and **blockquotes**, per `outline/volume-05.md` lock 1; see finding twenty for the one unreconcilable summary sentence |
| Emphasis parity (card item 26 test four) | **holds — 0 odd blocks, even mark count in all ten files** | `**` count per file: 18 / 16 / 22 / 18 / 20 / 22 / 22 / 22 / 22 / 24 |
| An emphasis run holding more than one sentence (card item 21, item 26 test ten) | **holds — 0** | internal `[.!?]` followed by a space inside paired `**`, per file |
| Tests one to seven of card item 26 | **all zero** | punctuation + two spaces 0; full stop + lowercase **with `\*\*` inside the look-ahead** 0; `[A-Za-z]\*\*[A-Za-z]` 0; per-paragraph `**` parity 0; a dialogue paragraph with an odd quotation-mark count 0; **the blunt test**, any non-blank line with an odd quotation-mark count not itself beginning with a quotation mark, 0; a paragraph opening with a quotation mark not carrying an even count, 0 |
| The `no form` / `not one form` motif, the governing second count (card item 25) | **holds exactly — 41, per file 2 / 3 / 8 / 5 / 5 / 3 / 7 / 1 / 2 / 5** | `\bno form\b` = 30 and `\bnot one form\b` = 11 per file; summed per file the two give the card's list cell for cell. **This is the one distributional figure in the card that reproduces to the digit, and it is the one printed beside the method that produces it** |
| Card item 25's first count, labelled *not reproducible* | **correctly labelled** | 0 + 1 + 2 + 2 + 4 + 2 + 4 + 0 + 2 + 2 sums to the claimed nineteen internally, but the four-frame list lives in the closed Batch 0004 card file. **The card withdrew it rather than asserting it, which is the standing working.** For the record, the two headline frames test at 13 and 4 on this range and *there is not one form for it* is 0 |
| Word figures per file and batch total (card header, item 35) | **holds exactly — 2,787 / 2,804 / 2,863 / 2,723 / 2,773 / 2,861 / 2,821 / 2,800 / 3,106 / 3,253 = 28,791**, and `wc -w` per file agrees on all ten | `m.words_in_file`, and `wc -w` file by file. **The prompt's printed figures reproduce to the digit** |
| The count of askings is four through Chapter 0249 and five at Chapter 0250 (card item 1) | **holds** | every one of the **23** occurrences of `\bfifth\b` printed and read: **eleven are the fifth month or the fifth hour** (`0241:65`, `0242:103`, `0243:7`, `0243:45`, `0247:15`, `0248:141`, `0249:39`, `0249:61`, `0249:75`, `0250:13`, `0250:83`); six are the fifth asking (`0246:119` forecasting it, `0248:49` and `:147` intending it, `0250:107` and `:125` recording it, plus the chapter title at `0250:1`); the rest are *the fifth person anybody has told* (`0241:129`), *the fifth of* five tellings (`0244:35`), *the fifth man* (`0249:21`) and *a fifth time* (`0249:23` ×2). **No chapter before 0250 makes it five** |
| `exception`, `precedent`, `schedule`, `ruling`, `Venn`, `Ashfall`, `ninety-second`, `envelope`, `counting-house`, `present holder`, `forty-four thousand eight hundred and nineteen`, `fourteen months` (standing locks, card items 35 and 46) | **hold — all 0** | per-term `re.findall` with `\b` boundaries over the ten files |
| None of the three Orises is named; Mosswake is not named; `dragon` does not occur | **hold — all 0** | as above. **The second half of the volume's question is not put on the page in any form**, per card item 12 |
| `thirty-one` (standing lock) | **holds as the card states it — exactly 1**, at `chapter-0248.md:5`, *his wife is thirty-one*; **`Mosswake` is 0**, so the thirty-one of Mosswake is not printed and nobody adds the six to the eighteen | `\bthirty-one\b` and `\bMosswake\b` |
| `four hundred miles` absent; `four hundred and thirty` the long form (standing lock) | **holds — 0 short, 26 long**, plus `four hundred and forty` 4, all the bank | both strings searched over the ten; **no inconsistency of the kind `reviews/volume-04-batch-0005.md` item five reported, and none to report** |
| The two documents stay two documents; the quarterly return, the counting-house mark and the sealed house are not named | **hold** | as above; `four hundred and thirty` 26 and no instrument joining them |
| The guarantee is not printed and no child is named (standing lock) | **holds** | `at no charge` **0** and `fire and water` **0**; `four hundred and forty foot` **4** at `0242:85`, `0245:113`, `0249:119`, `0250:125`; `sixty children` **3** at `0242:85`, `0249:119`, `0250:125`, exactly as card item 88 states |
| The Lowcross bill at nineteen pounds three and fourpence, unpaid, nobody liable, no line in nineteen years (standing lock) | **holds — four mentions**, at `0242:93`, `0244:115`, `0249:119`, `0250:125,` each carrying the sum and the unpaid state, and **no chapter pays it, funds it or forgives it**. `no line for a bridge in that fund in nineteen years` is at `0249:119`; `chapter-0244.md:115` varies it to *no line against it in nineteen years* and `0242:93` carries the full clause | `grep -n -o -E ".{0,55}nineteen pounds three and fourpence.{0,55}"` |
| The reader of seventeen is unnamed, unthanked, unsent anybody, not asked (standing lock) | **holds for the reader** | `written engagement` **4** and *at the rate the list is set at* **4**; **`forty-five pence` is 0 in this batch**, which is finding twenty-one. See finding sixteen for the one actual thank in the batch, at `chapter-0247.md:109`, belonging to a man of about forty paying fourpence for a copy |
| Nobody is thanked in the matter (standing lock) | **holds for the matter** | `thank` returns **23 lines** across the ten files and every one is a negation or a refusal — *not going to be thanked, has not been thanked, nobody has thanked, is not going to start, not one of them has ever said thank you, has never once been thanked* — **except `chapter-0247.md:109`**, which is the batch's only actual thank and is an ordinary paid copy service, the same beat and the same man as `chapter-0236.md:82` |
| No certification granted and none held (standing lock) | **holds** | `certif` returns `chapter-0247.md:47` (*a certificate is four shillings and she has never issued one*) and `chapter-0250.md:79`'s clerk of about fifty-five, who *has done about nine hundred of them correctly* and has never been asked whether a box ought to have been filled. **Both are a form priced and a form administered, not a certification held**, and Marek Kest is not in this batch |
| The bar sentence, word for word (card item 15) | **holds — 1**, at `chapter-0246.md:5` | literal search for *came off him on the twelfth of the ninth month of last year on an application of one line which he wrote himself* |
| `this year` is zero across the ten files (card item 15) | **holds — 0**; `last year` 1 (the bar sentence), `next year` 3 (`0247` ×2, `0248` ×1) | `\bthis year\b`, `\blast year\b`, `\bnext year\b` |
| No new named figures; the five principals and *Slade Cut* are the whole list (card item 10) | **holds exactly** | every capitalised two-word name extracted: **Halla Wray 9, Marn Ottery 7, Marek Kest 5, Nell Kest 4, Tamsin Rook 4, Slade Cut 3**, and every other pair is chapter-title text or a sentence-initial fragment |
| No out-of-world breach — no chapter, volume, page or reader-of-the-book token | **holds — none** | `grep -n -o -E ".{0,50}\b(chapter\|chapters\|volume\|reader\|pages? of this\|this page\|on the page\|in this batch\|this batch)\b.{0,50}"` returns **two hits, both `a reader of seventeen`**, at `0250:95` and `:125`, which is the in-world figure. `the page` **0** and `the book` **1**, at `chapter-0244.md:3`, a book on a table |
| Doubled blank lines; consecutive section rules | **hold — 0 and 0** | line-by-line scan for two consecutive blank lines and two consecutive `---` over all ten files. **The batch behind this one carries five doubled blank lines in four chapters and two doubled scene breaks; this batch carries neither, and that is worth saying so the difference is not re-derived** |
| The letter on the sill carries its day and nothing else (card item 90) | **holds** | `chapter-0245.md:19`, *the fourth day of the fourth week of the eighth month of the year after next*, with no name at the head or the foot and nothing on the back; `chapter-0245.md:57` calls it *a day about six weeks gone* against a chapter dated the second day of the first week of the tenth month, which is about six weeks |

---

## Section four — the live lead this review was handed, answered and corrected

The prompt for this run carried one lead from `workspace/review-debt-0003/PROMPT.md`: *"the same word-boundary method on Batch 0005's `chapter-0250.md` returns **1** against a card claiming 3 to 8. That card figure does not reproduce."*

**The lead is half right, and the half that is wrong is the half a reviewer would otherwise have spent the run on.** `reviews/volume-05-batch-0004.md` section four already corrected it once; this run confirms the correction on the tree.

**The figure reproduces exactly.** `re.findall(r"\babout nine\b", t, re.I)` minus `re.findall(r"\babout nine hundred\b", t, re.I)` over `chapters/volume-05/chapter-0250.md` returns **1**: four raw, three of them `about nine hundred`. **The card's figure for that file is 2, so the card is wrong at the cell — but the card never claimed 3 to 8.** The batch card claims *two to eight*, and **that is the bound that fails**: the batch's true range is **1 to 8**, with `chapter-0250.md` alone below the stated floor and `chapter-0243.md` and `chapter-0244.md` sitting on two. See finding seventeen for the full table.

**So the defect the lead points at is real, it is in the card's bound and its per-cell list, and the next reviewer should not re-derive one file's count.** **And the shape is the opposite of the batch behind this one:** there the lock held and the figures did not; here the lock holds, the figures do not, **and the bound does not.** Three batches in a row, and the third is the first in which a card's own stated *range* is the thing that fails while its cells and its lock both hold. That is a new shape and it is recorded because a range is the one figure in a card that no cell can be checked against.

---

## Section five — what this review could not do, and hands on

**The sixteen prose defects above need prose authority**: substitutions and deletions against base in a closed volume. **A review has no authority to make one, and this run did not make one.** They are listed with line numbers so that a phase given the authority does not have to re-find them, and **a line number in a file no phase has edited is a citation that resolves**, which is the standing `reviews/volume-04-batch-0005.md` section four records and which the whole of section one depends on — and which holds here for a second and independent reason: `m.lifts --base dedc831` returns **`ADDED 0 prose lines`**, so there is no repair-added prose in these ten files for a line number to be displaced by.

**One finding is below the standing's threshold and is reported as such.** Finding fourteen, `chapter-0247.md:85`'s *eleven words* against a nine-word question, is a gap of two, and the two prior reviews set the bar at 21 and 15 tokens. It is recorded because it is a self-measurement of a question printed ten lines above it, not because it is a large fault, and **the record says so rather than claiming the threshold.**

**Two things this review read and set aside, so that they are not re-reported.**

**One — the shed in which Halla Wray said things out loud.** `chapter-0242.md:29` and `chapter-0245.md:65`–`:67` date her shed to *the second week of the sixth month of the year after next*; `chapter-0248.md:141`, `chapter-0249.md:61` and `chapter-0249.md:75` date a shed of hers to *the fifth month of the year after next*. **That looks like a five-against-two contradiction and this review does not raise it**, because `chapter-0243.md:7` independently dates a shed in the fifth month — *"She said that to a foreman's face in a shed in the fifth month of the year after next"* — so **two sheds are on the page and the batch never says there was only one.** A reviewer with authority should read `chapter-0242.md:29`, `chapter-0243.md:7`, `chapter-0245.md:65`–`:67`, `chapter-0248.md:141` and `chapter-0249.md:61`–`:75` as one sequence and decide whether the shed is one occasion or two. **Recorded as an open question and not as a defect, because the reading that resolves it is available and this review did not want to charge a finding on a reading it had not excluded.**

**Two — `chapter-0243.md`'s two days and four days.** `:15` and `:21` give *about two days* of looking and `:95` gives *I have had four days to think about who I am going to tell*. **Not raised as a prose defect**, because a clerk who spent two days looking and had four days to decide who to tell is ordinary — the four can sit outside the two. **But card item 17's gloss is wrong and is recorded as a record defect**: it describes *"a clerk's four days in Chapter 0243"* as *"a span between the third week of the ninth month and the fourth week of the tenth"*, **and a span between two weeks seven weeks apart is not four days.** The prose figure is `four days`; the card's gloss turns it into a month. The figure needs no repair; the gloss does, and a phase with outline authority can cut the gloss without touching a word of prose.

**And the thing the next owed review inherits.** This batch's card certifies a per-file `about nine` list that is wrong in four cells with the total three low and a stated range that does not describe its own batch; a `may` instance count that is a line count; a twelve-word-shingle figure that reproduces under neither reading of its own metric; a canon pay figure placed in two chapters that do not contain it; a chapter list of six in which one chapter does not print the count; and two summary sentences about a single bound that cannot both be true. **That is six, and it is the largest number of record failures in a single card in the four reviews paid so far — and four of the six are figures a method beside the figure would have caught, which is the standing `reviews/volume-05-batch-0004.md` section two item nine established and this batch's card does not hold.** **The standing does not need restating; it needs applying to the file that wrote it.** A card that publishes a per-cell list beside a method is making a checkable claim, and **the cells are where a card is wrong** — the totals and the ranges and the flat statements of what holds have been the parts that survive.

**The instrument standing, restated once because this batch is the second range in a row where it decides the outcome.** Card item 26's test eight is a sliding **sixty**-word window over the ten files, compared at every position across every pair, and it returns **zero**, exactly as the card reports. **A sixty-word window requires sixty identical tokens.** Run at the floors below it, the same scan over the same files returns, counted at every starting position, **10** duplicated windows at forty words, **37** at thirty, **59** at twenty-four, **98** at twenty and **216** at sixteen — and the ten at forty words are ten offsets of **one** 49-token run, so the de-duplicated region count at forty is **1**. **The batch's largest shared run is 49 tokens and the scan sees it at forty words and is blind to it at sixty.** A zero from a windowed scan is evidence about that window and about nothing else, it must never be reported as a batch-level clearance, **and a sliding window is the wrong instrument because its floor and its threshold are the same number** — which is why section one findings fifteen and sixteen were found by taking the *longest shared run per pair* rather than by sliding anything. Item 258 and item 260 found the usable floor; **this batch shows that the floor has to be chosen below the size of the fault you are hunting and that the choice cannot be made from the size of the fault you already know about.**

---

**What this review touched:** no chapter file, no outline, no `tools/measure.py`, no controller file. It read `outline/batches/volume-05-batch-0005.md`, `outline/volume-05.md`, `reviews/volume-04-batch-0005.md`, `reviews/volume-05-batch-0003.md` and `reviews/volume-05-batch-0004.md`; it read `chapters/volume-05/chapter-0241.md` through `chapter-0250.md` in full; it measured `chapters/volume-05/chapter-0236.md:82` and `chapter-0238.md:125`, which are another batch's files, **for the two runs in finding sixteen and for nothing else**. **It was paid by the phase that took `workspace/review-debt-0003/PROMPT.md` and it is the fourth of the four owed reviews in `outline/volume-12.md` to be paid. One remains: Volume 06's own Batch 0003, `chapter-0261.md` to `chapter-0270.md` — which is the only one of the five that will land on repaired prose, whose prompt already exists at `workspace/review-debt-0004/PROMPT.md`, and whose base this run re-derived as `a747682` and not the `d8f15cd` that prompt names.**
