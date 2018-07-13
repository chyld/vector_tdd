class Vector:
    def __init__(self, nums):
        self.nums = nums
        self.dims = len(nums)
        self.norm = self._length()

    def _length(self):
        return sum([c**2 for c in self.nums]) ** 0.5
