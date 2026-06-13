class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        total = 0

        for i in nums:
            total += i - mn
        return total

    

        