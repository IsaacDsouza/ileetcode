# 621. You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label. Return the minimum number of CPU intervals required to complete all tasks.

class Solution:
    def leastInterval(self, tasks:list[int], n:int) -> int:
        count = [0] * 26
        max_count = 0
        max_count_num = 0
        for task in tasks:
            count[ord(task) - ord('A')] += 1
            max_count = max(max_count, count[ord(task) - ord('A')])
        for i in range(26):
            if count[i] == max_count:
                max_count_num += 1
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_num)

solution = Solution()
print(solution.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(solution.leastInterval(tasks = ["A","A","A","B","B","B"], n = 3))
print(solution.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))