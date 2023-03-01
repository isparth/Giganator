from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    is_organiser = db.Column(db.Boolean)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))
    tickets = db.relationship("Ticket",backref = "user")

    def __init__(self, first_name , last_name, Email, password_hash, is_organiser,event_id):
        self.first_name = first_name
        self.last_name = last_name
        self.Email = Email
        self.password_hash = password_hash
        self.is_organiser = is_organiser
        self.event_id = event_id

class Event(db.Model):
    _tablename_ ="events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date = db.Column(db.Text)
    time = db.Column(db.Text)
    duration = db.Column(db.Text)
    capacity = db.Column(db.Integer)
    location = db.Column(db.Text)
    organiser = db.Column(db.String)
    imgLink = db.Column(db.String)
    users = db.relationship("User",backref = "event")

    def __init__(self, name , date, time, duration, capacity, location, organiser):
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.capacity = capacity
        self.location = location
        self.organiser = organiser


   
class Ticket(db.Model):
    _tablename_ ="tickets"
    id = db.Column(db.Integer, primary_key=True)
    eventId = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    barcode = db.Colun(db.String)

   

    def __init__(self, eventId, user_id, barcode):
        self.eventId = eventId
        self.user_id = user_id
        self.barcode = barcode


    