class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = [0] * (len(grid) * len(grid))
        for i, row in enumerate(grid):
            for j, num in enumerate(grid[i]):
                nums[num-1] += 1
                if nums[num-1] == 2:
                    a = num
        for i, num in enumerate(nums):
            if num == 0:
                return [a, i+1]
            