"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_divisors = 0
        i = 1
        
        while i * i <= num:
            if num % i == 0:
                sum_divisors += i
                if i * i != num:
                    sum_divisors += num // i
            i += 1
        
        return sum_divisors - num == num
