# app.py
from flask import Flask
from user.routes import user_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user_bp)

@app.route('/')
def ping_server():
    return "Welcome to the login page"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
