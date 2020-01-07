from models.base_model import *


class Chart(BaseModel):
    def __init__(self):
        self.table = 'Charts'
        self.fields = [
            {'name': 'country_id', 'type': STRING, 'pk': True},
            {'name': 'track_id', 'type': STRING, 'pk': True},
            {'name': 'track_rank', 'type': STRING, 'pk': False}
        ]
