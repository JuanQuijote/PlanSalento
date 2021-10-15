from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql

delete_plan = Blueprint('delete_plan', __name__, static_folder="static", template_folder="plan")

#------------------------------DELETE-PLAN--------------------------------------
@delete_plan.route('/delete/plan/<id>', methods=['DELETE'])
def d_plan(id):

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM plans WHERE id_plan = %s',[id])
    mysql.connection.commit()
    
    return jsonify({"message":"borrado"}) 


@delete_plan.route('/delete/plans/<id>', methods=['DELETE'])
def d_plans(id):

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM plans WHERE id_business = %s',[id])
    mysql.connection.commit()
    
    return jsonify({"message":"borrado"}) 