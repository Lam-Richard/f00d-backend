from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS 
import time
from datetime import date
import pandas as pd
import json


load_dotenv()

app = Flask(__name__)

app.config["DEBUG"] = True
CORS(app, resources={r'/*': {'origins': '*', "Access-Control-Allow-Origin": "*"}})
# CORS(app)

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
    return { "data" : json.loads(df.to_json()) }

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

# @app.route("/nutrients", methods=["GET"])
# def nutrients():
#     args = request.args
#     meal = args.get('meal')
#     hall = args.get('hall')
#     df = pd.read_csv(f"{meal}_{hall}_{date.today()}.csv")
#     print("HELLO!?!?!")
#     return { "data": json.loads(df.iloc[0, :]['nutrients'].to_json()) }

if __name__ == '__main__':
    app.run(host='0.0.0.0')

