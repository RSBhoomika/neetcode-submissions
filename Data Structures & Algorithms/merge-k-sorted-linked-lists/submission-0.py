import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for i,head in enumerate(lists):
            if head:
                heapq.heappush(minheap,(head.val,i,head))
        
        dummy = ListNode(0)
        current = dummy
        while minheap:
            val,i,node = heapq.heappop(minheap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(minheap,(node.next.val,i,node.next))
        return dummy.next