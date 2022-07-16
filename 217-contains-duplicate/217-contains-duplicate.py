class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for n in nums:
            if n not in dictionary:
                dictionary[n] = True
            else:
                print(n,dictionary)
                return True
        return False