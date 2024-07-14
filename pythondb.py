class database:
    def __init__(self):
        self.database = {}

    def add(self, key, value):
        self.database[key] = value

    def delete(self, key):
        del self.database[key]

    def update(self, key, value):
        self.database[key] = value

    def search(self, key):
        return self.database[key]

    def print(self):
        print(self.database)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.database))

    def load(self, filename):
        with open(filename, 'r') as f:
            self.database = eval(f.read())
