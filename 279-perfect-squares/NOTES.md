**Intuiton One - Brute Force - TLE
**
**Intuition 2 - DP iterative logic will be same as brute force**
- assume dp[0] = 0
- and build up on that given dp[i] = min({dp[i-k] + 1}) where k = [all sq < sqrt(n)]
- at last dp[n] return
ACCEPTED
​
**Intuition 3**
instead of building whole dp stack.
we just check by top. using isDivided logic
if the number n is divided by any sq_num within count times that couunt will our ans.
given that is minimum
​
Hence we will start with min counr and move up to n.
​
**Intuition 4**
BFS + Greedy
12 -> 12 -1  -> 11-1
-> 12 - 4->  .....so on
-> 12 - 9
BFS will make sure to get the shortest poossible route