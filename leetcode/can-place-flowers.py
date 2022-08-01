class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) == 1 and n > flowerbed[0]:  return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i > 0 and i < len(flowerbed) - 1:
                    if flowerbed[i-1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i > 0 and flowerbed[-2] == 0:
                    n -= 1
                elif i < len(flowerbed) - 1 and not (flowerbed[1] ^ flowerbed[0]) and not flowerbed[0]:
                    flowerbed[0] = 1
                    n -= 1
        return n <= 0
    
sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0,0, 0, 1], 2))
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(sol.canPlaceFlowers([0, 0, 1, 0, 1], 1))
print(sol.canPlaceFlowers([0, 0], 2))
print(sol.canPlaceFlowers([0, 0], 2))
