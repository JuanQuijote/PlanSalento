from auth.auth import encode_u, encode_b
from flask import Blueprint, request, jsonify
from database import mysql
login = Blueprint('login', __name__)

#----------------------------LOGIN--------------------------------------------
@login.route('/login', methods=['POST'])
def login_contact():
    
    if request.method == 'POST':
        
        print("hola login 1")
        password = request.json['password']
        email = request.json['email']
        # ------------------------------------------------------
        
        print("hola login 2")
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM business WHERE email_b=%s AND password_b=%s', (email, password))
        dataRow = cur.fetchone()
        # -----------------------------------------------------
        print("hola login 3")
        print(dataRow)
        if dataRow != ():
            token = encode_b(dataRow)
            print("hola login 4")
            
            return jsonify({"token": token})

        else:
            
            return jsonify({"token": "fail"})

@login.route('/login/admin', methods=['POST'])
def login_admin():
    
    if request.method == 'POST':
        
        print("hola login 1")
        password = request.json['password']
        email = request.json['email']
        # ------------------------------------------------------
        
        print("hola login 2")
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM users WHERE email_u=%s AND password=%s', (email, password))
        dataRow = cur.fetchone()
        # -----------------------------------------------------
        print("hola login 3")
        print(dataRow)
        if dataRow != ():
            token = encode_u(dataRow)
            print("hola login 4")
            
            return jsonify({"token": token})

        else:
            
            return jsonify({"token": "fail"})
