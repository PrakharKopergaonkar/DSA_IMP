# Merge Sort implementation on Linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortlist(head):
            if(head==None or head.next==None):
                return head
            slow = head
            fast = head
            temp = head
        
            while(fast!=None and fast.next!=None):
                temp = slow
                slow = slow.next
                fast = fast.next.next
        
            temp.next = None
            left = sortlist(head)
            right = sortlist(slow)
        
            return merge(left,right)
        def merge(l1,l2):
            a = ListNode()
            dummy = a
            while(l1!=None or l2!=None):
                if(l1!=None and l2!=None):
                    if(l1.val < l2.val):
                        dummy.next = l1
                        dummy = dummy.next
                        l1 = l1.next
                    else:
                        dummy.next = l2
                        dummy = dummy.next
                        l2 = l2.next
                elif(l1!=None):
                    dummy.next = l1
                    dummy = dummy.next
                    l1 = l1.next
                elif(l2!=None):
                    dummy.next = l2
                    dummy = dummy.next
                    l2 = l2.next
            
            return a.next
       
        
        return sortlist(head)