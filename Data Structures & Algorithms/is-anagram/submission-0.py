class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dictionary = {}
        for i in range(len(s)):
            dictionary[s[i]] = dictionary.get(s[i], 0) + 1
            print("s" + dictionary[s[i]])
            dictionary[t[i]] = dictionary.get(t[i], 0) - 1
        if not dictionary:
            return True
        return False
        