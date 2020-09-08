class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        '''
        s : 输入的字符串
        n : 从第几位开始旋转

        例子：
            
            输入: s = "abcdefg", k = 2
            输出: "cdefgab"
            
            输入: s = "lrloseumgh", k = 6
            输出: "umghlrlose"

        分析：
            1、拆分成为两个字符串，然后再把这两个字符串做一个拼接
        算法流程：
            1、找到需要拆分的地方，用索引拆分
            2、将两个字符串倒序拼接，使用''.join()

        '''
        # 将str拆分开，然后合并成新的列表并转化字符串
        # part_1 = s[:n]
        # part_2 = s[n:]
        # result = []
        # for i in part_2:
        #     result.append(i)
        # for i in part_1:
        #     result.append(i)
        # return ''.join(result)

        # 将str拆分开，然后每部分各自转化成字符串，最后字符串拼接
        return str(s[n:])+str(s[:n])