from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql

update_user = Blueprint('update_user', __name__, static_folder="static", template_folder="plan")


#---------------------------UPDATE-USER----------------------------------------------
"""
@update_user.route('/user/update/<id>', methods = ['PUT'])
def up_user(id):
    if request.method == 'PUT':
        
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE id_user = %s',(id))
        dataRow = cur.fetchone()

        first_name = request.json['first_name']
        last_name = request.json['last_name']
        birthday = request.json['birthday']
        email = request.json['email']
        password = request.json['password']

        cur = mysql.connection.cursor()
        cur.execute(""""""
        UPDATE users
        SET first_name = %s,
            last_name = %s,
            birthday = %s,
            email = %s,
            password = %s
            WHERE id_user = %s
        """""", (first_name,last_name,birthday,email,password,id))
        mysql.connection.commit()

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE id_user = %s', (id))
        dataRow2 = cur.fetchone()

        return jsonify({"antes":dataRow, "ahora":dataRow2}) """
#----------------------------------------------------------------------------------------------
@update_user.route('/update/user/<id>', methods = ['PUT'])
def up_user(id):
    if request.method == 'PUT':

        first_name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE registro
        SET nombre = %s,
            correo = %s,
            contraseña = %s
            WHERE id = %s
        """, (first_name,email,password,id))
        mysql.connection.commit()

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM registro WHERE id = %s', (id))
        dataRow2 = cur.fetchone()

        return jsonify({"users":dataRow2})