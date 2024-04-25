class Post:
  def __init__(self, datetime, content, author, views):
      self.datetime = datetime  # Date and time of the post
      self.content = content    # Content of the post
      self.author = author      # Author of the post
      self.views = views        # Number of views of the post

# Part 1: Using a hash table to find a post by its unique datetime value
class PostManager:
  def __init__(self):
      self.post_table = {}  # Hash table to store posts by datetime

  def add_post(self, post):
      self.post_table[post.datetime] = post  # Add post to the hash table

  def get_post_by_datetime(self, datetime):
      return self.post_table.get(datetime)  # Retrieve post by datetime if exists

from tabulate import tabulate

# Test cases for Part 1
post_manager = PostManager()
post1 = Post("2023-05-13 11:00:00", "Good morning, happy saturday!", "Amani", 50)
post2 = Post("2024-04-18 10:00:00", "Spread love everywhere", "Sara", 100)
post3 = Post("2024-04-18 12:00:00", "Good afternoon everyone", "Ahmed", 85)
post4 = Post("2024-04-18 13:30:00", "I'm feeling great today!", "Khalifa", 123)
post_manager.add_post(post1)
post_manager.add_post(post2)
post_manager.add_post(post3)
post_manager.add_post(post4)

target_post = post_manager.get_post_by_datetime("2024-04-18 10:00:00")
if target_post:
    print("Post retrieved by datetime:")
    print(tabulate([[target_post.datetime, target_post.content, target_post.author, target_post.views]], 
                   headers=["Datetime", "Content", "Author", "Views"]))
else:
    print("Post not found for the specified datetime.")
