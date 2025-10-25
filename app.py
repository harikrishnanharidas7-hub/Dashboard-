from flask import Flask, render_template_string
import random, time

app = Flask(__name__)

# Simple HTML template with auto-refresh
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="1"> <!-- refresh every 1s -->
    <title>Heart Rate Dashboard</title>
    <style>
        body { font-family: Arial; text-align: center; background-color: #fdf6f6; }
        h1 { color: #d62828; }
        .rate { font-size: 48px; color: {{ color }}; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>💓 Heart Rate Monitor</h1>
    <div class="rate">{{ heart_rate }} BPM</div>
    <h2>{{ status }}</h2>
</body>
</html>
"""

@app.route('/')
def index():
    heart_rate = random.randint(55, 120)

    if heart_rate < 60:
        status = "⚠️ Low Heart Rate"
        color = "blue"
    elif heart_rate > 100:
        status = "🚨 High Heart Rate"
        color = "red"
    else:
        status = "✅ Normal Heart Rate"
        color = "green"

    return render_template_string(TEMPLATE, heart_rate=heart_rate, status=status, color=color)

if __name__ == "__main__":
    # For local development only; Render uses Gunicorn to start the app
    app.run(host="0.0.0.0", port=5000)
