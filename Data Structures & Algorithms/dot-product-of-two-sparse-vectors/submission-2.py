class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums
        self.open_slots = set()
        for i, num in enumerate(nums):
            if num != 0:
                self.open_slots.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for i, num in enumerate(vec.open_slots):
            if num in self.open_slots:
                prod += (vec.vector[num] * self.vector[num])
        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
