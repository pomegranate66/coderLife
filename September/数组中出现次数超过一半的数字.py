from typing import List
class Solution():
    def queryMultipleNum(self,nums:List[int]) -> int:
        '''
        输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
        输出: 2
        
        思路：
            1、哈希表法
            2、数组排序法
            3、摩尔投票法
                正负相抵消的思想，
                假设第一个n1为众数，遍历统计票数，当发生正负抵消的时候，剩余的数组的众数也不变
                    当n1 = x 抵消中的数字有一半时众数
                    当n1 ！= x 抵消中的数组，少于或者等于一半时众数
                利用这个特性，每轮都可以假设缩小当前的区间，当遍历完成时，最后一轮假设的数字就为众数。
        算法流程：
            初始化：x  votes 票数统计 

        '''
        votes= 0
        for i in nums:
            if votes == 0 : x = i
            votes +=1 if i==x else -1
        return x

            

if __name__ == "__main__":
    # s = Solution().queryMultipleNum(nums=[1, 2, 3, 2, 2, 2, 5, 4, 2])
    s = Solution().queryMultipleNum(nums=[3,2,3])
    print(s)