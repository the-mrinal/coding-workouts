class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for index,val in enumerate(nums):
            if val in hashMap:
                check = hashMap[val]
                for index1 in check:
                    if abs(index - index1) <= k:
                        return True
                hashMap[val].append(index)
            else:
                hashMap[val] = [index]
        return False