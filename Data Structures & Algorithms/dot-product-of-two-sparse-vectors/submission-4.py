class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = []
        for i, num in enumerate(nums):
            if num != 0:
                self.vector.append([i, num])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0

        c1, c2 = 0, 0

        while c1 < len(self.vector) and c2 < len(vec.vector):
            if self.vector[c1][0] == vec.vector[c2][0]:
                prod += (self.vector[c1][1] * vec.vector[c2][1])
                c1 += 1
                c2 += 1
            elif self.vector[c1][0] < vec.vector[c2][0]:
                c1 += 1
            else:
                c2 += 1
        
        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
