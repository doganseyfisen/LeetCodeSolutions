"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        updated_list = list(dict.fromkeys(nums)) # remove duplicates from nums list

        if len(updated_list) > 2:
            return updated_list[-3]
        elif len(updated_list) < 3 or len(updated_list) == 1:
            return updated_list[-1]
        
