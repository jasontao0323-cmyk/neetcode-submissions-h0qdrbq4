# groupAnagrams
# Hash table
# TC: O(m*nlogn)
# SC: O(m*n)
# Logic: Hash table represent every string by frequency

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())