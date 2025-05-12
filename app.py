from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to DevOps!"

if __name__ == '__main__':
    # استخدم المنفذ الذي توفره Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

