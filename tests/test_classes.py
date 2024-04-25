from src.classes import From_hh_api,Vacancy,Vacancies_File

import pytest
import json


def test_head_hunter_api():
    """проверяем работоспособность загрузки данных с сайта и записи в файл"""

    get_api = From_hh_api()
    get_api.get_vacancies('agile', 3, '../data/hh_vacancies_raw.json')


    with open('../data/hh_vacancies_raw.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 3

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

@pytest.fixture()
def test_file_json():
    with open('test_data.json', 'wt', encoding='utf-8') as file:
        vacancies = [
            {'id': '97420684', 'premium': False,
             'name': 'Уборщица',
             'department': None, 'has_test': False, 'response_letter_required': False,
             'area': {'id': '160', 'name': 'Алматы', 'url': 'https://api.hh.ru/areas/160'},
             'salary': {'from': 100000, 'to': 110000, 'currency': 'KZT', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Москва'}, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-04-19T12:32:07+0300', 'created_at': '2024-04-19T12:32:07+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=97420684',
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/97420684?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/97420684', 'relations': [],
             'employer': {'id': '10821541', 'name': 'CityHome', 'url': 'https://api.hh.ru/employers/10821541',
                          'alternate_url': 'https://hh.ru/employer/10821541', 'logo_urls': None,
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10821541',
                          'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': None,
                         'responsibility': 'Осуществляет уборку коридоров, лестниц. Удаляет пыль, подметает и моет полы, потолки, оконные рамы и стекла, дверные блоки. Следит за наличием...'},
             'contacts': None,
             'schedule': {'id': 'fullDay', 'name': 'Полный день'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '130', 'name': 'Уборщица, уборщик'}], 'accept_incomplete_resumes': True,
             'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '97455477', 'premium': False,
             'name': 'Домработница (домработник) / горничная',
             'department': None, 'has_test': False, 'response_letter_required': False,
             'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': 130000, 'to': None, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'anonymous', 'name': 'Анонимная'},
             'address': None, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-04-19T16:41:37+0300', 'created_at': '2024-04-19T16:41:37+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=97455477',
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/97455477?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/97455477', 'relations': [],
             'employer': {'name': 'Частное лицо', 'trusted': True},
             'snippet': {
                 'requirement': 'Опыт работы в семьях. Навыки ухода за сложными поверхностями. Навыки работы с современной бытовой техникой. Навыки ухода за гардеробом. ',
                 'responsibility': 'Генеральная и поддерживающая уборка. Работа с современной бытовой техникой. Уход за сложными поверхностями. Уход за VIP гардеробом (сортировка, стирка, глажка...'},
             'contacts': None,
             'schedule': {'id': 'fullDay', 'name': 'Полный день'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '130', 'name': 'Уборщица, уборщик'}], 'accept_incomplete_resumes': True,
             'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None}]

        json.dump(vacancies, file, ensure_ascii=False)


def test_remove(test_file_json):
    """ проверяем корректность работы метода remove_vacancy класса Vacancies_File """

    test_file_json = Vacancies_File('test_data.json','test_data.json')
    test_file_json.remove_vacancy('97455477')
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 1
    assert vacancies[0]['id'] == '97420684'

def test_add_vacancy(test_file_json):
    """ проверяем корректность работы метода add_vacancy класса Vacancies_File """

    vacancy = Vacancy('97228248'
                       , 'IT директор | CIO | pharma (офис)'
                       , 'https://api.hh.ru/vacancies/97228248?host=hh.ru'
                       , None
                       , None
                       , {'id': '100000', 'name': 'ABC'}
                       , {'requirement': 'Обязательное условие - Английский язык',
                          'responsibility': 'Управление ИТ-ландшафтом и стратегиями развития'})

    test_file_json = Vacancies_File('test_data.json', 'test_data.json')
    test_file_json.add_vacancy(vacancy)
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 3
    assert vacancies[2]['id'] == '97228248'

def test_sort_vacancy(test_file_json):
    """ проверяем корректность работы метода sort_vacancy класса Vacancies_File """

    test_file_json = Vacancies_File('test_data.json', 'test_data.json')
    test_file_json.sort_vacancy(2)
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 2
    assert vacancies[0]['id'] == '97455477'
    assert vacancies[1]['id'] == '97420684'

def test_filter_vacancy_by_city_1(test_file_json):
    """ проверяем корректность работы метода filter_vacancy_by_city класса Vacancies_File """

    test_file_json = Vacancies_File('test_data.json','test_data.json')
    test_file_json.filter_vacancy_by_city('Москва')
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 1
    assert vacancies[0]['id'] == '97420684'
def test_filter_vacancy_by_city_2(test_file_json):
    """ проверяем корректность работы метода filter_vacancy_by_city класса Vacancies_File """

    test_file_json = Vacancies_File('test_data.json','test_data.json')
    test_file_json.filter_vacancy_by_city('Нью-Йорк')
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 2
    assert vacancies[0]['id'] == '97420684'
    assert vacancies[1]['id'] == '97455477'

def test_filter_vacancy_by_word_1(test_file_json):
    """ проверяем корректность работы метода filter_vacancy_by_word класса Vacancies_File """

    test_file_json = Vacancies_File('test_data.json','test_data.json')
    test_file_json.filter_vacancy_by_word('пыль')
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 1
    assert vacancies[0]['id'] == '97420684'

def test_filter_vacancy_by_word_2(test_file_json):
    """ проверяем корректность работы метода filter_vacancy_by_word класса Vacancies_File """

    test_file_json = Vacancies_File('test_data.json','test_data.json')
    test_file_json.filter_vacancy_by_word('DevOps')
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies = json.load(file)

    assert len(vacancies) == 2
    assert vacancies[0]['id'] == '97420684'
    assert vacancies[1]['id'] == '97455477'