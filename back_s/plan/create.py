from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
from database import mysql
import os
from auth.auth import decode_tk
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOAD_FOLDER_PLANS = os.path.abspath("./uploads/plans_img/")

create_plan = Blueprint('create_plan', __name__, static_folder="static", template_folder="plan")


#--------------------------CREATE-PLAN----------------------------------------------

@create_plan.route('/create/plan/img', methods=['GET','POST'])
def c_plan():
    print("hola img")
    if request.method == 'POST':

        if 'file' in request.files:
            print("hola img 2")
            file = request.files['file'] 
            print("hola img 3")
            filename = file.filename       
            #file.content_type   # Gives Content type text/html etc
            #print(file.size)
            print("hola img 4")
            
            #print(name,nit,description,category,address,"this: ",type(file) ,email,password)
            print(type(file))
            print("hola img 5")
            file.save(os.path.join(UPLOAD_FOLDER_PLANS, filename))
            print("hola img 6")       

            return jsonify({"filename":filename}) 

        elif 'file' not in request.files:
            filename = "2021-07-03(1).png"       
 
            return jsonify({"filename":filename}) 
        else:
            return jsonify({"file": "error"})
        
        
@create_plan.route('/create/plan/data', methods=['GET','POST'])
def c_plan1():
    print("hola data")
    if request.method == 'POST':
        print("Hola data 1")
        tittle = request.json['tittle']
        description = request.json['description']
        price = request.json['price']
        filename = request.json['filename']
        token = request.headers.get("token")
        #token = request.json['token']
        print("si hay token del cliente: ", token)

        object_tk = decode_tk(token)
        print("object_tk: ",object_tk)
        id_business = object_tk['id']
        print("id_business: ",id_business)
        

        if request.json['active'] == True:
            active = 1
        elif request.json['active'] == False:
            active = 0
        else:
            print("active not set")
            
        date = datetime.today().strftime('%Y-%m-%d') #str(date.today()),  datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), datetime.today().isoformat()

        print("Hola data 2")
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute('INSERT INTO plans (id_business,tittle_p,description_p,price,active,create_p,img_p) VALUES (%s,%s,%s,%s,%s,%s,%s)',
        (id_business,tittle,description,price,active,date,filename))
        mysql.connection.commit()         
        print("Hola data 3")
        return jsonify({"file":"success"})




