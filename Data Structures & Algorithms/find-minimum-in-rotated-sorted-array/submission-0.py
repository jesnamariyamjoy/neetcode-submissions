class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            # If the sub-array is already sorted, the leftmost element is the minimum
            if nums[left] < nums[right]:
                return nums[left]
                
            mid = left + (right - left) // 2
            
            # If mid element is greater than or equal to left, 
            # the minimum must be in the right half
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                # The minimum is in the left half, including mid
                right = mid
                
        return nums[left]   