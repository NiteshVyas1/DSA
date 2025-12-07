class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k > n

            # Reverse the whole array
        nums.reverse()
                # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
             # Reverse the remaining n - k elements
        nums[k:] = reversed(nums[k:])

