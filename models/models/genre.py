from models.base_model import *
from models.data_types import *


class Genre(BaseModel):
    def __init__(self):
        self.table = 'Genres'
        self.fields = [
            {'name': 'genre_id', 'type': Types.INT, 'pk': True},
            {'name': 'genre_parent_id', 'type': Types.INT, 'pk': False},
            {'name': 'genre_name', 'type': Types.STRING, 'pk': False}
        ]
