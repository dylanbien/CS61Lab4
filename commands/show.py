from pymongo import MongoClient
import re

def showBlog(collection, params):

  if len(params) != 2:
    print("error: incorrect number of params")
    return

  blogName = params[1]