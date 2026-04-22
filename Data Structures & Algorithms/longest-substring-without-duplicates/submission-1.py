# lengthOfLongestSubstring
# Brute-force approach finds longest
# substring by checking each starting point 
# and extending until a duplicate character is found.
# TC: O(n*m)
# SC: O(m)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res