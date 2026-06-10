class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        n = len(nums)
        lo, hi = min(nums), max(nums)
        
        if lo == hi:
            return 0
        
        B = defaultdict(list)
        
        for i in nums:
            # Correct bucket index calculation
            ind = (i - lo) * (n - 1) // (hi - lo)
            B[ind].append(i)
        
        buckets = []
        for i in range(n):
            if B[i]:
                buckets.append((min(B[i]), max(B[i])))
        
        output = 0
        for i in range(1, len(buckets)):
            output = max(output, buckets[i][0] - buckets[i-1][1])
        
        return output