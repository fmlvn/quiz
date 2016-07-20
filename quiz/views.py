from flask import render_template, request, redirect, url_for
from wtforms import RadioField

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
    if request.method == 'POST':
        print(check_answer(qid, form.choices.data))
    return render_template('quiz.html', quiz=quiz, form=form)



@app.route('/test', methods=['GET', 'POST'])
def test():
    qids = [1, 2, 3, 4, 5]
    if request.method == 'GET':
        quiz_list = [Quiz.query.filter_by(id=qid).first() for qid in qids]
        choices = []
        for quiz in quiz_list:
            for choice in quiz.choices:
                if choice.correct == True:
                    choices.append(choice.content)
        return render_template('test.html', quizzes=quiz_list, choices=choices)

