from pymongo import MongoClient
import shlex
from getDatabase import get_database
from commands.post import postBlog
from commands.comment import commentBlog
from commands.delete import deleteBlog
from commands.show import showBlog

import sys
  
if __name__ == '__main__':

  dbname = get_database()
  blogs = dbname["blogs"]
  posts = dbname["posts"]
  comments = dbname["comments"]

  while True:
    command = sys.stdin.readline()[:-1] 

    if(command == 'done'):
      break
    else:
      params = shlex.split(command)

    if(params[0] == 'post'):
      postBlog(blogs, posts, params)
      print('posting blog')
    elif(params[0] == 'comment'):
      # commentBlog(collection, params)
      print('commenting blog')
    elif(params[0] == 'delete'):
      # deleteBlog(collection, params)
      print('deletng blog')
    elif(params[0] == 'show'):
      # showBlog(collection, params)
      print('showing blog')
    else:
      print("error: unrecognized command")