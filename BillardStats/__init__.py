from flask import Flask
#from flask_restful import Api
from BillardStats.models import db
from BillardStats.config import configure_app

import BillardStats.views.api

app = Flask(__name__)
#api = Api(app)

#Loads our configurations from config.ini and applies them
configure_app(app)

#Configure the database (From the app configurations)
db.init_app(app)

#Register API blueprint
app.register_blueprint(BillardStats.views.api.api_view, url_prefix='/api')
