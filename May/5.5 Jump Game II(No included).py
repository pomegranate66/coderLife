'''
题目：
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Your goal is to reach the last index in the minimum number of jumps.

Example:
        Input: [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2.
            Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note：
    You can assume that you can always reach the last index.
'''
from typing import List


class Solution:
    def junp(self, nums: List[int]) -> int:
        '''
        思路：
            索引+当前位置的数字 >= 数组的长度
            最少跳数到最后

        :param nums:
        :return:
        '''
        # 数组的长度
        maxstep = 0
        end_index = len(nums)
        maxstep = n - 1
        # 遍历每个元素，获取他的索引值，然后和他的值，去和数组长度比较
        for i in range(n - 1):
            if i + nums[i] >= n:
                maxstep = nums[i] if nums[i] <= maxstep else maxstep  # 满足条件的最小跳数
        return maxstep


'''
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
        '''

if __name__ == '__main__':
    s = Solution()
    result = Solution().junp([2, 3, 1, 1, 4])
    print(result)
