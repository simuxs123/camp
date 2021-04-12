from . import db
class Campground(db.Model):
    __tablename__ = "Campground"
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.VARCHAR(50),nullable=False)
    description=db.Column(db.VARCHAR(200),nullable=False)
    location=db.Column(db.VARCHAR(50),nullable=False)
    price=db.Column(db.Integer,nullable=False)
    image=db.Column(db.VARCHAR(256),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'),nullable=False)