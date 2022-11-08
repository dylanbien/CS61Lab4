from pymongo import MongoClient
import re

def postBlog(collection, params):

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
  result = list(collection.find({"_id": blogName}))
  if not result:
    blog = {
      '_id': blogName,
      'posts': {},
      'comments': {}
    }
    collection.insert_one(blog)

  post = {
    'permalink':permalink,
    'title': title, 
    'userName': userName,
    'tags': tags,
    'timestamp': timestamp,
    'postBody':  postBody,
    'comments': {}
  }

  post_path = "posts.{}".format(permalink.split('.')[1])

  # If the blog exist, throw an error it:
  if(list(collection.find({post_path:{"$exists":"true"}}))):
    print("post already exists")
    return

  #Add the post
  collection.update_one(
    { "_id": blogName},
    { "$set": {post_path: post}})