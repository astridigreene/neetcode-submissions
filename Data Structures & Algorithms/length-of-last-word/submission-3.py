class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        occured = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and occured:
                return res
            if s[i] != ' ':
                occured = True
                res += 1
        return res