from cars_api import app
from flask import render_template

# @ is a decorator so we need a function to go along with it
# decorator tells function below what url route is specified
# / referes to home route

# Home Route - aka main landing page
# url has to be string

# @app.route is used to map a url to the return of a function ('/' is local machine address)
# decorator tells the functions what url to direct return to!


@app.route('/')
def hello_world():
    return render_template('home.html')
