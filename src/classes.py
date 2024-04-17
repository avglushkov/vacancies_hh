import requests
import json

from abc import ABC, abstractmethod

class Abs_APIVacancy(ABC):
    """ Абстрактный класс для одъектов класса вакансия и его наследников """
    @abstractmethod
    def __init__(self):
        pass


class From_hh_api(Abs_APIVacancy):

    def __init__(self):
        self.api_url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_text):
        """ метод позволяющий запрашивать записи с сайта hh, содержащие текст search_text и записывать его в файл в формате json """

        response = requests.get(self.api_url, params={'text': search_text})
        print(response)
        print(response.status_code)

        vacancies = response.json()
        with open('data/hh_vacancies_row.json', 'wt', encoding='utf-8') as data_file:
            json.dump(vacancies['items'], data_file, ensure_ascii=False)




class Vacanse():
    """класс объекта Вакансия"""

    id: int
    name: str
    url: str
    salary: dict
    address: str
    employer: str
    snippet: dict

    def __init__(self, id, name, url, salary, address, employer, snippet):

        self.id = id
        self.name = name
        self.url = url
        self.address = address
        self.employer = employer
        self.snippet = snippet
        if salary == None:
            self.salary = {'from': 0, 'to': 0, "currency": "RUR", "gross": True}
        else:
            self.salary = salary

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.url}, {self.salary}, {self.address},{self.employer},{self.snippet}'

    def __le__(self, other):
        if self.salary['from'] <= other.salary['from']:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.salary['from'] >= other.salary['from']:
            return True
        else:
            return False

#
#
# vac1 = Vacanse(1,'fff','rrr',{'from': 40, 'to': 0, 'currency': 'RUR', 'gross': False},'rrrrrr','rrrrr',{})
#
#
# vac2 = Vacanse(1,'fff','rrr',{'from': 30, 'to': 0, 'currency': 'RUR', 'gross': False},'rrrrrr','rrrrr',{})
#
# print(repr(vac2))
# print(vac1 >= vac2)
# print(vac1 <= vac2)
class Vacansies_File():

    def __init__(self, row_file_path, source_file_path, result_file_path):
        # self.row_file_path = 'data/hh_vacancies_row.json'
        # self.source_file_path = 'data/hh_vacancies_source.json'
        # self.result_file_path = 'data/hh_vacancies_result.json'

        self.row_file_path = row_file_path
        self.source_file_path = source_file_path
        self.result_file_path = result_file_path

    def from_row_file(self):
        """  метод, который позволяет из исходного файла, полученного импортом с сайта hh.ru, получить файл в котором записи вакансий добавляются в формате класса Vacancy"""

        vacancies_to_source = []

        with open(self.row_file_path, 'rt', encoding='utf-8') as row_file:
            vacancies = json.load(row_file)

            for vacancy in vacancies:
                added_position = {}
                added_position['id'] = vacancy['id']
                added_position['name'] = vacancy['name']
                added_position['url'] = vacancy['url']
                added_position['address'] = (vacancy['address'])
                added_position['salary'] = vacancy['salary']
                added_position['employer'] = vacancy['employer']
                added_position['snippet'] = vacancy['snippet']

                vacancies_to_source.append(added_position)

        with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
            json.dump(vacancies_to_source, source_file, ensure_ascii=False)

    def get_vacancy_from_file(self,search_text, search_salary):
        """ Метод получения списка вакансий из файла, соответствующий введенным критериям"""

        vacancies_found = []

        with open(self.source_file_path, 'rt', encoding='utf-8') as source_file:
            vacancies = json.load(source_file)

            for vacancy in vacancies:

                #проверим наличие ключевого слова в кратком описании или описании обязанностей
                if search_text.lower() in vacancy['name'].lower() or search_text.lower() in vacancy['snippet']['requirement'].lower() or search_text.lower() in vacancy['snippet']['responsibility'].lower():

                    #проверим, что уровень ЗП превышает заданный порог
                    if vacancy['salary']['from'] <= search_salary:
                        vacancies_found.append(vacancy)

        with open(self.result_file_path, 'wt', encoding='utf-8') as result_file:
            json.dump(vacancies_found, result_file, ensure_ascii==False)

        return vacancies_found

    def add_vacancy(self, new_vacancy):
        """ Метод записи новой вакании в итоговый файл"""


        # Проверим соответствует ли новая вакансия формату класса Vacanse
        if issubclass(type(new_vacancy), Vacanse):
            with open(self.source_file_path, 'rt', encoding = 'utf-8') as source_file:
                vacancies = json.load(source_file)

            with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
                vacancies.append(new_vacancy)
                json.dump(vacancies, source_file, ensure_ascii=False)

        else:
            raise ValueError('Вы добавляете вакансию некорректного формата')

    def remove_vacancy(self, vacancy_id):
        """ Метод для удаления выкансии по нужному ID из файла с ваканчиями"""

        with open(self.source_file_path, 'rt', encoding='utf-8') as source_file:
            vacancies = json.load(source_file)

            for vacancy in vacancies:
                if vacancy['id'] == str(vacancy_id):
                    vacancies.remove(vacancy)

        with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
            json.dump(vacancies, source_file, ensure_ascii=False)

    # vacancies = []
    #
    # vac = Vacanse(vacancies[2]['id'], vacancies[2]['name'], vacancies[2]['url'], vacancies[2]['salary'],
    #               vacancies[2]['address'], vacancies[2]['employer'], vacancies[2]['snippet'])
    # print(vacancies[2]['name'])
    # print(vacancies[2]['salary'])
    # print(vac.snippet['responsibility'])
    #

