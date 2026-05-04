# Generate all length 2n strings of ‘(‘ and ‘)’, validate using balance.
# TC: O(2^2n*n)
# SC: O(2^2n*n)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open

        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs("")
        return res