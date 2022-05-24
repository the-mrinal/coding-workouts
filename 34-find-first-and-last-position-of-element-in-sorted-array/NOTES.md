Here the Question - Search Space is Sorted .
We need to find one number - and return the position
Only twist is number is repeated and we need to return range
​
This is a Bsearch
​
we can divide the problem  into 2 parts:
​
1. Find the starting Point
2. Find the ending point
​
Starting point find:
-----------
1. If num[mid]  <=  target:
if num[mid] == target
* if mid != 0 and num[mid] == num[mid - 1]  -> not left most num -> go left part
* else : go to right
else:
go to right
2. else: go to left
​
Post processing:
if left - 1 == target :
then go find right point
else:
nothing founfd return [-1,-1]
​
Ending Point Find:
-----------
1. If num[mid]  <=  target:
if num[mid] == target
* if mid != len(nums) - 1  and num[mid] == num[mid + 1]  -> not right most num -> go right part
* else : go to left
else:
go to right
2. else: go to left
​
left