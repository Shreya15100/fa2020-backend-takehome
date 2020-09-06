from flask import Flask, jsonify
import random
import csv
import pandas as pd
import json
import jsonpickle
from json import JSONEncoder
with open('data.csv') as csvfile:
     csv_reader= csv.reader(csvfile, delimiter=',')
app = Flask(__name__)
def make_json(csvFilePath, jsonFilePath):  
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for rows in csvReader: 
            key = rows['id'] 
            data[key] = rows 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonf.write(json.dumps(data, indent=4)) 
csvFilePath = r'data.csv'
jsonFilePath = r'employee.json'
make_json(csvFilePath, jsonFilePath)
with open('employee.json') as f:
     json_reader= json.load(f)
range =(1,99)
for rows in range:
    data={}
    key = rows[1]
    data[key]=rows
    @app.route('/')
    def redirect_to_api():
        return data
app.run(host="localhost", port=8000)

"""

TASK

Implement an endpoint `/api/fetch` that returns the contents of `data.csv` as JSON

1) Load/transcribe `data.csv`
2) Save each entry's full name, time zone, and department
3) Return the JSON data at the endpoint

"""


"""

DOCUMENTATION WEBPAGE BELOW

"""

"""
        <style>
            body {
                font-family: sans-serif;
                max-width: 900px;
                width: 90%;
                margin: 0 auto 0 auto;
                padding: 5vh 30px 0 30px;
                background: rgb(240,240,240);
            }

            pre, code {
                background: #121212;
                color: white;
            }

            code {
                padding: 4px;
            }

            pre code {
                padding: 0;
            }

            pre {
                padding: 10px;
            }

            hr {
                margin: 2em 0;
            }
        </style>
        <h1>Founders Fall 2020 Backend Take-Home API</h1>
        <p>Add the endpoint <code>`/api/fetch`</code> accessible via a GET request which returns the list of employees from <code>`data.csv`</code> as JSON.</p><hr />
        <h2>API (to be implemented)</h2>
        <h4>Request</h4>
<pre><code><b>GET</b>
Scheme: http
Filename: /api/fetch</code></pre>
        <h4>Response</h4>
<pre><code>employees: [
            <br />  {
            <br />      name: <i>FULL NAME OF EMPLOYEE</i>,
            <br />      timezone: <i>TIMEZONE</i>,
            <br />      dept: <i>EMPLOYEE'S DEPARTMENT</i>,
            <br />  }
            <br />  ...
        <br />]</code></pre>"""
