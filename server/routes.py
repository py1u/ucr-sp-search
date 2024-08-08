from flask import render_template, request

from models import Course


# avoiding import circulation 
def register_routes(app,db):
    
    
        