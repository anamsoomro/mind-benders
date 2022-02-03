"""
https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head, new_node=None):
        if head == None:
            return new_node
        else:
            new_node = ListNode(val=head.val, next=new_node)
            return self.reverseList(head.next, new_node)

    
#     def reverseList(self, head):
#         rev_node = None
#         while head:
#             if not rev_node: 
#                 rev_node = ListNode(val=head.val, next=None)
#             else: 
#                 rev_node = ListNode(val=head.val, next=rev_node)
#             head = head.next
#         return rev_node
        
        
        
#         # if head is empty or is single node
#         if head is None or head.next is None:
#             return head

#         first_elem = True
#         while head is not None: 
#             if first_elem: 
#                 new_node = ListNode(val = head.val, next=None)
#                 prev_node = new_node
#                 first_elem = False
#             else:
#                 new_node = ListNode(val = head.val, next = prev_node)
#                 prev_node = new_node
#             head = head.next
            
#         return new_node
    
    

#         # if head is empty
#         if head is None:
#             return head
#         nums = []
        
#         while head is not None: 
#             nums.insert(0, head.val)
#             head = head.next
        
#         # nums = [5,4,3,2,1]
#         for i in range(len(nums)):
            
#             if i == 0: # the first element
#                 root_node = ListNode(val=nums[i])
#                 head = root_node
            
#             head.val = nums[i]
            
#             if i == len(nums) - 1: # the last element
#                 head.next = None
#             else:
#                 head.next = ListNode()
            
#             head = head.next
            
#         return root_node

            
