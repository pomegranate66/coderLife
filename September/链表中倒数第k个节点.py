class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution():
    def getkKthFromEnd(self,head:ListNode,k:int) -> ListNode:
        '''
        输出链表倒数第k个节点
        输入：
            1->2->3->4->5   k = 2
        输出：
            4->5

        分析：
            链表最先想是不是双指针可以用
            本题把持好两个指针的距离，当第一个指针遍历完列表，那么后指针当前的链表就是结果
        
        算法流程：
            1、初始化：默认两个指针都是指向head的
            2、前指针 先走 
            3、两个指针一起走
        '''
        front,latter = head,head
        for _ in range(k):
            front = front.next
        while front:
            latter,front = latter.next,front.next
        return latter