class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = defaultdict(int)
        max_num = mat[0][len(mat[0])-1]
        for i, row in enumerate(mat):
            if row[len(row)-1] < max_num:
                max_num = row[len(row)-1]
            for j, num in enumerate(row):
                if num > max_num:
                    counts.pop(num, None)
                    break
                if counts[num] < i:
                    counts.pop(num, None)
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