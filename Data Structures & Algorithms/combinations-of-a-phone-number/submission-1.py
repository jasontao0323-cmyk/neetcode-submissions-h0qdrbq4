# Combinations are built level by level, starting 
# with an empty string and appending characters mapped to each digit.
# TC: O(n*4^n)
# SC: O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digitToChar[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res