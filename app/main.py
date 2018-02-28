import requests
from flask import Flask, render_template, abort

app = Flask(__name__)


EXERCISE_API_URL = 'https://exercises.openstax.org/api/exercises'


def make_exercise_url(exercise_uid):
    return '{0}/{1}.json'.format(EXERCISE_API_URL, exercise_uid)


def get_exercise_json(exercise_uid):
    url = make_exercise_url(exercise_uid)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None


def get_exercise(exercise_uid):
    data = get_exercise_json(exercise_uid)
    if data:
        exercise_data = data['questions'][0]
        exercise = dict(
            uid=data['uid'],
            exercise_html=exercise_data['stem_html'],
            choices=exercise_data['answers']
        )
        return exercise
    else:
        return None


@app.route('/<string:exercise_uid>')
def exercise_viewer(exercise_uid):
    exercise = get_exercise(exercise_uid)
    if exercise:
        return render_template('exercise.html', exercise=exercise)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
