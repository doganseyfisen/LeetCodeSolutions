"""
  @Author: Doğan Seyfi Şen 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempList = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x] + nums[y] == target and x != y):
                    tempList.append(x)
                    tempList.append(y)
                    return tempList
                else:
                    continue
