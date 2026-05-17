class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tot_string = ""
        curr_char = ''
        str_id = 0
        while True:
            if len(strs[0]) <= str_id:
                return tot_string
            curr_char = strs[0][str_id]
            for i, string in enumerate(strs):
                if len(string) <= str_id:
                    return tot_string
                if string[str_id] != curr_char:
                    return tot_string
            tot_string += curr_char
            str_id += 1
        return tot_string