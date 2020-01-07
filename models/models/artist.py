from models.base_model import *


class Artist(BaseModel):
    def __init__(self):
        self.table = 'Artists'
        self.fields = [
            {'name': 'artist_id', 'type': INT, 'pk': True},
            {'name': 'artist_name', 'type': STRING, 'pk': False},
            {'name': 'artist_country_id', 'type': STRING, 'pk': False},
            {'name': 'artist_rating', 'type': INT, 'pk': False}
        ]
