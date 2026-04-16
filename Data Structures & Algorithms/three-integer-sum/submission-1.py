class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n-2:
            l, r = i+1, n-1
            while l<r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                    while l<r and nums[r+1] == nums[r]:
                        r-=1
                elif summ < 0:
                    l+=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                else:
                    r-=1
                    while l<r and nums[r+1] == nums[r]:
                        r-=1
            i += 1
            while i < n-2 and nums[i] == nums[i-1]:
                i+=1
        return res



        # -4 -1 -1 0 1 2 