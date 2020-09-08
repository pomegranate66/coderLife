
from typing import List
class Solution():
    def findContinuousSequence(self,target:int) -> List[List[int]]:
        '''
        例子：
            输入：target = 9
            输出：[[2,3,4],[4,5]]

            输入：target = 15
            输出：[[1,2,3,4,5],[4,5,6],[7,8]]

        思路：
            暴力法：
                1、生成原始数组nums 
                2、
            滑动窗口法
                首先什么是滑动窗口？
                    可以理解为数组中的框起来的一部分，这部分就叫做滑动窗口，通常滑动窗口都为左闭右开区间，而且这个窗口只能像右移动，这时时间复杂度为O(N) ,如果允许来回滑动，那就是回溯，时间复杂度就不止O(N)
                如何使用滑动窗口求解这道题？
                    1、怎么判断窗口什么时候变大，什么时候变小？
                    2、怎么确定它就包含了全部的解？

                    一、什么时候变大什么时候变小？
                        当整个窗口的和>target的时候，需要减小，那么i = i+1 ,整个窗口的左边界往右移动，右边界不变
                        当整个窗口的和<target的时候，需要增大，那么j = j+1 ,整个窗口的左边界不变，右边界向右移动
                        当整个窗口的和=target的时候，这时需要记录下当前窗口的值，这也代表了，找到了第一个符合条件的窗口，以及左边界，接下来就要用i+1依次往下推
                    二、怎么确定了包含了全部的解？
                        举个例子：
                            当目标的数为9 时 [1，2，3，4，5，6，7，8，9]
                算法步骤：
                    初始化: 滑动的窗口的左右边界[i,j)，返回的列表res 滑动窗口的和 sum
                    循环: 当左边界大于target的一半时，之后一定大于target
                        sum > target : 左边界向右移动
                        sum < target : 右边界向右移动
                        sum == target : 记录当前的滑动窗口，添加到返回的res中，并且左边界向右移动
                    返回： res
        '''
        left,right ,sum,res = 1,1,0,[]
        while left<=target//2:
            if sum<target:
                sum+=right
                right +=1
            elif sum>target:
                sum -=left
                left +=1
            else:
                s = list(range(left,right))
                res.append(s)
                sum -= left
                left +=1
        return res

if __name__ == "__main__":
    print(Solution().findContinuousSequence(target=15))
