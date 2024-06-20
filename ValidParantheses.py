class Solution:
    def isValid(self, s: str) -> bool:
        # Keys are opening, values are closing brackets
        par_dict = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = [] # LIFO
        
        for char in s:
            if char in par_dict.keys(): 
                stack.append(char)
            elif char in par_dict.values():  
                if len(stack) > 0:
                    top_element = stack.pop()
                    if par_dict[top_element] != char: # Key: Value
                        return False
                else: # len(stack) == 0 it means that first element of s is one of the closing brackets
                    return False
        
        return len(stack) == 0
