# -*- coding: utf-8 -*-
"""Recipe apache"""

from raisin.recipe.load import database


class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

    def install(self):
        database.main(self.buildout['transform']['staging'],
                      self.buildout['load']['database'])

    def update(self):
        return self.install()
