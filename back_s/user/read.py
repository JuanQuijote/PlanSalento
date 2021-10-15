#from auth.auth import decode
import base64
import json
import time
from typing import Literal
from jose import jwt
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql

read_user = Blueprint('read_user', __name__, static_folder="static", template_folder="plan")


#--------------------------READ-USER-----------------------------------------
"""
@read_user.route('/user/read/<id>')
def r_user(id):
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users WHERE id_user = %s', (id))
    dataRow = cur.fetchone()

    #------------------------SET------------------------------
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    dataSet = cur.fetchall()
    #---------------------------------------------------------
    return jsonify({"user":dataRow, "all_set":dataSet}) 

"""
@read_user.route('/read/users', methods=['GET'])
def r_user():
    token = request.headers.get("token")
    print(type(token))
    #token1 = Literal(token)
    #print(token1)
    #token1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwidGltZSI6MTYyNjAzOTc3NX0.oZnAeLm88vcta1c1cFIQ7Pqk6Olmbh0zWq0E7r-e20c"
    #if token == token1:
    #    print(True)
    parts = token.split(".")
    if len(parts) != 3:
        raise Exception("Incorrect id token format")
    payload = parts[1]
    padded = payload + "=" * (4 - len(payload) % 4)
    decoded = base64.b64decode(padded)
    print(decoded)
    #return json.loads(decoded)
    # try:
    #     result = jwt.decode(token, "secreto1", algorithms=['HS256'])
    #     print(result)
    # except:
    #     print("An exception occurred")
    # else:
    #     print("Nothing went wrong")

    #------------------------SET------------------------------
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM registro')
    dataSet = cur.fetchall()
    #---------------------------------------------------------
    print(dataSet)
    response = jsonify({"users":dataSet}) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

"""
@read_user.route('/read/user/<id>', methods=['GET'])
def r_user(id):
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM registro WHERE id = %s', (id))
    dataRow = cur.fetchone()

    return jsonify({"user":dataRow}) """
