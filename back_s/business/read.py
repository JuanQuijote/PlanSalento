#from auth.auth import decode
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify
from database import mysql
from base64_img.base64_img import get_response_image;
from auth.auth import decode_tk 
import os

UPLOAD_FOLDER_BUSINESS = os.path.abspath("./uploads/business_img/")

read_business = Blueprint('read_business', __name__, static_folder="static", template_folder="plan")


#--------------------------READ-USER-----------------------------------------

@read_business.route('/read/business', methods=['POST'])
def r_business2():

    if request.method == 'POST':
        print("read 1")
        print("name ", type(request.json['name']))
        print("email ", type(request.json['email']))
        if request.json['name'] != "" and request.json['email'] != "":
            print("read 2")
            name_b = request.json['name']
            email_b = request.json['email']

            #----------------------------------------------------------------
            cur = mysql.connection.cursor()
            print("Hola MySQl")
            cur.execute( '''SELECT *
                            FROM business 
                            WHERE name_b = %s and email_b = %s''',(name_b, email_b))
            dataRow = cur.fetchall()
            print("Hola data 3")
            #----------------------------------------------------------------

            print(dataRow)
            print(type(dataRow))
            dataRow = list(dataRow)
            print(type(dataRow))

            paths = []
            path = UPLOAD_FOLDER_BUSINESS

            for data in dataRow:
                img_path = str(path+"/"+data[6])
                paths.append(img_path)

            print("lista de rutas: ",paths) 
            
            count = 0

            for image_path in paths:
                get_image = get_response_image(image_path)
                dataRow[count] = list(dataRow[count])
                dataRow[count][6] = get_image 
                count = count + 1
            
            return jsonify({"business_all":dataRow})
    

        elif request.json['name'] != "":
            name_b = request.json['name']

            #----------------------------------------------------------------
            cur = mysql.connection.cursor()
            print("Hola MySQl")
            cur.execute( '''SELECT *
                            FROM business 
                            WHERE name_b = %s''', [name_b])
            dataRow = cur.fetchall()
            print("Hola data 3")
            #----------------------------------------------------------------

            print(dataRow)
            print(type(dataRow))
            dataRow = list(dataRow)
            print(type(dataRow))

            paths = []
            path = UPLOAD_FOLDER_BUSINESS

            for data in dataRow:
                img_path = str(path+"/"+data[6])
                paths.append(img_path)

            print("lista de rutas: ",paths) 
            
            count = 0

            for image_path in paths:
                get_image = get_response_image(image_path)
                dataRow[count] = list(dataRow[count])
                dataRow[count][6] = get_image 
                count = count + 1
            
            return jsonify({"business_all":dataRow})
    
        elif request.json['email'] != "":
            
            email_b = request.json['email']

            #----------------------------------------------------------------
            cur = mysql.connection.cursor()
            print("Hola MySQl")
            cur.execute( '''SELECT *
                            FROM business 
                            WHERE email_b = %s''', [email_b])
            dataRow = cur.fetchall()
            print("Hola data 3")
            #----------------------------------------------------------------

            print(dataRow)
            print(type(dataRow))
            dataRow = list(dataRow)
            print(type(dataRow))

            paths = []
            path = UPLOAD_FOLDER_BUSINESS

            for data in dataRow:
                img_path = str(path+"/"+data[6])
                paths.append(img_path)

            print("lista de rutas: ",paths) 
            
            count = 0

            for image_path in paths:
                get_image = get_response_image(image_path)
                dataRow[count] = list(dataRow[count])
                dataRow[count][6] = get_image 
                count = count + 1
            
            return jsonify({"business_all":dataRow})
        else:

            #----------------------------------------------------------------
            return jsonify({"business_all":[]})



@read_business.route('/read/business/all', methods=['GET'])
def r_business3():
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute( '''SELECT *
                        FROM business''')
        dataRow = cur.fetchall()
        print("Hola data 3")
        #----------------------------------------------------------------

        print(dataRow)
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_BUSINESS

        for data in dataRow:
            img_path = str(path+"/"+data[6])
            paths.append(img_path)

        print("lista de rutas: ",paths) 
        
        count = 0

        for image_path in paths:
            get_image = get_response_image(image_path)
            dataRow[count] = list(dataRow[count])
            dataRow[count][6] = get_image 
            count = count + 1
        
        return jsonify({"business_all":dataRow}) 


