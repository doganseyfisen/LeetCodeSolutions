"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myStack = []
        for operation in operations:
            if operation == "C":
                myStack.pop() # pop out previous number
            elif operation == "+":
                myStack.append(myStack[-1] + myStack[-2]) # previous two numbers are summed
            elif operation == "D":
                myStack.append(2 * myStack[-1]) # previous number multiply by 2
            else:
                myStack.append(int(operation)) # add integer
        return sum(myStack)
