class Solution:
    def searchRange(self, nums: List[int], key: int) -> List[int]:
        n = len(nums)
        def find_starting():
            si = 0
            ei = n - 1

            while si <= ei:
                mid = si + (ei - si)//2

                if nums[mid] == key and (mid == 0  or nums[mid] != nums[mid - 1]):
                    return mid
                if nums[mid] >= key:
                    ei = mid - 1
                else:
                    si = mid + 1

            return -1

        def find_ending():
            si = 0
            ei = n - 1
            while si <= ei:
                mid = si + (ei - si)//2

                if nums[mid] == key and (mid == n - 1 or nums[mid] != nums[mid + 1]):
                    return mid
                if nums[mid] <= key:
                    si = mid + 1
                else:
                    ei = mid - 1
            return -1


        index1 = find_starting()
        index2 = find_ending()
        return [index1,index2]
