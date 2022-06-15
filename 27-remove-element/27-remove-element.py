class Solution:
    def removeElement(self, arr: List[int], k: int) -> int:
        si = 0
        ei = len(arr) - 1
        n = len(arr)

        while si <= ei:
            if arr[si] == k:
                arr[si] = arr[ei]
                ei -= 1
            else:
                si += 1
        return si
