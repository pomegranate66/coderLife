class Solution:
    def waysToChange(self, n: int) -> int:
        '''
        完全背包问题
        题目：
            Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent),
            write code to calculate the number of ways of representing n cents. (The result may be large, so you should
            return it modulo 1000000007)

        例子：
             Input: n = 5
             Output: 2
             Explanation: There are two ways:
             5=5
             5=1+1+1+1+1

             Input: n = 10
             Output: 4
             Explanation: There are four ways:
             10=10
             10=5+5
             10=5+1+1+1+1+1
             10=1+1+1+1+1+1+1+1+1+1

        Notes :
            You can assume:
                0 <= n <= 1000000

        思路：
            主要问题在于怎么去实现“组合”？
        算法：
            动态规划   DP

        :param n:
        :return:
        '''
        coins = [1, 5, 10, 25] # 题目规定的硬币
        dp = []

        dp.append(1)
        for coin in coins:  #遍历硬币
            for i in range(coin, n + 1):  # 看 coin有多少转化为n的方法
                if coin == 1:
                    dp.append(1)
                else:
                    dp[i] = (dp[i] + dp[i - coin]) % 1000000007
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    result = s.waysToChange(10)
    print(result)
