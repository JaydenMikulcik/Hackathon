from flask import Flask
from flask_restful import Api, Resource 
import pandas as pd


app = Flask(__name__)
api = Api(app)



@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_schools')
def get_schools_list():
    schools = pd.read_excel("Foundational-learning-2022-formatted.xlsx")
    return 'Hello, World!'

@app.route('/schools')
def get_schools():
    schools = pd.read_excel("Foundational-learning-2022-formatted.xlsx")
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)