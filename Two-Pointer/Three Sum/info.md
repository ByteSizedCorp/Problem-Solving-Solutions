# Three Sum Problem

## Problem Statement

Given an array of integers `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

### Example 1

**Input:**
```
nums = [-1, 0, 1, 2, -1, -4]
```

**Output:**
```
[[-1, -1, 2], [-1, 0, 1]]
```

### Example 2

**Input:**
```
nums = []
```

**Output:**
```
[]
```

### Example 3

**Input:**
```
nums = [0]
```

**Output:**
```
[]
```

## Constraints

- `0 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Notes

- The solution set must not contain duplicate triplets.
- The order of the output does not matter.
- Consider using sorting and two-pointer technique to optimize the solution.

## Approach

The solution uses sorting and the two-pointer technique to find all unique triplets that sum up to zero. Here is a step-by-step explanation of the approach:

1. **Sorting**: First, the input array `nums` is sorted. This helps in efficiently finding the triplets and avoiding duplicates.

2. **Iterating through the array**: We iterate through the sorted array using an index `index`. For each element `number` at position `index`, we use two pointers `i` and `j` to find the other two elements of the triplet:
   - `i` starts from `index + 1`
   - `j` starts from the end of the array

3. **Skipping duplicates**: If the current element `number` is the same as the previous element, we skip it to avoid duplicate triplets.

4. **Two-pointer technique**: We use the two pointers `i` and `j` to find pairs that, together with `number`, sum up to zero:
   - If the sum of `number`, `nums[i]`, and `nums[j]` is greater than zero, we decrement `j` to reduce the sum.
   - If the sum is less than zero, we increment `i` to increase the sum.
   - If the sum is zero, we have found a valid triplet, which we add to the result list. We then increment `i` and skip any duplicate elements to avoid duplicate triplets.

5. **Returning the result**: Finally, we return the list of all unique triplets.

Here is the code implementing this approach:

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    result = []
    for index, number in enumerate(nums):
        if index > 0 and number == nums[index - 1]:
            continue
        
        i, j = index + 1, len(nums) - 1
        while i < j:
            if number + nums[i] + nums[j] > 0:
                j -= 1
            elif number + nums[i] + nums[j] < 0:
                i += 1
            else:
                result.append([number, nums[i], nums[j]])
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
    
    return result
```