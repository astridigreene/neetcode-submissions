class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        eq_val = 0
        i = 0
        while i < len(nums)-eq_val:
            if nums[i] == val:
                eq_val += 1
                nums[i] = nums[len(nums)-eq_val]
            else:
                i += 1
        return len(nums)-eq_val