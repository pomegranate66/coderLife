class Solution:
    def canJump(self, nums) -> bool:
        # 判断 个例 如果是[0] 则默认返回True
        if nums == [0]: return True
        maxDist = 0
        end_index = len(nums) - 1  # 最终的索引
        for i, jump in enumerate(nums):
            if maxDist >= i and i + jump > maxDist:
                maxDist = i + jump
                if maxDist >= end_index:
                    return True
        return False


if __name__ == '__main__':
    s = Solution
    result = s().canJump(nums=[0])
    print(result)
