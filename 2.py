# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def MYaddTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0 # 进位
        head = l1  # 返回
        while l1 and l2:
            op1, op2 = l1.val ,l2.val
            sum = op1 + op2 
            nextcarry , res = divmod(sum , 10)
            l1.val = res + carry
            carry = nextcarry
            l1, l2 = l1.next, l2.next
        if l1: # 
            while l1.val == 9: # 只有这时候才会继续进位
                nextcarry, l1.val =  divmod(carry + l1.val , 10)
                l1 = l1.next
        # 我写的需要处理非常复杂的边界，这里就不继续了

    # Right Answer
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode() # dummy
        carry = tempsum = 0

        while carry or l1 or l2: # 没加完，或者还有进位1
            tempsum = carry

            if l1: l1, tempsum = l1.next, l1.val + tempsum
            if l2: l2, tempsum = l2.next, l2.val + tempsum

            carry, tempsum = divmod(tempsum, 10)
            curr.next = curr = ListNode(tempsum)
        
        return head.next
        
