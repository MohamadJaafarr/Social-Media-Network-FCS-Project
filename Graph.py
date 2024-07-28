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
