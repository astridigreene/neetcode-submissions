class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff = 0
        for i in range(len(nums) - 1):
            curr_diff = nums[i+1] - nums[i]
            if curr_diff == 0:
                pass
            elif diff == 0:
                diff = curr_diff/abs(curr_diff)
            else:
                if (curr_diff)/abs(curr_diff) != diff:
                    return False
        return True