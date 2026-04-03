class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = {}
        for task in tasks:
            task_freq[task] = 1 + task_freq.get(task, 0)
        
        min_heap = []
        for task, freq in task_freq.items():
            min_heap.append([0, -freq, task])
        heapq.heapify(min_heap)

        cycles = 0
        while min_heap:
            print(min_heap)
            if min_heap[0][0] == 0:
                task_to_run = heapq.heappop(min_heap)
                task_to_run[1] += 1
                if task_to_run[1] < 0:
                    task_to_run[0] = n + 1
                    heapq.heappush(min_heap, task_to_run)

            for task in min_heap:
                if task[0] > 0:
                    task[0] -= 1

            heapq.heapify(min_heap)
            cycles += 1

        return cycles
                