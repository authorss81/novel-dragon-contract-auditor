#!/usr/bin/env python3
"""The measurement instruments this project's figures are printed from.

A figure in a state file is a copy of a figure, and a copy is how this
project's numbers go stale. The claim this project has now printed six times
is that a disagreement about a number is cheap to settle by re-running the
named method and expensive to settle by reading a record. That claim is only
worth printing if the method is a thing somebody can run, so it is a file.

It is not a controller file. Nothing here dispatches, selects, retries or
claims a phase, and nothing here is a phase. It only reads `chapters/` and
`state/` and writes to standard output.

    python3 tools/measure.py selftest
    python3 tools/measure.py words
    python3 tools/measure.py calendar
    python3 tools/measure.py sentences --movement 5
    python3 tools/measure.py reprints --window 20
    python3 tools/measure.py reprints --window 16 --volume 10

Run `selftest` before trusting any other output. Three of the four
instruments this project has written were wrong on their first run and all
three returned a clean number, which is the failure mode the self-test
exists to catch:

  1. comparing tokens at equal index instead of aligning by token value,
     which returned zero over a set a thirty-word run had been planted in;
  2. a tokeniser written `[a-z0-9]` with no uppercase, which shifts every
     capitalised word by one character and reports every run one character
     off its true position;
  3. a classifier that unpacks a list of strings as a list of flags, where
     every non-empty string is truthy, so every run in the manuscript is
     called formula and the instrument reports a clean zero.

The methods below are the ones named in `state/open-threads.md` at items 121,
122, 125, 129, 135, 136 and 137. Where a record prints a figure, this file
prints the method next to it, and where a record and this file disagree the
files are the authority and the disagreement is worth more than either.
"""

import argparse
import io
import json
import os
import re
import subprocess
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# words
# ---------------------------------------------------------------------------
# The method this project has used for every word count since Volume 01:
# strip trailing whitespace from the line, count words, one file at a time,
# never with a glob. A glob expands in path order and the concatenation
# figure differs from the per-file sum by the number of files that do not
# end in a newline, and the difference is small enough to be mistaken for a
# rounding and large enough to be a wrong number.


def words_in_file(path):
    with open(path, encoding="utf-8") as handle:
        return sum(len(line.rstrip().split()) for line in handle)


def chapter_files():
    chapters = os.path.join(ROOT, "chapters")
    paths = []
    for volume in sorted(os.listdir(chapters)):
        vdir = os.path.join(chapters, volume)
        if not os.path.isdir(vdir):
            continue
        for name in sorted(os.listdir(vdir)):
            if name.startswith("chapter-") and name.endswith(".md"):
                paths.append((volume, os.path.join(vdir, name)))
    return paths


def cmd_words(args):
    files = chapter_files()
    per_volume = defaultdict(int)
    per_file = {}
    for volume, path in files:
        count = words_in_file(path)
        per_volume[volume] += count
        per_file[path] = count
    for volume in sorted(per_volume):
        print(f"{volume} {per_volume[volume]:>9,} words")
    print(f"{'MANUSCRIPT':<12} {sum(per_volume.values()):>9,} words in {len(files)} files")
    target = args.volume
    if target:
        total = sum(v for k, v in per_volume.items() if target in k)
        print(f"{'volume ' + target:<12} {total:>9,} words")


# ---------------------------------------------------------------------------
# tokenising, and the classifier
# ---------------------------------------------------------------------------
# Uppercase and digits are in the class. An earlier version of this
# instrument wrote `[a-z0-9]`, lowercased nothing, and reported every run one
# character off its true position, which is invisible in a count and obvious
# in the printed run text: *eceived* where the file says *Received*.

TOKEN = re.compile(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*")

# A date line is a whole line of the source, and it is flagged whole, and it
# is never flagged by its opening clause. The year name follows the opening
# clause, so a line flagged only at the front leaves its tail in the prose
# bucket, and every run made of that tail is reported as a re-print of a
# chapter's own calendar. The shape a real date line has is one sentence on
# one line, so the test is on the start of the line and the flag it produces
# covers the rest of the line as well.

DATE_LINE = re.compile(
    r"^\s*(?:\*\*)?\s*(?:[Ii][Tt]|[Tt]he date)\s+is\s+the\s+"
    r"(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    r"eleventh|twelfth)\s+day\s+of\s+the\s+"
    r"(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    r"eleventh|twelfth)\s+week\s+of\s+the\s+"
    r"(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    r"eleventh|twelfth)\s+month\b"
)

