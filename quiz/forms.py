from flask_wtf import Form
from wtforms import (SelectField, SubmitField, RadioField, SelectMultipleField,
                     validators, widgets)
from quiz.models import Quiz, Choice


class QuizForm(Form):
    choices = SelectMultipleField('Choices', coerce=int, choices=[],
                                  widget=widgets.ListWidget(prefix_label=True),
                                  option_widget=widgets.CheckboxInput())
    submit = SubmitField('Submit Answer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices_list = Choice.query.filter_by(quiz_id=kwargs['qid']).all()
        self.choices.choices = [(choice.id, choice.content)
                                for choice in choices_list]
