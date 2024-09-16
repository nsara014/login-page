from flask import Flask
from user.routes import user_bp  # Import user routes from user module

app = Flask(__name__)

# Register user routes blueprint
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Expose User Service on port 5001
