from flask import render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import SelectMultipleField, SubmitField, widgets

from quiz import app
from quiz.models import Quiz, Choice
from quiz.forms import QuizForm


def check_answer(qid, chosen):
    correct_choices = Choice.query.filter_by(quiz_id=qid,correct=True).all()
    correct = [choice.id for choice in correct_choices]
    return chosen == correct


@app.route('/')
def index():
    quizzes = Quiz.query.all()
    return render_template('index.html', quizzes=quizzes)


@app.route('/quiz/<qid>', methods=('GET', 'POST'))
def view_quiz(qid):
    quiz = Quiz.query.filter_by(id=qid).first()
    form = QuizForm(request.form, qid=qid)
    result = ''
    if form.validate_on_submit():
        chosen = [int(i) for i in request.form.getlist('quiz_{}'.format(qid))]
        result = check_answer(qid, chosen)
        #return render_template('quiz.html', quiz=quiz, form=form, result=result)

    return render_template('quiz.html', quiz=quiz, form=form, result=result)



@app.route('/test', methods=['GET', 'POST'])
def test():
    qids = [1, 4, 9, 14, 17, 18, 23, 24, 27, 28, 34, 35, 36, 38, 39, 40, 43, 54, 55, 56, 59, 61, 62, 63, 65]
    quizzes = Quiz.query.filter(Quiz.id.in_(qids)).all()


    class MultiQuizForm(Form):
        pass

    for quiz in quizzes:
        choices = [(choice.id, choice.content) for choice in quiz.choices]
        field_name = 'quiz_{}'.format(quiz.id)
        field = SelectMultipleField(field_name, coerce=int, choices=choices,
                                    widget=widgets.ListWidget(prefix_label=False),
                                    option_widget=widgets.CheckboxInput())
        setattr(MultiQuizForm, field_name, field)


    form = MultiQuizForm(request.form, quizzes=quizzes)

    quiz_list = []

    for quiz in quizzes:
        quiz_list.append({'quiz': quiz,
                          'choices': getattr(form, 'quiz_{}'.format(quiz.id))})

    results = []
    if form.validate_on_submit():
        for qid in qids:
            chosen = [int(i) for i in request.form.getlist('quiz_{}'.format(qid))]
            results.append((qid, check_answer(qid, chosen)))
    return render_template('multiquiz.html', form=form,
                           quiz_list=quiz_list, results=results)

