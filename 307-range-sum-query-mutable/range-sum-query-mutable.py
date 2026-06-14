class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.nums = nums[:]

        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, index, delta):
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def _sum(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right + 1) - self._sum(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index, val)
# param_2 = obj.sumRange(left, right)