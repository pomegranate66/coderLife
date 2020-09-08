# 题目: 返回数组中最小的数字
# 分析: 就是查找里面的最小数字呗 ， 用二分查找就可以得到

class Sulotion:
    def minArray(self,numbers:[int]) -> int:
        i , j  = 0,len(numbers)-1
        while i<j:
            mid = (i+j)//2
            if numbers[mid] > numbers[j] : j  = mid+1
            elif numbers[mid] < numbers[j] : j=mid
            else:
                j-=1
        return numbers[i]
