"""Runs the app"""
from app import app
from config import create_tables

create_tables()

if __name__ == '__main__':
    print (app.url_map)
    app.run(debug=True)