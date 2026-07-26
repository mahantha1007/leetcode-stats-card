class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        nums.sort()
        start = 0
        for i, num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                new_subsets = [curr+[num] for curr in res[start:]]
            else:
                new_subsets = [curr+[num] for curr in res]
            start = len(res)
            res += new_subsets
        return res
