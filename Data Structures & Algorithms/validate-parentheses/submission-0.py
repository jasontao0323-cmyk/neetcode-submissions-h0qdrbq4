# isValid
# Brute Force: If the string is valid, we can repeately 
# remove these matching pairs until nothing is left

class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
        