from flask import Flask

from BilliardStats.models import db
from BilliardStats.config import configure_app

import BilliardStats.views.users
import BilliardStats.views.games

app = Flask(__name__)
#api = Api(app)

#Loads our configurations from config.ini and applies them
configure_app(app)

#Configure the database (From the app configurations)
db.init_app(app)

#Register API blueprints
app.register_blueprint(BilliardStats.views.users.users_view,
                       url_prefix='/api/users')
app.register_blueprint(BilliardStats.views.games.games_view,
                       url_prefix='/api/games')
