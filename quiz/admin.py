from flask_admin.contrib import sqla
from flask_admin.form.fields import Select2Field
from flask_codemirror.fields import CodeMirrorField, CodeMirrorWidget
from quiz import admin, db, codemirror
from quiz.models import Quiz, Choice


class CodeMirrorPythonField(CodeMirrorField):
#    widget = CodeMirrorWidget(language='python', config = {'lineNumbers': 'true'})
    pass

class QuizAdmin(sqla.ModelView):
#    code = CodeMirrorField(language='python', config = {'lineNumbers': 'true'})
#    form_overrides = dict(code=CodeMirrorPythonField)
#    form_overrides = dict(code=CodeMirrorField(widget=CodeMirrorWidget(
#        language='python', config={'lineNumbers': 'true'})))
#    form_overrides = dict(code=CodeMirrorField(widget=CodeMirrorWidget(language='python')))

    inline_models = (Choice,)
    pass


class ChoiceAdmin(sqla.ModelView):
    pass

admin.add_view(QuizAdmin(Quiz, db.session))
admin.add_view(ChoiceAdmin(Choice, db.session))
