def commentBlog(posts, comments, params):
  
  # check params
  if len(params) != 6:
    print("error: incorrect number of params")
    return

  # parse params
  parentPermalink = params[2]
  userName = params[3]
  commentBody = params[4]
  timestamp = params[5]

  # find referenced post/comment
  result = list(posts.find({"_id": parentPermalink, "deleted": {"$exists": False}}))
  if not result:
    result = list(comments.find({"_id": parentPermalink, "deleted": {"$exists": False}}))
    if not result:
      print("error: referenced post/comment does not exist")
      return
    else: 
      type = "reply"
  else:
    type = "comment"

  # create comment
  comment = {
    '_id': timestamp,
    'userName': userName,
    'comment': commentBody,
    'replies': []
  }
  comments.insert_one(comment)

  # add to parent post/comment
  if type == "comment":
    posts.update_one({"_id": parentPermalink}, {"$push": {"comments": timestamp}})
    print("comment posted!")
  else:
    comments.update_one({"_id": parentPermalink}, {"$push": {"replies": timestamp}})
    print("reply posted!")