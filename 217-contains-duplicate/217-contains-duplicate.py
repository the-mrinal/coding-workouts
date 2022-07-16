class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = set()
        for n in nums:
            if n not in dictionary:
                dictionary.add(n)
            else:
                return True
        return False