"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum_standard_cases():
    # Standard LeetCode example
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    # Another example with positive sum
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
    # All positive numbers
    assert max_subarray_sum([1, 2, 3, 4]) == 10
    # Alternating positive and negative
    assert max_subarray_sum([1, -2, 3, -4, 5]) == 5

def test_max_subarray_sum_single_element():
    # Single positive element
    assert max_subarray_sum([1]) == 1
    # Single negative element
    assert max_subarray_sum([-1]) == -1
    # Single zero
    assert max_subarray_sum([0]) == 0

def test_max_subarray_sum_all_negative():
    # Two negative elements
    assert max_subarray_sum([-2, -1]) == -1
    # Three negative elements
    assert max_subarray_sum([-2, -3, -1]) == -1
    # All negative with varying values
    assert max_subarray_sum([-5, -1, -10, -3]) == -1

def test_max_subarray_sum_with_zeros():
    # All zeros
    assert max_subarray_sum([0, 0, 0]) == 0
    # Mixed with zeros
    assert max_subarray_sum([0, -1, 0, 1, 0]) == 1
    # Zeros separating negative and positive
    assert max_subarray_sum([-2, 0, 3, 0, -1]) == 3

def test_max_subarray_sum_edge_cases():
    # Empty list - assuming it raises ValueError (common implementation)
    with pytest.raises(ValueError):
        max_subarray_sum([])
    # Large numbers
    assert max_subarray_sum([1000000, -999999, 1]) == 1000000
    # Very small numbers
    assert max_subarray_sum([-1000000, 1, -999999]) == 1
    # Subarray at the beginning
    assert max_subarray_sum([5, 4, -10, 1, 2]) == 9
    # Subarray at the end
    assert max_subarray_sum([-10, -5, 1, 2, 3]) == 6
    # Subarray in the middle
    assert max_subarray_sum([-1, 10, 5, -20, 1]) == 15

def test_max_subarray_sum_floats():
    # Although problem specifies integers, test floats if supported
    # Assuming function handles floats
    assert max_subarray_sum([1.5, -0.5, 2.0]) == 3.0