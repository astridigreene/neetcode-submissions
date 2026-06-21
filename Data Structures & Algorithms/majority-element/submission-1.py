class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        curr=nums[0]
        for num in nums:
            if num == curr:
                count += 1
                if count > len(nums)/2:
                    return num
            else:
                count = 1
                curr = num
        return 0