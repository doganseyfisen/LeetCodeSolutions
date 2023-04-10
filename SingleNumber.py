"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result

      
"""
=====Another Solution====
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
      for i in nums:
          if (nums.count(i) == 1):
              return i
=========================
"""