# The formula list is deliberately long. A short list returns zero instead of
# prose, and a zero that means the list was short is indistinguishable from a
# zero that means the writing is clean. It is a second classifier and it is
# reported separately from the date-line classifier, because a record that
# prints one prose figure and reaches it with two different classifiers is a
# record whose figure cannot be re-run.
FORMULA_TERMS = (
    "it is the",
    "the year after the",
    "the year before the",
    "the month of the",
    "the week of the",
    "the day of the",
    "and it is the",
    "it is about the",
    "the first order of the",
    "on the registrar",
    "asked for by nobody",
    "by its own device",
    "the respondent has been entered",
    "the cinder court",
    "guarantor duty",
    "the hours at that counter",
    "the second hour",
    "the third hour",
    "the fourth hour",
    "the fifth hour",
    "the sixth hour",
    "the seventh hour",
    "the eighth hour",
    "the ninth hour",
    "the second day of the",
    "the first day of the",
    "the third day of the",
    "the fourth day of the",
    "the fifth day of the",
    "the sixth day of the",
    "the seventh day of the",
    "the eighth day of the",
    "the ninth day of the",
    "the tenth day of the",
    "the eleventh day of the",
    "the twelfth day of the",
    "the second week of the",
    "the first week of the",
    "the third week of the",
    "the fourth week of the",
    "of the year after",
    "of the year before",
)

_TERM_RE = re.compile(
    "|".join(re.escape(t) for t in FORMULA_TERMS), re.IGNORECASE
)


def tokenize(path):
    """Return (tokens, flags, raw) where flags is (is_date_line, is_formula_term).

    Both decisions are made on the raw line before tokenising and carried on
    the token, so the classifier is a lookup and not a second piece of code
    with its own idea of what a date is. The raw text of every token is kept
    beside the lowered form because a tokeniser with a character class missing
    its uppercase does not fail in a count, it fails in the printed run text,
    and the printed run text is the only place the failure is visible.
    """
    tokens = []
    raw = []
    on_date = []
    on_term = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            date = bool(DATE_LINE.match(line))
            spans = [m.span() for m in _TERM_RE.finditer(line)]
            for match in TOKEN.finditer(line):
                start, end = match.span()
                tokens.append(match.group(0).lower())
                raw.append(match.group(0))
                on_date.append(date)
                on_term.append(any(a <= start < b for a, b in spans))
    return tokens, (on_date, on_term), raw


def load_cached(paths):
    corpus = {}
    for path in paths:
        corpus[path] = tokenize(path)
    return corpus


def shared_runs(corpus, window):
    """Maximal shared runs, de-duplicated by covered position across files."""
    index = defaultdict(list)
    for path, (tokens, _flags, _raw) in corpus.items():
        for start in range(0, max(0, len(tokens) - window + 1)):
            index[tuple(tokens[start:start + window])].append((path, start))

    # candidate (path, start) positions, then extend each against every other
    # file that holds the same words at the same offsets
    runs = []
    for key, positions in index.items():
        if len(positions) < 2:
            continue
        by_file = defaultdict(list)
        for path, start in positions:
            by_file[path].append(start)
        for path, starts in by_file.items():
            tokens = corpus[path][0]
            for start in sorted(set(starts)):
                # find the longest match this position has in any other file
                best = window
                for other_path, other_start in positions:
                    if other_path == path:
                        continue
                    other = corpus[other_path][0]
                    n = 0
                    limit = min(len(tokens) - start, len(other) - other_start)
                    while n < limit and tokens[start + n] == other[other_start + n]:
                        n += 1
                    best = max(best, n)
                runs.append((path, start, start + best))

    # merge overlapping runs in the same file
    by_file = defaultdict(list)
    for path, start, end in runs:
        by_file[path].append([start, end])
    final = []
    for path in sorted(by_file):
        spans = sorted(by_file[path])
        merged = []
        for start, end in spans:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        for start, end in merged:
            if end - start >= window:
                final.append((path, start, end))
    return final


def classify(corpus, run, mode="either"):
    """Formula if at least half the tokens of the run fall inside a formula span.

    `mode` names which spans count, and it is named because the choice changes
    the figure: a run that is a court record rather than a calendar is
    formula to a term list and prose to a date-line test, and a record that
    prints one number for both is not re-runnable.
    """
    path, start, end = run
    flags = corpus[path][1]
    on_date = flags[0][start:end]
    on_term = flags[1][start:end]
    if not on_date:
        return "prose"
    if mode == "date":
        hits = sum(1 for f in on_date if f)
    elif mode == "terms":
        hits = sum(1 for f in on_term if f)
    else:
        hits = sum(1 for d, t in zip(on_date, on_term) if d or t)
    return "formula" if 2 * hits >= len(on_date) else "prose"


