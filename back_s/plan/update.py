from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql
import os
from auth.auth import decode_tk
from werkzeug.utils import secure_filename
from datetime import datetime

update_plan = Blueprint('update_plan', __name__, static_folder="static", template_folder="plan")
UPLOAD_FOLDER_PLANS = os.path.abspath("./uploads/plans_img/")


#---------------------------UPDATE-PLAN----------------------------------------------
@update_plan.route('/update/plan/<id>', methods = ['PUT'])
def upp_plan(id):
    if request.method == 'PUT':
        
        print("1")
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM plans WHERE id_plan = %s',(id))
        dataRow = cur.fetchone()

        tittle = request.json['tittle']
        description = request.json['description']
        address = request.json['address']
        create_plan = request.json['create_plan']

        print("2")
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE plans
        SET tittle = %s,
            description = %s,
            address = %s,
            create_plan = %s
            WHERE id_plan = %s
        """, (tittle,description,address,create_plan,id))
        mysql.connection.commit()

        print("3")
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM plans WHERE id_plan = %s', (id))
        dataRow2 = cur.fetchone()

        return jsonify({"antes":dataRow, "ahora":dataRow2})

@update_plan.route('/edit/plan/img', methods=['POST'])
def up_plan():
    print("hola img edit")
    if request.method == 'POST':
        print("hola img edit2")

        if 'file' in request.files:
            print("hola img 2")
            file = request.files['file'] 

            if (file == ""):
                filename = ""
                return jsonify({"filename":filename})
            else:
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
            print("hola file img not exist")
            filename = ""       
            return jsonify({"filename":filename}) 

        else:
            print("ni idea on img")
            return jsonify({"filename": ""})

    else: print("no entro img edit")
        
        
@update_plan.route('/edit/plan/data/<id_plan>', methods=['GET','POST'])
def up_plan1(id_plan):

    print("hola data id: ", id_plan)
    if request.method == 'POST':
        print("Hola data 1")
        tittle = request.json['tittle']
        description = request.json['description']
        price = request.json['price']
        filename = request.json['filename']
        token = request.headers.get("token")
        print("si hay token del cliente: ", token)

        #decode token and get id
        object_tk = decode_tk(token)
        print("object_tk: ",object_tk)
        id_business = object_tk['id']
        print("id_business: ",id_business)
        
        #Become acive to 1-0
        if request.json['active'] == True:
            active = 1
        elif request.json['active'] == False:
            active = 0
        else:
            print("active not set")
            
        date = datetime.today().strftime('%Y-%m-%d') #str(date.today()),  datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), datetime.today().isoformat()

        print("Hola data 2")

        if filename == "":
            print("whitout file img mysql")
            cur = mysql.connection.cursor()
            cur.execute("""
            UPDATE plans
            SET tittle_p = %s,
                description_p = %s,
                price = %s,
                active = %s,
                create_p = %s
                WHERE id_plan = %s
            """, (tittle,description,price,active,date,id_plan))
            mysql.connection.commit() 
        else:
            print("with file img mysql")
            cur = mysql.connection.cursor()
            cur.execute("""
            UPDATE plans
            SET tittle_p = %s,
                description_p = %s,
                price = %s,
                active = %s,
                create_p = %s,
                img_p = %s
                WHERE id_plan = %s
            """, (tittle,description,price,active,date,filename,id_plan))
            mysql.connection.commit()

        print("Hola data 3")
        return jsonify({"file":"success"})
