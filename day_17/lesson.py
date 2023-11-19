class User:
    # Constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    # methods always require the first parameter as "self"    
    def follow(self, user):
        user.followers += 1
        self.following += 1

Tommy = User("001", "Tommy")
Jack = User("002", "Jack")

Tommy.follow(Jack)
print(f"Tommy's followers: {Tommy.followers}")
print(f"Tommy's following: {Tommy.following}")
print(f"Jack's followers: {Jack.followers}")
print(f"Jack's following: {Jack.following}")
