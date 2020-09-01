from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        inter = Counter(nums1) & Counter(nums2)
        while inter:
            value = inter.popitem()
            res.extend([value[0]]*value[1])
        
        return res
      
