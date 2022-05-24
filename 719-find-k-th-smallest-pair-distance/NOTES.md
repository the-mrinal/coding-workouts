- candidate for Bsearch
- search space will be [minPossibleSum,maxPossibleSum] ie, sortedArr
- nums[0] + nums[1] <- min PossibleSum
- nums[0] + nums[-1] <- max possible sum
- isFeasible Function
```
def isFeasible(mid):
# here we have to find if mid is kth smallest among all pairs
sliding window approach
for eevery right :
while right - left > mid:
increase left index
# now right - left <= mid
# ie, all the index position now will have values smaller than mid
# hence we add all up
count += right - left
# atlast check if count >= k, if true ie, ans is this half --
```
​