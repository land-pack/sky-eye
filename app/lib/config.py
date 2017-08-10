import os

# export DB_NAME=your-data-base-name
DB_NAME =  os.environ.get('DB_NAME') or 'test'
DB_USERNAME =  os.environ.get('DB_USERNAME') or 'root'
DB_PASSWD =  os.environ.get('DB_PASSWD') or 'root'
DB_HOST =  os.environ.get('DB_HOST') or '127.0.0.1'
DB_PORT =  os.environ.get('DB_PORT') or 3306
DB_MONGO_URI  = "mongodb://"

DB_NAME_OFFLINE =  'crazy_bet'
DB_USERNAME_OFFLINE = 'crazy_bet'
DB_PASSWD_OFFLINE = 'crazy_bet'
DB_HOST_OFFLINE =  '10.0.1.27'
DB_PORT_OFFLINE =  3306
DB_MONGO_URI_OFFLIN = '///'

