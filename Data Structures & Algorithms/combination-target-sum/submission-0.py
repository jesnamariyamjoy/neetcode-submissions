class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path, current_sum):
            if current_sum == target:
                res.append(list(path))
                return
            if current_sum > target:
                return
                
            for i in range(start, len(nums)):
                path.append(nums[i])
                # Pass `i` instead of `i + 1` to allow reusing the same element
                backtrack(i, path, current_sum + nums[i])
                path.pop()  # Backtrack
                
        backtrack(0, [], 0)
        return res