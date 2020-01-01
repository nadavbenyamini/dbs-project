from models.base_model import *
from models.data_types import *


class Country(BaseModel):
    def __init__(self):
        self.table = 'countries'
        self.fields = [
            {'name': 'country_id', 'type': Types.STRING, 'pk': True},
            {'name': 'country_name', 'type': Types.String, 'pk': False}
        ]
