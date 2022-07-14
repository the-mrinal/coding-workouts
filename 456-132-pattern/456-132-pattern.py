class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        # here we want to compare - nums-i < nums-k < nums-j
        # keep track of max num till index i
        # ?? how to keep track of mins ?
        stack = []
        
        min_arr = [nums[0]]
        for i in range(1,n):
            min_arr.append(min(min_arr[i - 1],nums[i]))

        # [1,1,1,1]
        st = []
        for i in range(n - 1,0,-1):
            if nums[i] <= min_arr[i]:
                continue

            while st and st[-1] <= min_arr[i]:
                st.pop()
            if st and st[-1] < nums[i]:
                return True

            st.append(nums[i])

        return False
