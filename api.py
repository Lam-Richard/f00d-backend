from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS 
import time
from datetime import date
import pandas as pd


load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/", methods=["GET"])
def home():
    return {'time': time.time()}

@app.route("/options", methods=["GET"])
def options():
    args = request.args
    meal = args.get('meal')
    hall = args.get('hall')
    df = pd.read_csv(f"{meal}_{hall}_{date.today()}.csv")
    return {'options': [{df['name'][i]: df['name'][i]} for i in range(len(df))]}

if __name__ == '__main__':
    app.run(host="http://0.0.0.0:5000")
    

# from flask import Flask
# from dotenv import load_dotenv
# from flask_cors import CORS 

# load_dotenv()
# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def get_current_time():
#     return {'time': time.time()}


