from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps from Flask!"

if __name__ == '__main__':
    # Important: host='0.0.0.0' to work inside Docker
    app.run(host='0.0.0.0', port=5000)

