# 01_Big_O_Notation

## Overview

Big O notation helps us understand how an algorithm's running time or space requirements grow as the input size increases, which is crucial for selecting efficient algorithms.

## Files Structure

1. **constant_time.py (O(1))**  
   - Demonstrates algorithms that run in constant time, meaning the time it takes to complete doesn’t depend on the size of the input.

2. **linear_time.py (O(n))**  
   - Includes examples of algorithms where the time to complete is directly proportional to the size of the input.

3. **logarithmic_time.py (O(log n))**  
   - Shows algorithms with logarithmic time complexity, where the time grows logarithmically as the input size increases. Common in algorithms that repeatedly divide the input in half, such as binary search.

4. **quadratic_time.py (O(n^2))**  
   - Demonstrates algorithms with quadratic time complexity, where the time grows quadratically with the size of the input. Typically found in algorithms with nested loops.

5. **cubic_time.py (O(n^3))**  
   - Includes examples of algorithms with cubic time complexity, which is often seen in problems with three nested loops.

6. **Exponential Time (O(2^n))**  
   - Algorithms where the time grows exponentially with the input size, often seen in brute-force solutions to problems such as the traveling salesman problem.
   - **Example:** Recursive algorithms without pruning that explore all possible combinations.

7. **Factorial Time (O(n!))**  
   - Extremely slow algorithms where the time grows factorially with the input size. This is typical in problems that require generating all permutations.
   - **Example:** Permutation-based algorithms, such as solving the traveling salesman problem with brute force.

8. **Linearithmic Time (O(n log n))**  
   - Common in algorithms that combine linear and logarithmic growth, such as efficient sorting algorithms like mergesort and quicksort.
   - **Example:** Sorting algorithms that use a divide-and-conquer approach, such as quicksort or mergesort.

9. **Polylogarithmic Time (O((log n)^k))**  
   - Found in advanced algorithms, particularly in areas such as computational geometry or number theory, where the time grows polynomially with respect to the logarithm of the input size.
   - **Example:** Certain specialized algorithms in computational complexity.


## Why Big O Notation Matters

Big O notation allows us to:
- Compare algorithms objectively by their efficiency.
- Predict how an algorithm will perform as input sizes grow larger.
- Make informed decisions about which algorithms to use based on their time and space efficiency.

## Time Complexity Chart

![Big O Notation](./Time-Complexity-Chart.png)