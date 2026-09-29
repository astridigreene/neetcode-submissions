class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ""
        for i, string in enumerate(strs):
            encoded += str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
