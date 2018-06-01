import os
from flask import Flask
from app import views

# config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)