from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        题目：
            Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
            Return the number of nice sub-arrays.
        思路分析：
            判断奇偶数的方法： if x%2 == 0
            遍历列表中数字，挨个数字进行判断是否为奇数， 若为奇数可以生成一个list中，当这个list的len==k 那么计数+1
        letcode上的思路：
            1、找到第i个奇数，然后去找i+k-1个奇数的位置，这样i~i+k-1就是一个“优美子数组”，在看两遍的活动范围有多大，就能判断出有多少个“优美子数组”
            2、左边界的活动范围在当前的i -- i-1个奇数   右边界为 i+k-1 ~ i+k个奇数
            3、左边范围 * 右边活动范围 在各个位置上的累加就是结果。

        :param nums:
        :param k:
        :return:
        '''
        # odd_positions = [0]  # 设定一个数组记录奇数的位置，0代表当前位置之前的一个奇数的位置(fake point)
        # for i in range(len(nums)):  # 遍历传入的nums 去寻找每个奇数的下标
        #     if nums[i] % 2 == 1:
        #         odd_positions.append(i + 1)  # 找到下标，保存到之前定义的odd_position中
        # odd_positions.append(len(nums) + 1)  # len(nums)+1代表最后一个奇数位之后的奇数位置(fake point)
        # count = 0
        # for i in range(1, len(odd_positions) - k):
        #     # 当前奇数位置 i 到前一个奇数位置之间选一个位置 * i 后的第 k-1 个奇数的位置到 i 后的第 k 个奇数节点范围内选一个
        #     count += ((odd_positions[i] - odd_positions[i - 1]) * (odd_positions[i + k] - odd_positions[i + k - 1]))
        # return count
        # 定义个list记录奇数的下标
        odd_positions = [0]  # 这里0代表的是当前位置之前的一个奇数的位置
        # 遍历整个数组，找寻奇数的下标
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                # 添加下标到下标list中
                odd_positions.append(i + 1)
        # 添加最后一个奇数之后的奇数位置
        odd_positions.append(len(nums) + 1)
        # 记录数
        count = 0
        # 计算出可组合的可能
        for i in range(1, len(odd_positions) - k):
            # 当前i位置的奇数，到前一个奇数位置之间选一个位置* i后的第i+k位置的奇数到前一个奇数选一个位置  的乘积 代表当i 时的可能性。
            # 叠加之后 就是所有可能性
            count += ((odd_positions[i] - odd_positions[i - 1]) * (odd_positions[i + k] - odd_positions[i + k - 1]))
        return count


if __name__ == '__main__':
    s = Solution()
    result = s.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2)
    print(result)
