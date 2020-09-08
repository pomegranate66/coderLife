from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        题目：
            Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom
        思路：
            广度优先搜索 BFS
                利用广度优先搜索，进行层次的遍历
                记录下每层最后一个元素
            复杂度分析
                时间复杂度  因为每个节点都入队和出对了一次  所以时间复杂度是On
                空间复杂度  通过额外的队列空间去进行存储每一层的节点  O(n)
            深度优先搜索 DFS
                按照 根节点>右节点> 左节点顺序进行访问
                可以保证每层都是最先访问最右边的节点
            复杂度分析
                时间复杂度 O(n)
                空间复杂度 O(n)

        深度优先搜索：顺序是每次先把某个分支都遍历完整，在去遍历另一分支
        广度优先搜索： 顺序是每次同阶段节点从左往右遍历，在去下一个阶段从左往右遍历

        :param root:
        :return:
        '''

        # BFS  顺序是: 根节点>左分支>右分支
        # rightmost_value_at_depth = dict()  # 以深度为索引存放节点的值
        # max_depth = -1  # 最大的深度为-1
        #
        # stack = [(root, 0)]  # 先是添加节点为root节点，深度为0
        # while stack:
        #     # pop()移除列表一个元素，默认为最后一个元素
        #     node, depth = stack.pop()  # 获取其stack列表中最后一个节点 和他的深度
        #     if node is not None:  # 如果节点存在
        #         # 维护二叉树的最大深度
        #         max_depth = max(max_depth, depth)  # 最大的深度 则就是起初定义的深度和获取到的深度之间的最大值
        #
        #         # 如果不存在对应深度的节点我们才插入
        #         # setdefault函数  如果该键不在字典中，那么就添加该键值，并将其值设为默认值
        #         rightmost_value_at_depth.setdefault(depth, node.val)  # 我们插入对应深度，下的最右边的节点的值
        #         stack.append((node.left, depth + 1))  # 添加之后的左节点和右节点  并且深度是+1的
        #         stack.append((node.right, depth + 1))
        #
        # # 返回全部深度下的节点的值的列表，通过匿名函数来返回
        # return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

        # DFS 遍历的顺序是根节点>右节点>左节点
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        # deque函数 生成了一个序列，这个序列两边都可以pop()  popleft() ()  这意味着在这个序列的前后都可以进行添加
        queue = deque([(root, 0)])  # 形成了一个序列
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]


if __name__ == '__main__':
    s = Solution()
    result = s.rightSideView()
