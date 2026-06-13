from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0

        for x1, y1 in points:
            dist_count = defaultdict(int)

            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                dist = dx * dx + dy * dy

                dist_count[dist] += 1

            for count in dist_count.values():
                res += count * (count - 1)

        return res