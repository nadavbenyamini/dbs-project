from models.base_model import *


class Track(BaseModel):
    def __init__(self):
        self.table = 'Tracks'
        self.fields = [
            {'name': 'track_id', 'type': INT, 'pk': True},
            {'name': 'track_name', 'type': STRING, 'pk': False},
            {'name': 'track_rating', 'type': STRING, 'pk': False},
            {'name': 'genre_id', 'type': INT, 'pk': False},
            {'name': 'artist_id', 'type': INT, 'pk': False},
            {'name': 'album_id', 'type': INT, 'pk': False},
            {'name': 'track_release_date', 'type': TIMESTAMP, 'pk': False}
        ]
