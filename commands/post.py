from pymongo import MongoClient
import re

def postBlog(blogs, posts, params):

  if len(params) != 7:
    print("error: incorrect number of params")
    return
  
  blogName = params[1]
  userName = params[2]
  title = params[3]
  postBody = params[4]
  tags = params[5]
  timestamp = params[6]
  
  permalink  = blogName+'.'+re.sub('[^0-9a-zA-Z]+', '_', title)
  
  # If the blog doesnt exist, create it:
  result = list(blogs.find({"_id": blogName}))
  if not result:
    blog = {
      '_id': blogName,
      'posts': []
    }
    blogs.insert_one(blog)

  post = {
    '_id': permalink,
    'title': title, 
    'userName': userName,
    'tags': tags,
    'timestamp': timestamp,
    'postBody':  postBody,
    'comments': []
  }

  # If the blog exist, throw an error it:

  #Add the post
  posts.insert_one(post)

  # Add the post to the blogs array

