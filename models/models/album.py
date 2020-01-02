from models.data_types import Types


class Album:
    def __init__(self):
        self.table = 'Albums'
        self.fields = [
            {'name': 'album_id', 'type': Types.INT, 'pk': True},
            {'name': 'album_name', 'type': Types.STRING, 'pk': False},
            {'name': 'album_rating', 'type': Types.INT, 'pk': False},
            {'name': 'album_release_date', 'type': Types.TIMESTAMP, 'pk': False}
        ]
