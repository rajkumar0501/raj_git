class Solution:
    def compress(self, chars: [str]) -> int:

        length = len(chars)
        i = 0
        j = 0
        current = None
        count = 0

        while j < length:
            if chars[i] == current:
                chars.remove(chars[i])
                count += 1
                j += 1

            elif chars[i] != current and count > 1:
                if count > 9:
                    for a in str(count):
                        chars.append(str(a))
                elif count > 1:
                    chars.append(str(count))
                count = 0

            else:
                chars.append(chars[i])
                current = chars[i]
                count = 0
                chars.remove(chars[i])
                count += 1
                j += 1


        if count > 1:
            if count > 9:
                for b in str(count):
                    chars.append(str(b))
            else :
                chars.append(str(count))



        return len(chars)

solution = Solution()
print(solution.compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))
