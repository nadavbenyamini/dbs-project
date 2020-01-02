from models.base_model import *
from models.data_types import *


class Country(BaseModel):
    def __init__(self):
        self.table = 'Countries'
        self.fields = [
            {'name': 'country_id', 'type': Types.INT, 'pk': True},
            {'name': 'country_code', 'type': Types.STRING, 'pk': False},
            {'name': 'country_name', 'type': Types.STRING, 'pk': False}
        ]
