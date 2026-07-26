# Definition for singly-linked list.
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before, after = ListNode(0), ListNode(0)
        b, a = before, after
        while head:
            if head.val < x:
                b.next = head
                b = b.next
            else:
                a.next = head
                a = a.next
            head = head.next
        a.next = None
        b.next = after.next
        return before.next
