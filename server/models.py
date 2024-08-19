from app import db

class Course(db.Model):
    
    # relation named course
    __tablename__ = 'course'
    
    
    # 6 primary columns from 2021-2024 course catalogue
    cid = db.Column("course_id", db.String(50), nullable=False , primary_key=True)
    level = db.Column("class_level", db.String(50), nullable=False)
    college = db.Column("college", db.Text, nullable=False)
    
    dept = db.Column("department", db.Text, nullable=False)
    course_title = db.Column("course_title", db.String(50), nullable=False)
    course_desc = db.Column("description", db.Text, nullable=False, index=True)
    
    #unique 
    sgd = db.Column("sgd", db.String)
    
    
    # get a list for the sdgs
    
    def sgd_list(self):
        if self.sgd:
            return list(map(int, self.sgd.split(',')))
        return []
    
    # setter for sgd string type field from list
    def sgd_list(self, values):
        self.sgd = ','.join(map(str, values))
    
    # returning data as string per row
    def __repr__(self):
        return f"{self.cid} {self.college}"