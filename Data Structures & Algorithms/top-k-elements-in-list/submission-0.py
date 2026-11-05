class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # Step 2: Create frequency buckets (index represents frequency)
        # The maximum possible frequency of any element is len(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
            
        # Step 3: Collect the top k frequent elements from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res