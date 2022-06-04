class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_arr = []
        min_arr.append(nums[0])
        for i in range(1,len(nums)):
            min_arr.append(min(min_arr[i-1],nums[i]))
        
        st = []
        for i in range(len(nums)-1,0,-1):
                if nums[i] <= min_arr[i]:
                    continue
            
                while st and st[-1] <= min_arr[i]:
                    st.pop()
                
                if st and st[-1] < nums[i]:
                    return True # found 132
                
                st.append(nums[i])
        return False