def cmd_reprints(args):
    files = chapter_files()
    if args.volume:
        files = [(v, p) for v, p in files if args.volume in v]
    paths = [p for _v, p in files]
    name_of = {p: os.path.basename(p) for p in paths}
    corpus = load_cached(paths)
    runs = shared_runs(corpus, args.window)

    print(f"window: {args.window} words; files: {len(paths)}")
    print(f"maximal runs of {args.window} words or more: {len(runs):,}")
    print("the three buckets below are three classifiers over the same runs:")
    print("  date  — a window is formula when half its tokens sit on a date line")
    print("  terms — a window is formula when half its tokens sit inside a formula term")
    print("  either— the two spans together, which is the loose reading")
    for mode in ("date", "terms", "either"):
        formula = [r for r in runs if classify(corpus, r, mode) == "formula"]
        prose = [r for r in runs if classify(corpus, r, mode) == "prose"]
        line = f"  {mode:<6} formula {len(formula):>6,}   prose {len(prose):>6,}"
        if prose:
            longest = max(prose, key=lambda r: r[2] - r[1])
            line += f"   longest {longest[2] - longest[1]} in {name_of[longest[0]]}"
        print(line)
    prose = [r for r in runs if classify(corpus, r, args.mode) == "prose"]
    if prose:
        print(f"reporting runs from here on with the {args.mode!r} classifier")
    if args.show:
        for path, start, end in sorted(prose, key=lambda r: (-(r[2] - r[1])))[:args.show]:
            text = " ".join(corpus[path][2][start:end])
            print(f"  [{end - start}] {name_of[path]}: {text[:200]}")


# ---------------------------------------------------------------------------
# lifts
# ---------------------------------------------------------------------------
# `reprints` above answers a different question and the difference is the whole
# reason this section exists. `reprints` finds runs shared between two files
# *that are both in the corpus you name*, so a window of twenty words is the
# smallest thing it can see and any repair written in this project's own idiom
# returns a clean figure, because the idiom is shared by definition. The prose
# repair of chapters 0571 to 0580 was checked that way and the check passed
# while a dozen of its added lines lifted a nine-to-eleven word span verbatim
# out of a chapter that had already narrated the same fixture.
#
# `lifts` asks the other question: for one line of new prose, what is the
# longest run of words that also stands, contiguously and in that order, in
# some OTHER chapter? The index is built over every chapter except the ten
# under repair, so a run has to leave the range to count and a sentence that
# echoes its own chapter is not a lift.
#
# And it prints the volume's own formula baseline beside the added figure,
# because a bare count is unreadable in a book whose sentence frames are shared
# on purpose. On the range 0571 to 0580 the original prose carries a mean lift
# of 9.4 words with 53% of its lines over nine, and prose written in that same
# register cannot and should not be held to a lower bar than the prose it sits
# beside. The added lines came in *under* the baseline. The lifts that were
# real were the ones that re-narrated a fixture canon had already settled, and
# those are found by reading, not by the threshold.

LIFT_N = 5
LIFT_CAP = 24


def prose_lines(text):
    """The lines of a chapter that carry prose, in order, with their numbers.

    The heading, the section rules and the date line are out. The date line is
    out by this module's own DATE_LINE and not by a `startswith("It is ")`, so
    a chapter that opens its date line differently is still measured the same
    way as one that does not.
    """
    out = []
    for number, line in enumerate(text.split("\n"), 1):
        stripped = line.strip()
        if not stripped or stripped == "---" or stripped.startswith("#"):
            continue
        if DATE_LINE.match(line):
            continue
        out.append((number, line))
    return out


def build_lift_index(paths, n=LIFT_N):
    """n-gram -> the chapters holding it, for every chapter named."""
    index = defaultdict(set)
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            tokens = []
            for line in handle:
                stripped = line.strip()
                if not stripped or stripped == "---" or stripped.startswith("#"):
                    continue
                if DATE_LINE.match(line):
                    continue
                tokens.extend(TOKEN.findall(line))
            for i in range(len(tokens) - n + 1):
                index[" ".join(tokens[i:i + n])].add(path)
    return index


def longest_lift(tokens, index, n=LIFT_N, cap=LIFT_CAP):
    """The longest contiguous run of `tokens` held by one single other chapter.

    Returns (length, text, path). The run is grown while the set of chapters
    holding the run so far still intersects the set holding the next n-gram, so
    the answer is always a run that exists whole in one chapter rather than a
    run stitched out of several.
    """
    best = (0, None, None)
    for i in range(len(tokens) - n + 1):
        held = index.get(" ".join(tokens[i:i + n]))
        if not held:
            continue
        source = held
        j = i + n
        while j < len(tokens) and (j - i) < cap:
            nxt = index.get(" ".join(tokens[j - n + 1:j + 1]))
            if not nxt:
                break
            both = held & nxt
            if not both:
                break
            held = both
            source = both
            j += 1
        if (j - i) > best[0]:
            best = (j - i, " ".join(tokens[i:j]), sorted(source)[0])
    return best


def at_commit(base, path):
    """The text of `path` at `base`, or None when that commit does not hold it."""
    proc = subprocess.run(["git", "show", f"{base}:{os.path.relpath(path, ROOT)}"],
                          capture_output=True, text=True, cwd=ROOT)
    if proc.returncode != 0:
        return None
    return proc.stdout


