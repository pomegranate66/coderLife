
class Solution:
    def reverse(self,x:int):
        x = list(str(x))[::-1]
        lenindex = len(x)-1
        if x[lenindex] == "-":
            x = x[:-1]
            int_x = int(''.join(x))*-1
        else:
            str_x = ''.join(x)
            int_x = int(str_x)
        if int_x >= 2**32 or int_x<=-(2**32):
            return 0
        else:
            return int_x

    def reverse_better(
            self,
            x: int) -> int:

        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res




if __name__ == '__main__':
    s = Solution()
    result = s.reverse(-123)
    print(result)