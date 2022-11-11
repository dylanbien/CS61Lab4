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
    print("\nin " + blog.get("_id") + ":\n")

  # find and print posts
  blogPosts = blog.get("posts")

  for permalink in blogPosts:
    result = list(posts.find({"_id": permalink}))
    if not result:  # should never reach here
      print("error: post does not exist")
      return
    else:
      post = result[0]

      title = post.get("title")
      userName = post.get("userName")
      tags = post.get("tags")
      timestamp = post.get("timestamp")
      body = post.get("postBody")

      print("\t- - - -")
      print("\ttitle: " + title)
      print("\tuserName: " + userName)
      if tags is not None:
        print("\ttags: " + tags)
      print("\tpermalink: " + permalink)
      if (post.get("deleted") is None):
        print("\ttimestamp: " + timestamp)
        print("\tbody:\n\t  " + body + "\n")
      else:
        print("\t**post deleted at " + timestamp + "**:\n\t  " + body + "\n")

    # find and print comments
    postComments = post.get("comments")

    for permalink in postComments:
      showComment(comments, permalink, 2)    

# function to recursively print replies
def showComment(comments, permalink, level):

  # find and print comment
  result = list(comments.find({"_id": permalink}))
  if not result:  # should never reach here
    print("error: comment does not exist")
    return
  else:
    comment = result[0]
    tabs = ""
    for i in range(level):
      tabs = tabs + "\t"
    userName = comment.get("userName")
    body = comment.get("comment")
    deletedTimestamp = comment.get("deleted")
    
    print(tabs + "- - - -")
    print(tabs + "userName: " + userName)
    print(tabs + "permalink: " + permalink)
    if (deletedTimestamp is None):
      print(tabs + "comment:\n" + tabs + "  " + body + "\n")
    else:
      print(tabs + "**comment deleted at " + deletedTimestamp + "**:\n" + tabs + "  " + body + "\n")

  # find and print all replies
  replies = comment.get("replies")

  for replyPermalink in replies:
    showComment(comments, replyPermalink, level + 1)