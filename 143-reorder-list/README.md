# 143. Reorder List

## Medium

***

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

_Reorder the list to be on the following form:_

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

<pre><code>Input: head = [1,2,3,4]
<strong>Output:
</strong> [1,4,2,3]</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

<pre><code>Input: head = [1,2,3,4,5]
<strong>Output:
</strong> [1,5,2,4,3]</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the list is in the range `[1, 5 * 104]`.
* `1 <= Node.val <= 1000`
