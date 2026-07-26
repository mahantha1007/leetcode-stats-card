class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            nxt = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = nxt
            prev, curr = curr, nxt
        return dummy.next
