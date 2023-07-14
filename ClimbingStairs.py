"""
  @Author: Doğan Seyfi Şen
"""
# Dynamic Program
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dynamic_ways = [0] * (n + 1)
        dynamic_ways[1] = 1
        dynamic_ways[2] = 2
        
        for i in range(3, n + 1):
            dynamic_ways[i] = dynamic_ways[i - 1] + dynamic_ways[i - 2]
        
        return dynamic_ways[n]
