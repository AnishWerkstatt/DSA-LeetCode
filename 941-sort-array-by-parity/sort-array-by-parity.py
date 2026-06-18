class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        od = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                od.append(i)

        even.extend(od)
        return even

        