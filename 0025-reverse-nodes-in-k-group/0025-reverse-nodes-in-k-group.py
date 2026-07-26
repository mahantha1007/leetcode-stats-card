class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(start, end):
            prev, curr = end, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            return prev
        
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            start = group_prev.next
            group_prev.next = reverse(start, group_next)
            start.next = group_next
            group_prev = start
