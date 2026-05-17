class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_char = ''
        str_id = 0
        while True:
            if len(strs[0]) <= str_id:
                return strs[0][:str_id]
            curr_char = strs[0][str_id]
            for i, string in enumerate(strs):
                if len(string) <= str_id:
                    return strs[0][:str_id]
                if string[str_id] != curr_char:
                    return strs[0][:str_id]
            str_id += 1
        return strs[0][:str_id]