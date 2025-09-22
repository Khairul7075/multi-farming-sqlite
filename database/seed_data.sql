-- Insert sample fields
INSERT INTO Fields (field_id, location, area_sq_meters, water_source) VALUES
(1, 'Siliguri North', 5000, 'Canal'),
(2, 'Siliguri South', 3000, 'Rain-fed');

-- Insert sample crops
INSERT INTO Crops (crop_id, name_en, name_bn, water_need, duration_days) VALUES
(1, 'Paddy', 'ধান', 'High', 90),
(2, 'Bhutta (Corn)', 'ভুট্টা', 'Medium', 60);

-- Insert sample animals
INSERT INTO Animals (animal_id, name_en, name_bn, compatible_crop_id, notes) VALUES
(1, 'Fish', 'মাছ', 1, 'Can thrive in waterlogged paddy fields'),
(2, 'Hans (Duck)', 'হাঁস', 2, 'Feeds on pests and weeds in corn fields');

-- Insert seasonal activities
INSERT INTO SeasonalActivities (activity_id, field_id, crop_id, animal_id, season, start_date, end_date) VALUES
(1, 1, 1, 1, 'Monsoon', '2025-07-01', '2025-09-30'),
(2, 2, 2, 2, 'Autumn', '2025-10-01', '2025-11-30');
