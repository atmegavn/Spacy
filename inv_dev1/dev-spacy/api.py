import data_processing as dp
import mysql.connector
from resume_parser import resumeparse
import os
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="",
# database="resume_details"
# )

@app.route("/hello")
def hello_world():
    return "Hello, World!"

@app.route('/resumetest', methods=['GET'])
def resumetest():
    import glob
    resume_file_name = (glob.glob("resume/*"))
    return resume_file_name

if __name__ == '__main__':
   app.run(port=5000)