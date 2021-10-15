from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
from database import mysql
from auth.auth import encode_b
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER_BUSINESS = os.path.abspath("./uploads/business_img/")

create_business = Blueprint('create_business', __name__, static_folder="static", template_folder="plan")

#--------------------------CREATE-USER----------------------------------------------

@create_business.route('/create/business/img', methods=['GET','POST'])
def c_business():
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
            file.save(os.path.join(UPLOAD_FOLDER_BUSINESS, filename))
            print("hola img 6")       

            return jsonify({"filename":filename}) 

        elif 'file' not in request.files:
            filename = "2021-07-03(1).png"       
 
            return jsonify({"filename":filename}) 
        else:
            return jsonify({"file": "error"})
        
        
@create_business.route('/create/business/data', methods=['GET','POST'])
def c_business1():
    print("hola data")
    if request.method == 'POST':
        print("Hola data 1")
        name = request.json['name']
        description = request.json['description']
        address = request.json['address']
        email = request.json['email']
        category = request.json['category']
        nit = request.json['nit']
        password = request.json['password'] 
        filename = request.json['filename']
        map = request.json['map']

        if request.json['facebook']:
            facebook = request.json['facebook']
        else:
            facebook = "Null"

        if request.json['instagram']:  
            instagram = request.json['instagram']
        else:
            instagram = "Null"

        if request.json['whatsapp']:
            whatsapp = request.json['whatsapp']
        else:
            whatsapp = "Null"


        list_map = map.split('"')
        map = list_map[1]
        print(map)
        print("filename: ", filename)

        print("Hola data 2")
        cur = mysql.connection.cursor()
        print("Hola data 2.5")
        cur.execute('INSERT INTO business (name_b,nit,description_b,category,address,img_b,email_b,password_b,embed_map,facebook,instagram,whatsapp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (name,nit,description,category,address,filename,email,password,map,facebook,instagram,whatsapp))
        mysql.connection.commit()
               
        print("Hola data 3")

        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM business WHERE email_b=%s AND password_b=%s', (email, password))
        dataRow = cur.fetchone()
        print("Hola data 4")

        print(dataRow)
        if dataRow:
            token = encode_b(dataRow)
            print("Hola data 5")
            
            return jsonify({"token": token})

        

      

         



        

