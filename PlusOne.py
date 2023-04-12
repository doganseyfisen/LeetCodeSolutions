"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lengthOf = len(digits)
        digitsTotalValue = 0
        lst = []
        for i in digits:
            powOf = 10 ** (lengthOf - 1)
            digitsTotalValue += (i * powOf)
            lengthOf -= 1
        digitsTotalValue += 1
        for j in str(digitsTotalValue):
            lst.append(int(j))
        return lst        
