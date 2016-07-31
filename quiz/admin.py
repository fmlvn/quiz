from flask_admin.contrib import sqla
from flask_admin.form.fields import Select2Field
from flask_codemirror.fields import CodeMirrorField, CodeMirrorWidget
from quiz import admin, db, codemirror
from quiz.models import Quiz, Choice


class QuizAdmin(sqla.ModelView):
    inline_models = (Choice,)


class ChoiceAdmin(sqla.ModelView):
    pass

admin.add_view(QuizAdmin(Quiz, db.session))
admin.add_view(ChoiceAdmin(Choice, db.session))
