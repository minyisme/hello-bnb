""" Models and database function for Hello AirBnB application"""

# python std libs

# third-part libs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# connect to database here.
# replace "my_database" with the name of your database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///my_database'
db = SQLAlchemy()

# All models go here


if __name__ == "__main__":
    print "Successful Connected to database"