# NOTES

basic logic : Instead of finding whole block: just find the starting index and from there till si + k will be your ans ​ Condition of finding si:

* Compare arr\[si] and arr\[si+k]
* &#x20;   since both are boundary elem ! any one of them can be in arr
* &#x20;   pick one side basedd on this. whoever is closed to k
* &#x20;   x - arr\[mid] -> left bound
* &#x20;   arr\[mid +k] - x -> right bound
