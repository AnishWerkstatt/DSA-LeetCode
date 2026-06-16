class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sm = 0
        prod = 1
        while temp > 0:
            r = temp % 10
            prod *= r
            sm += r
            temp //= 10
       
        return prod - sm

        