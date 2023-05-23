class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(ListNode):
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

a = [1,2,4,6,7]
b = [1,3,5,6,7]
O = Solution()
print(O.mergeTwoLists(a, b))