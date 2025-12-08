class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # Pointer for the position of the next non-zero element
        
        # Iterate through the list with pointer j
        for j in range(len(nums)):
            if nums[j] != 0:
                # Swap the elements if nums[j] is non-zero
                nums[i], nums[j] = nums[j], nums[i]
                i += 1  # Move i to the next position for the next non-zero element


        # [1, 0, 0, 3, 12]
