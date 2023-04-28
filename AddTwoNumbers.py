"""
  @Author: Doğan Seyfi Şen
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp = 0
        head = ListNode()
        current = head
        
        while l1 or l2 or temp:
            value_one = l1.val if l1 else 0
            value_two = l2.val if l2 else 0
            
            result = value_one + value_two + temp
            temp = result // 10
            digit = result % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
