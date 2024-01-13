#!/usr/bin/python3
"""
initilize et storage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
