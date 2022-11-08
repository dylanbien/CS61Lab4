from pymongo import MongoClient
from configparser import ConfigParser
import getpass

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
  CONNECTION_STRING = "mongodb+srv://{}:{}@cluster0.{}.mongodb.net/test".format(dbconfig['user'], dbconfig['password'], dbconfig['connect'])
 
  # Create a connection using MongoClient.
  try:
    print('Connecting to MongoDB database...')
    client = MongoClient(CONNECTION_STRING)
  except Exception as e:
    print("Failure Connecting")
    print(e)
    sys.exit(1)
 
  # Success and return the database
  print('Connected to MongoDB database.')
  return client[dbconfig['db']]