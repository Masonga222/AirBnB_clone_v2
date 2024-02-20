#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

import os
from .engine.file_storage import FileStorage
from .engine.db_storage import DBStorage


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    #  from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    #  from .engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
