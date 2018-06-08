"""Runs the app"""
from app.views import app
from app.users import app

if __name__ == '__main__':
    app.run(debug=True)