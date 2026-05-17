class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_chars = []
        curr_char = ''
        str_id = 0
        while True:
            if len(strs[0]) <= str_id:
                return "".join(prefix_chars)
            curr_char = strs[0][str_id]
            for i, string in enumerate(strs):
                if len(string) <= str_id:
                    return "".join(prefix_chars)
                if string[str_id] != curr_char:
                    return "".join(prefix_chars)
            prefix_chars.append(curr_char)
            str_id += 1
        return "".join(prefix_chars)