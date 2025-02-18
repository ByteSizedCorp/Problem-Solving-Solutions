# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

### Example 1:
**Input:**  
```plaintext
nums = [2,7,11,15], target = 9
```
**Output:**  
```plaintext
[0,1]
```
**Explanation:**  
Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

### Example 2:
**Input:**  
```plaintext
nums = [3,2,4], target = 6
```
**Output:**  
```plaintext
[1,2]
```

---

### Example 3:
**Input:**  
```plaintext
nums = [3,3], target = 6
```
**Output:**  
```plaintext
[0,1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Solution Approach

Here is an efficient solution using a hash map to store the indices of visited elements:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dist = {}

        for i in range(len(nums)):
            t = target - nums[i]
            if t in dist:
                return [dist[t], i]
            dist[nums[i]] = i
        return
```
