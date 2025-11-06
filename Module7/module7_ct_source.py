# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 7: Critical Thinking
# Created by Mukul Mondal
# Saturday, October 26, 2025
#
# Python Program:
#

'''
Problem statement:

Optimize a food delivery app's route planning using Dijkstra's algorithm to 
find the shortest path for couriers, considering real-time traffic data. 

Algorithm: Dijkstra's Algorithm 
Analysis (one page, excluding cover and references): Explore the applicability
of Dijkstra's algorithm to courier route optimization, analyze its time complexity
given varying traffic conditions, and discuss the real-life variables impacting 
its performance. Evaluate external factors influencing the lower bound of route
planning efficiency.
'''


from time import time
from os import system, name
import heapq



# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    print("")
    return



# Graph representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
    'E': {}
    }
# dictionary used to represent the Graph data structure
# vertex: dictionary key, like 'A' 
# edges: collection of Key-Value-Pair (map's 1st item - key: Edge's end vertex, map's second item - edge's Weight)
# Vertex may have no edge, like vertex 'E'


# Implementation of Dijkstra Algorithm
# This implementation does not use any Priority-Queue
# So, certainly we need to have 'loop' inside another 'loop', which will lead to Quadratic time complexity.
# time complexity without a priority queue (min-heap) is: 𝑂(𝑉**2)
def dijkstra_No_pQueue_fullPath(graph, start):
    # Initialize distances and previous node tracker
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    visited = set()

    while len(visited) < len(graph):
        # Find the unvisited node with the smallest distance
        current_node = None
        for node in graph:
            if node not in visited:
                if current_node is None or distances[node] < distances[current_node]:
                    current_node = node

        if current_node is None:
            break  # Remaining nodes are inaccessible

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node

    return distances, previous


# Implementation of Dijkstra Algorithm
# This implementation does use Priority-Queue
# We can expect much better efficiency than the earlier implementation, but we'll also need to maintain the priority queue.
# time complexity with a priority queue (min-heap) is: 𝑂((𝑉+𝐸)⋅log𝑉) 
def dijkstra_pQueue_fullPath(graph, start):
    # Initialize distances and previous node tracker
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    # Priority queue: (distance, node)
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Skip if we already found a better path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous


# this just shows the min-cost path created by the algorithm for the graph nodes
def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path if path[0] == start else []



# test methods:
# Creates some basic graph, following the defined graph format as mentioned above
# Run priority queue (min-heap) based implementation of the 'Dijkstra' algorithm
# Shows all min-cost paths from the 'source vertex'
def test1_dijkstra_pQueue_fullPath():
    graph1 = {
    'A': {'B': 1, 'C': 4, 'F': 6},
    'B': {'A': 1, 'C': 2, 'D': 5, 'E': 7},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'G': 8, 'H': 4},
    'E': {'B': 7, 'F': 3},
    'F': {'A': 6, 'E': 3, 'G': 2},
    'G': {'D': 8, 'F': 2, 'H': 1},
    'H': {'D': 4, 'G': 1}
    }
    
    start = time()
    start_node = 'A'
    distances, previous = dijkstra_pQueue_fullPath(graph1, start_node)
    end = time()
    print("Execution time:", end-start)

    print(f"Shortest distances from {start_node}:")
    for node, dist in distances.items():
        print(f"  {node}: {dist}")

    print("\nShortest Paths Route details from A:")
    for node in graph1:
        if node != start_node:
            path = reconstruct_path(previous, start_node, node)
            print(f"  Path to {node}: {' -> '.join(path)}")
    return

# test methods:
# Creates the same basic graph, as used above
# Run no priority queue (min-heap) based implementation of the 'Dijkstra' algorithm
# Shows all min-cost paths from the 'source vertex'
def test1_dijkstra_No_pQueue_fullPath():
    graph2 = {
    'A': {'B': 1, 'C': 4, 'F': 6},
    'B': {'A': 1, 'C': 2, 'D': 5, 'E': 7},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'G': 8, 'H': 4},
    'E': {'B': 7, 'F': 3},
    'F': {'A': 6, 'E': 3, 'G': 2},
    'G': {'D': 8, 'F': 2, 'H': 1},
    'H': {'D': 4, 'G': 1}
    }
    
    start = time()
    start_node = 'A'
    distances, previous = dijkstra_No_pQueue_fullPath(graph2, start_node)
    end = time()
    print("Execution time:", end-start)
    print(f"Shortest distances from {start_node}:")
    for node, dist in distances.items():
        print(f"  {node}: {dist}")

    print("\nShortest Paths Route details from A:")
    for node in graph2:
        if node != start_node:
            path = reconstruct_path(previous, start_node, node)
            print(f"  Path to {node}: {' -> '.join(path)}")
    return

# Main test function
# Executes Algorithms
def run_allTests():
    """
    Runs algorithms on different inputs.    
        
    Parameters
    ----------
    Input : None
    Return : None
    ----------
    """ 
    print("\n== Using priority Queue ==")
    test1_dijkstra_pQueue_fullPath()
    print("\n\n== Using no priority Queue ==")
    test1_dijkstra_No_pQueue_fullPath()
    return
    

if __name__ == "__main__":
    clearScreen()
    print("=== CSC506 - Module 7: Critical Thinking ===")
    print("=== Dijkstra's Algorithm ===")
    print("-------------------------------------------\n")   
    print("=== Two Tests executed ===")
    print("=== Data Structure execution performance ===\n")
    run_allTests()
    

