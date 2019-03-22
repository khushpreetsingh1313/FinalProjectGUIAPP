from unittest import TestCase
from FinalProject import FinalProject


class TestFinalProject(TestCase):
    """Test class for FinalProject class"""

    __author__ = "Khushpreet Singh"

    def test_loadcsv(self):
        """Test method for loadcsv() function in the FinalProject class """
        test = FinalProject.loadcsv(self)
        self.assertEqual(test, "CSVloaded")