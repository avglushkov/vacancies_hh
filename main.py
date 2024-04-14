import requests
import json
from src.classes import From_hh_api, Vacanse, Vacansies_File



def interface():
    search = input("Введите  текст запроса\n")
    hh_api = From_hh_api()
    hh_api.get_vacancies(search)

interface()

test_file = Vacansies_File('data/hh_vacancies_row.json','data/hh_vacancies_source.json', 'data/hh_vacancies_result.json')
test_file.from_row_file()


# vacancies = []
# with open('data/hh_vacancies_row.json', 'rt', encoding='utf-8') as file:
#     vacancies = json.load(file)
#
# vac = Vacanse(vacancies[2]['id'], vacancies[2]['name'], vacancies[2]['url'], vacancies[2]['salary'], vacancies[2]['address'], vacancies[2]['employer'],vacancies[2]['snippet'])
# print(vacancies[2]['name'])
# print(vacancies[2]['salary'])
# print(vac.snippet['responsibility'])
# print(vac)