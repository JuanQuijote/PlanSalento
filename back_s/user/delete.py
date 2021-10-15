from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql

delete_user = Blueprint('delete_user', __name__, static_folder="static", template_folder="plan")

#------------------------------DELETE-USER--------------------------------------
"""
@delete_user.route('/user/delete/<id>', methods=['DELETE'])
def d_user(id):
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM users WHERE id_user = %s',(id))
    mysql.connection.commit()
    
    return jsonify({"message":"borrado"}) """


@delete_user.route('/delete/user/<id>', methods=['DELETE'])
def d_user(id):
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM registro WHERE id = %s',(id))
    mysql.connection.commit()
    
    return jsonify({"message":"borrado"}) 