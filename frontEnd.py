from pymongo import MongoClient
import shlex
from getDatabase import get_database
from commands.post import postBlog
from commands.comment import commentBlog
from commands.delete import deleteBlog
from commands.show import showBlog
from commands.find import findBlog

import sys
  
if __name__ == '__main__':

  dbname = get_database()
  blogs = dbname["blogs"]
  posts = dbname["posts"]
  comments = dbname["comments"]

  blogs.drop()
  posts.drop()
  comments.drop()

  while True:
    print("What would you like to do?: ")
    command = sys.stdin.readline().strip()

    if(command == 'done'):
      break
    else:
      params = shlex.split(command)
    
    if(len(params) == 0):
      continue
    elif(params[0] == 'post'):
      print('posting...')
      postBlog(blogs, posts, params)
    elif(params[0] == 'comment'):
      print('commenting...')
      commentBlog(posts, comments, params)
    elif(params[0] == 'delete'):
      print('deleting...')
      deleteBlog(posts, comments, params)
    elif(params[0] == 'show'):
      print('loading...')
      showBlog(blogs, posts, comments, params)
    elif(params[0] == 'find'):
      print('finding...')
      findBlog(blogs, posts, comments, params)
    else:
      print("error: unrecognized command")