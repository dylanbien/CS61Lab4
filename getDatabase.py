from configparser import ConfigParser
import getpass
from pymongo import MongoClient

  
def read_db_config(filename='Team23Lab4.ini', section='Atlas'):
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
 
  # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
  client = MongoClient(CONNECTION_STRING)
 
  # Return the database
  return client['lab4']
  

if __name__ == '__main__':

  dbname = get_database()
  collection_name = dbname["blog"]

  item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
  }

  item_2 = {
    "_id" : "U1IT00002",
    "item_name" : "Egg",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "brown country eggs"
  }
  collection_name.insert_many([item_1,item_2])
