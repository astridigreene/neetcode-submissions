class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(0, len(nums) - 1):
            if nums[i + 1] > nums[i]:
                decreasing = False
            elif nums[i + 1] < nums[i]:
                increasing = False
        return increasing or decreasing