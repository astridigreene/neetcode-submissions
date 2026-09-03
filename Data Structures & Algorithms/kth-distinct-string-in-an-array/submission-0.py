class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        nums = defaultdict(int)

        for i, num in enumerate(arr):
            if nums[num] == 0:
                nums[num] = 1
            else:
                nums[num] = -1
        
        cnt = 0
        for i, num in enumerate(arr):
            if nums[num] == 1:
                cnt += 1
            if cnt == k:
                return num
        return ""

        # we need to know the first one's index