def cmd_lifts(args):
    files = chapter_files()
    if args.volume:
        files = [(v, p) for v, p in files if args.volume in v]
    if args.first or args.last:
        lo = args.first or 0
        hi = args.last or 10 ** 9
        files = [(v, p) for v, p in files if lo <= chapter_number(p) <= hi]
    if not files:
        print("nothing was measured: no chapter matched", file=sys.stderr)
        return 1

    targets = [p for _v, p in files]
    others = [p for _v, p in chapter_files() if p not in set(targets)]
    print(f"range: {len(targets)} chapters; index: {len(others)} chapters "
          f"(the range is excluded, so a run has to leave it to count)")
    print(f"longest contiguous run held by one other chapter, n-gram seed {LIFT_N}, "
          f"cap {LIFT_CAP}")

    added = []   # (path, line number, text) not present at base
    baseline = []  # (path, line number, text) the base held and the tree still holds
    for path in targets:
        current = open(path, encoding="utf-8").read()
        old = at_commit(args.base, path) if args.base else None
        if old is None:
            for number, line in prose_lines(current):
                added.append((path, number, line))
            continue
        old_flat = " ".join(old.split())
        seen_old = set()
        for number, line in prose_lines(old):
            seen_old.add(" ".join(line.split()))
            baseline.append((path, number, line))
        for number, line in prose_lines(current):
            if " ".join(line.split()) not in seen_old:
                added.append((path, number, line))

    index = build_lift_index(others)
    report = []
    for label, rows in (("ADDED", added), ("BASELINE", baseline)):
        hits = []
        for path, number, line in rows:
            tokens = [t.lower() for t in TOKEN.findall(line)]
            length, text, other = longest_lift(tokens, index)
            if length >= args.min:
                hits.append((length, os.path.basename(path), number,
                             os.path.basename(other) if other else "-", text))
        hits.sort(key=lambda r: (-r[0], r[1], r[2]))
        over = sum(1 for h in hits if h[0] >= args.min)
        mean = (sum(h[0] for h in hits) / len(hits)) if hits else 0.0
        print(f"  {label:<8} {len(rows):>4} prose lines | >= {args.min} words: {over:>4} "
              f"| >= 9 words: {sum(1 for h in hits if h[0] >= 9):>3} | mean {mean:.2f}")
        report.extend((label,) + h for h in hits)

    if args.show:
        print()
        shown = [r for r in report if r[0] == "ADDED"][:args.show]
        for label, length, name, number, other, text in shown:
            print(f"  {length:>2} w  {name[8:12]}:{number:<3} <- {other[8:12]}  '{text}'")
    return 0


# ---------------------------------------------------------------------------
# calendar
# ---------------------------------------------------------------------------
# The day inside the week is the inherited cycle second, second, fourth,
# fourth, restarting at each month boundary. A check run as one global cycle
# across a run of files reports a break at the first chapter of every month,
# and there is no break there, and the way that reports a break is the way
# that is wrong.

CYCLE = [2, 2, 4, 4]
ORDINALS = {
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6,
    "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11,
    "twelfth": 12,
}
DATE_LINE_ORD = re.compile(
    r"^\s*(?:\*\*)?\s*(?:[Ii][Tt]|[Tt]he date)\s+is\s+the\s+(\w+)\s+day\s+of\s+the\s+"
    r"(\w+)\s+week\s+of\s+the\s+(\w+)\s+month\b"
)


def chapter_number(path):
    stem = os.path.basename(path)
    digits = "".join(ch for ch in stem if ch.isdigit())
    return int(digits) if digits else 0


