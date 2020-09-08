from typing import List
class Solution():
    def queryMultipleNum(self,nums:List[int]) -> int:
        '''
        输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
        输出: 2
        
        思路：
            1、首先计算数组长度
            2、然后对

        '''
        dic = {} # key-> 数字  value -> 出现的次数
        n = len(nums)//2    # 数组长度的一半
        s  = set()  # 数组生成无序集合
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                pass
        for i in s:
            dic[i] =0
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                pass
        for k,v in dic.items():
            if v>n:
                return k
            

if __name__ == "__main__":
    # s = Solution().queryMultipleNum(nums=[1, 2, 3, 2, 2, 2, 5, 4, 2])
    s = Solution().queryMultipleNum(nums=[3,2,3])
    print(s)