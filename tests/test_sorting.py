import pytest
from algorithms.sorting import bubble_sort, merge_sort

def test_bubble_sort():
    arr = [5, 2, 9, 1, 5, 6]
    sorted_arr = bubble_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_merge_sort():
    arr = [3, 0, -1, 8, 7]
    sorted_arr = merge_sort(arr.copy())
    assert sorted_arr == sorted(arr)
