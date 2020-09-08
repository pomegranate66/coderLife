class Solution:
    def maxArea(self, height) -> int:
        '''
            思路分析：
                本题是一道双向指针的题目
                可以找两端的数值大小，去进行容器的面积计算
                哪边数值更小，往里面收缩，在计算容器的面积数值，知道找到最大容积
        :param height:
        :return:
        '''
        # l, r = 0, len(height) - 1
        # ans = 0
        # while l < r:
        #     area = min(height[l], height[r]) * (r - l)
        #     ans = max(ans, area)
        #     if height[l] <= height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return ans
        # 先定义两端数值的下标为
        l, r = 0, len(height)-1
        # 输出的最大值
        max_vo = 0
        # 循环遍历  满足 l<r
        while l < r:
            # 此时的l和s 对应的最大容积值
            area = min(height[l], height[r]) * (r - l)
            # 和之前定义的最大容积对比 取最大值
            max_vo = max(area, max_vo)
            # 接下来 判断 左右两边指针到底哪个矮一些  矮的往里挪一下
            if height[l] < height[r]:
                l += 1
            else:
                r += 1
        return max_vo


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    result = s.maxArea(height=height)
    print(result)
