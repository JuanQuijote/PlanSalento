from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql

delete_business = Blueprint('delete_business', __name__, static_folder="static", template_folder="plan")

#------------------------------DELETE-USER--------------------------------------
"""
@delete_user.route('/user/delete/<id>', methods=['DELETE'])
def d_user(id):
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM users WHERE id_user = %s',(id))
    mysql.connection.commit()
    
    return jsonify({"message":"borrado"}) """


@delete_business.route('/delete/business/<id>', methods=['DELETE'])
def d_bus(id):
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM business WHERE id_business = %s',[id])
    mysql.connection.commit()
    
    return jsonify({"message":"borrado"}) 