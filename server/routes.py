from flask import render_template, request
from models import Course
from app import db
from  sqlalchemy.sql.expression import func

# avoiding import circulation 
def register_routes(app,db):
    print('check db:', db)
    
    @app.route('/')
    def home():
        
        course = Course.query.with_entities(Course.cid).order_by(func.random()).limit(10).all()
        
        
        return render_template('index.html', course=course)
        
            