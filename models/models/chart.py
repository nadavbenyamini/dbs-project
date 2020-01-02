from models.base_model import *
from models.data_types import *


class Chart(BaseModel):
    def __init__(self):
        self.table = 'Charts'
        self.fields = [
            {'name': 'country_id', 'type': Types.INT, 'pk': True},
            {'name': 'track_id', 'type': Types.STRING, 'pk': False},
            {'name': 'rank', 'type': Types.STRING, 'pk': False}
        ]
