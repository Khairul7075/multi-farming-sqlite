"""Here’s a clean and modular version of crop.py, which defines a Crop class to represent crop data and interact with the database. 
This is useful if you're building a Python-based interface or using an ORM-style approach."""

from db_manager import execute_query, execute_non_query

class Crop:
    def __init__(self, crop_id, name_en, name_bn, water_need, duration_days):
        self.crop_id = crop_id
        self.name_en = name_en
        self.name_bn = name_bn
        self.water_need = water_need
        self.duration_days = duration_days

    def save_to_db(self):
        query = """
        INSERT INTO Crops (crop_id, name_en, name_bn, water_need, duration_days)
        VALUES (?, ?, ?, ?, ?);
        """
        params = (self.crop_id, self.name_en, self.name_bn, self.water_need, self.duration_days)
        execute_non_query(query, params)

    @staticmethod
    def get_all_crops():
        query = "SELECT crop_id, name_en, name_bn, water_need, duration_days FROM Crops;"
        results = execute_query(query)
        crops = []
        for row in results:
            crop = Crop(*row)
            crops.append(crop)
        return crops

    def __str__(self):
        return f"{self.name_en} ({self.name_bn}) - Water: {self.water_need}, Duration: {self.duration_days} days"
