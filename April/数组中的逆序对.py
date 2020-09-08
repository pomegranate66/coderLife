import bisect
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        题目：
            在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
        例子：
            输入: [7,5,6,4]
            输出: 5
        限制：
            0 <= 数组长度 <= 50000

        思路：
            count 计数
            按照索引生成字典
            遍历索引，然后与后面的进行比较，while
        :param nums:
        :return:
        '''
        # 自己写的  超出时间限制 哈哈哈哈
        # count = 0
        # array_dict = dict()
        # length = len(nums)
        # # 构造出字典
        # for i in range(length):
        #     array_dict.setdefault(i, nums[i])
        # # 在构建出一个值，初始化为0
        # k = 0
        # while (k < length):
        #     # 生成临时字典，遍历比较
        #     short = {key: value for key, value in array_dict.items() if key > k}
        #     for key in short:
        #         if array_dict[k] > short[key]:
        #             count += 1
        #     k += 1
        # return count

        #  大佬的做法
        q = []
        count = 0
        for v in nums:
            # bisect 是一个python的针对有序 数组的插入和排序操作的一个模块
            # bisect_left(a, x, lo=0, hi=None) 函数 查找该数值将会插入的位置并返回，而不会插入
            i = bisect.bisect_left(q, -v)
            # 源码
            # def bisect_left(a, x, lo=0, hi=None):
            #     # a 原列表
            #     # x 插入的元素
            #     # lo 起始位置 默认值为0
            #     # hi 结束位置 默认值为len(a)
            #
            #     # 如果起始位置小于0 则报错
            #     if lo < 0:
            #         raise ValueError('lo must be non-negative')
            #     # 如果没有 结束位置 则 默认为 列表的长度
            #     if hi is None:
            #         hi = len(a)
            #     # 二分法
            #     while lo < hi:
            #         mid = (lo + hi) // 2
            #         if a[mid] < x:
            #             lo = mid + 1
            #         else:
            #             hi = mid
            #     # 仅返回位置
            #     return lo
            count += i
            q[i:i] = [-v]
        return count


if __name__ == '__main__':
    s = Solution()
    result = s.reversePairs([7, 5, 6, 4])
    print(result)

