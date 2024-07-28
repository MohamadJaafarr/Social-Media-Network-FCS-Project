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