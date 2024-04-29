# Requirement 2 : Package Distribution Algorithm (Breadth First Search /priority queue (min-heap) )
import heapq # Import the heapq library to use the priority queue 

# Function to deliver packages using Best-First Search
def deliver_packages(graph, start):
    # Priority queue to hold the nodes to be visited along with the current cost
    queue = [(0, start, [])]  # The queue will also store the path taken
    # Set to keep track of visited houses to prevent re-delivering
    delivered_to = set()
    # Dictionary to store the delivery paths for each house
    delivery_paths = {}
# Process nodes until there are no more or all houses have received packages
    while queue:
        # Pop the node with the smallest depth
        depth, current_node, path = heapq.heappop(queue)
        # Check if the current node is a house and not yet visited
        if current_node.startswith('H') and current_node not in delivered_to:
            # Deliver package and add to delivered houses
            delivered_to.add(current_node)
            # Record the delivery path and cost for this house
            delivery_paths[current_node] = (path + [current_node], depth)
        # If all houses are delivered, break out of the loop
        if len(delivered_to) == len([node for node in graph if node.startswith('H')]):
            break
        # Explore adjacent nodes (neighbors)
        for neighbor, weight in graph[current_node].items():
            # Add the neighbor to the queue if it is not delivered to or is an intersection
            if neighbor not in delivered_to or not neighbor.startswith('H'):
                heapq.heappush(queue, (depth + 1, neighbor, path + [current_node]))

    # Return the paths and costs of delivery for all houses
    return delivery_paths

# Function to run test cases
def test_cases(graph):
    # Define starting nodes for the delivery tests
    tests = ['1', '6', '14']
    # Iterate through each test case
    for test in tests:
        print(f"Starting delivery from intersection: {test}")
        # Get the delivery paths for the current test case
        delivery_paths = deliver_packages(graph, test)
        # Print out the delivery details for each house
        for house, (path, depth) in delivery_paths.items():
            print(f"Delivered to {house}: Path taken: {' -> '.join(path)}, Total distance: {depth}")
        # Print a separator for readability between test cases
        print("\n" + "="*50 + "\n")

# Main function to set up the graph and initiate the test cases
def main():
    # Define the graph with nodes and weighted edges
    graph = {
        '1': {'2': 200},
        '2': {'1': 200, '7': 100, '8': 150},
        '7': {'2': 100, 'H1': 80, 'H2': 80, '11': 150},
        'H1': {'7': 80},
        'H2': {'7': 80},
        '8': {'2': 150, 'H16': 80, 'H17': 80, '3': 100, '12': 140, '11': 170},
        'H16': {'8': 80},
        'H17': {'8': 80},
        '3': {'8': 100, '9': 150},
        '9': {'3': 150, '4': 100, 'H19': 80, 'H18': 80, '13': 160, '12': 170},
        'H18': {'9': 80},
        'H19': {'9': 80},
        '4': {'9': 100, 'H20': 80, '10': 160},
        'H20': {'4': 80},
        '10': {'4': 160, '6': 100, 'H15': 80, 'H14': 80, 'H13': 80, '14': 100, '13': 160},
        'H13': {'10': 80},
        'H14': {'10': 80},
        'H15': {'10': 80},
        '6': {'10': 100},
        '11': {'7': 150, '8': 170, 'H3': 80, 'H4': 80, 'H5': 80, 'H6': 80, '12': 50, '15': 250},
        'H3': {'11': 80},
        'H4': {'11': 80},
        'H5': {'11': 80},
        'H6': {'11': 80},
        '12': {'8': 140, '9': 170, '11': 50, '13': 60},
        '13': {'9': 160, '10': 160, '12': 60, 'H21': 80, 'H22': 80, '14': 90},
        'H21': {'13': 80},
        'H22': {'13': 80},
        '14': {'10': 100, '13': 90, '15': 100, 'H10': 80, 'H11': 80, 'H12': 80},
        'H10': {'14': 80},
        'H11': {'14': 80},
        'H12': {'14': 80},
        '15': {'11': 250, '14': 100, 'H7': 80, 'H8': 80, 'H9': 80},
        'H7': {'15': 80},
        'H8': {'15': 80},
        'H9': {'15': 80},
    }

    # Run the test cases with the defined graph
    test_cases(graph)

