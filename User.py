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

def clear_screen():
    # Clear the console screen for a cleaner interface
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Create multiple user instances
    user1 = User(1, "Mhamad", 25)  # Create User 1
    user2 = User(2, "Ali", 23)  # Create User 2
    user3 = User(3, "Nisreen", 28)  # Create User 3
    user4 = User(4, "Sara", 21)  # Create User 4
    user5 = User(5, "Abbass", 29)  # Create User 5
    user6 = User(6, "Layla", 23)  # Create User 6
    user7 = User(7, "Imane", 21)  # Create User 7
    user8 = User(8, "Caren", 26)  # Create User 8
    user9 = User(9, "Yara", 20)  # Create User 9
    user10 = User(10, "Omar", 18)  # Create User 10
    user11 = User(11, "Rama", 19)  # Create User 11
    user12 = User(12, "Rana", 27)  # Create User 12

    # Example of Sorting Users
    print("Before sorting by age:")
    for user in User.all_users:
        print(user)

    # Sort users by age
    User.sort_users(key='age')
    print("\nAfter sorting by age:")
    for user in User.all_users:
        print(user)

    # Sort users by name in descending order
    User.sort_users(key='name', reverse=True)
    print("\nAfter sorting by name (descending):")
    for user in User.all_users:
        print(user)

    # Example of Searching Users
    print("\nSearching for user with user_id=3:")
    result = User.search_users(key='user_id', value=3)
    for user in result:
        print(user)

    print("\nSearching for user named 'Ali':")
    result = User.search_users(key='name', value='Ali')
    for user in result:
        print(user)

    print("\nSearching for users with age 23:")
    result = User.search_users(key='age', value=23)
    for user in result:
        print(user)
    
    # Sending and accepting friend requests
    user1.add_friend(user2)  # User 1 sends a friend request to User 2
    user1.accept_friend_request(user2)  # User 2 accepts the friend request

    # Adding friends
    user1.add_friend(user3)  # User 1 sends a friend request to User 3
    user2.add_friend(user4)  # User 2 sends a friend request to User 4

    # Adding posts
    user1.add_post("Hello world!")  # User 1 adds a post
    user2.add_post("It's a beautiful day!")  # User 2 adds a post
    user3.add_post("Good morning everyone!")  # User 3 adds a post

    # Liking posts
    user1.like_post("It's a beautiful day!", user2)  # User 1 likes User 2's post
    user3.like_post("Hello world!", user1)  # User 3 likes User 1's post

    # Messaging
    user1.send_message(user2, "Hey Ali! How's it going?")  # User 1 sends a message to User 2
    user2.send_message(user1, "I'm good, thanks!")  # User 2 replies to User 1

    # Displaying user information
    user1.display_profile()  # Display User 1's profile
    user2.display_posts()  # Display User 2's posts
    user2.display_messages()  # Display User 2's messages
    user1.display_activity_log()  # Display User 1's activity log
    user3.display_posts()  # Display User 3's posts
    # Accessing and displaying the list of all users
    print("\nAll Users:") 
    for user in User.all_users: 
        print(user)  


main()  