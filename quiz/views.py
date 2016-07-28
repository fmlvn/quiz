from flask import render_template, request, redirect, url_for
from wtforms import RadioField

from quiz import app
from quiz.models import Quiz, Choice
from quiz.forms import QuizForm, MultiQuizForm


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
        chosen = request.form.getlist('quiz_{}'.format(qid))
        chosen = [int(i) for i in chosen]
        result = check_answer(qid, chosen)
        return render_template('quiz.html', quiz=quiz, form=form, result=result)

    return render_template('quiz.html', quiz=quiz, form=form, result=result)



@app.route('/test', methods=['GET', 'POST'])
def test():
    qids = [1, 4, 9, 14, 17, 18, 23, 24, 27, 28, 34, 35, 36, 38, 39, 40, 43, 54, 55, 56, 59, 61, 62, 63, 65]
    form = MultiQuizForm(request.form, qids=qids)
    return render_template('multiquiz.html', qids=qids)
    return render_template('multiquiz.html', form=form)

