from src.classes import From_hh_api,Vacance,Vacancies_File

# import pytest
#
# import pytest


# @pytest.fixture()
# def test_row_data_from_hh():
#     vacancies = [{'id': '97228248', 'premium': False, 'name': 'IT директор | CIO | pharma (офис)', 'department': None,
#                   'has_test': False, 'response_letter_required': False,
#                   'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
#                   'salary': {'from': None, 'to': 600000, 'currency': 'RUR', 'gross': True},
#                   'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
#                   'sort_point_distance': None,
#                   'published_at': '2024-04-17T14:14:29+0300', 'created_at': '2024-04-17T14:14:29+0300',
#                   'archived': False,
#                   'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=97228248',
#                   'insider_interview': None,
#                   'url': 'https://api.hh.ru/vacancies/97228248?host=hh.ru',
#                   'alternate_url': 'https://hh.ru/vacancy/97228248',
#                   'relations': [], 'employer': {'id': '10499641', 'name': 'Межова Татьяна Владимировна',
#                                                 'url': 'https://api.hh.ru/employers/10499641',
#                                                 'alternate_url': 'https://hh.ru/employer/10499641', 'logo_urls': None,
#                                                 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10499641',
#                                                 'accredited_it_employer': False, 'trusted': False},
#                   'snippet': {'requirement': 'Обязательное условие - Английский язык(собеседование с экспатом).',
#                               'responsibility': 'Управление ИТ-ландшафтом и стратегиями развития. Контроль проектов по автоматизации и цифровизации. Управление информационными системами: Анализ потребностей пользователей и выбор...'},
#                   'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
#                   'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
#                   'professional_roles': [{'id': '36', 'name': 'Директор по информационным технологиям (CIO)'}],
#                   'accept_incomplete_resumes': False, 'experience': {'id': 'moreThan6', 'name': 'Более 6 лет'},
#                   'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
#                   'is_adv_vacancy': False,
#                   'adv_context': None}]
#
#     return vacancies


# def test_menu_remove_vacancy(test_row_data_from_hh):
#     with open('data/test_data.json', 'wt', encoding='utf-8') as test_file:
#         json.dump(test_row_data_from_hh, test_file, ensure_ascii == False)
#
#     result_file = Vacancies_File('_', 'data/test_data.json')
#     assert result_file.remove_vacancy('97228248') == []
vacancies = [{'id': '97228248', 'premium': False, 'name': 'IT директор | CIO | pharma (офис)', 'department': None,
                  'has_test': False, 'response_letter_required': False,
                  'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                  'salary': {'from': None, 'to': 600000, 'currency': 'RUR', 'gross': True},
                  'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
                  'sort_point_distance': None,
                  'published_at': '2024-04-17T14:14:29+0300', 'created_at': '2024-04-17T14:14:29+0300',
                  'archived': False,
                  'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=97228248',
                  'insider_interview': None,
                  'url': 'https://api.hh.ru/vacancies/97228248?host=hh.ru',
                  'alternate_url': 'https://hh.ru/vacancy/97228248',
                  'relations': [], 'employer': {'id': '10499641', 'name': 'Межова Татьяна Владимировна',
                                                'url': 'https://api.hh.ru/employers/10499641',
                                                'alternate_url': 'https://hh.ru/employer/10499641', 'logo_urls': None,
                                                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10499641',
                                                'accredited_it_employer': False, 'trusted': False},
                  'snippet': {'requirement': 'Обязательное условие - Английский язык(собеседование с экспатом).',
                              'responsibility': 'Управление ИТ-ландшафтом и стратегиями развития. Контроль проектов по автоматизации и цифровизации. Управление информационными системами: Анализ потребностей пользователей и выбор...'},
                  'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
                  'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
                  'professional_roles': [{'id': '36', 'name': 'Директор по информационным технологиям (CIO)'}],
                  'accept_incomplete_resumes': False, 'experience': {'id': 'moreThan6', 'name': 'Более 6 лет'},
                  'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
                  'is_adv_vacancy': False,
                  'adv_context': None}]

with open('data/test_data.json', 'wt', encoding='utf-8') as test_file:
         json.dump(vacancies, test_file, ensure_ascii == False)
result_file = Vacancies_File('data/hh_vacancies_row.json', 'data/test_data.json')
print(result_file.remove_vacancy('97228248'))