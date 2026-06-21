class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr_count = 0
        eq_val = 0
        for i, num in enumerate(nums):
            if i >= len(nums)-eq_val:
                break
            if num == val:
                swap = True
                while swap and i != len(nums)-eq_val:
                    eq_val += 1
                    nums[i] = nums[len(nums)-eq_val]
                    if nums[i] != val:
                        swap = False
        return len(nums)-eq_val