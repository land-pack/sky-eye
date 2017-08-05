import os

# export DB_NAME=your-data-base-name
DB_NAME =  os.environ.get('DB_NAME') or 'test'
DB_USERNAME =  os.environ.get('DB_USERNAME') or 'root'
DB_PASSWD =  os.environ.get('DB_PASSWD') or 'root'
DB_HOST =  os.environ.get('DB_HOST') or '127.0.0.1'
DB_PORT =  os.environ.get('DB_PORT') or 3306


