from models.base_model import *
from models.data_types import *


class Artist(BaseModel):
    def __init__(self):
        self.table = 'Artists'
        self.fields = [
            {'name': 'artist_id', 'type': Types.INT, 'pk': True},
            {'name': 'artist_name', 'type': Types.STRING, 'pk': False},
            {'name': 'artist_country', 'type': Types.STRING, 'pk': False},
            {'name': 'artist_rating', 'type': Types.INT, 'pk': False},
            {'name': 'updated_time', 'type': Types.TIMESTAMP, 'pk': False}
        ]
