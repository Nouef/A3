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
# Part 2: Using a binary search tree to find posts in a specific time range
class BSTNode:
  def __init__(self, post):
      self.post = post    # The post stored in the node
      self.left = None    # Reference to the left child node
      self.right = None   # Reference to the right child node

class PostBST:
  def __init__(self):
      self.root = None # Initialize the root of the binary search tree

  def insert(self, post):
      if not self.root:
          self.root = BSTNode(post) # If tree is empty set new node as root
      else:
          self._insert_helper(post, self.root)

  def _insert_helper(self, post, node):
    # Helper function to recursively insert a post into the tree
    if post.datetime < node.post.datetime:
        if node.left:
            self._insert_helper(post, node.left)  # If datetime is smaller, go left
        else:
            node.left = BSTNode(post)  # If left child is None, insert new node here
    else:
        if node.right:
            self._insert_helper(post, node.right)  # If datetime is greater, go right
