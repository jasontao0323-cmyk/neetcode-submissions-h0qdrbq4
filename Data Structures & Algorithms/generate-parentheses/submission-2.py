# Valid parentheses strings are built from smaller valid strings, 
# combining smaller answers to form every valid result for k pairs.
# TC: O(4n/sqrt(n))
# SC: O(n)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)

        return res[-1]