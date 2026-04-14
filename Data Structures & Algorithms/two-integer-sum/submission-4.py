from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hm = defaultdict(list)
        res = []

        for i in range(n):
            hm[nums[i]].append(i)
        
        for el in nums:
            compl = target-el
            if compl == el and len(hm[el]) == 2:
                res += hm[el][0], hm[el][1]
                break
            elif compl in hm and compl != el:
                res += hm[el][0], hm[compl][0]
                break
        return res
        
        