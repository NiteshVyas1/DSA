class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        new_list = []

        for num in nums:
            if num not in new_list:
                new_list.append(num)

        # Update nums in place
        for i in range(len(new_list)):
            nums[i] = new_list[i]

        return len(new_list)