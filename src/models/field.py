"""Here’s a clean and functional version of field.py, which defines a Field class to represent farming plots and interact with your 
SQLite database. This matches the style of your crop.py and animal.py files for consistency. """ 

from db_manager import execute_query, execute_non_query

class Field:
    def __init__(self, field_id, location, area_sq_meters, water_source):
        self.field_id = field_id
        self.location = location
        self.area_sq_meters = area_sq_meters
        self.water_source = water_source

    def save_to_db(self):
        query = """
        INSERT INTO Fields (field_id, location, area_sq_meters, water_source)
        VALUES (?, ?, ?, ?);
        """
        params = (self.field_id, self.location, self.area_sq_meters, self.water_source)
        execute_non_query(query, params)

    @staticmethod
    def get_all_fields():
        query = "SELECT field_id, location, area_sq_meters, water_source FROM Fields;"
        results = execute_query(query)
        fields = []
        for row in results:
            field = Field(*row)
            fields.append(field)
        return fields

    def __str__(self):
        return f"Field {self.field_id} - {self.location}, {self.area_sq_meters} m², Water Source: {self.water_source}"
