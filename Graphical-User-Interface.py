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