from algorithms.sorting import bubble_sort, merge_sort
from algorithms.searching import linear_search, binary_search
from algorithms.graphs import bfs, dfs
import numpy as np

def main():
    print("=== Algorithm Visualizer ===")
    print("1. Sorting Algorithms")
    print("2. Searching Algorithms")
    print("3. Graph Algorithms")
    choice = input("Select an option (1-3): ")

    if choice == "1":
        arr = np.random.randint(1, 100, 10)
        print(f"Original array: {arr}")
        sorted_arr = bubble_sort(arr.copy())
        print(f"Bubble sorted: {sorted_arr}")
        sorted_arr = merge_sort(arr.copy())
        print(f"Merge sorted: {sorted_arr}")
    elif choice == "2":
        arr = np.arange(10)
        target = 5
        print(f"Array: {arr}, Target: {target}")
        print(f"Linear search index: {linear_search(arr, target)}")
        print(f"Binary search index: {binary_search(arr, target)}")
    elif choice == "3":
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        start_node = 'A'
        print(f"BFS starting from {start_node}: {bfs(graph, start_node)}")
        print(f"DFS starting from {start_node}: {dfs(graph, start_node)}")
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    main()
