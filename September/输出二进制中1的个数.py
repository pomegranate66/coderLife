class Solution():
    def outBinaryCount(self,n:int) -> int:
        '''
        思路1：首先把输入的十进制，转化为二进制，将这个二进制转化为字符串，遍历字符串获取1的个数   ok 
        '''
        # str_binary_n = bin(n)
        # count = 0
        # for s in str_binary_n:
        #     if s  == '1':
        #         count +=1
        #     else:
        #         pass
        # return count
        '''
        思路2：
            
        '''

if __name__ == "__main__":
    s = Solution()
    result =s.outBinaryCount(n=9)