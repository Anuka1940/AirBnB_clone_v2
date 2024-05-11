#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream


class TestHBNBCommand(unittest.TestCase):
    """Represent the test cases for the HBNBCommand class
    """
    @unittest.skipif(
            os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Tests the create command with the file storage.
        """
        with patch('sys.stdout', new=StringIO()) as count:
            cons = HBNBCommand()
            cons.onecmd('create City name="Texes"')
            md1_id = count.getvalue().strip()
            clear_stream(count)
            self.assertIn('City.{}'.format(md1_id), storage.all().keys())
            cons.onecmd('show City {}'.format(md1_id))
            self.assertIn("name': 'Texes'", count.getvalue().strip())
            clear_stream(count)
            cons.onecmd('create User name="James" age=17 height=5.9')
            md1_id = count.getvalue().strip()
            self.assertIn('User.{}'.format(md1_id), storage.all().keys())
            clear_stream(count)
            cons.onecmd('show User {}'.format(md1_id))
            self.assertIn("'name': 'James'", count.getvalue().strip())
            self.assertIn("'age': 17", count.getvalue().strip())
            self.assertIn("'height': 5.9", count.getvalue().strip())
