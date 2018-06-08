"""Runs the app"""
from app.views import app
<<<<<<< HEAD
from app.users import app
=======
from config import create_tables

create_tables()
>>>>>>> b0bc8c371eb3cc4c8d8a613ec5c5e49eca35a9d8

if __name__ == '__main__':
    app.run(debug=True)