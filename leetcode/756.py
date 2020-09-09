# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-08 19:52:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-08 19:53:53

"""
756. Pyramid Transition Matrix Medium
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
 

Example 2:

Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Constraints:

bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
Accepted 21,225 Submissions 38,710
"""
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def dfs(pre: list, now: list):
            # print(pre, now)
            if self.res:
                return
            if len(now) >= 2:
                if now[-2] + now[-1] not in g:
                    return
            if len(now) == len(pre) - 1:
                if len(now) == 1:
                    self.res = True
                    return
                if self.res:
                    return
                dfs(now, [])
                return
            idx = len(now)
            for ii in g[pre[idx] + pre[idx + 1]]:
                if self.res:
                    return
                dfs(pre, now + [ii])

        N = len(bottom)
        self.res = False
        g = defaultdict(set)
        for ii in allowed:
            g[ii[:2]].add(ii[-1])
        dfs(list(bottom), [])
        return self.res
