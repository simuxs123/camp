from . import db

class User(db.Model):
    __tablename__="User"
    id=db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.VARCHAR(50),nullable=False)
    last_name = db.Column(db.VARCHAR(50), nullable=False)
    email=db.Column(db.VARCHAR(50), nullable=False,unique=True)
    password=db.Column(db.VARCHAR(50), nullable=False)
    campground=db.relationship("Campground",backref='User',lazy=True)