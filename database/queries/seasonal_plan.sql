/*Your seasonal_plan.sql file should contain SQL 
queries that help analyze and plan farming activities across different seasons.
These queries will pull data from your SeasonalActivities, Fields, Crops, and Animals tables
to show what’s being farmed, where, and when.*/ 

-- Show all seasonal farming plans with field, crop, and animal details
SELECT 
    sa.season,
    f.location AS field_location,
    c.name_en AS crop,
    a.name_en AS animal,
    sa.start_date,
    sa.end_date
FROM SeasonalActivities sa
JOIN Fields f ON sa.field_id = f.field_id
JOIN Crops c ON sa.crop_id = c.crop_id
JOIN Animals a ON sa.animal_id = a.animal_id
ORDER BY sa.start_date;

-- List all activities planned for a specific season (e.g., Monsoon)
SELECT 
    f.location,
    c.name_en AS crop,
    a.name_en AS animal,
    sa.start_date,
    sa.end_date
FROM SeasonalActivities sa
JOIN Fields f ON sa.field_id = f.field_id
JOIN Crops c ON sa.crop_id = c.crop_id
JOIN Animals a ON sa.animal_id = a.animal_id
WHERE sa.season = 'Monsoon';

-- Count how many fields are active in each season
SELECT 
    season,
    COUNT(DISTINCT field_id) AS active_fields
FROM SeasonalActivities
GROUP BY season;

