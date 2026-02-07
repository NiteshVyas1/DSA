from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for i in range(len(nums)):
            # remove indices out of window
            if dq and dq[0] <= i-k:
                dq.popleft()

            # remove smaller elements from queue , check previous one
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # add current index to queue
            dq.append(i)

            # append queue ka first element(max) to result when window form  
            if i >= k - 1: # coz window shifts to right by 1
                result.append(nums[dq[0]])
        return result