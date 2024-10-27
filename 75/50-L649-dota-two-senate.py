# https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75
'''
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on
a change in the Dota2 game. The voting for this change is a round-based procedure. In each round,
each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and
all the following rounds.

Announce the victory: If this senator found the senators who still have rights to vote are all from
the same party, he can announce the victory and decide on the change in the game.

Given a string senate representing each senator's party belonging. The character 'R' and 'D'
represent the Radiant party and the Dire party. Then if there are n senators, the size of the given
string will be n.

The round-based procedure starts from the first senator to the last senator in the given order.
This procedure will last until the end of voting. All the senators who have lost their rights will be
skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party.
Predict which party will finally announce the victory and change the Dota2 game.
The output should be "Radiant" or "Dire".
'''

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Queue for Radiant (R) and Dire (D) senators
        qr, qd, z = deque(), deque(), len(senate)

        # Populate the queues with the initial indices of 'R' and 'D' in sequence
        for i, s in enumerate(senate):
            if s == 'R': qr.append(i)
            else: qd.append(i)

        # Process each round until one party is banned entirely
        # (each party is smart enough to win)
        while qr and qd:
            ir = qr.popleft()
            id = qd.popleft()

            # The senator with the smaller index acts first
            if ir < id:
                # Radiant senator acts first, so add them back with an updated index
                qr.append(ir + z)
            else:
                # Dire senator acts first, so add them back with an updated index
                qd.append(id + z)

        # Because the remaining party will announce the victory,
        # if Radiant queue is empty, Dire wins; otherwise, Radiant wins.
        return "Radiant" if qr else "Dire"


def run_tests():
    test_cases = [
        ("RRRRR", "Radiant"),
        ("RDDRR", "Radiant"),
        ("DDRRR", "Dire"),
        ("RDRDR", "Radiant"),
        ("RDDR", "Radiant"),
    ]

    for i, (senate, expected) in enumerate(test_cases):
        result = Solution().predictPartyVictory(senate)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed!")

run_tests()



'''
Let’s break down the process step by step for the input string "DDRRR" and clarify why the output is "Dire."

Initial Setup
The input "DDRRR" represents senators from two parties:

D for Dire
R for Radiant
From the string:

D senators: D0 (index 0) and D1 (index 1)
R senators: R0 (index 2), R1 (index 3), and R2 (index 4)
Step-by-Step Elimination Process
Starting Point: The list of senators is:

D0, D1, R0, R1, R2
First Round:

The first senator is D0 (index 0).
The next senator is D1 (index 1).
Since D0 (Dire) and D1 (Dire) are both from the same party, D0 can’t eliminate an enemy senator. So, it will ban D1.
After this ban, the list is now:
D0, R0, R1, R2
Second Round:

Now the first senator is still D0.
The next senator in line is R0 (index 2).
D0 eliminates R0 because the first D senator acts first.
The remaining senators now are:
D0, R1, R2
Third Round:

The first senator is still D0.
The next senator is R1 (index 3).
D0 eliminates R1.
The remaining senators now are:
D0, R2
Fourth Round:

The first senator is still D0.
The next senator is R2 (index 4).
D0 eliminates R2.
Now the list has only:
D0
Conclusion
At this point:

D has 1 senator left (D0).
R has 0 senators left.
Since all Radiant senators have been eliminated and only Dire senators remain, the output is "Dire."
'''