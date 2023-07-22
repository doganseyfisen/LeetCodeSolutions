"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def fib(self, n: int) -> int:
        '''
        for i in range(n):
            index_0 = index_1
            index_1 = index_n
            index_n = index_0 + index_1
        return index_n
        '''
        if n == 0: return 0
        elif n == 1: return 1
        else: return self.fib(n - 1) + self.fib(n - 2)
            
