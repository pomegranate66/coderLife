class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution():
    def reverseList(self,root:ListNode) -> ListNode:
        '''
        分析：
            可以使用双指针解答这个问题
        算法流程：
            1、初始化: 初始化两个指针，一个在前front，默认就是root，一个在后latter
            2、循环：终止条件是front等于Null
                1、每次需要构建一个辅助节点帮助存储值
                2、存储值附加给latter 
                3、front = front.next
        '''
        front,latter = root,None
        while front:
            temp = ListNode(front.val)
            temp.next = latter
            latter = temp
            front = front.next
        return latter
if __name__ == "__main__":
    pass