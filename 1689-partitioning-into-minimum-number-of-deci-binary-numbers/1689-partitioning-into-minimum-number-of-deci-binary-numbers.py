class Solution:
    def minPartitions(self, n: str) -> int:
        max_num = -1
        for i in n:
            num = int(i)
            if num > max_num:
                max_num = num
        return max_num