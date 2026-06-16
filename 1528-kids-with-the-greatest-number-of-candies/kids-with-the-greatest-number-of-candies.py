class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = 0
        answer = []
        for i in candies:
            if i > mx:
                mx = i
        for i in candies:
            if i + extraCandies >= mx:
                answer.append(True)
            else:
                answer.append(False)
        return answer
                

        