from models.base_model import *
from models.data_types import *


class Track(BaseModel):
    def __init__(self):
        self.table = 'Charts'
        self.fields = [
            {'name': 'track_id', 'type': Types.INT, 'pk': True},
            {'name': 'track_name', 'type': Types.STRING, 'pk': False},
            {'name': 'track_rating', 'type': Types.STRING, 'pk': False},
            {'name': 'artist_id', 'type': Types.INT, 'pk': False},
            {'name': 'album_id', 'type': Types.INT, 'pk': False},
            {'name': 'updated_time', 'type': Types.TIMESTAMP, 'pk': False}
        ]
