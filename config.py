import configparser
config = configparser.ConfigParser()
config.read('config.ini')

database_name = config.get('Database', 'name')
database_host = config.get('Database', 'host')
database_user = config.get('Database', 'user')
database_password = config.get('Database', 'password')
