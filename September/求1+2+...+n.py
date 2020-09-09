class Solution():
    def __init__(self):
        self.res = 0
    def sumNums(self,n:int)-> int:
        '''
        例子：
            输入: n = 3
            输出: 6

            输入: n = 9
            输出: 45
        
        注：不能使用乘除法、for、while、if、else、switch、case等关键字以及条件判断语句（A?B:C）

        思路：
            求和的方法： 平均计算、迭代、递归
            平均计算：
                （1+n）*n /2 用到除法不可用
            迭代：
                res = 0
                for i in range(n):
                    res+=1
                用到循环 for /while  不可用
            递归：
                终止条件需要if判断
                if (n==1) return 1
                n+=sumNums(n-1)

                思考一下是否可以用其他的办法去终止递归呢？
                    逻辑运算的的短路？
                        if (A &&B ) 若A为false ，则不会执行判断B 
                        if (A ||B ) 若A为true ,则不会执行判断B 

                        n > 1 && sumNums(n-1)
                            若n>1成立，则开启下层的递归
                            若n>1不成立，也终止下层的递归
                复杂度分析：
                    时间复杂度O(N): 计算和需要开启n个递归函数
                    空间复杂度O(N)：递归深度达到n，系统利用O(n)大小的额外空间
        '''
        n>1 and self.sumNums(n-1)
        self.res += n
        return self.res