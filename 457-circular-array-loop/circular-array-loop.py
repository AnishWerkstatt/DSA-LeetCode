class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nxt(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            direction = nums[i] > 0

            while True:
                next_slow = nxt(slow)

                if (nums[next_slow] > 0) != direction:
                    break

                next_fast = nxt(fast)
                if (nums[next_fast] > 0) != direction:
                    break

                next_fast = nxt(next_fast)
                if (nums[next_fast] > 0) != direction:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    if slow == nxt(slow):  # self-loop
                        break
                    return True

            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                nxt_j = nxt(j)
                nums[j] = 0
                j = nxt_j

        return False