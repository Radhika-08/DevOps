from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": os.getenv("APP_NAME"),
        "environment": os.getenv("ENVIRONMENT"),
        "status": "Running Successfully"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)