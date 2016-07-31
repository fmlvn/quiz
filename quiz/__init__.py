import os

from flask import Flask, current_app
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_codemirror import CodeMirror
import jinja2_highlight


app = Flask(__name__)
with app.app_context():
    current_app.jinja_options = dict(Flask.jinja_options)
    current_app.jinja_options.setdefault('extensions', [])
    current_app.jinja_options['extensions'].append('jinja2_highlight.HighlightExtension')
    current_app.config.from_object('config')
    bootstrap = Bootstrap(current_app)
    db = SQLAlchemy(current_app)
    admin = Admin(current_app, name='quiz', template_mode='bootstrap3')
    codemirror = CodeMirror(current_app)

    from quiz.models import import_db
    import quiz.views

    if not os.path.exists(os.path.join(app.config['BASE_DIR'], 'app.db')):
        db.create_all()
        import_db()

    import quiz.admin
