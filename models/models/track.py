from models.base_model import *
from models.data_types import *


class Track(BaseModel):
    def __init__(self):
        self.table = 'Tracks'
        self.fields = [
            {'name': 'track_id', 'type': Types.INT, 'pk': True},
            {'name': 'track_name', 'type': Types.STRING, 'pk': False},
            {'name': 'track_rating', 'type': Types.STRING, 'pk': False},
            {'name': 'genre_id', 'type': Types.INT, 'pk': False},
            {'name': 'artist_id', 'type': Types.INT, 'pk': False},
            {'name': 'album_id', 'type': Types.INT, 'pk': False},
            {'name': 'track_release_date', 'type': Types.TIMESTAMP, 'pk': False}
        ]
