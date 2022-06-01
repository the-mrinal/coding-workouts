# 	def merge(l1,l2):
# 		a = len(l1)
# 		b = len(l2)
# 		a1 = 0
# 		b1 = 0
# 		res = []
# 		while a1 < a and b1 < b:
# 			if l1[a1] < l2[b1]:
# 				res.append(l1[a1])
# 				a1 += 1
# else	
# 				res.append(l2[b2])
# 				b1 += 1
# 		if a1 < a :
# 			res = res +  l1[a1:]
# 		elid b1 < b
# 			res = res + l1[b1:]
# return res
		
		

# 	def helper(l):
# 		if len(l) == 1:
# 			return l
		
# 		mid = len(l) // 2
# 		left = helper(l[0:mid])
# 		right = helper(l[mid+1:])
		
# 		return merge(left,right)

			

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        
        def merge(left_list, right_list):
            left_cursor = right_cursor = 0
            ret = []
            while left_cursor < len(left_list) and right_cursor < len(right_list):
                if left_list[left_cursor] < right_list[right_cursor]:
                    ret.append(left_list[left_cursor])
                    left_cursor += 1
                else:
                    ret.append(right_list[right_cursor])
                    right_cursor += 1

            # append what is remained in either of the lists
            ret.extend(left_list[left_cursor:])
            ret.extend(right_list[right_cursor:])

            return ret

        
        def helper(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = helper(arr[0:mid])
            right = helper(arr[mid:])

            return merge(left,right)
        
        return helper(nums)

        
        
        