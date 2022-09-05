import json

'''
Напишите функции, которые получали бы данные:

`load_candidates()`, которая загрузит данные из файла
`get_all()`, которая покажет всех кандидатов
`get_by_pk(pk)`, которая вернет кандидата по pk
`get_by_skill(skill_name)`, которая вернет кандидатов по навыку
'''


def load_candidates():
    with open('candidates.json', encoding="utf-8") as file:
        CANDIDATES = json.load(file)
        return CANDIDATES


def get_all_candidates():
    candidates = load_candidates()
    return candidates

def get_candidates_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return 'Такого кандидата в списке нет'

def get_candidates_by_skill(skill_name):
    list_skills = []
    candidates = load_candidates()
    for candidate in candidates:
        skills = candidate['skills'].lower().split(', ')
        if skill_name in skills:
            list_skills.append(candidate)
    return list_skills