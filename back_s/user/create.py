from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql

create_user = Blueprint('create_user', __name__, static_folder="static", template_folder="plan")

#--------------------------CREATE-USER----------------------------------------------
"""
@create_user.route('/register', methods=['POST'])
def c_user():
    if request.method == 'POST':
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        birthday = request.json['birthday']
        email = request.json['email']
        password = request.json['password']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (first_name,last_name,birthday,email,password) VALUES (%s,%s,%s,%s,%s)',
        (first_name,last_name,birthday,email,password))
        mysql.connection.commit()
        
        return jsonify({"message":"registrado"})   """


@create_user.route('/create/user', methods=['POST'])
def c_user():
    if request.method == 'POST':
        first_name = request.json['name']
        #last_name = request.json['last_name']
        #birthday = request.json['birthday']
        email = request.json['email']
        password = request.json['password']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO registro (nombre,correo,contraseña) VALUES (%s,%s,%s)',
        (first_name,email,password))
        mysql.connection.commit()
        
        return jsonify({"message":"registrado"})  