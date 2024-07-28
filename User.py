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
