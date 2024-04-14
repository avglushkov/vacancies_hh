import requests
import json
#
#
# class HH(Parser):
#     """
#     Класс для работы с API HeadHunter
#     Класс Parser является родительским классом, который вам необходимо реализовать
#     """
#
#     def __init__(self, file_worker):
#         self.url = 'https://api.hh.ru/vacancies'
#         self.headers = {'User-Agent': 'HH-User-Agent'}
#         self.params = {'text': '', 'page': 0, 'per_page': 100}
#         self.vacancies = []
#         super().__init__(file_worker)
#
#     def load_vacancies(self, keyword):
#         self.params['text'] = keyword
#         while self.params.get('page') != 20:
#             response = requests.get(self.url, headers=self.headers, params=self.params)
#             vacancies = response.json()['items']
#             self.vacancies.extend(vacancies)
#             self.params['page'] += 1

# url_get = "https://api.hh.ru/vacancies"  # используемый адрес для отправки запроса
#
# response = requests.get(url_get, headers={'User-Agent': 'HH-User-Agent'}, params={'text': '', 'page': 0, 'per_page': 3}) # отправка GET-запроса
#
# print(response)  # вывод объекта класса Response
#     # Вывод:
# # >> < Response[200] >
#
# print(response.status_code)  # вывод статуса запроса, 200 означает, что всё хорошо, остальные коды нас пока не интересуют и их можно считать показателем ошибки
# # Вывод:
# # >> 200
#
# print(response.text)

api_url = 'https://api.hh.ru/vacancies'


response = requests.get(api_url, params={'text':'ITIL','salary': 1000, 'currency':'EUR'})
vacancies = response.json()
with open('data/hh_vacancies.json', 'wt', encoding='utf-8') as data_file:
    json.dump(vacancies['items'], data_file, ensure_ascii=False)