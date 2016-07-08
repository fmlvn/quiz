from flask import render_template, request

from quiz import app
from quiz.models import Quiz
from quiz.forms import QuizForm


@app.route('/')
def index():
    quizzes = Quiz.query.all()
    return render_template('index.html', quizzes=quizzes)


@app.route('/quiz/<qid>', methods=['GET', 'POST'])
def quiz(qid):
    if request.method == 'GET':
        quiz = Quiz.query.filter_by(id=qid).first()
        form = QuizForm()
#         choices = dict(quiz.choices)
#         print('*'*100)
#         print(choices, type(choices))
#         form.answers.choices =
        return render_template('quiz.html', quiz=quiz, form=form)
