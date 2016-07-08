import json
import os

from quiz import app, db


def read_json_quiz():
    with open(os.path.join(app.config['BASE_DIR'], 'data.json')) as f:
        data = json.loads(f.read())
    return data


def import_db():
    questions = read_json_quiz()
    for question in questions:
        quiz = Quiz(title=question['title'],
                    question=question['question'],
                    code=question['code'],
                    choices=str(question['choices']),
                    correct=question['correct'],
                    description=question['description'])
        db.session.add(quiz)
    db.session.commit()


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    question = db.Column(db.String)
    code = db.Column(db.String)
    choices = db.Column(db.String)
    correct = db.Column(db.String)
    description = db.Column(db.String)


    def __init__(self, title, question, code, choices, correct, description):
        self.title = title
        self.question = question
        self.code = code
        self.choices = choices
        self.correct = correct
        self.descrption = description


    def __repr__(self):
        return '<{}>'.format(self.title)

