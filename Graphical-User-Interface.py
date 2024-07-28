import tkinter as tk  # For creating graphical user interfaces (GUIs) in Python.
from tkinter import messagebox, simpledialog, ttk
# - messagebox: for displaying message boxes.
# - simpledialog: for prompting the user to enter simple data.
# - ttk: for using widgets.
import networkx as nx 
import matplotlib.pyplot as plt  
from Graph import AdjacencyMatrix  # Importing the AdjacencyMatrix class from the Graph module.
import os


class GraphApp(tk.Tk):
    """
    GraphApp class inherits from tk.Tk and represents the main application window
    for the social media network graph application.

    """
    def __init__(self):
        """
        Initialize the GraphApp window.
        Sets up the main application window properties and initializes the graph.

        """
        super().__init__()
        self.title("Social Media Network")
        self.geometry("400x500")
        self.configure(bg="#f0f0f0")
        self.create_widgets()
        self.graph = AdjacencyMatrix()

    def create_widgets(self):
        """
        Create and place UI components (buttons) on the application window.
        Each button corresponds to a different functionality of the application.

        """
        # Title label
        self.title_label = tk.Label(self, text="Social Media Network", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Add User Button
        self.add_user_button = ttk.Button(self, text="Add User", command=self.add_user)
        self.add_user_button.pack(pady=5)

        # Add Connection Button
        self.add_connection_button = ttk.Button(self, text="Add Connection", command=self.add_connection)
        self.add_connection_button.pack(pady=5)

        # Remove User Button
        self.remove_user_button = ttk.Button(self, text="Remove User", command=self.remove_user)
        self.remove_user_button.pack(pady=5)

        # Remove Connection Button
        self.remove_connection_button = ttk.Button(self, text="Remove Connection", command=self.remove_connection)
        self.remove_connection_button.pack(pady=5)

        # Visualize Graph Button
        self.visualize_button = ttk.Button(self, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.pack(pady=5)

        # Show Stats Button
        self.stats_button = ttk.Button(self, text="Show Stats", command=self.show_stats)
        self.stats_button.pack(pady=5)

        # Quit Button
        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=20)

    def add_user(self):
        """
        Prompt the user to enter a username and add it to the graph.

        """
        user_name = simpledialog.askstring("Input", "Enter user name:", parent=self)
        if user_name:
            if self.graph.adduser(user_name):
                messagebox.showinfo("Success", f"User '{user_name}' added successfully!", parent=self)
            else:
                messagebox.showwarning("Warning", f"User '{user_name}' already exists.", parent=self)

    def add_connection(self):
        """
        Prompt the user to enter two usernames and add a connection between them.

        """
        user1 = simpledialog.askstring("Input", "Enter first user name:", parent=self)
        user2 = simpledialog.askstring("Input", "Enter second user name:", parent=self)
        
        if user1 and user2:
            # Attempt to add the connection
            result = self.graph.addconnection(user1, user2)  # Assuming self.graph is an instance of AdjacencyMatrix
            
            if result is None:  # No return means the connection was added successfully
                messagebox.showinfo("Success", f"Connection between '{user1}' and '{user2}' added!", parent=self)
            else:
                messagebox.showwarning("Warning", f"Connection could not be made. Check user names.", parent=self)

    def remove_user(self):
        """
        Prompt the user to enter a username and remove it from the graph.

        """
        user_name = simpledialog.askstring("Input", "Enter user name to remove:", parent=self)
        if user_name:
            self.graph.removeuser(user_name)
            messagebox.showinfo("Success", f"User '{user_name}' removed successfully!", parent=self)

    def remove_connection(self):
        """
        Prompt the user to enter two usernames and remove the connection between them.
        
        """
        user1 = simpledialog.askstring("Input", "Enter first user name:", parent=self)
        user2 = simpledialog.askstring("Input", "Enter second user name:", parent=self)
        if user1 and user2:
            # Attempt to remove the connection
            self.graph.removeconnection(user1, user2)

            # Check if the users exist and if the connection has been effectively removed
            if user1 in self.graph.users and user2 in self.graph.users:
                if self.graph.graph[self.graph.users[user1]][self.graph.users[user2]] == 0:
                    messagebox.showinfo("Success", f"Connection between '{user1}' and '{user2}' removed!", parent=self)
                else:
                    messagebox.showwarning("Warning", f"Connection could not be removed. Check user names.", parent=self)
            else:
                messagebox.showwarning("Warning", f"One or both user names do not exist.", parent=self)