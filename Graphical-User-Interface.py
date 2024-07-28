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