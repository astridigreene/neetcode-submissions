class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''

        iterate rows, use a set to check 1-9
        iterate cols, use a set to check 1-9
        iterate boxes, use a set to check 1-9
            rows: 0-2, cols 0-2
            rows: 0-2, cols 3-5
            rows: 0-2, cols 6-8
        
        3 maps:
        - rows map, key: row, val: set
        - cols map, key: col, val: set
        - boxes map:
            key: ((row//3), (col//3)), val: set

        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False 
                if board[i][j] in cols[j]:
                    print("in col")
                    return False
                if board[i][j] in boxes[(i//3, j//3)]:
                    print("in box")
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3, j//3)].add(board[i][j])
        return True


