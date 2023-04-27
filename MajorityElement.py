"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = 0
        counter = 0

        for num in nums:
            if counter == 0:
                major = num
            if num == major:
                counter += 1
            else:
                counter -= 1
                
        return major
