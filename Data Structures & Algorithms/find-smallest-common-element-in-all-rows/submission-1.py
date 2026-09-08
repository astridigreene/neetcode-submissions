class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = defaultdict(int)
        max_num = mat[0][len(mat[0])-1]
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                if num > max_num:
                    # print(num, counts[num], i)
                    break
                if counts[num] < i:
                    continue
                counts[num] += 1
        
        res = -1
        for n, c in counts.items():
            print(n, c)
            if c == len(mat):
                if res == -1:
                    res = n
                else:
                    if n < res:
                        res = n
        
        return res