class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()

        for val in nums:
            if (val not in my_set):
                my_set.add(val)
        
        temp_list = sorted(list(my_set))

        for idx, val in enumerate(temp_list):
            nums[idx] = temp_list[idx]

        return len(my_set)