class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lets_id = defaultdict(list)
        for i, string in enumerate(strs):
            lets_id["".join(sorted(string))].append(i)
        res = []
        for i in lets_id.values():
            curr_list = []
            for j in i:
                curr_list.append(strs[j])
            res.append(curr_list)

        return res