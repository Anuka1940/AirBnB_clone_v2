#!/usr/bin/python3
#!/usr/bin/python
"""
    This module instantiates an object of class DBStorage or
    FileStorage
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()

else:
    storage = FileStorage()
    storage.reload()
