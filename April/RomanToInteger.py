class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        思路剖析  把目标的字符串和数值写成字典，然后通过分解字符串来定位数据再相加
        :param s:
        :return:
        '''
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))


