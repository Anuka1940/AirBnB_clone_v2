#!/usr/bin/python3
"""Tests for the  AIRBNB clone modules"""
import os
from typing import TEXTIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TEXTIO):
    """Clears the contents of a given stream 
    Args:
        stream (TEXTIO): The stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)
