from models.base_model import *
from models.data_types import *


class Lyrics(BaseModel):
    def __init__(self):
        self.table = 'Lyrics'
        self.fields = [
            {'name': 'track_id', 'type': INT, 'pk': True},
            {'name': 'track_lyrics', 'type': STRING, 'pk': False}
        ]
