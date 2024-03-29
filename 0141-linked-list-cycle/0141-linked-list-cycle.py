# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break 
        if not cycle:
            return False
        while head != slow:
            slow = slow.next
            head = head.next
        return  head
        output = set()
        temp = head
        while temp and temp.next:
            if temp in output:
                return True
            output.add(temp)
            temp = temp.next
        return False
                
        