#!/usr/bin/env python
import json
import time

from bs4 import BeautifulSoup
import requests


def get_correct_answer(question_id, choices):
    ret = []
    for choice in choices:
        data = {'answer': choice,
                'qid': question_id}
        while True:
            try:
                res = requests.post('http://www.mypythonquiz.com/question.php',
                                    data=data)
                break
            except Exception as e:
                # print(e)
                time.sleep(5)
        soup = BeautifulSoup(res.text, 'lxml')
        if 'incorrect' not in res.text:
            ret.append((choices[choice], True))
            description = soup.select('.description')[0].text
            description = description.split('description: ')[1].strip()
        else:
            ret.append((choices[choice], False))
    return ret, description


def get_question_info(question_link):
    print('processing: {}'.format(question_link.text))
    res = requests.get(requests.compat.urljoin('http://www.mypythonquiz.com/',
                                               question_link.attrs['href']))
    soup = BeautifulSoup(res.text, 'lxml')
    title = question_link.text
    question_id = question_link.attrs['href'].split('qid=')
    question = soup.select('.myspan')[0]
    question = question.getText().split(':')[1].strip()
    try:
        code = soup.select('.codesample code')[0]
        code = code.getText()
    except IndexError:
        code = None

    answer_values = [i.attrs['value'] for i in
                     soup.select('input[name="answer"]')]
    answer_list = [i.getText() for i in soup.select('.content .myspan')[1:]]
    answers = dict(zip(answer_values, answer_list))

    choices, description = get_correct_answer(question_id, answers)

    print('done')

    return {'title': title,
            'question': question,
            'code': code,
            'choices': choices,
            'description': description}


def get_quiz():
    res = requests.get('http://www.mypythonquiz.com/list.php')
    soup = BeautifulSoup(res.text, 'lxml')
    question_links = [a for a in soup.select('.question a')]

    questions = []
    for link in question_links:
        question_info = get_question_info(link)
        questions.append(question_info)

    return questions


if __name__ == '__main__':
    data = get_quiz()
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))
