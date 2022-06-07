# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        si = 1
        ei = n
        while si <= ei:
            mid = si + (ei - si)//2
            curr = guess(mid)
            if curr == -1:
                ei = mid - 1
            elif curr == 1:
                si = mid + 1
            else:
                return mid
        return -1 