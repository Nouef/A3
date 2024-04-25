# Requirement 2 : Package Distribution Algorithm (Best-First Search /priority queue (min-heap) )
import heapq # Import the heapq library to use the priority queue 

# Function to deliver packages using Best-First Search
def deliver_packages(graph, start):
    # Priority queue to hold the nodes to be visited along with the current cost
    queue = [(0, start, [])]  # The queue will also store the path taken
    # Set to keep track of visited houses to prevent re-delivering
    delivered_to = set()
    # Dictionary to store the delivery paths for each house
    delivery_paths = {}
























# Requirement 3 :Shortest Path Algorithm for Point A to Point B (Dijkstra's algorithm/ priority queue (min-heap))
