"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = []
        str_x = str(x)
        negative_str = str_x.lstrip('-')

        if str_x[0] == '-':
            negative_str = '-' + negative_str

        for i in negative_str:
            l.append(i)

        if l == l[::-1]:
            return True

        else:
            return False
