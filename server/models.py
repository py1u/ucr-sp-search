from app import db

class Course(db.Model):
    
    # relation named course
    __tablename__ = 'course'
    
    
    # 6 primary columns from 2021-2024 course catalogue
    cid = db.Column(db.String, nullable=False , primary_key=True)
    level = db.Column(db.String, nullable=False)
    college = db.Column(db.Text, nullable=False)
    
    