def cmd_calendar(args):
    files = chapter_files()
    if args.volume:
        files = [(v, p) for v, p in files if args.volume in v]
    rows = []
    unparsed = []
    for _volume, path in files:
        found = None
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                match = DATE_LINE_ORD.match(line)
                if not match:
                    continue
                day = ORDINALS.get(match.group(1).lower())
                week = ORDINALS.get(match.group(2).lower())
                month = ORDINALS.get(match.group(3).lower())
                if day is None or week is None or month is None:
                    unparsed.append((os.path.basename(path), match.group(0)[:70]))
                    continue
                found = (month, week, day)
        if found is None:
            unparsed.append((os.path.basename(path), "no date line"))
        else:
            rows.append((chapter_number(path), found))

    rows.sort()
    months = defaultdict(list)
    for number, (month, week, day) in rows:
        months[month].append((number, week, day))

    # The cycle is second, second, fourth, fourth, and it restarts at each
    # month boundary. Checked as one global sequence it reports a break at the
    # first chapter of every month, and there is no break there, and the way
    # that reports a break is the way that is wrong.
    breaks = []
    for month in sorted(months):
        entries = months[month]
        days = [d for _n, _w, d in entries]
        weeks = sorted({w for _n, w, _d in entries})
        expected = CYCLE
        if days != (expected * ((len(days) // len(expected)) + 1))[:len(days)]:
            breaks.append((month, days))
        print(f"month {month}: {len(entries)} chapters, days {days}, weeks seen {weeks}")
    print(f"files read: {len(files)}; chapters with a parsed date line: {len(rows)}")
    print(f"month-boundary restarts of the cycle: {len(months)}; breaks inside a month: {len(breaks)}")
    for month, days in breaks:
        print(f"  break in month {month}: {days}")
    if unparsed:
        print("unparsed:")
        for entry in unparsed[:20]:
            print("  ", entry)
    else:
        print("unparsed: none")


# ---------------------------------------------------------------------------
# sentences
# ---------------------------------------------------------------------------
# The splitter must allow a closing quotation mark between the full stop and
# the space. Requiring whitespace immediately after the full stop swallows
# every closing mark and reports a maximum where the real maximum is smaller.

SPLIT = re.compile(r"(?<=[.!?])[\"'’”)\]]*\s+")
HEADING = re.compile(r"^#.*$", re.M)


def sentences_of(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    text = HEADING.sub("", text)
    text = text.replace("---", " ").replace("*", "")
    parts = [p for p in SPLIT.split(text) if p.strip()]
    return [len(p.split()) for p in parts]


def cmd_sentences(args):
    files = chapter_files()
    if args.volume:
        files = [(v, p) for v, p in files if args.volume in v]
    if not files:
        # The batch prompt orders this run against the volume the batch is
        # about to write, and a writer who runs it before the first chapter
        # exists gets no mean, no median and no maximum. Printing a traceback
        # and exiting 0 is the case this project calls a clean number of the
        # expensive kind: the run looks like it worked and nothing was
        # measured. Say what was not found, on the error stream, and exit
        # non-zero, so that a script reading the exit code and a writer
        # reading the screen are told the same thing.
        where = f"volume {args.volume}" if args.volume else "chapters/"
        print(f"no chapter files matched {where}; nothing was measured",
              file=sys.stderr)
        return 1
    lengths = []
    worst = (0, None)
    for _volume, path in files:
        for n in sentences_of(path):
            lengths.append(n)
            if n > worst[0]:
                worst = (n, os.path.basename(path))
    if not lengths:
        print(f"{len(files)} files read and no sentence in any of them; "
              f"nothing was measured", file=sys.stderr)
        return 1
    lengths.sort()
    mean = sum(lengths) / len(lengths)
    median = lengths[len(lengths) // 2]
    print(f"files: {len(files)}; sentences: {len(lengths):,}")
    print(f"mean {mean:.3f}; median {median}; max {worst[0]} in {worst[1]}")
    return 0


# ---------------------------------------------------------------------------
# bold markers
# ---------------------------------------------------------------------------
# An unclosed `**` swallows the rest of a paragraph in most renderers, and
# every string sweep in this project counts words and matches tokens, so a
# defect in the markup is not a defect in the tokens. Counting every `**` in
# a file is not the check either: this project writes the literal token
# `**N. OPEN` inside a code span to name the shape of one of its own rows,
# and a naive count reads that as an unclosed bold and reports a defect
# where there is none. A check that has not been tested against the thing it
# reports is a check that has already reported something false, and this one
# had. Code spans are removed before the markers are counted, and a planted
# case with a `**` inside a code span and an odd number of real markers is
# in the self-test below.

CODE_SPAN = re.compile(r"`[^`]*`")


def strip_code_spans(text):
    """Blank out code spans, tolerating an unpaired backtick.

    A naive `` `[^`]*` `` pairs backticks left to right, so a file with an
    odd number of them pairs wrongly from that point to the end of the file
    and the count of anything in it depends on how much text was appended
    after the odd one. This project writes an odd number of backticks in
    more than one file, and appending to one of them changed the marker
    count of a block this repair had not touched at all — which is the
    shape of item 122 arriving through the back door. An unpaired backtick
    is treated as opening a span that runs to the end of its line, which is
    what a renderer does with it and which makes the count independent of
    anything appended later.
    """
    run = re.compile(r"`+")
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "`":
            opener = run.match(text, i)
            ticks = len(opener.group(0))
            end_of_line = text.find("\n", i)
            closer = None
            for candidate in run.finditer(text, opener.end()):
                if len(candidate.group(0)) == ticks:
                    closer = candidate
                    break
            if closer is not None and (end_of_line == -1 or closer.start() < end_of_line):
                stop = closer.end()
            else:
                # an unpaired run opens a span that runs to the end of its
                # line, which is what a renderer does with it
                stop = end_of_line if end_of_line != -1 else n
            out.append(" " * (stop - i))
            i = stop
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def bold_markers(text):
    """Real `**` markers only: those outside a code span."""
    return strip_code_spans(text).count("**")


def cmd_markers(args):
    paths = args.paths or ([os.path.join(ROOT, "state", n) for n in sorted(os.listdir(os.path.join(ROOT, "state"))) if n.endswith(".md")]
                          + [os.path.join(ROOT, "state", "archive", n) for n in sorted(os.listdir(os.path.join(ROOT, "state", "archive"))) if n.endswith(".md")])
    bad = 0
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        raw = text.count("**")
        real = bold_markers(text)
        if real % 2:
            bad += 1
            print(f"  ODD   {os.path.relpath(path, ROOT)}: {real} real markers, {raw} raw")
        elif raw != real:
            print(f"  note  {os.path.relpath(path, ROOT)}: {real} real markers, "
                  f"{raw} raw, {raw - real} inside a code span")
    print(f"files read: {len(paths)}; files with an odd count of real markers: {bad}")
    return 0


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------
# Every instrument here is planted against a case whose answer is known before
# it runs. A number returned without one of these having been run is a
# number reported with confidence.

DATE_LINE_SENTENCE = (
    "It is the second day of the second week of the third month of the year "
    "after the year after the year after the year after the year after the "
    "year after next, and it is the second hour, and the hours at that "
    "counter are the second to the sixth."
)

# thirty-two words, longer than a twenty-word window and shorter than a
# forty-word one, so the same plant is found at one threshold and is not
# found at the other
PLANTED_RUN = ("a room taken by the week has a table and a stool and a bed "
               "against one wall and a chair against none of the walls and "
               "four feet of bare plaster")

PLANTED_A = f"""# Chapter 9001: Planted A

{DATE_LINE_SENTENCE}

The boards came down at the second hour and the case came up out from behind the near end of them and stood on the counter with its lid open.

{PLANTED_RUN}
"""

PLANTED_B = f"""# Chapter 9002: Planted B

{DATE_LINE_SENTENCE}

The lid was shut and the stair at the back of that room went up past four floors before it came to anything at all.

{PLANTED_RUN}
"""

# a third file that shares the date line with A and B and no prose with either
PLANTED_C = f"""# Chapter 9003: Planted C

{DATE_LINE_SENTENCE}

The shed at the end of the lane off the Slade is about nine foot by eleven and there is a chain on the front bench.

The counters were not yet down and the case had not been lifted off its shelf behind them.
"""

PLANTED_SOLO = """# Chapter 9004: Planted D

the second half of a sentence a foreman of fifty-one began in a doorway about two years ago has still not arrived and nobody on that floor is going to ask her for it
"""

# A thirteen-word span lifted whole out of PLANTED_A into a fifth file, wrapped
# in different words at both ends. Thirteen is the point: it is under the
# twenty-word window `reprints` needs and over the five a lift has to be visible
# at, so the plant is found by one instrument and not by the other, which is the
# whole reason `lifts` exists.
PLANTED_LIFT = (
    "out from behind the near end of them and stood on the counter, and nobody "
    "in the room looked at it once"
)
PLANTED_E = f"""# Chapter 9005: Planted E

{DATE_LINE_SENTENCE}

{PLANTED_LIFT}
"""


def run_quietly(func, args):
    """Call a command function and capture what it prints and what it returns.

    A self-test that lets a command write to the terminal cannot tell a
    passing run from a failing one by looking, and a command that raises
    writes a traceback to the real stderr where it cannot be caught at all.
    Both streams are swapped for the duration and put back in a finally, so
    a plant that itself fails does not leave the rest of the run writing into
    a buffer that is about to be thrown away.
    """
    out, err = io.StringIO(), io.StringIO()
    real_out, real_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        code = func(args)
    finally:
        sys.stdout, sys.stderr = real_out, real_err
    return out.getvalue(), err.getvalue(), code


def cmd_selftest(args):
    ok = True

    def check(label, condition, detail):
        nonlocal ok
        mark = "ok  " if condition else "FAIL"
        print(f"  {mark} {label}: {detail}")
        if not condition:
            ok = False

    tmp_dir = os.path.join(ROOT, "tools", ".selftest")
    os.makedirs(tmp_dir, exist_ok=True)
    paths = {}
    try:
        for name, body in (("a", PLANTED_A), ("b", PLANTED_B), ("c", PLANTED_C),
                           ("d", PLANTED_SOLO), ("e", PLANTED_E)):
            paths[name] = os.path.join(tmp_dir, f"chapter-900{name}.md")
            with open(paths[name], "w", encoding="utf-8") as handle:
                handle.write(body)

        print("plant 1 — the date line is flagged whole, not by its opening clause")
        tokens, (on_date, on_term), raws = tokenize(paths["a"])
        date_tokens = sum(1 for f in on_date if f)
        term_tokens = sum(1 for f in on_term if f)
        planted_date = len(TOKEN.findall(DATE_LINE_SENTENCE))
        check("the whole date sentence is on the date line", date_tokens == planted_date,
              f"{date_tokens} tokens flagged, {planted_date} in the sentence")
        check("it is not flagged by its opening clause", date_tokens > 4,
              "a clause test would have flagged four words")
        check("the term list is a different classifier, not the same one twice",
              0 < term_tokens < date_tokens,
              f"{term_tokens} tokens inside a formula term against {date_tokens} on a date "
              f"line; the two sets are not equal, which is why the buckets are printed "
              f"separately and not merged before the figure is")

        print("plant 2 — a planted identical run is found at a twenty-word window")
        corpus = load_cached([paths["a"], paths["b"], paths["c"], paths["d"]])
        runs = shared_runs(corpus, 20)
        prose = [r for r in runs if classify(corpus, r) == "prose"]
        planted_run = len(TOKEN.findall(PLANTED_RUN))
        longest = max((r[2] - r[1] for r in prose), default=0)
        check("the planted run is found at its full length", longest == planted_run,
              f"longest prose run {longest} words, the plant is {planted_run}")
        touched = {os.path.basename(p) for p, _s, _e in prose}
        check("and only the two files that hold it are named",
              touched == {"chapter-900a.md", "chapter-900b.md"}, f"{sorted(touched)}")

        print("plant 3 — the same files return nothing at a window above the run")
        narrow = shared_runs(corpus, planted_run + 1)
        narrow_prose = [r for r in narrow if classify(corpus, r) == "prose"]
        narrow_longest = max((r[2] - r[1] for r in narrow_prose), default=0)
        check("a window above the run returns no prose", narrow_longest == 0,
              f"at a {planted_run + 1}-word window the longest prose run is {narrow_longest}")

        print("plant 4 — the classifier is a lookup and does not invent a formula bucket")
        for mode in ("date", "terms", "either"):
            formula = [r for r in runs if classify(corpus, r, mode) == "formula"]
            rest = [r for r in runs if classify(corpus, r, mode) == "prose"]
            check(f"under the {mode!r} classifier the buckets are every run",
                  len(formula) + len(rest) == len(runs),
                  f"{len(formula)} formula + {len(rest)} prose of {len(runs)}")
            if mode == "date":
                check("the date run is formula", len(formula) == 3,
                      f"{len(formula)} formula run(s), one per file that carries the date line")
                check("the prose run is prose", len(rest) == 2,
                      f"{len(rest)} prose run(s), one per file that carries the run")

        print("plant 5 — a file that shares only the date line is not a prose re-print")
        pair = load_cached([paths["a"], paths["c"]])
        solo = shared_runs(pair, 20)
        solo_prose = [r for r in solo if classify(pair, r) == "prose"]
        check("date-only sharing is not prose", len(solo_prose) == 0,
              f"{len(solo_prose)} prose run(s) between a file and its calendar twin")

        print("plant 6 — the token text is read, not trusted: case and digits are in the class")
        caps = [t for t in raws if any(c.isupper() for c in t)]
        check("uppercase survives tokenising", len(caps) > 0,
              f"{len(caps)} tokens carried a capital, e.g. {caps[:4]}")
        probe = TOKEN.findall("Received it on the fourth of the month.")
        check("a capitalised word is one token", "Received" in probe, f"{probe}")
        check("no token begins one character into a word", "eceived" not in probe,
              "the failure this plant exists for is a chopped capital, not a count")
        digits = [t for t in tokens if any(c.isdigit() for c in t)]
        check("digits survive tokenising", len(digits) > 0, f"{len(digits)} tokens carried a digit")

        print("plant 7 — a `**` inside a code span is not an unclosed bold")
        shaped = "a row called `**N. OPEN` here, and **a real bold that is closed**"
        check("code-span marker is not counted", bold_markers(shaped) == 2,
              f"{shaped.count('**')} raw, {bold_markers(shaped)} real")
        check("an unclosed real bold is counted", bold_markers("**opened and never closed") == 1,
              f"{bold_markers('**opened and never closed')} real marker, odd, reported")
        doubled = "``a span holding a ` inside it, and **a bold** after it`` then **another bold**\n"
        check("a doubled-backtick span is one span, not two",
              bold_markers(doubled) == 2,
              f"{doubled.count('**')} raw, {bold_markers(doubled)} real: the bold outside the "
              f"span counts and the bold inside it does not, and a stripper that treated the "
              f"two backticks as two openers would have got a different answer")
        unpaired = "`a code span that is never closed\n**a real bold** and more\n"
        check("an unpaired backtick does not swallow the rest of the file",
              bold_markers(unpaired) == 2,
              f"{bold_markers(unpaired)} real markers, and the same count with a line appended after it: "
              f"{bold_markers(unpaired + 'appended text with a ` of its own\n')}")

        print("plant 8 — the splitter keeps a closing mark after a full stop")
        joined = 'He said "It is done." Then she left, and the room went on.'
        parts = SPLIT.split(joined)
        check("two sentences, not one", len(parts) == 2, f"{len(parts)}")
        check("no fragment begins with a closing mark",
              not any(p.lstrip().startswith(('"', "'", ")", "]")) for p in parts),
              "checked")
        harmful = len([p for p in re.split(r"(?<=[.!?])\s+", joined) if p.strip()])
        check("the harmful rule merges the two", harmful == 1,
              f"whitespace-after-full-stop splitter gives {harmful}; "
              f"the two rules differ by {len(parts) - harmful}")

        print("plant 9 — a volume with no chapters is a failure and not a zero")
        empty_out, empty_err, empty_code = run_quietly(
            cmd_sentences, argparse.Namespace(volume="volume-00"))
        check("a volume that matches no file exits non-zero", empty_code == 1,
              f"exit {empty_code}")
        check("and it says on the error stream that nothing was measured",
              "nothing was measured" in empty_err and "Traceback" not in empty_err
              and "Traceback" not in empty_out,
              f"stdout {empty_out!r}, stderr {empty_err!r}")
        full_out, _full_err, full_code = run_quietly(
            cmd_sentences, argparse.Namespace(volume="volume-11"))
        check("a volume that does match a file exits zero", full_code == 0,
              f"exit {full_code}; it printed {full_out.splitlines()[0]!r}")

        print("plant 10 — a lift is found at a size `reprints` cannot see")
        lift_index = build_lift_index([paths["a"], paths["b"], paths["c"], paths["d"]])
        lifted = [t.lower() for t in TOKEN.findall(PLANTED_LIFT)]
        length, text, other = longest_lift(lifted, lift_index)
        planted_lift = len(TOKEN.findall(
            "out from behind the near end of them and stood on the counter"))
        check("the lifted span is returned at its full length", length == planted_lift,
              f"longest lift {length} words, the plant is {planted_lift}; '{text}'")
        check("and it names the chapter it came out of",
              other is not None and os.path.basename(other) == "chapter-900a.md",
              f"{os.path.basename(other) if other else None}")
        pair_lift = load_cached([paths["a"], paths["e"]])
        rep = shared_runs(pair_lift, 20)
        rep_prose = [r for r in rep if classify(pair_lift, r) == "prose"]
        check("the same span is invisible to a twenty-word re-print window",
              not any((r[2] - r[1]) >= planted_lift for r in rep_prose),
              f"reprints at 20 words returns {len(rep_prose)} prose run(s) over A and E; "
              f"the lift is {planted_lift} words and sits under the window, so a repair "
              f"checked only with reprints passes with the plant standing")

        print("plant 11 — the range under repair is out of its own index")
        outside = build_lift_index([paths["c"]])
        run_tokens = [t.lower() for t in TOKEN.findall(PLANTED_RUN)]
        solo_tokens = [t.lower() for t in TOKEN.findall(PLANTED_SOLO)]
        inside_zero = longest_lift(run_tokens, outside)[0]
        check("a run held only by chapters inside the range is not a lift",
              inside_zero == 0,
              f"PLANTED_RUN lives in chapter-900a and -900b and the index holds neither, "
              f"so it returns {inside_zero}; a lift has to reach a chapter the range does "
              f"not contain, or every chapter lifts from its own neighbour")
        check("and the same run does lift once a holder is in the index",
              longest_lift(run_tokens, build_lift_index([paths["a"], paths["c"]]))[0]
              == min(len(TOKEN.findall(PLANTED_RUN)), LIFT_CAP),
              f"with chapter-900a in the index the run returns {min(len(TOKEN.findall(PLANTED_RUN)), LIFT_CAP)} "
              f"words, which is the full {len(TOKEN.findall(PLANTED_RUN))}-word plant at the "
              f"{LIFT_CAP}-word cap; the zero above is the exclusion and not a broken matcher")
        check("prose that shares nothing lifts nothing",
              longest_lift(solo_tokens, outside)[0] == 0,
              f"{longest_lift(solo_tokens, outside)[0]}; PLANTED_SOLO stands only in "
              f"chapter-900d, which is not in the index, and a real lift is not a self-match")

    finally:
        for path in paths.values():
            if os.path.exists(path):
                os.remove(path)
        if os.path.isdir(tmp_dir) and not os.listdir(tmp_dir):
            os.rmdir(tmp_dir)

    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("selftest")

    p_mark = sub.add_parser("markers")
    p_mark.add_argument("paths", nargs="*")

    p_words = sub.add_parser("words")
    p_words.add_argument("--volume", default=None)

    p_cal = sub.add_parser("calendar")
    p_cal.add_argument("--volume", default=None)

    p_sent = sub.add_parser("sentences")
    p_sent.add_argument("--volume", default=None)

    p_rep = sub.add_parser("reprints")
    p_rep.add_argument("--window", type=int, default=20)
    p_rep.add_argument("--volume", default=None)
    p_rep.add_argument("--mode", choices=("date", "terms", "either"), default="either")
    p_rep.add_argument("--show", type=int, default=0)

    p_lift = sub.add_parser("lifts")
    p_lift.add_argument("--volume", default=None)
    p_lift.add_argument("--first", type=int, default=None)
    p_lift.add_argument("--last", type=int, default=None)
    p_lift.add_argument("--base", default=None,
                        help="a commit to read the range at; the lines it does not "
                             "hold are the added ones and the lines it does hold are "
                             "the volume's own formula baseline")
    p_lift.add_argument("--min", type=int, default=6)
    p_lift.add_argument("--show", type=int, default=0)

    args = parser.parse_args()
    if args.cmd == "selftest":
        return cmd_selftest(args)
    if args.cmd == "words":
        cmd_words(args)
    if args.cmd == "calendar":
        cmd_calendar(args)
    if args.cmd == "sentences":
        return cmd_sentences(args)
    if args.cmd == "markers":
        return cmd_markers(args)
    if args.cmd == "reprints":
        cmd_reprints(args)
    if args.cmd == "lifts":
        return cmd_lifts(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
