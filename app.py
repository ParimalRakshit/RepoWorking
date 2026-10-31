from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Flask app is running on EC2 via Docker!"

if __name__ == '__main__':
    # Crucial: host must be 0.0.0.0 to be accessible outside the container
    app.run(host='0.0.0.0', port=5000) 
