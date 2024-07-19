class Solution:
    def maxOperations(self, nums: [int], k: int) -> int:

        hash_map = {}
        count_pairs = 0

        for num in nums:
            y = k - num

            if y in hash_map and hash_map[y] > 0:
                count_pairs += 1
                hash_map[y] -= 1
            else:
                if num in hash_map:
                    hash_map[num] += 1
                else:
                    hash_map[num] = 1

        return count_pairs


solution = Solution()
print(solution.maxOperations([1,2,3,4], 5))
