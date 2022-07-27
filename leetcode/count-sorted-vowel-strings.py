from itertools import count
from math import comb


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n+4, 4)
        # (n + 1) * (n + 2) * (n + 3) * (n + 4) / 24

sol = Solution()
print(sol.countVowelStrings(1))
print(sol.countVowelStrings(2))
print(sol.countVowelStrings(33))