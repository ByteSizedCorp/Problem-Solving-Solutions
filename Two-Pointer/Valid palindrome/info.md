# Valid Palindrome

**Solved**

Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

## Example 1:

**Input:** `s = "Was it a car or a cat I saw?"`

**Output:** `true`

**Explanation:** After considering only alphanumerical characters we have `"wasitacaroracatisaw"`, which is a palindrome.

## Example 2:

**Input:** `s = "tab a cat"`

**Output:** `false`

**Explanation:** `"tabacat"` is not a palindrome.

## Constraints:

- `1 <= s.length <= 1000`
- `s` is made up of only printable ASCII characters.

## Approach

To determine if a given string `s` is a palindrome, we follow these steps:

1. **Filter and Normalize the String**:
   - Initialize an empty string `ns` to store the filtered characters.
   - Iterate through each character `i` in the input string `s`.
   - Check if the character `i` is alphanumeric using `i.isalnum()`.
   - If it is alphanumeric, convert it to lowercase using `i.lower()` and append it to `ns`.
   - This step ensures that we only consider alphanumeric characters and ignore case differences.

2. **Two-pointer Technique**:
   - Initialize two pointers, `i` at the start (0) and `j` at the end (len(ns) - 1) of the filtered string `ns`.
   - Use a while loop to compare characters from both ends towards the center:
     - If the characters at positions `i` and `j` are not equal, return `False` as the string is not a palindrome.
     - If they are equal, move the pointers closer to the center (`i` is incremented by 1 and `j` is decremented by 1).
   - Continue this process until the pointers meet or cross each other.

3. **Return Result**:
   - If all characters matched correctly, return `True` indicating that the string is a palindrome.

This approach ensures that we efficiently check for palindromes by considering only relevant characters and using a two-pointer technique to compare characters from both ends.
