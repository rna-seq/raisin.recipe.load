"""
Test for raisin.recipe.transformation
"""

import os
import unittest
import shutil
from pkg_resources import get_provider
from raisin.recipe.load.database import produce_files
from raisin.recipe.load.database import produce_accessions
from raisin.recipe.load.database import produce_experiments
from raisin.recipe.load.database import produce_runs
from raisin.recipe.load.database import produce_sqlite3_database

PROVIDER = get_provider('raisin.recipe.load')
SANDBOX = PROVIDER.get_resource_filename("", 'tests/sandbox/')
PATH = os.path.join(SANDBOX, 'buildout')


class RecipeTests(unittest.TestCase):
    """
    Test the main method in database.py
    """

    def setUp(self):  # pylint: disable=C0103
        pass
        
    def test_produce_files(self):
        """
        Test producing files
        """
        data = {'experiments':[],'accessions':[], 
                'view':[{'project_id':'',
                        'accession_id':'',
                        'file_location':''},
                        ],
                'files':[],
                'read_length':[],
               }
        database = SANDBOX
        self.failUnless(produce_files(data, database) == None)

    def test_produce_accessions(self):
        """
        Test producing accessions
        """
        data = {'experiments':[],'accessions':[],'read_length':[]}
        database = SANDBOX
        self.failUnless(produce_accessions(data, database) == None)

    def test_produce_experiments(self):
        """
        Test producing experiments
        """
        data = {'experiments':[],'accessions':[], 'annotations':[],'read_length':[],
                'replicates':[]}
        database = SANDBOX
        project_parameters = None
        self.failUnless(produce_experiments(data, database, project_parameters) == None)

    def test_produce_runs(self):
        """
        Test producing runs
        """
        data = {'experiments':[],
                'accessions':[],
                'read_length':[],
                'replicates':[],
                'runs':[],
               }
        database = SANDBOX
        project_parameters = None
        self.failUnless(produce_runs(data, database, project_parameters) == None)

    def test_produce_sqlite3_database(self):
        """
        Test producing the sqlite3 database
        """
        data = None
        database = SANDBOX
        self.failUnless(produce_sqlite3_database(data, database) == None)


def test_suite():
    """
    Run the test suite
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
