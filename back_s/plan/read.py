from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, jsonify 
from database import mysql
import os
from base64_img.base64_img import get_response_image;
from auth.auth import decode_tk 

read_plan = Blueprint('read_plan', __name__, static_folder="static", template_folder="plan")
UPLOAD_FOLDER_PLANS = os.path.abspath("./uploads/plans_img/")
#UPLOAD_FOLDER_PLANS = "D:\my-proyect\back_s\uploads\plans_img"

#--------------------------READ-PLAN-----------------------------------------
@read_plan.route('/plans/read', methods=['GET'])
def r_plans():

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
        #id_business = str(id_business)
        print("Hola data 2")

        #-----------------------------------------------------------
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute('SELECT * FROM plans WHERE active = 1 ORDER BY create_p DESC')
        dataRow = cur.fetchall()
        print("Hola data 3")
        #------------------------------------------------------------

        print(dataRow)
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_PLANS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[7])
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

@read_plan.route('/plans/read/<id>', methods=['GET'])
def r_plans_id(id):

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
        #id_business = str(id_business)
        print("Hola data 2")

        #-----------------------------------------------------------
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute('SELECT * FROM plans WHERE id_business = %s ORDER BY create_p DESC',[id])
        dataRow = cur.fetchall()
        print("Hola data 3")
        #------------------------------------------------------------

        print(dataRow)
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_PLANS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[7])
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

@read_plan.route('/plans/gastronomia', methods=['GET'])
def r_gastro():

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
        #id_business = str(id_business)
        print("Hola data 2")
        category = 'gastronomia'

        #--------------------------------------------------------
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute( '''SELECT plans.*, business.category
                        FROM plans 
                        INNER JOIN business  
                        ON business.id_business = plans.id_business
                        AND (business.category = %s ) 
                        AND (active = 1)
                        ORDER BY create_p DESC''', [category] )
        dataRow = cur.fetchall()
        print("Hola data 3") 
        #--------------------------------------------------------

        print(dataRow)
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_PLANS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[7])
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


@read_plan.route('/plans/turismo', methods=['GET'])
def r_tur():

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
        #id_business = str(id_business)
        print("Hola data 2")

        category = 'turismo'

        #-------------------------------------------------------------
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute( '''SELECT plans.*, business.category
                        FROM plans 
                        INNER JOIN business  
                        ON business.id_business = plans.id_business
                        AND (business.category = %s ) 
                        AND (active = 1)
                        ORDER BY create_p DESC''', [category] )
        dataRow = cur.fetchall()
        print("Hola data 3")
        #-------------------------------------------------------------

        print(dataRow)
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_PLANS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[7])
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

        

@read_plan.route('/plans/hospedaje', methods=['GET'])
def r_hosp():

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
        #id_business = str(id_business)
        print("Hola data 2")

        category = 'hospedaje'

        #----------------------------------------------------------------
        cur = mysql.connection.cursor()
        print("Hola MySQl")
        cur.execute( '''SELECT plans.*, business.category
                        FROM plans 
                        INNER JOIN business  
                        ON business.id_business = plans.id_business
                        AND (business.category = %s) 
                        AND (active = 1)
                        ORDER BY create_p DESC''', [category] )
        dataRow = cur.fetchall()
        print("Hola data 3")
        #----------------------------------------------------------------

        print(dataRow)
        print(type(dataRow))
        dataRow = list(dataRow)
        print(type(dataRow))

        paths = []
        path = UPLOAD_FOLDER_PLANS

        for data in dataRow:
            #print(data)
            #img_path = os.path.join(path, data[7])
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
    
