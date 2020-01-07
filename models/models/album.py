from models.base_model import *


class Artist(BaseModel):
    def __init__(self):
        self.table = 'Albums'
        self.fields = [
            {'name': 'album_id', 'type': INT, 'pk': True},
            {'name': 'artist_id', 'type': INT, 'pk': False},
            {'name': 'album_name', 'type': STRING, 'pk': False},
            {'name': 'album_rating', 'type': INT, 'pk': False},
            {'name': 'album_release_date', 'type': TIMESTAMP, 'pk': False}
        ]
