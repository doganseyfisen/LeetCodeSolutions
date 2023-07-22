"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def checkString(self, s: str) -> bool:
        there_is_b_before_a = False

        for char in s:
            if char == 'b':
                there_is_b_before_a = True
            elif char == 'a' and there_is_b_before_a: 
                # Only T and T gives T, so
                # When elif's condition is True, next line is going to return False
                return False

        return True
