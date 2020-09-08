class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        伪代码：
            要求不可以把int转化为str来操作
                想想那些可以直接排除的（负数和末尾为0的数）
                0 是可以的

        '''
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            reverse_x = 0
            while x > reverse_x:
                remainder = x % 10   # 取处罚的玉树
                reverse_x = reverse_x * 10 + remainder
                x = x // 10  # 取整数
            # 当x为奇数时, 只要满足 reverse_x//10 == x 即可
            if reverse_x == x or reverse_x // 10 == x:
                return True
            else:
                return False




if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(x=13)
    print(result)
