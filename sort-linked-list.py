"""
https://leetcode.com/problems/sort-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        nodes = {}
        while head: 
            if head.val in nodes.keys():
                nodes[head.val] += 1
            else: 
                nodes[head.val] = 1
            head = head.next
        keys = nodes.keys() 
        root = None
        tail = None
        while len(keys) > 0: 
            key = keys[-1]
            qty = nodes[key]
            # first item(s) in sorted list 
            if not root: 
                root = ListNode(val=key, next=root)
                tail = root
                for i in range(qty-1):
                    root = ListNode(val=key, next=root)
            # key is less than root, insert 
            elif key < root.val:
                for i in range(qty):
                    root = ListNode(val=key, next=root)
            # key is greater than tail, append
            elif key > tail.val:
                for i in range(qty):
                    tail.next = ListNode(val=key, next=None)
                    tail = tail.next
            # search where to insert it
            else: 
                insert = root
                while insert.next: 
                    if insert.next.val > key:
                        for i in range(qty):
                            insert.next = ListNode(val=key, next=insert.next)
                        break
                    else:
                        insert = insert.next
            keys.pop()
        return root
     
""" SECOND THOUGHT     
        node = head 
        sorted_head = head
        sorted_tail = head 
        
        nodes_dict = {}
        print(nodes_dict)
        while node: 
            print(nodes_dict)
            
            # insert node at head of sorted list
            if node.val <= sorted_head.val: 
                sorted_head = ListNode(val=node.val, next=sorted_head)
                nodes_dict= self.add_to_nodes_dict(nodes_dict, sorted_head)
            # append node to tail of sorted list 
            elif node.val >= sorted_tail.val: 
                sorted_tail.next = ListNode(val=node.val, next=None)
                sorted_tail = sorted_tail.next
                nodes_dict= self.add_to_nodes_dict(nodes_dict, sorted_tail)
            else:
                saved_eq_node, nodes_dict = self.check_nodes_dict(nodes_dict, node)
                # insert node at equivalent value 
                if saved_eq_node:
                    # IDK COME BACK  
                    saved_eq_node.next = ListNode(val=head.val, next=saved_eq_node.next)
                # search where to insert it and add to dict
                else: 
                    insertion_node = sorted_head
                    while insertion_node:
                        if insertion_node.next:
                            # if 6 -> 9  >  7
                            if insertion_node.next.val > node.val: 
                                # 6 ->  =  7 -> 9
                                insertion_node.next = ListNode(val=node.val, next=insertion_node.next)
                                nodes_dict = self.add_to_nodes_dict(nodes_dict, insertion_node.next)
                                break
                            else: 
                                insertion_node = insertion_node.next
                
            node = node.next
        
        return sorted_head
    
    def check_nodes_dict(self, nodes_dict, node):
        if node.val in nodes_dict: 
            return nodes_dict[node.val], nodes_dict
        else: 
            return None, nodes_dict

    def add_to_nodes_dict(self, nodes_dict, node):
        nodes_dict[node.val] = node
        return nodes_dict
"""


""" FIRST THOUGHT
        if not head or head.next == None:
            return head
        curr = head
        
        root = ListNode(val=head.val, next=None) 
        tail = root 
        
        curr = curr.next 
        
        while curr: 
            # in ascending order, append
            if tail.val <= curr.val:
                tail.next = ListNode(val=curr.val, next=None)
                tail = tail.next
            # re-assign root, insert to beginning
            elif root.val > curr.val:
                root = ListNode(val=curr.val, next=root)
                self
            # insert curr into sorted list
            elif tail.val > curr.val:
                temp = root
                while temp: 
                    if temp.next:
                        if temp.next.val >= curr.val:
                            temp.next = ListNode(val=curr.val, next=temp.next)
                            break
                            # do not need to reassign node 
                        else:
                            # try the next node in the sorted list
                            temp = temp.next
            curr = curr.next
        return root
"""
