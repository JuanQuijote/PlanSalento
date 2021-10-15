from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify
# from flask_mysqldb import MySQL
from database import mysql
from auth.auth import decode_tk 

role = Blueprint('role', __name__)

@role.route("/role", methods=["GET"])
def role_tk():
    print("Hola role")
    
    token = request.headers.get("token")
    print(token)
        #print("si hay token del cliente: ", token)
        #print("type token ==> ", type(token))
    object1 = decode_tk(token)
    print("object_tk: ",object1)
    role = object1['role']
    return str(role)