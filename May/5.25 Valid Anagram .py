'''
    Valid Anagram
        字符串s的全部字符是否都在字符串t中

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            思路：
            分别对字符串进行处理，生成字符和出现次数的dict
            然后对这些dict进行对比

        '''
        # 思路1  但是新生成至少4个变量，然后时间复杂度为O(2n)
        # ls,lt = len(s),len(t)
        # if ls!=lt:
        #     return False
        # stas,stat = {},{}
        # for ch in s :
        #     stas[ch] = stas.get(ch,0)+1
        # for ch in t:
        #     stat[ch] = stat.get(ch,0)+1
        # if stas ==stat:
        #     return True
        # return False

        # 思路2 先判断长度，然后对其排序，排序后对比看是否一致
        # if len(s)!=len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # if s == t :
        #     return True
        # return False


if __name__ == '__main__':
    S = Solution()
    result = S.isAnagram("anagram","nagaram")
    print(result)