class Solution(object):
    def productExceptSelf(self, nums):
        """:type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        
        # 1. Compute prefix products and store in res
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # 2. Compute suffix products on the fly and multiply with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res