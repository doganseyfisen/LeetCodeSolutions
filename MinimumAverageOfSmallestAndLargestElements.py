"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        
        while nums:
            smallest_num = min(nums)
            largest_num = max(nums)
            nums.remove(smallest_num)
            nums.remove(largest_num)
        
            average = (smallest_num + largest_num) / 2
            
            averages.append(average)
        
        smallest_average = min(averages)
        
        return smallest_average
        
