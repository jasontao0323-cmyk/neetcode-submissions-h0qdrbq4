# groupAnagrams
# Sorting
# TC: O(m*nlogn)
# SC: O(m*n)
# Logic: Hash map store key as sorted version, value is the list of ftring

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())