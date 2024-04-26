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
            node.right = BSTNode(post)  # If right child is None, insert new node here

  def find_posts_in_range(self, start_datetime, end_datetime):
      posts_in_range = [] # Initialize list to store posts within the specified range
      self._find_posts_in_range_helper(start_datetime, end_datetime, self.root, posts_in_range)
      return posts_in_range
  def _find_posts_in_range_helper(self, start, end, node, result):
    # Helper function to recursively find posts within a specified range
    if not node:
        return  # Base case: If node is None, return
    if start <= node.post.datetime <= end:
        result.append(node.post)  # If post datetime falls within the range, append to result list
    if start < node.post.datetime:
        self._find_posts_in_range_helper(start, end, node.left, result)  # Search left subtree
    if end > node.post.datetime:
        self._find_posts_in_range_helper(start, end, node.right, result)  # Search right subtree

# Test cases for Part 2
bst = PostBST()
bst.insert(post1)
bst.insert(post2)
bst.insert(post3)
bst.insert(post4)
posts_in_range = bst.find_posts_in_range("2024-04-18 10:00:00", "2024-04-18 12:00:00")
print("\nPosts within time range:")
print(tabulate([[post.datetime, post.content, post.author, post.views] 
                for post in posts_in_range], 
               headers=["Datetime", "Content", "Author", "Views"]))
print()
# Part 3: Using a max heap to prioritize posts by number of views
import heapq

class PostHeap:
  def __init__(self):
      self.heap = []  # Max heap to store posts by views

  def add_post(self, post):
      heapq.heappush(self.heap, (-post.views, post)) # Add post to the max heap based on views

  def get_most_viewed_post(self):
      if self.heap:
          return self.heap[0][1] # Return the post with the most views

# Test cases for Part 3
max_heap = PostHeap()
max_heap.add_post(post1)
max_heap.add_post(post2)
max_heap.add_post(post3)
max_heap.add_post(post4)
most_viewed_post = max_heap.get_most_viewed_post()
print("Most viewed post:")
print(tabulate([[most_viewed_post.datetime, most_viewed_post.content, most_viewed_post.author, most_viewed_post.views]], 
               headers=["Datetime", "Content", "Author", "Views"]))
