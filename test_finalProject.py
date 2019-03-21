import sqlite3
from unittest import TestCase
from unittest.mock import MagicMock

import FinalProject as pro


class TestFinalProject(TestCase):
    """Test class for Exercise4 class"""

    __author__ = "Khushpreet Singh"

    def test_sqlite3_connect_success(self):
        sqlite3.connect = MagicMock(return_value='connection succeeded')

        sqlite3.connect.assert_called_with('test_database')

    def test_insertData(self):
        """Test method for insertData() function in the Exercise4 class """
        test = pro.insert(self)
        self.assertEqual(test, "g")
        print("Author is Khushpreet Singh")


    def test_deleterow(self):
        test = pro.deleterow(self)
        self.assertEqual(test, "g")
