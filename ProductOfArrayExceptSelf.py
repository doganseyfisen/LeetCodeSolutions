"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length # an array answer's first element is 1, so len(nums) times 1 give us length of answer actually

        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]

        fromRight = 1 # since we want to add first result as answer[0], and second one as ans...[1] and so on...
        for i in range(length-1, -1, -1): # from last to first
            answer[i] *= fromRight
            fromRight *= nums[i]

        return answer
