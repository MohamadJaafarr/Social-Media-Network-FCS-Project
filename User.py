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

    def remove_friend(self, friend):
        """Remove a friend from the user's friend list"""
        if friend in self.friends:
            self.friends.remove(friend)  # Remove from friends list
            print(f"{friend.name} has been removed from your friends.")  # Notify about the removal
            self.activity_log.append(f"Removed {friend.name} from friends.")  # Log the activity
        else:
            print(f"{friend.name} is not in your friends list.")  # Handle case where friend not found

    def update_profile(self, key, value):
        """Update the user's profile with a key-value pair"""
        self.profile[key] = value  # Update the profile dictionary with the new key-value pair
        print(f"Profile updated for {self.name}: {key} = {value}")  # Notify about the profile update
        self.activity_log.append(f"Updated profile: {key} = {value}")  # Log the activity

    def display_profile(self):
        """Display the user's profile information"""
        print(f"Profile for {self.name}: {self.profile}")  # Print the user's profile details

    def add_post(self, post_content):
        """Add a new post to the user's profile"""
        self.profile_posts['posts'].append(post_content)  # Add post_content to the posts list
        self.profile_posts['likes'][post_content] = []  # Initialize likes for the post
        print(f"Post added by {self.name}: {post_content}")  # Notify about the new post
        self.activity_log.append(f"Added post: {post_content}")  # Log the activity

    def like_post(self, post_content, user):
        """Like a post made by another user"""
        if post_content in user.profile_posts['posts']:  # Check if the post exists
            if user.profile_posts['likes'][post_content] is not None:
                user.profile_posts['likes'][post_content].append(self.name)  # Add user to likes
                print(f"{self.name} liked {user.name}'s post: {post_content}")  # Notify about the like
                self.activity_log.append(f"Liked {user.name}'s post: {post_content}")  # Log the activity
            else:
                print(f"You already liked this post.")  # Handle case of duplicate like
        else:
            print(f"Post not found.")  # Handle case where post does not exist

    def display_posts(self):
        """Display all posts by the user"""
        print(f"Posts by {self.name}:")  # Header for the post display
        for post in self.profile_posts['posts']:
            likes_count = len(self.profile_posts['likes'][post])  # Count likes for each post
            print(f"{post} (Likes: {likes_count})")  # Print each post with its like count

    def send_message(self, recipient, message_content):
        """Send a message to another user"""
        message = {"from": self.name, "message": message_content}  # Create a message dictionary
        recipient.messages.append(message)  # Add message to recipient's message list
        print(f"Message sent to {recipient.name}: {message_content}")  # Notify about the sent message
        self.activity_log.append(f"Sent message to {recipient.name}: {message_content}")  # Log the activity

    def display_messages(self):
        """Display all received messages"""
        print(f"Messages for {self.name}:")  # Header for message display
        for message in self.messages:  # Iterate over received messages
            print(f"From {message['from']}: {message['message']}")  # Print each message with sender info

    @classmethod  # Is used to define a method that belongs to the class rather than any particular instance of the class.
    def sort_users(cls, key='user_id', reverse=False):
        """Sort all_users list based on the specified key"""
        if key == 'user_id':
            cls.all_users.sort(key=lambda user: user.user_id, reverse=reverse)  # Sort by user_id
        elif key == 'name':
            cls.all_users.sort(key=lambda user: user.name.lower(), reverse=reverse)  # Sort by name
        elif key == 'age':
            cls.all_users.sort(key=lambda user: user.age, reverse=reverse)  # Sort by age
        else:
            print("Invalid sorting key!")  # Handle invalid key

    @classmethod
    def search_users(cls, key, value):
        """Search for users based on the specified key and value"""
        if key == 'user_id':
            return [user for user in cls.all_users if user.user_id == value]  # Search by user_id
        elif key == 'name':
            return [user for user in cls.all_users if user.name.lower() == value.lower()]  # Search by name
        elif key == 'age':
            return [user for user in cls.all_users if user.age == value]  # Search by age
        else:
            print("Invalid search key!")  # Handle invalid key
            return []  # Return an empty list if the key is invalid
        
    def set_profile_picture(self, picture_url):
        """Set the user's profile picture"""
        self.profile_picture = picture_url  # Update the profile picture attribute
        print(f"Profile picture updated for {self.name}.")  # Notify about the picture update

    def display_activity_log(self):
        """Display the user's activity log"""
        print(f"Activity Log for {self.name}:")  # Header for the activity log
        for activity in self.activity_log:  # Iterate over activities
            print(f"- {activity}")  # Print each activity
    