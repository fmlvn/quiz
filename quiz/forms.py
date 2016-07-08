from flask_wtf import Form
from wtforms import SelectField, SubmitField, validators


class QuizForm(Form):
    answers = SelectField('Choices:')
    submit = SubmitField('Submit Answer')

