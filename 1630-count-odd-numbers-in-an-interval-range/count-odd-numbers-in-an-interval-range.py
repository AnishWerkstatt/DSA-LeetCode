class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        So we know the total odd numbers from 1 to n = (n + 1)/2
        Using the same logic, total odd between low and high will be [odd(1 -> high) - odd(1 -> low-1)]
        Note: We use (low-1) because we want to include low.
        So, therefore ((low-1)+1)/2 = low/2

        """
        return (high + 1)//2 - low//2

        