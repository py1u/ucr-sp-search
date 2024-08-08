import csv
from app import create_app, db
from models import Course

app = create_app()


# populate the instance/testdb.db
def populate_database():
    
    with open('course.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            course = Course(
                cid=row['course_id'],
                level=row['level'],
                college=row['college_desc'],
                dept=row['department_desc'],
                course_title=row['title_long_desc'],
                course_desc=row['course_text_narrative'],
                sgd=row['sgd']  
            )

            db.session.add(course)
            
           
            db.session.commit()
    
    

if __name__ == '__main__':
    with app.app_context():
        populate_database()
