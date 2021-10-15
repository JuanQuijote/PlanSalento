from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql
import os
from auth.auth import decode_tk

UPLOAD_FOLDER_BUSINESS = os.path.abspath("./uploads/business_img/")

update_business = Blueprint('update_business', __name__, static_folder="static", template_folder="plan")


#---------------------------UPDATE-USER----------------------------------------------

@update_business.route('/edit/business/img', methods=['POST'])
def up_business():
    print("hola img")
    if request.method == 'POST':

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
                file.save(os.path.join(UPLOAD_FOLDER_BUSINESS, filename))
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
        
        
@update_business.route('/edit/business/data', methods=['GET','POST'])
def up_business1():
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

        if request.headers.get("token1"):
            id_business = request.headers.get("token1")
        else:
            #decode token and get id_business
            token = request.headers.get("token")
            object_tk = decode_tk(token)
            print("object_tk: ",object_tk)
            id_business = object_tk['id']
            print("id_business: ",id_business)

        #Split "embed map" and get url
        try:
            embed_map = request.json['map']
            list_map = embed_map.split('"')
            map = list_map[1]
            print(map)
        except:
            map = request.json['map']

        print("Hola data 2")
        
        if filename == "":
            print("whitout file img mysql")
            cur = mysql.connection.cursor()
            cur.execute("""
            UPDATE business
            SET name_b = %s,
                nit = %s, 
                description_b = %s,
                category = %s,
                address = %s,
                email_b = %s,
                password_b = %s,
                embed_map = %s
                WHERE id_business = %s
            """, (name,nit,description,category,address,email,
            password,map,id_business))
            mysql.connection.commit() 
        else:
            print("with file img mysql")
            cur = mysql.connection.cursor()
            cur.execute("""
            UPDATE business
            SET name_b = %s,
                nit = %s, 
                description_b = %s,
                category = %s,
                address = %s,
                email_b = %s,
                password_b = %s,
                embed_map = %s,
                img_b = %s
                WHERE id_business = %s
            """, (name,nit,description,category,address,email,
            password,embed_map,filename,id_business)) 
            mysql.connection.commit()

        print("Hola data 3")
        return jsonify({"file":"success"})

        

      

         



