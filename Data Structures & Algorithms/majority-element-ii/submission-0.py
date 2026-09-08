class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        res = []
        for i, num in enumerate(nums):
            counts[num] += 1
            if counts[num] == len(nums)//3 + 1:
                res.append(num)
        return res

            # 10/3 = 3