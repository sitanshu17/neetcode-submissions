class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index,val in enumerate(nums):
            if(val in my_dict):
                return [my_dict[val], index]  
            else:
                my_dict[target - val] = index
        
