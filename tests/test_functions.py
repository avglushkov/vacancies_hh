import pytest
import json
from pathlib import Path

from src.functions import menu_remove_vacancy, menu_new_vacancy, menu_search_params, menu_top_salary, print_vacancies
from src.classes import Vacancy, Vacancies_File, From_hh_api
#


data_folder = Path('/data')
test_file = data_folder / 'test_data.json'


# @pytest.fixture()
# def result_data_file():
#     with open(test_file, 'rt', encoding='utf-8') as file:
#         vacancies = json.load(file)
#
#     return
#
# def test_menu_remove_vacancy(test_data_file,result_data_file):
#
#     assert (menu_remove_vacancy('data/hh_vacancies_raw.json',test_file, '97455477')
#             result== result_data)
#
#
#
#
#
#
