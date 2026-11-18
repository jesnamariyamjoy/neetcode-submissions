class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # Add a copy of the current subset to results
            res.append(list(path))
            
            # Iterate through remaining elements to form larger subsets
            for i in range(start, len(nums)):
                path.append(nums[i])       # Include the element
                backtrack(i + 1, path)     # Move to the next index
                path.pop()                 # Exclude the element (backtrack)
                
        backtrack(0, [])
        return res