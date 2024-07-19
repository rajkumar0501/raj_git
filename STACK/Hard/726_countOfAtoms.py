class Solution:
    def countOfAtoms(self, formula: str) -> str:

        sk = None
        skl = None
        stack = []
        for i in range(len(formula)):
            x = []
            if i == sk or i == skl:
                continue

            if i < len(formula) - 1 and formula[i] == ")" and formula[i + 1].isdigit():
                while stack and stack[-1] != "(":
                    x.append(stack.pop())

                if stack and stack[-1] == "(":
                    stack.pop()

                if i + 1 < len(formula) and formula[i + 1].isdigit():
                    if i + 2 < len(formula) and formula[i + 2].isdigit():
                        n = int(formula[i + 1:i + 3])
                        skl = i + 2
                    else:
                        n = int(formula[i + 1])
                        skl = i + 1
                else:
                    n = 1

                sk = i + 1

                x = x* n
                for q in reversed(x):
                    stack.append(q)

            else:
                stack.append(formula[i])

        li = []
        k = 0
        l = len(stack)

        while k < l:
            if stack[k] == "(" or stack[k] ==")":
                k += 1
                continue
            elif k < (l - 1) and stack[k].isdigit() and stack[k + 1].isdigit():
                s = stack[k] + stack[k + 1]
                li.append(s)
                k += 2
            elif k < (l - 1) and stack[k].isupper() and stack[k + 1].islower():
                s = stack[k] + stack[k + 1]
                li.append(s)
                k += 2
            else:
                li.append(stack[k])
                k += 1


        le = len(li)
        hash_map = {}
        i = 0
        while i < le:
            if i < (le - 1) and li[i].isdigit():
                li[i], li[i + 1] = li[i + 1], li[i]
                hash_map[li[i]] = int(li[i + 1])
                i += 1

            elif i < (le - 1) and li[i + 1].isdigit():
                if li[i] in hash_map:
                    hash_map[li[i]] += int(li[i + 1])
                else:
                    hash_map[li[i]] = int(li[i + 1])
                i += 1

            else:
                if li[i] in hash_map:
                    hash_map[li[i]] += 1
                else:
                    hash_map[li[i]] = 1

            i += 1

        sorted_hash_map = dict(sorted(hash_map.items()))


        output = ""

        for key, value in sorted_hash_map.items():
            if value > 1:
                output += f"{key}{value}"
            else:
                output += key

        return output



solution = Solution()
print(solution.countOfAtoms("Mg(H2O)N"))
