class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        for i in range(1,len(nums)):
            output[i] = output[i-1] * nums[i-1]
        
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod *= nums[i]
            output[i-1] *= prod
            
        return output
    
    # 1 2 4 6
    #   1 2 8 