from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
#rom flask.helpers import send_from_directory 
from database import mysql
import os
from base64_img.base64_img import get_response_image;
from auth.auth import decode_tk 

read_one_plan = Blueprint('read_one_plan', __name__, static_folder="static", template_folder="plan")

#UPLOAD_FOLDER_PLANS = os.path.abspath("./uploads/plans_img/")
UPLOAD_FOLDER_PLANS = os.path.abspath("./uploads/plans_img/")
#UPLOAD_FOLDER_BUSINESS = "D:/my-proyect/back_s/uploads/business_img"

@read_one_plan.route('/plan/read', methods=['GET'])
def r_plan_one():

    print("hola data")
    if request.method == 'GET':
        print("Hola data 1")
        token = request.headers.get("token")
        print("si hay token del cliente: ", token)
        print("type token ==> ", type(token))
        object_tk = decode_tk(token)
        print("object_tk: ",object_tk)
        id_business = object_tk['id']
        print("id_business: ",id_business)
        print(type(id_business))
        #id_business = str(id_business)
            
        #------------------------------------------------------------------------------
        print("Hola data 2")
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute('SELECT * FROM plans WHERE id_business = %s', [id_business])
        dataRow = cur.fetchall()
        #-----------------------------------------------------------------------------

        print("Hola data 3")
        print(dataRow)
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_PLANS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[9])
            img_path = str(path+"/"+data[7])
            
            paths.append(img_path)

        #print("UPLOAD_FOLDER_PLANS: ", UPLOAD_FOLDER_PLANS)

        print("lista de rutas: ",paths)
        
        ##reuslt  contains list of path images
        #result = get_images_from_local_storage()
        ##encoded_images = []
        count = 0
        for image_path in paths:
            ##encoded_images.append(get_response_image(image_path))
            print(image_path)
            print(type(image_path))
            #image_path = "D:/my-proyect/back_s/uploads/plans_img\2021-07-03(1).png"
            get_image = get_response_image(image_path)
            
            dataRow[count] = list(dataRow[count])
            print("list of list",type(dataRow[count]))

            dataRow[count][7] = get_image
            count = count + 1
        
        #print("lista de img: ",encoded_images)
        ##print(type(encoded_images))
        #print(dataRow)
        return jsonify({"plans":dataRow}) 


@read_one_plan.route('/plan/read/<id_plan>', methods=['GET'])
def r_plan_one_id_1(id_plan):

    print("hola data")
    if request.method == 'GET':
        print("Hola data 1")
        token = request.headers.get("token")
        #print("si hay token del cliente: ", token)
        #print("type token ==> ", type(token))
        object_tk = decode_tk(token)
        print("object_tk: ",object_tk)
        #id_business = object_tk['id']
        #print("id_business: ",id_business)
        #print(type(id_business))
        #id_plan = id_plan
        print("id_plan: ", id_plan)
        #id_business = id_business
        #print("id_business: ", id_business)
        #id_business = str(id_business)
            
        #------------------------------------------------------------------------------
        print("Hola data 2")
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute('SELECT * FROM plans WHERE id_plan = %s', [id_plan])
        dataRow = cur.fetchone()
        #-----------------------------------------------------------------------------
        
        print("Hola data 3")
        #print(dataRow)
        
        return jsonify({"plans":dataRow})


@read_one_plan.route('/plan/read/<id_plan>/<id_business>', methods=['GET'])
def r_plan_one_id_2(id_plan, id_business):

    print("hola data")
    if request.method == 'GET':
        #print("Hola data 1")
        #token = request.headers.get("token")
        #print("si hay token del cliente: ", token)
        #print("type token ==> ", type(token))
        #object_tk = decode_tk(token)
        #print("object_tk: ",object_tk)
        #id_business = object_tk['id']
        #print("id_business: ",id_business)
        #print(type(id_business))
        #id_plan = id_plan
        print("id_plan: ", id_plan)
        #id_business = id_business
        print("id_business: ", id_business)
        #id_business = str(id_business)
            
        #------------------------------------------------------------------------------
        print("Hola data 2")
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute('SELECT * FROM plans WHERE id_business = %s AND id_plan = %s', (id_business, id_plan))
        dataRow = cur.fetchall()
        #-----------------------------------------------------------------------------
        
        print("Hola data 3")
        print(dataRow)
        #print(type(dataRow))
        dataRow = list(dataRow)
        #print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_PLANS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[9])
            img_path = str(path+"/"+data[7])
            
            paths.append(img_path)

        #print("UPLOAD_FOLDER_PLANS: ", UPLOAD_FOLDER_PLANS)

        print("lista de rutas: ",paths)
        
        ##reuslt  contains list of path images
        #result = get_images_from_local_storage()
        ##encoded_images = []
        count = 0
        for image_path in paths:
            ##encoded_images.append(get_response_image(image_path))
            #print(image_path)
            #print(type(image_path))
            #image_path = "D:/my-proyect/back_s/uploads/plans_img\2021-07-03(1).png"
            get_image = get_response_image(image_path)
            
            dataRow[count] = list(dataRow[count])
            #print("list of list",dataRow[count])

            dataRow[count][7] = get_image
            count = count + 1
        
        #print("lista de img: ",encoded_images)
        ##print(type(encoded_images))
        #print(dataRow)
        return jsonify({"plans":dataRow})
    
    

     