# NSAHackathon
Chiya Overflow - NSA Hackathon Project

# Smart Trek Planner - Backend

Backend service for our Hackathon project **Smart Trek Planner**.  
Built with **FastAPI + SQLite**, it provides trekking routes, safety assessments, recommendations, and nearby places of interest.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/nasana908-beep/NSAHackathon.git
cd NSAHackathon


python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# CMD
.venv\Scripts\activate.bat
# Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
