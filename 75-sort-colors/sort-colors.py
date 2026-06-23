class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0
        def num_swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        while i <= r:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                num_swap(l, i)
                i += 1
                l += 1
            else:
                num_swap(i, r)
                r -= 1


        
        