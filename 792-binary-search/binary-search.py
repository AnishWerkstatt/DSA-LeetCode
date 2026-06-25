class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for indx, n in enumerate(nums):
            if target == n:
                return indx
                break
            
        else:
            return -1
            
        