# Arrays

## Introduction
An array is a data structure that stores elements in a contiguous block of memory. Elements in an array are accessed using an index, with the first element usually having an index of 0.

### Key Properties:
- **Fixed Size**: Once an array's size is defined, it cannot be changed (for static arrays).
- **Random Access**: Arrays allow direct access to any element using its index, making operations like searching and updating efficient.
- **Homogeneous**: All elements in an array must be of the same type.

# Big O Analysis of Common Array Operations

| Operation            | Time Complexity |
|----------------------|-----------------|
| Access (arr[i])      | O(1)            |
| Search (linear)      | O(n)            |
| Insertion (end)      | O(1)            |
| Insertion (middle)   | O(n)            |
| Deletion (end)       | O(1)            |
| Deletion (middle)    | O(n)            |

# Static vs Dynamic Array

## Static Array:
A static array has a fixed size determined at compile time. Once an array is created, its size cannot be changed. Static arrays are faster for small fixed datasets but are limited by their size.

## Dynamic Array:
A dynamic array allows resizing at runtime. When the array is full, it automatically resizes by allocating a larger block of memory and copying the existing elements into it. This resizing process ensures that a dynamic array can grow as needed.

**Example:** Python lists are dynamic arrays.
