from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices of elements
        l = r = 0

        while r < len(nums):
            # Remove smaller elements from the right of the deque 
            # because they will never be the maximum while nums[r] is around
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove the index from the left if it's out of the current window bounds
            if l > q[0]:
                q.popleft()

            # Once the window reaches size k, record the max and slide the left pointer
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1

        return output