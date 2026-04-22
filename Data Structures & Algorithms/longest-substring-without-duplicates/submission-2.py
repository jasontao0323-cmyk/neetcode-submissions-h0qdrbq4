# lengthOfLongestSubstring
#A sliding window approach with a map for character indices optimizes the process of 
# finding the longest substring without repeating characters.
# TC: O(n*m)
# SC: O(m)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res