from flask import Flask

from BillardStats.models import db
from BillardStats.config import configure_app

import BillardStats.views.users
import BillardStats.views.games

app = Flask(__name__)
#api = Api(app)

#Loads our configurations from config.ini and applies them
configure_app(app)

#Configure the database (From the app configurations)
db.init_app(app)

#Register API blueprints
app.register_blueprint(BillardStats.views.users.users_view,
                       url_prefix='/api/users')
app.register_blueprint(BillardStats.views.games.games_view,
                       url_prefix='/api/games')
