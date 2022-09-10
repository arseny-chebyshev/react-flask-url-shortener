import mongoengine

class URL(mongoengine.Document):
    long_url = mongoengine.StringField()
    short_url = mongoengine.StringField()
    meta = {
        'db': 'flask-db',
        'collection': 'urls'
    }
