"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum_basic_cases():
    # Standard LeetCode example
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    # Another basic case
    assert two_sum([3, 2, 4], 6) == [1, 2]
    # Target at the end
    assert two_sum([1, 5, 3, 7], 10) == [2, 3]

def test_two_sum_with_negatives():
    # Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    # Mixed positive and negative
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
    # Negative target
    assert two_sum([1, -1, 2, -2], -3) == [1, 3]

def test_two_sum_with_zeros():
    # Zeros in array
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
    # All zeros except one
    assert two_sum([0, 0, 0, 5], 5) == [2, 3]  # Wait, indices where sum to 5, but 0+5=5, but 5 is at 3, 0 at 0,1,2

def test_two_sum_duplicates():
    # Duplicate values
    assert two_sum([3, 3], 6) == [0, 1]
    # Multiple same values
    assert two_sum([1, 1, 1, 1], 2) == [0, 1]

def test_two_sum_minimum_length():
    # Minimum array length
    assert two_sum([1, 2], 3) == [0, 1]

def test_two_sum_edge_cases():
    # Large numbers
    assert two_sum([1000000, 2000000, -3000000], 3000000) == [0, 1]
    # Target is zero
    assert two_sum([1, -1], 0) == [0, 1]
    # Positive and negative summing to positive
    assert two_sum([-5, 10, 3], 5) == [0, 1]
    # Sum at different positions
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]  # 4+5=9

def test_two_sum_no_solution():
    # Although problem guarantees solution, test robustness
    # Empty array
    assert two_sum([], 5) == []
    # Single element
    assert two_sum([5], 5) == []
    # No pair sums to target
    assert two_sum([1, 2, 3], 10) == []

def test_two_sum_order():
    # Ensure indices are returned in ascending order
    result = two_sum([3, 2, 4], 6)
    assert result == [1, 2] and result[0] < result[1]