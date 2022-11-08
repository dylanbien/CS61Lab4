from configparser import ConfigParser
import getpass
from pymongo import MongoClient
import shlex
from commands.post import postBlog
from commands.comment import commentBlog
from commands.delete import deleteBlog
from commands.show import showBlog


import sys
  
def read_db_config(filename='Team23Lab4.ini', section='Mongodb'):
    """ Read database configuration file and return a dictionary object
    Based on examples from [MySQL with Python tutorial ](http://www.mysqltutorial.org/python-mysql)
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """

    # create parser and read ini configuration file, default 'dbconfig.ini'
    parser = ConfigParser()
    parser.read(filename)
 
    # get section, default to mysql
    dbconfig = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            dbconfig[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
 
    return dbconfig


def get_database():

  dbconfig = read_db_config()
  if dbconfig['password'] == "": 
    dbconfig['password'] = getpass.getpass("database password ? :")
  
  # Provide the mongodb atlas url to connect python to mongodb using pymongo
  CONNECTION_STRING = "mongodb+srv://{}:{}@cluster0.zgbwym3.mongodb.net/test".format(dbconfig['user'], dbconfig['password'])
 
  # Create a connection using MongoClient.
  try:
    print('Connecting to MySQL database...')
    client = MongoClient(CONNECTION_STRING)
  except Exception as e:
    print("Failure Connecting")
    print(e)
    sys.exit(1)
 
  # Return the database
  return client['lab4']
  

if __name__ == '__main__':

  dbname = get_database()
  collection = dbname["blog"]

  while True:
    command = sys.stdin.readline()[:-1] 

    if(command == 'done'):
      break
    else:
      params = shlex.split(command)

    if(params[0] == 'post'):
      postBlog(collection, params)
      print('posting blog')
    elif(params[0] == 'comment'):
      commentBlog(collection, params)
      print('commenting blog')
    elif(params[0] == 'delete'):
      deleteBlog(collection, params)
      print('deletng blog')
    elif(params[0] == 'show'):
      showBlog(collection, params)
      print('showing blog')
    else:
      print("error: unrecognized command")