if __name__ == "__main__":
    main()



    


# Requirement 3 :Shortest Path Algorithm for Point A to Point B (Dijkstra's algorithm/ priority queue (min-heap))

import heapq  # Import the heapq library to use the priority queue 

def dijkstra_shortest_path(graph, start, end):
    """
    Implements Dijkstra's algorithm to find the shortest path from 'start' to 'end' in a weighted graph.
      """
    # Priority queue to store nodes during the exploration, with initial node having 0 distance
    queue = [(0, start, [])]
    # Distance dictionary, initialized with infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Set to track visited nodes to prevent re-processing
    visited = set()

   while queue:
        # Extract the node with the smallest distance from the queue
           current_distance, current_node, path = heapq.heappop(queue)
           if current_node not in visited:
               visited.add(current_node)
               path = path + [current_node]
            
            # Return the path and distance if the end node is reached
               if current_node == end:
                   return path, current_distance
            
            # Explore each adjacent node
               for neighbor, distance in graph[current_node].items():
                   if neighbor not in visited:
                       new_distance = current_distance + distance
                    # Only consider this new path if it's better than any previously found path to the neighbor
                       if new_distance < distances[neighbor]:
                           distances[neighbor] = new_distance
                           heapq.heappush(queue, (new_distance, neighbor, path))
    
    # If the end node is not reachable, return an empty path and infinite distance
     return [], float('infinity')

def main():
    """
    Main function to test the Dijkstra's algorithm with predefined graph and test cases.
    """
    # Define the graph representing the city with intersections and houses
    graph = {
        '1': {'2': 200},
        '2': {'1': 200, '7': 100, '8': 150},
        '7': {'2': 100, 'H1': 80, 'H2': 80, '11': 150},
        'H1': {'7': 80},
        'H2': {'7': 80},
        '8': {'2': 150, 'H16': 80, 'H17': 80, '3': 100, '12': 140, '11': 170},
        'H16': {'8': 80},
        'H17': {'8': 80},
        '3': {'8': 100, '9': 150},
        '9': {'3': 150, '4': 100, 'H19': 80, 'H18': 80, '13': 160, '12': 170},
        'H18': {'9': 80},
        'H19': {'9': 80},
        '4': {'9': 100, 'H20': 80, '10': 160},
        'H20': {'4': 80},
        '10': {'4': 160, '6': 100, 'H15': 80, 'H14': 80, 'H13': 80, '14': 100, '13': 160},
        'H13': {'10': 80},
        'H14': {'10': 80},
        'H15': {'10': 80},
        '6': {'10': 100},
        '11': {'7': 150, '8': 170, 'H3': 80, 'H4': 80, 'H5': 80, 'H6': 80, '12': 50, '15': 250},
        'H3': {'11': 80},
        'H4': {'11': 80},
        'H5': {'11': 80},
        'H6': {'11': 80},
        '12': {'8': 140, '9': 170, '11': 50, '13': 60},
        '13': {'9': 160, '10': 160, '12': 60, 'H21': 80, 'H22': 80, '14': 90},
        'H21': {'13': 80},
        'H22': {'13': 80},
        '14': {'10': 100, '13': 90, '15': 100, 'H10': 80, 'H11': 80, 'H12': 80},
        'H10': {'14': 80},
        'H11': {'14': 80},
        'H12': {'14': 80},
        '15': {'11': 250, '14': 100, 'H7': 80, 'H8': 80, 'H9': 80},
        'H7': {'15': 80},
        'H8': {'15': 80},
        'H9': {'15': 80},
    }

     # Define test cases with start and end points
    test_cases = [
        ('1', '15', "Test Case 1: From Intersection 1 to Intersection 15"),
        ('2', 'H20', "Test Case 2: From Intersection 2 to House H20"),
        ('7', 'H10', "Test Case 3: From Intersection 7 to House H10")
    ]
    
    # Run each test case using Dijkstra's algorithm
    for start, end, description in test_cases:
        print(description)
        path, distance = dijkstra_shortest_path(graph, start, end)
        print(f"Shortest path: {' -> '.join(path)}, Distance: {distance} meters.\n")

if __name__ == '__main__':
    main()


