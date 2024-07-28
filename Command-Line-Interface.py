import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
from Graph import AdjacencyMatrix


def cli_menu(graph):
    """
    Displays a command-line interface menu for managing the graph.
    
    Parameters:
    graph (AdjacencyMatrix): The graph object used to store user connections.

    """
    while True: # Infinite loop to keep the menu active until the user chooses to exit
        # Print the menu header with stylized colors
        print(Fore.CYAN + Style.BRIGHT + "----- Graph CLI Menu -----")
        print(Fore.YELLOW + "1. Add User")
        print("2. Add Connection")
        print("3. Remove Connection")
        print("4. Remove User")
        print("5. Display Graph")
        print("6. Visualize Graph")
        print("7. DFS")
        print("8. BFS")
        print("9. Average Friends Per User")
        print("10. Network Density")
        print("11. Clustering Coefficient")
        print("12. Exit")
        print(Fore.CYAN + Style.BRIGHT + "---------------------------")