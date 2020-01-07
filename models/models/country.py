from models.base_model import *


class Country(BaseModel):
    def __init__(self):
        self.table = 'Countries'
        self.fields = [
            {'name': 'country_id', 'type': STRING, 'pk': True},
            {'name': 'country_name', 'type': STRING, 'pk': False},
            {'name': 'population', 'type': INT, 'pk': False}
        ]
