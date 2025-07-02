from db import db
 
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    experiences = db.relationship('UserExperience', back_populates="user", cascade="all, delete-orphan")

class UserExperience(db.Model):
    __tablename__ = 'experience'
    id = db.Column(db.Integer, primary_key = True)
    experience = db.Column(db.Integer, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", back_populates="experiences")