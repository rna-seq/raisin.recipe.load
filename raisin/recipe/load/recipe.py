import database

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

    def install(self):
        staging = self.buildout['transform']['staging']
        database.main(staging)

    def update(self):
        return self.install()