class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        space = False
        for i, let in enumerate(s):
            if let == ' ':
                space = True
            elif space:
                word = let
                space = False
            else:
                word += let
        return len(word)