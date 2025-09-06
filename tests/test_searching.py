import pytest
from algorithms.searching import linear_search, binary_search

def test_linear_search_found():
    arr = [1, 3, 5, 7, 9]
    assert linear_search(arr, 5) == 2
    assert linear_search(arr, 1) == 0
    assert linear_search(arr, 9) == 4

def test_linear_search_not_found():
    arr = [1, 3, 5, 7, 9]
    assert linear_search(arr, 4) == -1

def test_binary_search_found():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 9) == 4

def test_binary_search_not_found():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 4) == -1
