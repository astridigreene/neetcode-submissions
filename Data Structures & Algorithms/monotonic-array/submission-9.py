class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False

        for i in range(0, len(nums) - 1):
            if nums[i + 1] > nums[i]:
                increasing = True
            elif nums[i + 1] < nums[i]:
                decreasing = True
            if increasing and decreasing:
                return False
        return not(increasing and decreasing)