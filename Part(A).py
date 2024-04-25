class Post:
    def __init__(self, datetime, content, author, views):
        self.datetime = datetime
        self.content = content
        self.author = author
        self.views = views

# Part 1: Using a hash table to find a post by its unique datetime value
class PostManager:
    def __init__(self):
        self.post_table = {}

    def add_post(self, post):
        self.post_table[post.datetime] = post

    def get_post_by_datetime(self, datetime):
        return self.post_table.get(datetime)

# Test cases for Part 1
post_manager = PostManager()
post1 = Post("2024-04-18 10:00:00", "Hello World!", "User1", 100)
post2 = Post("2024-04-18 11:00:00", "Good morning!", "User2", 50)
post_manager.add_post(post1)
post_manager.add_post(post2)
print(post_manager.get_post_by_datetime("2024-04-18 10:00:00").content)  
print(post_manager.get_post_by_datetime("2024-04-18 11:00:00").author)
  
