import math
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{i}/{j}" for i in range(1, n) for j in range(i + 1, n + 1) if math.gcd(i, j) == 1]

sol = Solution()
for i in range(10):
    print(len(sol.simplifiedFractions(i)), end=" ")