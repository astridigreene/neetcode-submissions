class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            # nums to add = i - 1
            # row 2, 0 + 1
            # row 3: 0 + 1, 1 + 2
            # row 4: 0 + 1, 1 + 2, 2 + 3
            res.append([1])
            for j in range(0, i-1):
                res[i].append(res[i-1][j] + res[i-1][j+1])
            res[i].append(1)
        return res