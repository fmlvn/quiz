import os

from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_codemirror import CodeMirror
import jinja2_highlight


app = Flask(__name__)
app.jinja_options = dict(Flask.jinja_options)
app.jinja_options.setdefault('extensions', []).append('jinja2_highlight.HighlightExtension')
app.config.from_object('config')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
admin = Admin(app, name='quiz', template_mode='bootstrap3')
codemirror = CodeMirror(app)



from quiz.models import import_db
import quiz.views


if not os.path.exists(os.path.join(app.config['BASE_DIR'], 'app.db')):
    db.create_all()
    import_db()

import quiz.admin
