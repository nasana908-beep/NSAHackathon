# NSAHackathon
Chiya Overflow
🏔️ Smart Trek Planner (NSAHackathon Project)
📌 Project Overview

Smart Trek Planner is a web-based application designed to assist mountaineers and trekkers in planning safe and efficient expeditions.
It integrates:

Trekking data (routes, altitude, difficulty, duration, best seasons)

Safety risk assessments (avalanche, blizzard, landslide risks by coordinates)

Guide and lodging recommendations

An AI-powered chatbot to answer trek-related queries

The project was developed as part of the NSAHackathon to demonstrate how AI + geospatial data can improve mountaineering safety and accessibility.



⚙️ Setup and Run Instructions
1. Clone the repo - bash
git clone https://github.com/nasana908-beep/NSAHackathon.git
cd NSAHackathon

2. Create a virtual environment - bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3. Install dependencies - bash
pip install -r requirements.txt

4. Run backend locally - bash
uvicorn app.main:app --reload


App will be available at: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

5. Hosted Deployment

The project is also deployed on Render:
👉 Live API: https://nsahackathon-3ai2.onrender.com

👉 Swagger Docs: https://nsahackathon-3ai2.onrender.com/docs


🛠 Dependencies and Tools Used

FastAPI → API framework
Uvicorn → ASGI server
SQLite3 → local database for storing risk assessments
RapidFuzz → text search for places
Streamlit → chatbot frontend (prototype)
Render → hosting
Python 3.11/3.12/3.13 (tested on 3.13)

📡 API Endpoints (summary)

GET / → Health check
GET /treks → List all treks
GET /treks/{id} → Get trek by ID
GET /treks/{id}/plan → Get trek + guides + lodging
POST /recommendations → Get trek recommendations
POST /chat → Ask chatbot about treks
POST /risk/assess → Assess risk for lat/lon/elevation
GET /risk/history → Show assessment history
GET /places/nearby → Nearby places search
GET /places/search → Text search for places
(Full interactive docs at /docs)

👥 Team Members and Roles

Shreeyut Karmacharya → Backend development

Rehash Adhikari → Backend development
Nasna Bajracharya → UI_UX/Front End Dev
Medhavi Pandit → Product Owner
Spriha Paudel → Program Manager

