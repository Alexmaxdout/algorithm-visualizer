import pytest
from algorithms.graphs import bfs, dfs

def test_bfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']

def test_dfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    dfs_result = dfs(graph, 'A')
    # DFS may vary in order depending on recursion, but must contain all nodes
    assert set(dfs_result) == {'A', 'B', 'C', 'D', 'E', 'F'}
