# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # dummy node to simplify list handling
        curr = dummy
        carry = 0               # carry from addition
        
        # loop until both lists are done and no carry left
        while l1 or l2 or carry:
            x = l1.val if l1 else 0   # digit from l1
            y = l2.val if l2 else 0   # digit from l2
            total = x + y + carry
            
            carry = total // 10       # update carry
            curr.next = ListNode(total % 10)  # create new node with result digit
            curr = curr.next          # move to next
            
            # move l1 and l2 pointers forward if possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next