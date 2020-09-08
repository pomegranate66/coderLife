class Solution:
    def replaceSpace(self, s: str) -> str:
        '''第一反应'''
        # return s.replace(' ','%20')
        # ''' 通过列表去生成字符串'''
        l = []
        for i in s :
            if i == ' ':
                l.append('%20')
            else:
                l.append(i)
        return ''.join(l)
if __name__ == "__main__":
    s = Solution()
    st = "We are happy."
    print(s.replaceSpace(s=st))