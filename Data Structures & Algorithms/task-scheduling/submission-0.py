from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)
        max_freq = max(count.values())
        
        # Count how many tasks share the maximum frequency
        count_max = sum(1 for freq in count.values() if freq == max_freq)
        
        # Calculate minimum cycles based on the most frequent task layout
        min_intervals = (max_freq - 1) * (n + 1) + count_max
        
        # Return the maximum between total tasks and the formula result
        return max(len(tasks), min_intervals)