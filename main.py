from flask import Flask
import utils

app = Flask(__name__)

"""Создайте представление для роута `/` (главная страница).

Выведите список в таком формате (тег <pre> - преформатирование)"""

@app.route("/")
def index():
    candidates = utils.get_all_candidates()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += '<br>'
    return f"<pre> {result} </pre>"

"""Создайте представление для роута candidates/<x>"""

@app.route("/candidate/<int:pk>")
def get_candidates_by_pk(pk):
    candidate = utils.get_candidates_by_pk(pk)
    result = '<br>'
    result += candidate['name'] + "<br>"
    result += candidate['position'] + "<br>"
    result += candidate['skills'] + "<br>"
    result += '<br>'
    return f"""<img src="{candidate['picture']}">
           <pre> {result} </pre>
    """

"""Создайте представление `/skills/<x>` для поиска по навыкам.

Выведите тех кандидатов, в списке навыков у которых содержится `skill`.

Поиск по навыку не должен зависеть от регистра."""

@app.route("/candidate/<skill_name>")
def get_candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name.lower())
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += '<br>'
    return f"<pre> {result} </pre>"

app.run(debug=True)
