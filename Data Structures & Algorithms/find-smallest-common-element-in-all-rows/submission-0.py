class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = defaultdict(int)
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                counts[num] += 1
        
        res = -1
        for n, c in counts.items():
            if c == len(mat):
                if res == -1:
                    res = n
                else:
                    if n < res:
                        res = n
        
        return res