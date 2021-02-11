# virtual_environment_name\Scripts\activate.bat is the file that activates the virutal environment
# api_env\Scripts\activate.bat

# how and where to run its information
# importing app = Flask(__name__) from init file
from cars_api import app, routes

# DO I NEED TO import APP?

# when we deploy we will turn this to false
# main is refers to the main python program
# special method
if __name__ == '__main__':
    app.run(debug=True)
