from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def reversePrint(self, head: ListNode) -> List[int]:
        '''
        遍历链表存放在数组中，然后在对数组逆序  这叫做辅助栈法 
        '''
        # re = []
        # while head.next :
        #     re.append(head.val)
        #     head= head.next
        # return re[::-1]

        '''
        递归法 ：函数调用本身，并且做处理

        每次需要进行的处理是，将每次的head都存入到列表中，等到最后head没有值那么就是空列表

        '''
        return self.reversePrint(head.next) + [head.val] if head else []