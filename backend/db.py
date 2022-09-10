from mongoengine import connect, disconnect

class Client:
    """Return a MongoDB client connection with Admin (read-write) priveleges.
       Supports atomic connections with help of Python syntax 'with ... as ..:'"""

    def __init__(self, db=''):
        self.host=f"mongodb://localhost:27017/{db}", 
        self.username='flask', 
        self.password='flask'

    def __enter__(self):
        self = connect(host=self.host, username='flask', password=self.password)
        print(f"Succesfully connected to database with client: {self}")

    def __exit__(self, type, value, traceback):
        disconnect()
        print("Succesfully disconnected client")
