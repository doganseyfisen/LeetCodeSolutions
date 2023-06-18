"""
  @Author: Doğan Seyfi Şen
"""
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if round(math.log(n, 3), 9).is_integer(): # By specifying a precision of 9, you can obtain the rounded value 5.0, which is a closer representation of the mathematical value. For example, log(243, 3) = 4.999...
            return True
        else: 
            return False
