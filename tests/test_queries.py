"""To Run Use the Below Command:
   python tests/test_queries.py

""" 
import unittest
from db_manager import execute_query

class TestCustomQueries(unittest.TestCase):

    def test_compatible_farming_query(self):
        query = """
        SELECT c.name_en, a.name_en
        FROM Crops c
        JOIN Animals a ON c.crop_id = a.compatible_crop_id;
        """
        results = execute_query(query)
        self.assertTrue(len(results) > 0, "No compatible crop-animal pairs found")
        for crop, animal in results:
            self.assertIsInstance(crop, str)
            self.assertIsInstance(animal, str)

    def test_seasonal_plan_query(self):
        query = """
        SELECT sa.season, f.location, c.name_en, a.name_en
        FROM SeasonalActivities sa
        JOIN Fields f ON sa.field_id = f.field_id
        JOIN Crops c ON sa.crop_id = c.crop_id
        JOIN Animals a ON sa.animal_id = a.animal_id;
        """
        results = execute_query(query)
        self.assertTrue(len(results) > 0, "No seasonal activities found")
        for season, location, crop, animal in results:
            self.assertIn(season, ['Monsoon', 'Autumn', 'Winter', 'Spring', 'Summer'])

    def test_field_usage_count(self):
        query = """
        SELECT season, COUNT(DISTINCT field_id) AS active_fields
        FROM SeasonalActivities
        GROUP BY season;
        """
        results = execute_query(query)
        self.assertTrue(len(results) > 0, "No seasonal field usage data found")
        for season, count in results:
            self.assertGreaterEqual(count, 0)

if __name__ == '__main__':
    unittest.main()
