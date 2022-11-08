from pymongo import MongoClient
import re 
def commentBlog(collection, params):
  
  if len(params) != 6:
    print("error: incorrect number of params")
    return
  
  blogName = params[1]
  permalink = params[2]
  userName = params[3]
  commentBody = params[4]
  timestamp = params[5]

  permalink  = re.sub('[^0-9a-zA-Z]+', '_', permalink) 
  comment_path = "comments.{}".format(permalink.split('.')[1])

  comment = {
    'userName': userName,
    'permalink': timestamp,
    'comment': commentBody
  }


  #Add the post
  collection.update_one(
    { "_id": blogName},
    { "$set": {comment_path: comment}})