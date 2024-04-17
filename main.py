import requests
import json
from src.classes import From_hh_api, Vacanse, Vacansies_File
from src.functions import main_menu, menu_new_vacancy




main_menu()
def interface():
    search = input("Введите  текст запроса\n")
    hh_api = From_hh_api()
    hh_api.get_vacancies(search)

interface()

test_file = Vacansies_File('data/hh_vacancies_row.json','data/hh_vacancies_source.json', 'data/hh_vacancies_result.json')
test_file.from_row_file()
