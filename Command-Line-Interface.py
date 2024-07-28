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

        choice = input(Fore.WHITE + "Enter your choice: ") # Prompt user for their menu choice

        if choice == '1':
            user_name = input("Enter user name to add: ")
            graph.adduser(user_name)
        elif choice == '2':
            user1 = input("Enter first user: ")
            user2 = input("Enter second user: ")
            graph.addconnection(user1, user2)
        elif choice == '3':
            user1 = input("Enter first user: ")
            user2 = input("Enter second user: ")
            graph.removeconnection(user1, user2)
        elif choice == '4':
            user = input("Enter user name to remove: ")
            graph.removeuser(user)
        elif choice == '5':
            graph.displayGraph()
            input("Press Enter to continue...")
        elif choice == '6':
            graph.visualize()
        elif choice == '7':
            start_user = input("Enter starting user for DFS: ")
            graph.dfs(start_user)
            print()
            input("Press Enter to continue...")
        elif choice == '8':
            start_user = input("Enter starting user for BFS: ")
            graph.bfs(start_user)
            print()
            input("Press Enter to continue...")
        elif choice == '9':
            avg_friends = graph.average_friends_per_user()
            print(f"Average number of friends per user: {avg_friends:.2f}")
            input("Press Enter to continue...")
        elif choice == '10':
            density = graph.network_density()
            print(f"Network density: {density:.2f}")
            input("Press Enter to continue...")
        elif choice == '11':
            clustering_coeff = graph.clustering_coefficient()
            print(f"Clustering coefficient: {clustering_coeff:.2f}")
            input("Press Enter to continue...")
        elif choice == '12':
            print(Fore.GREEN + "Exiting program...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number from 1 to 12.")
            input("Press Enter to continue...")