# Linked List 

## Introduction

A Linked List is a sequence of elements, called nodes, where each node has two components: data and a reference (or link) to the next node. Unlike arrays, Linked Lists do not require contiguous memory allocation, making them a more flexible structure for certain types of operations.

## Issues with Arrays that Linked List Solves

Arrays have some limitations that Linked Lists overcome:

- **Fixed Size**: Arrays have a fixed size, meaning you cannot easily add or remove elements without resizing the array.
- **Expensive Insertions/Deletions**: Inserting or deleting elements from the middle of an array can be inefficient, requiring elements to be shifted.
- **Contiguous Memory**: Arrays require contiguous blocks of memory, which may be problematic when the array grows too large and there isn't enough contiguous memory.

Linked Lists solve these issues by allowing dynamic memory allocation and more efficient insertions/deletions at any point in the list.

## Doubly Linked List

A **Doubly Linked List** is an extension of the Singly Linked List where each node contains two references:
- One to the **next** node.
- One to the **previous** node.

This allows traversal in both directions, making operations like deletion or searching from the tail of the list more efficient.

## Big O Analysis (Array vs Linked List)

Here’s a comparison of the time complexities for arrays and linked lists:

| Operation          | Array (Worst Case) | Linked List (Singly) | Linked List (Doubly) |
|--------------------|--------------------|----------------------|----------------------|
| Access             | O(1)               | O(n)                 | O(n)                 |
| Insertion (Begin)  | O(n)               | O(1)                 | O(1)                 |
| Insertion (End)    | O(1)               | O(n)                 | O(1)                 |
| Deletion (Begin)   | O(n)               | O(1)                 | O(1)                 |
| Deletion (End)     | O(1)               | O(n)                 | O(1)                 |

- **Array**: Accessing an element is efficient, but insertions and deletions are slow due to the need to shift elements.
- **Singly Linked List**: Insertion and deletion are efficient, but accessing elements requires traversal.
- **Doubly Linked List**: Similar to a singly linked list but with more efficient traversal in both directions.

