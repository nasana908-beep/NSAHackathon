# NSAHackathon
Chiya Overflow - NSA Hackathon Project


# NSAHackathon
Chiya Overflow - NSA Hackathon Project

# NSAHackathon - Smart Trek Planner Backend

Backend service for our Hackathon project **Smart Trek Planner**.  
Built with **FastAPI + SQLite**, it provides trekking routes, safety assessments, recommendations, and nearby places of interest.

---

## 🚀 Getting Started

1. Clone the repository
```bash
git clone https://github.com/nasana908-beep/NSAHackathon.git
cd NSAHackathon

2. Create & activate virtual environment
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# CMD
.venv\Scripts\activate.bat
# Mac/Linux
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the backend server
uvicorn app.main:app --reload

The server will start at:
👉 http://127.0.0.1:8000

Interactive API docs:
👉 http://127.0.0.1:8000/docs
