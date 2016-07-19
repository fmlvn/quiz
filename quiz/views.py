from flask import render_template, request, redirect, url_for
from wtforms import RadioField

from quiz import app
from quiz.models import Quiz
from quiz.forms import QuizForm


@app.route('/')
def index():
    quizzes = Quiz.query.all()
    return render_template('index.html', quizzes=quizzes)


@app.route('/quiz/<qid>', methods=('GET', 'POST'))
def view_quiz(qid):
    quiz = Quiz.query.filter_by(id=qid).first()
    form = QuizForm(request.form, quiz)
    if form.choices.choices == []:
        for choice in quiz.choices:
            form.choices.choices.append((choice.id, choice.content))
            form.choices.name = str(quiz.id)
            print(choice)
    if request.method == 'POST':
        print(form.choices.choices)
        if form.validate():
            print('validated')
        else:
            print('not validated')
        if form.validate_on_submit():
            print('validate on submit')
        else:
            print('not validate on submit')
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

