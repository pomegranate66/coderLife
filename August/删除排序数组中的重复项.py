from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1

if __name__ == '__main__':
    l = [1,1,2]
    s = Solution()
    print(s.removeDuplicates(nums=l))