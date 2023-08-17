from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    # Define customer model here

class Transaction(db.Model):
    # Define transaction model here
