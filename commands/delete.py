from pymongo import MongoClient
import re

def deleteBlog(collection, params):

  if len(params) != 5:
    print("error: incorrect number of params")
    return

  blogName = params[1]
  permalink = params[2]
  userName = params[3]
  timestamp = params[4]