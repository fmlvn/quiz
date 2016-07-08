import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config')
admin = Admin(app, name='quiz', template_mode='bootstrap3')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

import quiz.models
import quiz.views

if not os.path.exists(os.path.join(app.config['BASE_DIR'], 'app.db')):
    db.create_all()
quiz.models.import_db()
