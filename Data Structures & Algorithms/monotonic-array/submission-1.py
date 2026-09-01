class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff = 0
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 0:
                pass
            elif diff == 0:
                diff = (nums[i+1] - nums[i])/abs(nums[i+1] - nums[i])
            else:
                if (nums[i+1] - nums[i])/abs(nums[i+1] - nums[i]) != diff:
                    return False
        return True