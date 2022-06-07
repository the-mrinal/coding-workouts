class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        size = m + n
        l1 = m - 1
        l2 = n - 1	

        for i in range(size - 1,-1,-1):
            if l1 >= 0 and l2 >= 0:
                if num1[l1] > num2[l2]:
                    num1[i] = num1[l1]
                    l1 -= 1
                else:
                    num1[i] = num2[l2]
                    l2 -= 1
            elif l1 < 0:
                num1[i] = num2[l2]
                l2 -= 1
