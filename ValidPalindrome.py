"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        string = self.remove_whitespaces(string)
        string = self.remove_non_alpha_num(string)
        reverse_string = string[::-1]

        if reverse_string == string: 
            return True
        else: 
            return False

    def remove_whitespaces(self, string: str) -> str:
        updated_str = string.strip()
        updated_str = updated_str.replace(' ', '')
        
        return updated_str

    def remove_non_alpha_num(self, string: str) -> str:
        non_alpha_num_str = ''
        for char in string:
            if char.isalpha() or char.isnumeric():
                non_alpha_num_str += char

        return non_alpha_num_str
