from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 自己解法
        '''
        先比较每一行的最前面的那个，如果比输入数字小，那么这一行就不需要比较
        在比较每一行的最后一个数组，如果比输入数字小，那么这一行也就不需要比较了
        在挨个遍历比较？
        '''
        # for i in range(len(matrix)):
        #     partNum = matrix[i] # 获取分数组
        #     if partNum[0] > target:    # 如果分数组的第一个要大于目标数字
        #         pass
        #     elif partNum[len(partNum)-1] < target: # 如果分数组的最后一个到小于目标数字
        #         pass
        #     else:
        #         for j in range(len(partNum)):   # 在对于剩下的数组 遍历操作
        #             if partNum[j] == target:    # 如果数字找到了  那么返回True  不然返回false
        #                 return True
        # return False

        # 题解解法
        '''
        将二维数组旋转45°，形成图的样式，发现很像“二叉树”的数据结构，也就是对于每个元素，它的左分支一定要比右分支大，可以根据“根节点”开始搜索，遇到比
        target的打的就向左，比target小就向右。

        "根节点" 就是矩阵的左下角和右上角
        如果flag > target 那么就得到 target 一定在flag行的上方 
        若flag< target  那么 flag所在的这一列就可以排除了
        
        算法流程：
            从左下角元素开始遍历比较（i，j）
            和目标值进行对比：
            小于  i -- 
            大于 j++
            等于  返回True
        '''
        
        i,j  = len(matrix)-1,0   # 左下角的那个值
        while i>=0 and j < len(matrix[0]):
            if matrix[i][j] > target :i-=1
            elif matrix[i][j] < target: j+=1
            else:
                return True
        return False



if __name__ == "__main__":
    s = Solution()
    # l = [
    # [1,   4,  7, 11, 15],
    # [2,   5,  8, 12, 19],
    # [3,   6,  9, 16, 22],
    # [10, 13, 14, 17, 24],
    # [18, 21, 23, 26, 30]
    # ]
    l = [[-5]]
    target  = -5
    print(s.findNumberIn2DArray(matrix=l,target=target))