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
                    # swap curr and last(ish)
                    temp = nums[len(nums)-eq_val]
                    nums[len(nums)-eq_val] = num
                    nums[i] = temp
                    if nums[i] != val:
                        swap = False
                    # self.print_arr(nums)
        return len(nums)-eq_val

    def print_arr(self, nums: List[int]):
        for num in nums:
            print(nums)