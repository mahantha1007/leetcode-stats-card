class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        nums = list(range(1, n+1))
        k -= 1
        res = ""
        for i in range(n, 0, -1):
            idx, k = divmod(k, math.factorial(i-1))
            res += str(nums.pop(idx))
        return res
