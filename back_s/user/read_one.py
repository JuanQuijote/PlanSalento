from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql

read_one = Blueprint('read_one', __name__, static_folder="static", template_folder="plan")


@read_one.route('/read/user/<id>', methods=['GET'])
def r_user(id):
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM registro WHERE id = %s', (id))
    dataRow = cur.fetchone()

    return jsonify({"user":dataRow}) 