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
"""

import os

LINE = "Entered 156 bounties this week, won $0, and GitHub said no more repos today."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
