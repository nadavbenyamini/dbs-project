from models.base_model import *


class Genre(BaseModel):
    def __init__(self):
        self.table = 'Genres'
        self.fields = [
            {'name': 'genre_id', 'type': INT, 'pk': True},
            {'name': 'genre_parent_id', 'type': INT, 'pk': False},
            {'name': 'genre_name', 'type': STRING, 'pk': False}
        ]
