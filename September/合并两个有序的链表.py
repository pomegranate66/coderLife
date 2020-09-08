class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution():
    def mergeTwoListNode(self,l1:ListNode,l2:ListNode) -> ListNode:
        '''
        分析过程：
            使用双指针遍历链表，然后根据每个val的大小关系确定节点的添加顺序，两个节点指针交替进行，直到遍历完成

            需要构建一个新的节点，不然之后的节点无法在之后进行添加

        算法步骤：
            1、初始化： 初始化伪节点dum，并且让后指针latter指向dum
            2、循环合并：当l1或者l2为空的时候跳出：
                1、当l1.val<l2.val的时候，latter.next = l1 ,l1并且向前走一部
                2、当l1.val>=l2.val的时候，latter.next = l2 ,并且l2向前走一步
                3、节点latter = latter.next latter的节点也要向前走一步
            3、合并剩余的尾部：跳出循环条件  - l1/l2为空
                1、若l1 != null ：将l1添加到latter之后
                2、否则：将l2添加到latter后面
            4、返回值：
                合并链表在伪接待dum之后，因此返回dum.next就欧克了
        '''
        dum = latter  = ListNode(0)
        while l1 and l2 :
            if l1.val < l2.val :
                latter.next,l1 = l1,l1.next 
            else:
                latter.next,l2 = l2,l2.next
            latter = latter.next
        latter.next = l1 if l1 else l2
        return dum.next
        
