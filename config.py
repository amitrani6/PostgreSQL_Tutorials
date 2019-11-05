# This file was adapted from http://www.postgresqltutorial.com/postgresql-python/connect/

# The following config() function read the database.ini file and returns the connection parameters. We put the config() function in the config.py file:

#!/usr/bin/python
from configparser import ConfigParser
 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    
    #Checks to see if section (postgresql) parser exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db