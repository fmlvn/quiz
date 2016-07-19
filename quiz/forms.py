from flask_wtf import Form
from wtforms import SelectField, SubmitField, RadioField, validators
from quiz.models import Quiz, Choice


class QuizForm(Form):
    choices = RadioField('Choices', choices=[])
    submit = SubmitField('Submit Answer')

