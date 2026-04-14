from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq_buck = [[] for i in range(len(nums)+1)]
        res = []

        # hashmap for freq counting
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        # insert in bucket
        for num, freq in hm.items():
            freq_buck[freq].append(num)

        for i in range(len(freq_buck) - 1, 0, -1):
            for num in freq_buck[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        