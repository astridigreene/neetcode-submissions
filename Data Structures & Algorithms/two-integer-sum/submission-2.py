class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if (nums[i]) in d and d[nums[i]] != i:
                return [min(i, d[nums[i]]), max(i, d[nums[i]])]
            d[target - nums[i]] = i
        return[0,0]