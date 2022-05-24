basic logic :
Instead of finding whole block:
just find the starting index
and from there till si + k will be your ans
​
Condition of finding si:
- Compare arr[si] and arr[si+k]
*     since both are boundary elem ! any one of them can be in arr
*     pick one side basedd on this. whoever is closed to k
*     x - arr[mid] -> left bound
*     arr[mid +k] - x -> right bound