from typing import List
class Solution():
    def printNumbers(self,n:int) -> List[int]:
        '''
        暴力法：
            遍历出每一个数字，直接添加到列表中，返回结果列表
        
        其实这道题是考大数越界的情况

    
        '''
        # 写法1.1
        # result = []
        # for i in range((10**n)-1):
        #     result.append(i)
        # return result
        # 写法1.2
        # return List(range(1,10**n))

