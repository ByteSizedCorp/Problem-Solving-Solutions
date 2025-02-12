# Container With Most Water - Two Pointer

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice that you may not slant the container.**

## Examples

### Example 1

**Input:** `height = [1,8,6,2,5,4,8,3,7]`  
**Output:** `49`  
**Explanation:** The above vertical lines are represented by array `[1,8,6,2,5,4,8,3,7]`. In this case, the max area of water (blue section) the container can contain is `49`.

### Example 2

**Input:** `height = [1,1]`  
**Output:** `1`

## Approach
To solve this problem using the two-pointer technique, we can follow these steps:

1. Initialize two pointers, `left` at the beginning (index 0) and `right` at the end (index `n-1`) of the array.
2. Initialize a variable `maxw` to store the maximum water area found.
3. Use a while loop to iterate until the `left` pointer is less than the `right` pointer.
4. In each iteration, calculate the area of water that can be contained between the lines at the `left` and `right` pointers using the formula `min(height[left], height[right]) * (right - left)`.
5. Update `maxw` if the calculated area is greater than the current `maxw`.
6. Move the pointer pointing to the shorter line inward (i.e., increment `left` if `height[left]` is less than `height[right]`, otherwise decrement `right`). We do this as this might increase the height of the container as the longer line can give more height for container than the shorter one, 
7. Continue this process until the two pointers meet.
8. Return the maximum area stored in `maxw`.

This approach ensures that we explore all possible containers formed by the lines and find the one with the maximum water area.


## Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the array.
- **Space Complexity:** `O(1)`, as we are using only a constant amount of extra space.

## Solution

Here is a Python implementation of the above approach:

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxw = 0
        while(left < right):
            water = min(height[left], height[right])*(right-left)
            if(water>maxw):
                maxw = water
            if(height[left]<height[right]):
                left = left+1
            else:
                right = right - 1
        
        return maxw
```
