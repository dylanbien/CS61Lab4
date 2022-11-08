from pprint import pprint

def showBlog(blogs, posts, comments, params):

  # check params
  if len(params) != 2:
    print("error: incorrect number of params")
    return

  # parse params
  blogName = params[1]

  # find and print blog
  result = list(blogs.find({"_id": blogName}))
  if not result:
    print("error: blog does not exist")
    return
  else:
    blog = result[0]
    pprint(blog)

  # find and print posts
  blogPosts = blog.get("posts")

  for permalink in blogPosts:
    result = list(posts.find({"_id": permalink}))
    if not result:  # should never reach here
      print("error: post does not exist")
      return
    else:
      post = result[0]
      pprint(post)

    # find and print comments
    postComments = post.get("comments")

    for permalink in postComments:
      showComment(comments, permalink, 0)    

# function to recursively print replies
def showComment(comments, permalink, level):

  # find and print comment
  result = list(comments.find({"_id": permalink}))
  if not result:  # should never reach here
    print("error: comment does not exist")
    return
  else:
    comment = result[0]
    pprint(comment)

  # find and print all replies
  replies = comment.get("replies")

  for replyPermalink in replies:
    showComment(comments, replyPermalink, level + 1)