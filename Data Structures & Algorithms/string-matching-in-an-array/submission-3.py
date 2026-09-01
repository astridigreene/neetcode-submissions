class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i, word in enumerate(words):
            for j in range(len(words)):
                if (i == j):
                    pass
                elif self.isSubstring(word, words[j]):
                    res.append(word)
                    break
        return res

    def isSubstring(self, small: str, word: str) -> bool:
        index = 0
        for i, let in enumerate(word):
            if index == len(small):
                return True
            if small[index] == let:
                if small == word[i:i+len(small)]:
                    return True
        if index == len(small):
            return True
        return False