JSON to MongoDB Ingestion
==========================

A simple Python project that reads a JSON file, processes the data, and sends it to a MongoDB database.

How to Use
----------

1. Install dependencies:
   pip install -r requirements.txt

2. Start MongoDB (locally)

3. Run the script:
   cd ingest
   python send_to_mongo.py

Data Structure
--------------

Example of a JSON object:

{
  "name": "Mario Super",
  "email": "mario.super@example.com",
  "age": 24
}

Project Structure
-----------------

json-to-mongo-ingestion/
├── data/
│   └── sample_data.json
├── ingest/
│   ├── parse_json.py
│   └── send_to_mongo.py
├── requirements.txt
└── README.txt

Requirements
------------

- Python 3.x
- MongoDB (running locally)
