"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        stack = []

        length = len(strs[0])

        for i in range(length):
            char = strs[0][i]
            stack.append(char)

            for str in strs:
                if len(str) <= i or str[i] != char:
                    stack.pop()
                    break

            if len(stack) > i:
                common_prefix += char

        return common_prefix
