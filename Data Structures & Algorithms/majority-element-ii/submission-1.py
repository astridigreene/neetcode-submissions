class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        
        for i, num in enumerate(nums):
            counts[num] += 1

            if len(counts) > 2:
                new_count = defaultdict(int)

                for n, c in counts.items():
                    if c > 1:
                        new_count[n] = c - 1
                counts = new_count

        res = []
        for n, c in counts.items():
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res

