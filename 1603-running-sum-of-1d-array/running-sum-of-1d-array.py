class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm = []
        sm.append(nums[0])
        n = len(nums)
        for i in range(1, n):
            x = nums[i] + sm[i - 1]
            sm.append(x)
        
        return sm


    



        