import os

from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_codemirror import CodeMirror


app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
admin = Admin(app, name='quiz', template_mode='bootstrap3')
codemirror = CodeMirror(app)
# login_manager = LoginManager()
# login_manager.init_app(app)



import quiz.models
import quiz.views

if not os.path.exists(os.path.join(app.config['BASE_DIR'], 'app.db')):
    db.create_all()
    quiz.models.import_db()

# from flask_admin.contrib.sqla import ModelView
# from quiz.admin import QuizAdmin
import quiz.admin
