from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        array_length = len(nums)

        # Check all possible rotations
        for i in range(array_length):
            rotated_array = nums[i:] + nums[:i]
            if rotated_array == sorted_nums:
                return True

        return False