class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        nums = defaultdict(int)

        for i, num in enumerate(arr):
            if nums[num] == 0:
                nums[num] = 1
            else:
                nums[num] = -1
        
        for i, num in enumerate(arr):
            if nums[num] == 1:
                k -= 1
            if k == 0:
                return num
        return ""



