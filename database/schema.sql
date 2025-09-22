-- SQL script to create tables 

--Field Table 

CREATE TABLE Fields (
    field_id INTEGER PRIMARY KEY,
    location TEXT,
    area_sq_meters REAL,
    water_source TEXT
);

-- Crops Table 

CREATE TABLE Crops (
    crop_id INTEGER PRIMARY KEY,
    name_en TEXT,
    name_bn TEXT,
    water_need TEXT,
    duration_days INTEGER
);

--Animals Table 
CREATE TABLE Animals (
    animal_id INTEGER PRIMARY KEY,
    name_en TEXT,
    name_bn TEXT,
    compatible_crop_id INTEGER,
    notes TEXT,
    FOREIGN KEY (compatible_crop_id) REFERENCES Crops(crop_id)
);

-- SeasonalActivities Table 

CREATE TABLE SeasonalActivities (
    activity_id INTEGER PRIMARY KEY,
    field_id INTEGER,
    crop_id INTEGER,
    animal_id INTEGER,
    season TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (field_id) REFERENCES Fields(field_id),
    FOREIGN KEY (crop_id) REFERENCES Crops(crop_id),
    FOREIGN KEY (animal_id) REFERENCES Animals(animal_id)
);

/*Crops:

Paddy → Needs continuous water → 90 days

Bhutta (Corn) → Moderate water → 60 days

Animals:

Fish → Compatible with Paddy

Hans (Duck) → Compatible with Bhutta*/ 
