from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    bio = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean)
    notes = db.relationship('Note', backref='writer', lazy='dynamic')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))
    note_body = db.Column(db.String(100))
    note_writer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.Column(db.String(255))
    date_created = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    # date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    
    