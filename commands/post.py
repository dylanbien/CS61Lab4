from pymongo import MongoClient
import re

def postBlog(collection, params):

	if len(params) != 7:
		print("error: incorrect number of params")
		return
	
	blogName = params[1]
	userName = params[2]
	title = params[3]
	timestamp = params[4]
	blogName = params[5]

	permalink  = blogName+'.'+re.sub('[^0-9a-zA-Z]+', '_', title)