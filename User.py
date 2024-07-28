import os # Import OS for system operations


class User:
    # Class variable to store all user instances
    all_users = []

    def __init__(self, user_id: int, name: str, age: int):
        # Initialize user attributes
        self.user_id = user_id  # ID for the user
        self.name = name  # User's name
        self.age = age  # User's age
        self.messages = []  # List of messages for the user
        self.friends = []  # Empty list of friends
        self.friend_requests = []  # Empty list of pending friend requests
        self.profile = {}  # Dictionary for additional profile information
        self.profile_posts = {"posts": [], "likes": {}}  # Dictionary to hold posts and likes
        self.activity_log = []  # User activities
        self.profile_picture = None  # Placeholder for profile picture
        User.all_users.append(self)  # Add the user instance to the class-level list

    def __str__(self) -> str:
        # Return a string representation of the user
        return f"User ID: {self.user_id}, Name: {self.name}, Age: {self.age}"
    
    def add_friend(self, friend):
        """Send a friend request to another user"""
        if friend not in self.friends and friend not in self.friend_requests:
            self.friend_requests.append(friend)  # Add to pending requests
            print(f"Friend request sent to {friend.name}.")  # Notify about the sent request
            self.activity_log.append(f"Sent friend request to {friend.name}.")  # Log the activity
        else:
            print(f"{friend.name} is already your friend or a pending request.")  # Handle duplicate requests

    def accept_friend_request(self, friend):
        """Accept a friend request from another user"""
        if friend in self.friend_requests:
            self.friends.append(friend)  # Add friend to friends list
            self.friend_requests.remove(friend)  # Remove from pending requests
            print(f"{friend.name} is now your friend.")  # Notify about the new friendship
            self.activity_log.append(f"Accepted friend request from {friend.name}.")  # Log the activity
        else:
            print(f"No friend request from {friend.name}.")  # Handle case where there is no request
