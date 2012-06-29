"""
Test for raisin.recipe.transformation
"""

import os
import unittest
import shutil
from pkg_resources import get_provider
from raisin.recipe.load import database

PROVIDER = get_provider('raisin.recipe.load')
SANDBOX = PROVIDER.get_resource_filename("", 'tests/sandbox/')
PATH = os.path.join(SANDBOX, 'buildout')


class RecipeTests(unittest.TestCase):
    """
    Test the main method in database.py
    """

    def setUp(self):  # pylint: disable=C0103
        pass
        
    def test_1(self):
        """
        Test 1
        """
        self.failUnless(database.main(None, None, None) == None)


def test_suite():
    """
    Run the test suite
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
