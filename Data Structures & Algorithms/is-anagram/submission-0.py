class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for val in s:
            if(val not in my_dict):
                my_dict[val] = 1
            else:
                my_dict[val] = my_dict[val] + 1
        # print(my_dict)
        
        for val in t:
            if(val not in my_dict):
                return False
            else:
                my_dict[val] = my_dict[val] - 1

        # print(my_dict)
        for val in my_dict.values():
            if(val != 0):
                return False
        return True