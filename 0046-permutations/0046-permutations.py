class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        res.append(nums[:])
        def fact(n):
            if n==1:return 1
            return n*fact(n-1)
        k=fact(len(nums))
        while len(res)!=k:
            pivot=None
            for i in range(len(nums)-1,-1,-1):
                if nums[i-1] < nums[i]:
                    pivot=i-1
                    break
            swap=None
            for i in range(pivot,len(nums)):
                if nums[i]>nums[pivot]:swap=i
            temp=nums[pivot]
            nums[pivot]=nums[swap]
            nums[swap]=temp
            nums[pivot+1:] = sorted(nums[pivot+1:])
            res.append(nums[:])
        return res