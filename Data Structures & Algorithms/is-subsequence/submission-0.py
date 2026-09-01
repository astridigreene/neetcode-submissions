class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for l, letter in enumerate(t):
            if index >= len(s):
                return True
            if s[index] == letter:
                index += 1
        if index == len(s):
            return True
        return False