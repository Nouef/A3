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
  
