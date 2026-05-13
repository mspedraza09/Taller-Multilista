from node import node
class country:
    def __init__(self, name, lat=None, lon=None):
        super().__init__(id,name)
        self.lat = float(str(lat).replace(',','.'))if lat is not None else None
        self.lon = float(str(lon).replace(',','.'))if lon is not None else None
