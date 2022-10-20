# Create a database complete written in python3
# Let the database be a dictionary
# Make a function that can add a new entry to the database
# Make a function that can delete an entry from the database
# Make a function that can update an entry from the database
# Make a function that can search an entry from the database
# Make a function that can print the database
# Make a function that can save the database to a file
# Make a function that can load the database from a file
# And make a class called DB containing the functions mentioned above
class DB:
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


