-- List all crops and their compatible animals
SELECT 
    c.name_en AS crop_name,
    c.name_bn AS crop_name_bn,
    a.name_en AS animal_name,
    a.name_bn AS animal_name_bn,
    a.notes
FROM Crops c
JOIN Animals a ON c.crop_id = a.compatible_crop_id;

-- Find compatible farming options for a specific crop (e.g., Paddy)
SELECT 
    c.name_en AS crop_name,
    a.name_en AS compatible_animal
FROM Crops c
JOIN Animals a ON c.crop_id = a.compatible_crop_id
WHERE c.name_en = 'Paddy';

-- Show all seasonal activities with compatible crop-animal pairs
SELECT 
    f.location,
    c.name_en AS crop,
    a.name_en AS animal,
    sa.season,
    sa.start_date,
    sa.end_date
FROM SeasonalActivities sa
JOIN Fields f ON sa.field_id = f.field_id
JOIN Crops c ON sa.crop_id = c.crop_id
JOIN Animals a ON sa.animal_id = a.animal_id
WHERE a.compatible_crop_id = c.crop_id;
