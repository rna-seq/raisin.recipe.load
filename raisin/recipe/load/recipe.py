import database

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

    def install(self):
        database.main(self.options, self.buildout)

    def update(self):
        return self.install()