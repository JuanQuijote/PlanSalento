import io
from base64 import encodebytes
import os
from PIL import Image
import base64

def get_response_image(image_path):
    print(os.path.isfile(image_path))
    encoded_string = ""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        #print(encoded_string)
        file = encoded_string
        encoding = 'utf-8'
        file = file.decode(encoding)
        #print(file)
        print(type(file))
        image_file.close()
        del image_file
        return file

    #print("Hola path1")
    #pil_img = Image.open(image_path, mode='r') # reads the PIL image
    #print("Hola path2")
    #byte_arr = io.BytesIO()
    #print("Hola path3")
    #pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    #print("Hola path4")
    #encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    #encoded_img = encodebytes(pil_img).decode('ascii')
    #print("Hola path5")
    #pil_img.close()
    #del pil_img
    #print(encoded_img)
    #print(type(encoded_img))

    #message = "Python is fun"
    #message_bytes = message.encode('ascii')
    #base64_bytes = base64.b64encode(message_bytes)
    #base64_message = base64_bytes.decode('ascii')
    #return encoded_img
    