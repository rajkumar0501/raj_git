class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0
        prev_value = 0

        for value in reversed(s):
            if value in roman:
                if roman[value] >= prev_value:
                    total = roman[value] + total
                    prev_value = roman[value]
                elif roman[value] < prev_value:
                    total = total - roman[value]
                    prev_value = roman[value]
            else:
                return "Invalid Input"

        return total



solution = Solution()
print(solution.romanToInt('MCMXCIV'))
