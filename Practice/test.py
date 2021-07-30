from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peek = max(arr)
        pindex = arr.index(peek)
        for i in range(pindex):
            if arr[i+1] <= arr[i]:
                return False
        for i in range(pindex, len(arr)-1):
            if arr[i+1] >= arr[i]:
                return False
        return True
            

sol = Solution()
arr = [0,1,2,3,4,5,6,7,8,9]
print(sol.validMountainArray(arr))