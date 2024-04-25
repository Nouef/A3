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
# Process nodes until there are no more or all houses have received packages
    while queue:
        # Get the node with the smallest cost so far
        cost, current_node, path = heapq.heappop(queue)
        # Check if the current node is a house and not yet visited
        if current_node.startswith('H') and current_node not in delivered_to:
            # Deliver package and add to delivered houses
            delivered_to.add(current_node)
            # Record the delivery path and cost for this house
            delivery_paths[current_node] = (path + [current_node], cost)
        # If all houses are delivered, break out of the loop
        if len(delivered_to) == len([node for node in graph if node.startswith('H')]):
            break
        # Explore adjacent nodes (neighbors)
        for neighbor, weight in graph[current_node].items():
            # Add the neighbor to the queue if it is not delivered to or is an intersection
            if neighbor not in delivered_to or not neighbor.startswith('H'):
                heapq.heappush(queue, (cost + weight, neighbor, path + [current_node]))

    # Return the paths and costs of delivery for all houses
    return delivery_paths

    
























# Requirement 3 :Shortest Path Algorithm for Point A to Point B (Dijkstra's algorithm/ priority queue (min-heap))
