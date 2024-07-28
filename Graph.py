import networkx as nx  #For the creation, manipulation, and study of complex networks.
import matplotlib.pyplot as plt  # For creating static, animated, and interactive visualizations in Python.
from colorama import Fore, Style, init  # For format text output in the console with colors.
import os  # For interacting with the operating system, such as clearing the console screen.
import heapq  # For the priority queue implementation


# Initialize colorama
init(autoreset=True)
# Automatically resets the color and style after each print statement, so you don't need to manually reset styles.
class AdjacencyMatrix:

    def __init__(self):
        self.users = {}  # Dictionary to store user indices
        self.graph = []  # Adjacency matrix
        self.num_users = 0  # Number of users

    def adduser(self, user_name):
        """Add a new user to the graph."""
        if user_name not in self.users:
            # If the user does not already exist, add them to the users dictionary
            self.users[user_name] = self.num_users  # Map user name to a unique index
            self.num_users += 1  # Increment the total number of users

            # Extend the graph by adding a new column for the new user in each existing row
            for row in self.graph:
                row.append(float('inf'))  # Using float('inf') is often useful in algorithms,
                # particularly those involving optimization or graph-related algorithms,
                #  such as Dijkstra's algorithm for shortest paths
            
            # Append a new row for the new user initialized to zero 
            self.graph.append([float('inf')] * self.num_users)
            return True  # Indicate success in adding the user
        else:
            # Notify if the user already exists
            print(f"{Fore.RED}User {user_name} already exists.")
            return False  # Indicate failure in adding the user
        
    def addconnection(self, user1, user2):
        """Add a connection (friendship) between two users."""
        if user1 in self.users and user2 in self.users:
            # Get the index of each user
            idx1 = self.users[user1]
            idx2 = self.users[user2]
            # Update the adjacency matrix to indicate a connection between the two users
            self.graph[idx1][idx2] = 1  # Set the connection for user1 to user2
            self.graph[idx2][idx1] = 1  # Set the connection for user2 to user1 
        else:
            # Notify if either user is not found
            print(f"{Fore.RED}Users {user1} and/or {user2} not found.")

    def removeconnection(self, user1, user2):
        """Remove the connection (friendship) between two users."""
        if user1 in self.users and user2 in self.users:
            # Get the index of each user
            idx1 = self.users[user1]
            idx2 = self.users[user2]
            # Update the adjacency matrix to remove the connection between the two users
            self.graph[idx1][idx2] = 0  # Remove the connection for user1 to user2
            self.graph[idx2][idx1] = 0  # Remove the connection for user2 to user1
        else:
            # Notify if either user is not found
            print(f"{Fore.RED}Users {user1} and/or {user2} not found.")

    def removeuser(self, user):
        """Remove a user from the graph along with their connections."""
        if user in self.users:
            index = self.users[user]  # Get the index of the user to be removed
            del self.users[user]  # Remove the user from the users dictionary
            del self.graph[index]  # Remove the user's row from the adjacency matrix

            # Remove the user's column from each row in the adjacency matrix
            for row in self.graph:
                del row[index]
            
            self.num_users -= 1  # Decrease the total number of users

            # Update the user indices for users that came after the removed user
            for key, value in self.users.items():
                if value > index:
                    self.users[key] = value - 1  # Decrement their index by one

    def get_all_users(self):
        """Return a list of all user names."""
        return list(self.users.keys())  # Return the keys from the users dictionary
    
    def displayGraph(self):
        """Display the adjacency matrix of the graph with colors and formatting."""
        users = sorted(self.users.keys())  # Sort users for consistent display
        
        # Calculate the maximum width needed for the user names
        max_user_length = max(len(user) for user in users)
        
        # Print the header with user names, right-aligned
        print(Fore.GREEN + "\nAdjacency Matrix:")
        header = Fore.BLUE + " " * (max_user_length + 3) + "  ".join(f"{user:>{max_user_length}}" for user in users)
        print(header)
        
        # Print a separator
        print(Fore.YELLOW + " " * (max_user_length + 3) + "-" * (max_user_length * len(users) + 2 * (len(users) - 1)))
        
        # Print each user's connections
        for i, user in enumerate(users):
            row_display = Fore.BLUE + f"{user:<{max_user_length}} | "  # User name in blue
            for j in range(len(users)):
                # Check for a valid connection
                value = self.graph[i][j]
                if value < float('inf'):  # There's a connection
                    row_display += Fore.GREEN + f"{value:>{max_user_length}}"  # Connection weight (1 or other weight)
                else:  # No connection
                    row_display += Fore.RED + f"{0:>{max_user_length}}"  # No connection (0)
            
            # Print the complete row with connections
            print(row_display + Style.RESET_ALL)  # Reset to default style after each row

    def dijkstra(self, start_user, end_user):
        """Find the shortest path between two users using Dijkstra's algorithm."""
        if start_user not in self.users or end_user not in self.users:
            print(f"{Fore.RED}Start user or end user not found.")
            return
        
        # Initialize distances and priority queue
        distances = {user: float('inf') for user in self.users}  # Set all distances to infinity
        distances[start_user] = 0  # Distance to the start user is zero
        queue = [(0, start_user)]  # Priority queue initialized with the start user
        
        predecessors = {user: None for user in self.users}  # To reconstruct the path

        while queue:
            current_distance, current_user = heapq.heappop(queue)  # Get the user with the smallest distance
            
            # If we reach the end user, we can reconstruct the path
            if current_user == end_user:
                path = []
                while current_user is not None:
                    path.append(current_user)
                    current_user = predecessors[current_user]
                path.reverse()  # Reverse the path to get it from start to end
                print(f"Shortest path from {start_user} to {end_user}: {' -> '.join(path)}")
                print(f"Total distance: {distances[end_user]}")
                return
            
            # Skip processing if the distance is not optimal anymore
            if current_distance > distances[current_user]:
                continue
            
            # Check all neighbors of the current user
            for neighbor_index in range(self.num_users):
                weight = self.graph[self.users[current_user]][neighbor_index]
                if weight < float('inf'):  # Check if there is a valid edge
                    neighbor = self.get_all_users()[neighbor_index]
                    distance = current_distance + weight
                    
                    # If found a shorter path to the neighbor
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        predecessors[neighbor] = current_user
                        heapq.heappush(queue, (distance, neighbor))  # Add neighbor to the priority queue

        print(f"{Fore.RED}No path found from {start_user} to {end_user}.")

    def bfs(self, start_user):
        """Perform a Breadth-First Search (BFS) starting from the given user."""
        visited = set()  # Set to keep track of visited users
        queue = [start_user]  # Initialize the queue with the starting user
        
        if start_user not in self.users:
            # Notify if the starting user is not found
            print(f"{Fore.RED}User {start_user} not found.")
            return
        
        start_index = self.users[start_user]  # Get the index of the starting user
        visited.add(start_user)  # Mark the starting user as visited
        print(Fore.GREEN + "BFS traversal starting from", start_user + ":")
        print(start_user, end=' ')  # Print the starting user
        
        while queue:
            user = queue.pop(0)  # Dequeue a user from the front of the queue
            index = self.users[user]  # Get the index of the user
            
            # Check all possible connections from the current user
            for neighbor_index in range(self.num_users):
                # If a connection exists and the neighbor hasn't been visited
                if self.graph[index][neighbor_index] == 1 and self.get_all_users()[neighbor_index] not in visited:
                    neighbor = self.get_all_users()[neighbor_index]  # Get the neighbor's name
                    queue.append(neighbor)  # Enqueue the neighbor
                    visited.add(neighbor)  # Mark the neighbor as visited
                    print(neighbor, end=' ')  # Print the neighbor

    def dfs(self, start_user):
        """Perform a Depth-First Search (DFS) starting from the given user."""
        visited = set()  # Set to keep track of visited users
        stack = [start_user]  # Initialize the stack with the starting user
        
        if start_user not in self.users:
            # Notify if the starting user is not found
            print(f"{Fore.RED}User {start_user} not found.")
            return
        
        start_index = self.users[start_user]  # Get the index of the starting user
        visited.add(start_user)  # Mark the starting user as visited
        print(Fore.GREEN + "DFS traversal starting from", start_user + ":")
        print(start_user, end=' ')  # Print the starting user
        
        while stack:
            user = stack.pop()  # Pop a user from the stack
            index = self.users[user]  # Get the index of the user
            
            # Check all possible connections from the current user
            for neighbor_index in range(self.num_users):
                # If a connection exists and the neighbor hasn't been visited
                if self.graph[index][neighbor_index] == 1 and self.get_all_users()[neighbor_index] not in visited:
                    neighbor = self.get_all_users()[neighbor_index]  # Get the neighbor's name
                    stack.append(neighbor)  # Add the neighbor to the stack
                    visited.add(neighbor)  # Mark the neighbor as visited
                    print(neighbor, end=' ')  # Print the neighbor

    def connected_components(self):
        """Find and return all connected components in the graph."""
        visited = set()  # Set to keep track of visited users
        components = []  # List to hold all connected components

        for user in self.users:
            if user not in visited:
                # If the user has not been visited, perform a DFS/BFS to find all connected users
                component = self._explore_component(user, visited)
                components.append(component)  # Add the found component to the list
        
        return components
    
    def _explore_component(self, start_user, visited):
        """Explore all users in the connected component starting from start_user."""
        stack = [start_user]  # Initialize the stack for DFS
        component = []  # List to hold the current connected component

        while stack:
            user = stack.pop()  # Pop a user from the stack
            if user not in visited:
                visited.add(user)  # Mark the user as visited
                component.append(user)  # Add the user to the current component
                
                # Check all possible connections from the current user
                index = self.users[user]  # Get the index of the user
                for neighbor_index in range(self.num_users):
                    if self.graph[index][neighbor_index] < float('inf'):  # Check if there is a valid connection
                        neighbor = self.get_all_users()[neighbor_index]
                        if neighbor not in visited:
                            stack.append(neighbor)  # Add unvisited neighbors to the stack
        
        return component  # Return the connected component found

