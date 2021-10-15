from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql
from base64_img.base64_img import get_response_image;
from auth.auth import decode_tk 
import os

read_one_business = Blueprint('read_one_business', __name__, static_folder="static", template_folder="plan")

UPLOAD_FOLDER_BUSINESS = os.path.abspath("./uploads/business_img/")

@read_one_business.route('/business/read', methods=['GET'])
def r_business():

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
        #-------------------------------------------------------------
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM business WHERE id_business = %s', [id_business])
        dataRow = cur.fetchall()
        #------------------------------------------------------------
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_BUSINESS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[9])
            img_path = str(path+"/"+data[6])
            
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

            dataRow[count][6] = get_image
            count = count + 1
        
        #print("lista de img: ",encoded_images)
        ##print(type(encoded_images))
        #print(dataRow)
        return jsonify({"business_one":dataRow}) 


@read_one_business.route('/business/read/<id>', methods=['GET'])
def r_business1(id):

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
        id_business = id

        #-------------------------------------------------------------
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM business WHERE id_business = %s', [id_business])
        dataRow = cur.fetchall()
        #------------------------------------------------------------
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_BUSINESS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[9])
            img_path = str(path+"/"+data[6])
            
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

            dataRow[count][6] = get_image
            count = count + 1
        
        #print("lista de img: ",encoded_images)
        ##print(type(encoded_images))
        #print(dataRow)
        return jsonify({"business_one":dataRow}) 