from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        arr3_temp = []
        cnt = 0
        i = 0
        for n in arr2:
            cnt = arr1.count(n)
            i = cnt
            for i in range(cnt):
                arr3.append(n)
        # print(arr3)

        for n in arr1:
            if n not in arr2:
                arr3_temp.append(n)
        # print(arr3_temp)
        # print(sorted(arr3_temp))
        res = arr3 + sorted(arr3_temp)
        # print(res)
        return res


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

num = Solution.relativeSortArray(0, arr1, arr2)
print(num)





# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         arr3 = []
#         cnt = 0
#         i = 0
#         for n in arr2:
#             cnt = arr1.count(n)
#             i = cnt
#             for i in range(cnt):
#                 arr3.append(n)
#
#         set_arr3 = set(arr1)-set(arr2)
#         arr3.extend(sorted(set_arr3))
#
#
# arr1 = [2,3,1,3,2,4,6,7,9,2,19]
# arr2 = [2,1,4,3,9,6]
#
# num = Solution.relativeSortArray(0, arr1, arr2)
# print(num)
