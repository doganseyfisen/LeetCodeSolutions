"""
  @Author: Doğan Seyfi Şen
"""
class MyStack:
    
    def __init__(self):
        self.elements = deque()
    
    def push(self, x: int):
        self.elements.append(x)
    
    def pop(self):
        ## return self.elements.pop()
        for element in range(len(self.elements - 1)):
          self.elements.append(self.elements.popleft())
        return self.elements.popleft()
        
    def top(self):
        return self.elements[len(self.elements) - 1]
    
    def empty(self):
        return len(self.elements) == 0
