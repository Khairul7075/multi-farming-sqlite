"""Here’s a clean and functional version of animal.py, which defines an Animal class to represent and interact with animal farming 
data in your SQLite database. It follows the same structure as crop.py for consistency and modularity. """ 
from db_manager import execute_query, execute_non_query

class Animal:
    def __init__(self, animal_id, name_en, name_bn, compatible_crop_id, notes):
        self.animal_id = animal_id
        self.name_en = name_en
        self.name_bn = name_bn
        self.compatible_crop_id = compatible_crop_id
        self.notes = notes

    def save_to_db(self):
        query = """
        INSERT INTO Animals (animal_id, name_en, name_bn, compatible_crop_id, notes)
        VALUES (?, ?, ?, ?, ?);
        """
        params = (self.animal_id, self.name_en, self.name_bn, self.compatible_crop_id, self.notes)
        execute_non_query(query, params)

    @staticmethod
    def get_all_animals():
        query = "SELECT animal_id, name_en, name_bn, compatible_crop_id, notes FROM Animals;"
        results = execute_query(query)
        animals = []
        for row in results:
            animal = Animal(*row)
            animals.append(animal)
        return animals

    def __str__(self):
        return f"{self.name_en} ({self.name_bn}) - Compatible with Crop ID: {self.compatible_crop_id}, Notes: {self.notes}"



