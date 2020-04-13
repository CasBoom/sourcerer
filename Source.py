class Source:
    def __init__(self):
        print('creating a new source...')
        self.key = input('Assign a key to this source: ')
        self.title = input('Enter the title of the source: ')
        self.authors = self.add_authors()

    def dict(self):
        return {self.key:[self.title, {'Authors': self.authors}]}

    def add_authors(self):
        authors = input('Enter the names of the Authors: (<lastname>. <firstname>. <letters>.,')
        return authors.split(',')