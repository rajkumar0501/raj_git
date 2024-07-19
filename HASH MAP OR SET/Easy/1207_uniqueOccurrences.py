class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:

        hash_map = {}

        for num in arr:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        s = set(hash_map.values())


        return len(hash_map) == len(s)


solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
