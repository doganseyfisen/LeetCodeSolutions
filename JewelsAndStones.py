"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for char in jewels:
            total += stones.count(char)
    
        if total > 0:
            return total
        else:
            return 0
