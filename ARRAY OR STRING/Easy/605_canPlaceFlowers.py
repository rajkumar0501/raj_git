class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:

        count = 0
        i = 0

        while i < len(flowerbed):
            if (flowerbed[i] == 0) and (i == 0 or flowerbed[i - 1] == 0) and (i == (len(flowerbed) - 1) or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1

            i += 1

        print(count)

        if count >= n:
            return True
        else:
            return False


solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,0,1], 2))
