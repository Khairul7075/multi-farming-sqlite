# 🌾 Multi-Farming SQLite

**Multi-Farming SQLite** is a relational database system designed to support integrated farming practices—where multiple crops and animals are cultivated together in the same field and season. Examples include growing paddy with fish or corn (*bhutta*) with ducks (*hans*). This project helps farmers and researchers plan, track, and optimize multi-farming strategies using SQLite.

---

## 🚜 Features

- Relational schema for fields, crops, animals, and seasonal activities
- Bengali-English terminology support for local farming practices
- Compatibility mapping between crops and livestock
- Seasonal planning and field utilization tracking
- Modular Python scripts for database interaction and testing

---

## 🧱 Project Structure 
multi-farming-sqlite/ ├── database/ │ ├── schema.sql │ ├── seed_data.sql │ └── queries/ │ ├── compatible_farming.sql │ └── seasonal_plan.sql ├── src/ │ ├── main.py │ ├── db_manager.py │ └── models/ │ ├── crop.py │ ├── animal.py │ └── field.py ├── tests/ │ ├── test_db.py │ └── test_queries.py ├── assets/ │ └── docs/ │ ├── schema_diagram.png │ ├── use_cases.md │ └── benali_terms.md ├── requirements.txt ├── LICENSE └── README.md


---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi-farming-sqlite.git
   cd multi-farming-sqlite'''

   
  2. Create the SQLite database:

bash
sqlite3 database/multi_farming.db < database/schema.sql
sqlite3 database/multi_farming.db < database/seed_data.sql
Install dependencies:

bash
pip install -r requirements.txt
Run the main script:

bash
python src/main.py
🧪 Testing
Run unit tests to verify database operations and query logic:

bash
python tests/test_db.py
python tests/test_queries.py
📚 Use Cases
Agricultural extension services

Local farmer cooperatives

Sustainable farming research

Educational tools for agri-tech students

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

Code

---

Let me know if you’d like help customizing the Bengali glossary or adding a visual 
