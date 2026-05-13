class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        resp = [0]*size
        p = [0]*size
        s = [0]*size
        p[0] = s[size-1]=1
        for n in range(1,size):
            p[n]=nums[n-1]*p[n-1]
        for n in range(size-2, -1, -1):
            s[n]=nums[n+1]*s[n+1]
        for n in range(size):
            resp[n]=p[n]*s[n]
        return resp