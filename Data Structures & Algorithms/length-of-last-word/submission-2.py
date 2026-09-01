class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        occured = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and occured:
                return len(word)
            if s[i] != ' ':
                occured = True
                word += s[i]
        return len(word)