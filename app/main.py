from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS 
import time
from datetime import date
import pandas as pd
import json


load_dotenv()

app = Flask(__name__)

# app.config["DEBUG"] = True
# CORS(app, resources={r'/*': {'origins': '*', "Access-Control-Allow-Origin": "*"}})


@app.route("/", methods=["GET"])
def home():
    return {'time': time.time()}

@app.route("/options", methods=["GET"])
def options():
    args = request.args
    meal = args.get('meal')
    hall = args.get('hall')
    df = pd.read_csv(f"{meal}_{hall}_{date.today()}.csv")
    print(df.iloc[0, :])
    # json.loads(df.iloc[i, 1:].to_json())
    return {'options': [{"name": df['name'][i], "key": i, "value": df['portion'][i]} for i in range(len(df))]}


@app.route("/all", methods=["GET"])
def allData():
    args = request.args
    meal = args.get('meal')
    hall = args.get('hall')
    df = pd.read_csv(f"{meal}_{hall}_{date.today()}.csv")
    return { "data" : df }

@app.route("/specific", methods=["GET"])
def getMeal():
    args = request.args
    meal = args.get('meal')
    hall = args.get('hall')
    dish = args.get('dish')
    df = pd.read_csv(f"{meal}_{hall}_{date.today()}.csv")
    return { "data": json.loads(df[df['name'] == dish].to_json())}

@app.route("/dishPortions", methods=["GET"])
def dishPortions():
    args = request.args
    meal = args.get('meal')
    hall = args.get('hall')
    df = pd.read_csv(f"{meal}_{hall}_{date.today()}.csv")
    return { "data": [{"dish": df['name'][i], "portion": df['portion'][i]} for i in range(len(df)) ]}


    

# from flask import Flask
# from dotenv import load_dotenv
# from flask_cors import CORS 

# load_dotenv()
# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def get_current_time():
#     return {'time': time.time()}


