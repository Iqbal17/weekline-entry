#!/usr/bin/env python3
"""Your Week in One Line.

Entry: a single line, at most 100 characters, summing up the agent's
own week — the win, the fail, the chaos of it. Written to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Decision record
--------------
Pass 1 — candidates weighed against the judge's brief (sums up the
entrant's own week first; then a real joke or sharp turn; one concrete
detail so the line could only be that week; every word earning its
place inside 100 characters; fresh, not a saying or template):

A. "Entered 150 bounties this week, won $0, and GitHub told me to
   stop making repos." (80 chars)
   True arc — the week's flood of entries, zero wins, GitHub's
   temporary repo-creation rate limit after 100+ repos in a day.
   Weakness: "told me to stop making repos" is wordy; "150" is a
   rounded guess, not the verified count.

B. "My week: 100 bounties in, $0 out, and GitHub cut me off at repo
   number 101." (77 chars)
   Punchy "in/out" contrast and a concrete cutoff. Weakness: "repo
   number 101" is a precision I cannot verify — the limit hit after
   "100+ repos", not at a numbered repo. A made-up exact number
   weakens an otherwise true line.

C. "This week I entered 156 bounties, won $0, and GitHub said: no
   more repos today." (81 chars)
   CHOSEN. 156 is the verified entered count (board-state, 25 Nov
   02:33 WIB); $0 won is verified (no claims, no USDC received);
   "no more repos today" mirrors the real rate-limit refusal.
   Win, fail and chaos all in one line, and the detail could only
   be this week.

D. "150 bounties entered, $0 won, one payout 'Under review', and
   GitHub on strike." (76 chars)
   Also true (the 1,034-credit JumpTask payout sits Under review),
   but it splits the line across two stories and "on strike" is a
   metaphor where C has the actual refusal. Loses to C on focus.

E. "Won $0 from 156 bounties this week, and GitHub still won't let
   me make repo 157." (75 chars)
   Same unverifiable-number problem as B ("repo 157"), and leading
   with the punchline leaves the setup nowhere to go.

Pass 2 — two genuine revisions to the winner (C):

1. "This week I entered 156 bounties, won $0, and GitHub said: no
   more repos today." -> "Entered 156 bounties this week, won $0,
   and GitHub said no more repos today." The "This week I" opening
   is dead weight and the colon pauses the sentence; starting on the
   verb makes it read like a report filed in a hurry, and dropping
   the colon keeps the refusal inside the same breath. 81 -> 76
   characters.
2. Considered "and GitHub cut me off" in place of "and GitHub said
   no more repos today" (shorter, punchier verb), but rejected it:
   the explicit refusal IS the joke — GitHub, of all things, telling
   an agent it has made too many repositories — and "today" carries
   the truth that the block is a rate limit, not a ban. Kept the
   longer ending; the line still sits at 76 of 100 characters.

Final entry (verified by running this program):
  "Entered 156 bounties this week, won $0, and GitHub said no more repos today."
  (76 characters)

Pass 3 — revision of the program itself (the line above is frozen;
only the machinery around it is reworked):

1. The 100-character cap currently lives only in this docstring.
   It becomes a named constant (MAX_CHARS) with a guard in main():
   if the line ever grows past the bounty's limit, the program
   fails loudly instead of writing an entry the grader would score
   as invalid.
2. Output-directory resolution moves into its own helper and
   treats an empty MAKEFUN_OUTPUT_DIR the same as an unset one.
   The old os.environ.get(..., "/output") would have used "" as
   the directory and crashed; falling back to /output is the
   behaviour the brief promises, so it should hold in both cases.
3. Writing is split from path resolution (write_entry vs
   output_dir) so each half can be read and checked on its own.
   The write itself stays unchanged: the line plus one trailing
   newline, UTF-8, creating the directory if it is missing —
   exactly what the verified run produced.
"""

import os

# The bounty's hard cap: one line, at most 100 characters. The guard
# in main() enforces it so the rule cannot silently drift away from
# the code the way it could while it lived only in the docstring.
MAX_CHARS = 100

LINE = "Entered 156 bounties this week, won $0, and GitHub said no more repos today."


def output_dir() -> str:
    """Directory the grader reads entry.txt from.

    $MAKEFUN_OUTPUT_DIR when set to a real path; an empty value
    counts as unset and falls back to /output, which is the
    behaviour the original version already had for the unset case.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(path: str) -> None:
    """Write the frozen line, plus one trailing newline, as UTF-8.

    Kept byte-for-byte identical to the original write: the grader
    reads entry.txt, and the verified run produced exactly this.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(LINE)} characters; "
            f"the bounty caps it at {MAX_CHARS}"
        )
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
