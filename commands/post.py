import re

def postBlog(blogs, posts, params):

  # check params
  if len(params) != 7:
    print("error: incorrect number of params")
    return
  
  # parse params
  blogName = params[1]
  userName = params[2]
  title = params[3]
  postBody = params[4]
  tags = params[5]
  timestamp = params[6]

  permalink = blogName + '.' + re.sub('[^0-9a-zA-Z]+', '_', title)
  
  # If the blog doesnt exist, create it:
  result = list(blogs.find({"_id": blogName}))
  if not result:
    blog = {
      '_id': blogName,
      'posts': []
    }
    blogs.insert_one(blog)

  # check if post with same name exists
  result = list(posts.find({"_id": permalink}))
  if result:
    print("error: post with same name already exists")
    return

  # create post
  if len(tags) != 0:
    post = {
      '_id': permalink,
      'title': title, 
      'userName': userName,
      'tags': tags.split(","),
      'timestamp': timestamp,
      'postBody':  postBody,
      'comments': []
    }
  else:
    post = {
      '_id': permalink,
      'title': title, 
      'userName': userName,
      'timestamp': timestamp,
      'postBody':  postBody,
      'comments': []
    }
  posts.insert_one(post)

  # add to parent blog
  blogs.update_one({"_id": blogName}, {"$push": {"posts": permalink}})
  print("post uploaded!")