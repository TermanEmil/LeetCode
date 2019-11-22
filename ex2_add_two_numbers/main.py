# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_nb(head: ListNode):
    if not head.next:
        return head.val
    
    return head.val + 10 * list_to_nb(head.next)

def nb_to_list(nb: int):
    node = ListNode(nb % 10)
    
    if nb > 9:
        next_node = nb_to_list(nb // 10)
        node.next = next_node
    return node
    

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        the_sum = list_to_nb(l1) + list_to_nb(l2)
        return nb_to_list(the_sum)
