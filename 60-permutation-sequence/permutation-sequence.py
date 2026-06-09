from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # convert to 0-based indexing

        ans = []

        for i in range(n, 0, -1):
            fact = factorial(i - 1)

            idx = k // fact
            ans.append(nums.pop(idx))

            k %= fact

        return "".join(ans)