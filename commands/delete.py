from pymongo import MongoClient

def deleteBlog(posts, comments, params):

  # check params
  if len(params) != 5:
    print("error: incorrect number of params")
    return

  # parse params
  permalink = params[2]
  userName = params[3]
  timestamp = params[4]

  # find referenced post/comment
  result = list(posts.find({"_id": permalink, "deleted": {"$exists": False}}))
  if not result:
    result = list(comments.find({"_id": permalink, "deleted": {"$exists": False}}))
    if not result:
      print("error: referenced post/comment does not exist")
      return
    else: 
      type = "comment"
  else:
    type = "post"

  # delete post/comment
  deleteMessage = "deleted by " + userName
  if type == "post":
    posts.update_one({"_id": permalink}, {"$set": {"timestamp": timestamp, "postBody": deleteMessage, "deleted": True}})
    print("post deleted!")
  else:
    comments.update_one({"_id": permalink}, {"$set": {"comment": deleteMessage, "deleted": timestamp}})
    print("comment deleted!")