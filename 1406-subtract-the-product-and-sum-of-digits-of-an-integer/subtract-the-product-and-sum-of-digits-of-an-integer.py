class Solution:
    def subtractProductAndSum(self, n: int) -> int:
    
        sm = 0
        prod = 1
        while n > 0:
            r = n % 10
            prod *= r
            sm += r
            n //= 10
       
        return prod - sm

        