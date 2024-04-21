from src.classes import From_hh_api,Vacancy,Vacancies_File

import pytest

@pytest.fixture()
def vacancy_1():
    return Vacancy('97228248'
                   ,'IT директор | CIO | pharma (офис)'
                   ,'https://api.hh.ru/vacancies/97228248?host=hh.ru'
                   ,None
                   ,None
                   ,{'id': '100000', 'name': 'ABC'}
                   ,{'requirement': 'Обязательное условие - Английский язык','responsibility': 'Управление ИТ-ландшафтом и стратегиями развития'})

@pytest.fixture()
def vacancy_2():
    return Vacancy('97160285'
                   ,'Site reliability engineer/devops'
                   ,'https://api.hh.ru/vacancies?employer_id=5531122'
                   ,{'from': 500000, 'to': None, 'currency': 'RUR', 'gross': True}
                   ,None
                   ,{"id": "5531122", "name": "Heaad"}
                   ,{"requirement": "Что нам хотелось бы видеть у кандидата из hard skills: Git, GitLab, GitLab-CI. Docker, docker-compose","responsibility": "Поддержание и развитие существующей инфраструктуры, процессов CI/CD"})

def test_Vacancy(vacancy_1):
    """ Проверяем корректность работы с атрибутами класса Vacancy """

    assert vacancy_1.id == '97228248'
    assert vacancy_1.name == 'IT директор | CIO | pharma (офис)'
    assert vacancy_1.url == 'https://api.hh.ru/vacancies/97228248?host=hh.ru'
    assert vacancy_1.salary == {'from': 0, 'to': 0, 'currency': 'RUR', 'gross': True}
    assert vacancy_1.address == {'city':'-'}
    assert vacancy_1.snippet['requirement'] == 'Обязательное условие - Английский язык'

def test_Vacancy_le(vacancy_1,vacancy_2):
    """ Проверяем корректность работы метода сравнения __le__"""

    assert vacancy_1 <= vacancy_2

def test_Vacancy_ge(vacancy_2,vacancy_1):
    """ Проверяем корректность работы метода сравнения __ge__"""

    assert vacancy_2 >= vacancy_1

