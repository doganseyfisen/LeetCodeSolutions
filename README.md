# LeetCodeSolutions

## Author: Doğan Seyfi Şen

### 1. [Two Sum](https://leetcode.com/problems/two-sum/)
**Description**

[This Python code](https://github.com/doganseyfisen/LeetCodeSolutions/blob/main/TwoSum.py) defines a class Solution with a method twoSum, which takes a list of integers (nums) and an integer (target) as input. The method aims to find two distinct elements from the list whose sum equals the given target. Once the pair is found, it returns a list containing the indices of the two elements.

**Time and Space Complexity**

The time complexity of the TwoSum algorithm is O(n^2), where 'n' is the number of elements in the input list `nums`. This is because the algorithm uses nested loops to compare all possible pairs of elements in the list. The space complexity of the TwoSum algorithm is O(1). The space used by the algorithm does not depend on the size of the input list, but rather remains constant, as it only uses a single `tempList` to store the indices of the two elements that sum up to the target. Thus, the space complexity is constant, regardless of the input size.

### 69. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
**Description**

[This code](https://github.com/doganseyfisen/LeetCodeSolutions/blob/main/Sqrt(x).py) implements the `mySqrt` function in Python. The `mySqrt` function takes an integer `x` as input and returns the integer square root of `x`, which is the largest integer `r` such that `r*r <= x`. It uses the `math.floor` function to compute the square root, ensuring the result is an integer.

**Time and Space Complexity**

The time complexity of this function is O(1) because it performs a constant number of operations, regardless of the input value `x`. The exponentiation and floor operations take constant time, making the algorithm highly efficient. The space complexity of this function is also O(1). It only uses a fixed amount of memory to store the input `x`, and the local variables involved in the computation of the square root have a constant space requirement. Thus, the algorithm has a constant space overhead, irrespective of the input size.

*Others will be added soon...*
