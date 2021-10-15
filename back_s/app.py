from flask import Flask
from flask.helpers import url_for
from home import home
from login import login
from role import role 
from database import MySQL

from plan.create import create_plan
from plan.read import read_plan
from plan.read_one import read_one_plan
from plan.update import update_plan
from plan.delete import delete_plan

from user.create import create_user
from user.read import read_user 
from user.update import update_user 
from user.delete import delete_user
from user.read_one import read_one

from business.create import create_business
from business.read_one import read_one_business
from business.read import read_business
from business.update import update_business
from business.delete import delete_business

from flask_cors import CORS, cross_origin

import os

#UPLOAD_FOLDER_BUSINESS = os.path.abspath("./uploads/business_img/")
#UPLOAD_FOLDER_PLANS = os.path.abspath("./uploads/plans_img/")

app = Flask(__name__)

#app.config['UPLOAD_FOLDER_BUSINESS'] = UPLOAD_FOLDER_BUSINESS 
#app.config['UPLOAD_FOLDER_PLANS'] = UPLOAD_FOLDER_PLANS
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = "111213"
app.config['MYSQL_DB'] = 'plansalento2'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'
CORS(app, support_credentials=True) #support_credentials=True

#----------------------------------END-POINTS-----------------------------------------------
app.register_blueprint(home)
app.register_blueprint(login) 
app.register_blueprint(role)

app.register_blueprint(create_plan, url_prefix='')
app.register_blueprint(read_plan, url_prefix='')
app.register_blueprint(read_one_plan, url_prefix='')
app.register_blueprint(update_plan, url_prefix='')
app.register_blueprint(delete_plan, url_prefix='')

app.register_blueprint(create_user, url_prefix='')
app.register_blueprint(read_user, url_prefix='')
app.register_blueprint(update_user, url_prefix='')
app.register_blueprint(delete_user, url_prefix='')
app.register_blueprint(read_one, url_prefix='')

app.register_blueprint(create_business)
app.register_blueprint(read_one_business)
app.register_blueprint(read_business)
app.register_blueprint(update_business)
app.register_blueprint(delete_business)


#----------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)




