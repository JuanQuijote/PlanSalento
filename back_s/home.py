from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify
# from flask_mysqldb import MySQL
from database import mysql

home = Blueprint('home', __name__)


# ------------------------------HOME-----------------------------------------
@home.route('/', methods=['GET'])
@home.route('/home', methods=['GET'])
@home.route('/home/user/<id>', methods=['GET'])
def index(id):
    
    if id:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM plans WHERE id_plan = %s', (id))
        dataRow = cur.fetchall()
        return jsonify({"plans_user":dataRow}) 
    else: 
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM plans')
        dataSet = cur.fetchall()
        return jsonify({"all_set": dataSet})