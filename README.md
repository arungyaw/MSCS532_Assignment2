# Assignment 2: Divide-and-Conquer Algorithms

This project implements and compares two divide-and-conquer sorting algorithms: Merge Sort and Quick Sort.

## Files

- `comparisonOfAlgorithm.py` - Python implementation of Merge Sort and Quick Sort
- `results.csv` - Performance results from running the algorithms
- `execution_time_graph.png` - Graph comparing execution time
- `graphResults.py` - Python program to print Graph
- `README.md` - Project overview

## Algorithms

### Merge Sort
Merge Sort divides the list into two halves, recursively sorts each half, and then merges the sorted halves.

### Quick Sort
Quick Sort chooses a pivot, separates smaller and larger values, and recursively sorts each side. In this implementation, the last element is used as the pivot.

## Datasets Tested

The algorithms were tested on:

- Sorted data
- Reverse sorted data
- Random data

Input sizes used:

- 1000
- 3000
- 5000

## How to Run

Run the Python file using:

```bash
python comparisonOfAlgorithm.py