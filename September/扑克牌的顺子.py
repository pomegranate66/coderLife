class Solution():
    def isStraight(self,nums:List[int]) -> bool:
        '''
        例子：
            输入: [1,2,3,4,5]
            输出: True

            输入: [0,0,1,2,5]
            输出: True
        
        思路:
            1、限制条件：
                除了大小王，所有牌“无重复”
                最大张牌为max,最小牌为min(大小王除外)
                    max- min < 5
                
            2、集合set+遍历
                遍历5张牌，遇到大小王跳过
                判别重复：利用set实现遍历判重，set的查找方法的时间复杂度为O(1)
                获取最大/最小的牌，借助辅助变量ma,mi 遍历统计得到

                复杂度分析：
                    时间复杂度O(N)  其中N为数组长度，遍历数组的时间需要O(N)
                    空间复杂度O(N)  判重的辅助set使用O(N)的额外空间
            
            3、排序+遍历
                先对数组排序。
                判断是否有重复，排序数组中的相同元素的位置相邻，因此可以遍历数组，判断num[i]=num[i+1]是否成立来判断是否重复
                获取最大/最小牌 ：排序后，数组末尾的nums[4]为最大牌。nums[0]为最小牌

                复杂度分析：
                    时间复杂度O(NlogN):其中N为数组长度
                    空间复杂度O(1):变量joker需要O(1)的额外空间


        '''
        # ma = 0  # 初始的最大值
        # mi = 14 # 初始最小值
        # repeat  =set()  # 构建集合数组
        # for num in nums:    # 遍历数组
        #     if num == 0 : continue  # 如果存在大小王，那么继续
        #     ma = max(ma,num)    # 获取当前最大的数
        #     mi = min(mi,num)    # 获取当前最小的数
        #     if num in repeat : return False # 若有重复，提前发挥false
        #     repeat.add(num) # 添加牌到set中
        # return ma-mi < 5  # 最大牌-最小牌 <5 就可以构成顺子

        joker = 0 
        nums.sort()
        for i in range(4):
            if num[i] == 0: joker +=1 
            elif nums[i] == nums[i+1]:return False
        return nums[4]-nums[joker] < 5