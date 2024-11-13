from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(228), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Admin, Manager, User


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)  # Foreign key to Branch

    event = db.relationship('Event', backref=db.backref('participants', lazy=True))
    branch = db.relationship('Branch', backref=db.backref('participants', lazy=True))

    def __repr__(self):
        return f'<Participant {self.name} - Branch: {self.branch.name}>'


    def __repr__(self):
        return f'<Participant {self.name} - Event ID: {self.event_id}>'
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "event_id": self.event_id,
            "branch_id":self.branch_id
        }

class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)

    # Relationship with Branch
    branch = db.relationship('Branch', backref=db.backref('birthdays', lazy=True))

    def __repr__(self):
        return f'<Birthday {self.date} {self.name} - Branch: {self.branch.city}>'


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), nullable=False)
    event_description = db.Column(db.String(80), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
    google_form_link = db.Column(db.String(255), nullable=True)  # שדה חדש לקישור Google Form

    branch = db.relationship('Branch', backref=db.backref('events', lazy=True))

    def __repr__(self):
        return f'<Event {self.date} {self.event_description} - Branch: {self.branch.city}>'


class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False, unique=True)
    address = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Branch {self.city} - {self.address}>'
