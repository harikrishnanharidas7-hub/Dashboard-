# 💓 Heart Rate Dashboard (Flask)

A simple **Flask-based web dashboard** that simulates a live heart rate monitor.  
Auto-refreshes every second to display a random heart rate value and updates the status dynamically.

## 🚀 Features
- Auto-refresh every 1 second
- Displays random heart rate (55–120 BPM)
- Color-coded status:
  - 🩵 Blue = Low Heart Rate (<60 BPM)
  - ✅ Green = Normal Heart Rate (60–100 BPM)
  - 🔴 Red = High Heart Rate (>100 BPM)

## 🧩 Requirements
- Python 3.x
- Flask
- Gunicorn (for Render deployment)

Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Run Locally
```bash
python app.py
```
Then open your browser at:  
👉 **http://localhost:5000**

## ☁️ Deploy on Render
1. Push this repo to **GitHub**
2. Go to [Render.com](https://render.com)
3. Create a **New Web Service**
4. Connect your GitHub repo
5. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Deploy 🚀

## 📁 Project Structure
```
heart_rate_dashboard/
├── app.py
├── requirements.txt
├── Procfile
└── README.md
```
