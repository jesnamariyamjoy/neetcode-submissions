class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            # If the current number is positive, the rest of the array is positive too
            if n > 0:
                break
            
            # Skip duplicates for the first element
            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for the second element
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res