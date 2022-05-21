for w in weights:
total += w
if total > capacity:  #overload -> nxt day
total = weight
d += 1
if d > D: #days limitt reached
return false
return True
​
left = max(weigths)
right = sum(weights)
while left < right:
mid = left + (right - left)//2
if isfeasible(mid):
right = mid
else:
left = mid + 1
return left