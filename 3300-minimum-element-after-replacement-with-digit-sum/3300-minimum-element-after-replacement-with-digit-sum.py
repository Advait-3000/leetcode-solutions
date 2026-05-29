class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=float('inf')
        for i in range(len(nums)):
            if len(str(nums[i]))>1:
                temp=0
                curr=nums[i]
                while curr:
                    temp+=curr%10
                    curr//=10
                if temp<mini:mini=temp
            elif nums[i]<mini:mini=nums[i]
        return mini