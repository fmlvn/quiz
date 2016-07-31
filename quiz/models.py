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
                    description=question['description'])

        choices = question['choices']
        for choice in choices:
            choice = Choice(content=choice[0],
                            correct=choice[1],
                            quiz_id=quiz.id)
            db.session.add(choice)
            quiz.choices.append(choice)
        db.session.add(quiz)
    db.session.commit()


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    question = db.Column(db.String)
    code = db.Column(db.Text)
    description = db.Column(db.String)
    choices = db.relationship('Choice', backref='quiz')

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<{}>'.format(self.title)


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    correct = db.Column(db.Boolean)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))

    def __str__(self):
        return '{}: {}'.format(self.content, self.correct)

    def __repr__(self):
        return '<{}: {} for quiz {}>'.format(self.content,
                                             self.correct,
                                             self.quiz_id)
