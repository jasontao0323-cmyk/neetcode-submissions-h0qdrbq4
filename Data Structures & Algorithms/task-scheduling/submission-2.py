# The minimum schedule time is determined by the task with the highest frequency, considering cooldown periods. If the total number of tasks exceeds this calculated time, the actual
# answer is the maximum of the task count and the calculated time.
# TC: O(m)
# SC: O(1)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)