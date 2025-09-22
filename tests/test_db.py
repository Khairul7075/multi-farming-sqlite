"""How to Run  
python tests/test_db.py

"""
 
import unittest
from db_manager import execute_query, execute_non_query

class TestDatabaseOperations(unittest.TestCase):

    def test_insert_and_fetch_crop(self):
        # Insert a test crop
        insert_query = """
        INSERT INTO Crops (crop_id, name_en, name_bn, water_need, duration_days)
        VALUES (?, ?, ?, ?, ?);
        """
        test_data = (999, 'TestCrop', 'টেস্ট ফসল', 'Low', 45)
        execute_non_query(insert_query, test_data)

        # Fetch the inserted crop
        select_query = "SELECT name_en, name_bn FROM Crops WHERE crop_id = 999;"
        result = execute_query(select_query)
        self.assertEqual(result[0][0], 'TestCrop')
        self.assertEqual(result[0][1], 'টেস্ট ফসল')

    def test_field_count(self):
        query = "SELECT COUNT(*) FROM Fields;"
        result = execute_query(query)
        self.assertTrue(result[0][0] >= 0)

    def test_animal_compatibility(self):
        query = """
        SELECT a.name_en FROM Animals a
        JOIN Crops c ON a.compatible_crop_id = c.crop_id
        WHERE c.name_en = 'Paddy';
        """
        result = execute_query(query)
        self.assertTrue(any('Fish' in row for row in result))

if __name__ == '__main__':
    unittest.main()
