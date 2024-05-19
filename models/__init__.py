#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

#create the variable storage, an instance of FileStorage
storage = FileStorage()

#call reload() method on this variable
storage.reload()
