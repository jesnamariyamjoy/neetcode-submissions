class Solution(object):
    def longestConsecutive(self, nums):
        """:type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Check if it's the start of a sequence
            if (num - 1) not in num_set:
                length = 1
                # Count consecutive numbers
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
                
        return longest