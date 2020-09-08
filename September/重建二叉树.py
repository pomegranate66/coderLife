from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        例子：
            前序遍历 preorder = [3,9,20,15,7]
            中序遍历 inorder = [9,3,15,20,7]
        返回：
                 3
                / \
                9  20
                    /  \
                    15  7

        分析：
            前序遍历（跟左右）
            中序遍历（左跟右）
            并且每个数的节点值都是唯一的
            
            根据上述的特点：
                1、前序遍历的首个元素就是root的值
                2、在中序遍历中，列表可以分为[左节点|根节点|右节点]
                3、根据中序遍历的左右子数的数量，将前序遍历分为[根节点|左节点|右节点]
            
            这样可以确定三个节点的关系：
                1、根节点
                2、左子树根节点
                3、右子树跟节点
                （分别是前序遍历中左右子数的首个元素的值）
            
            同时子树也是符合上述特点的
            那么，咱们可以一次划分，确定三个节点的关系 - 》 采用递归方法处理
        

        算法流程：
            1、递归参数：  前序遍历中根节点的索引proRoot 中序遍历左边界inLeft 中序遍历右边界inRight
            2、终止条件：  当左边界超过右边界的时候，子数中序遍历为空，说明已经越过子节点，返回null
            3、递推工作：
                1、建立根节点root : 值为前序遍历中索引为pre_root的值
                2、搜索根节点root在中序遍历的索引i : 为了提升搜索效率，使用哈希表，预存中序遍历的值和索引映射的关系，每次搜索的时间复杂度都是O(1)
                3、构建根节点root的左子树和右子树：
                    通过return来开启下一层的递归
                    1、左子树：根节点的索引为：proRoot+1 , 中序遍历的左右边界分别是inLeft，i-1
                    2、右子树：根节点的索引为：左子树的长度加上当前位置在+1  proRoot-inLeft +i+1  中序的的左右边界分别为 i+1 ,inright
            4、返回值：
                返回root 含义是当前递归层级建立的根节点 root 为上一递归层级的根节点的左或右子节点。
        '''

        self.dic ,self.pro = {},preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.treeBuild(0,0,len(inorder)-1)
    def treeBuild(self,proRoot,inLeft,inRight):
        '''
        proRoot:   前序遍历中索引的值
        inLeft:     中序遍历中左子树的边界
        inRight:    中序遍历中右子树的边界
        '''
        if inLeft>inRight : return
        root = TreeNode(self.pro[proRoot])
        index = self.dic[self.pro[proRoot]]
        root.left = self.treeBuild(proRoot+1,inLeft,index-1)
        root.right = self.treeBuild(proRoot-inLeft+index+1,proRoot+1,inRight)
        return root
    #     self.dic , self.po = {},preorder
    #     for i in range(len(inorder)):
    #         self.dic[inorder[i]] = i
    #     return self.treeSort(0,0,len(inorder)-1)
    
    # def treeSort(self,perRoot,inLeft,inRight):
    #     if inLeft>inRight:return 
    #     # 创建节点
    #     root = TreeNode(self.po[perRoot])
    #     index = self.dic[self.po[perRoot]]  # 找到当前跟节点在中序中的索引
    #     root.left = self.treeSort(perRoot+1,inLeft,index-1)
    #     root.right = self.treeSort(perRoot-inLeft+index+1,index+1,inRight)
    #     return root







    

