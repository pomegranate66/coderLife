from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        '''
        使用无序集合去获取重复的数
        '''
        dic = set()
        for num in nums:
            if num in dic:
                return num
            dic.add(num)
        return -1


