class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if (n) in d and d[n] != i:
                return [min(i, d[n]), max(i, d[n])]
            d[target - n] = i
        return[0,0]