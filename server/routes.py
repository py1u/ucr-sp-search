from flask import render_template, request
from models import Course
from app import db
from sqlalchemy.sql.expression import func

# avoiding import circulation 
def register_routes(app, db):
    print('check db:', db)
    
    @app.route('/')
    def home():
        # Query 50 random courses
        courses = Course.query.with_entities(Course.cid).order_by(func.random()).limit(200).all()
        
        # Split courses into 5 columns, each with 10 items
        num_columns = 17
        num_items_per_column = 5
        category_col = [courses[i:i + num_items_per_column] for i in range(0, len(courses), num_items_per_column)]
        
        # Create labels for each column
        category_title = [f'SDG {i+1}' for i in range(num_columns)]
        
        # Combine labels and columns into a list of dictionaries
        category_col_with_labels = [{'label': category_title[i], 'courses': category_col[i]} for i in range(num_columns)]
        
        return render_template('index.html', category_col_with_labels=category_col_with_labels)
