class Source:
    def __init__(self):
        self.key = ""
        self.title = ""
        self.authors = []
    
    # allows the user to manually create a source object
    def create(self, sources):
        print('creating a new source...')
        self.add_key(sources)
        self.title = input('Enter the title of the source: ')
        self.authors = self.add_authors()

    # adds an unique user defined key
    def add_key(self, sources):
        key = input('Assign a key to this source: ')
        if(self.validate_key(key, sources)):
            self.key = key
        else:
            print('Sorry, this key in not unique')
            self.add_key(sources)

    def validate_key(self, key, sources):
        for source in sources:
            if source.key == key:
                return False
        return True
    
    # generates a source object based on the parameters
    def generate(self, key, title, authors):
        print('generating '+ key + '...')
        self.key = key
        self.title = title
        self.authors = authors

    #returns the source as a dict
    def dict(self):
        return {'title': self.title, 'authors': self.authors}

    #formats and adds the authors specified by the user
    def add_authors(self):
        authors = input('Enter the names of the Authors: (<lastname>. <firstname>. <letters>.,): ')
        return authors.split(',')