import requests
import json

from abc import ABC, abstractmethod
from operator import itemgetter

class Abs_APIVacancy(ABC):
    """ Абстрактный класс для одъектов класса вакансия и его наследников """
    @abstractmethod
    def __init__(self):
        pass


class From_hh_api(Abs_APIVacancy):
    """ Класс для запроса данных с сайта hh.ru """

    def __init__(self):
        self.api_url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_text, vacancies_number):
        """ метод позволяющий запрашивать записи с сайта hh, содержащие текст search_text и записывать его в файл в формате json """

        response = requests.get(self.api_url, params={'text': search_text, 'per_page': vacancies_number})
        print(response)
        print(response.status_code)

        vacancies = response.json()
        with open('data/hh_vacancies_row.json', 'wt', encoding='utf-8') as data_file:
            json.dump(vacancies['items'], data_file, ensure_ascii=False)


class Vacance():
    """класс объекта Вакансия"""

    id: int
    name: str
    url: str
    salary: dict
    address: dict
    employer: dict
    snippet: dict

    def __init__(self, id, name, url, salary, address, employer, snippet):

        self.id = id
        self.name = name
        self.url = url
        if address == None:
            self.address = {'city': '-'}
        else:
            self.address = address

        self.employer = employer
        self.snippet = snippet
        if salary == None:
            self.salary = {'from': 0, 'to': 0, "currency": "RUR", "gross": True}
        else:
            self.salary = salary

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.url}, {self.salary}, {self.address},{self.employer},{self.snippet}'

    def __str__(self):

        return f'{self.id}, {self.name} в "{self.employer['name']}" с доходом от {self.salary['from']} до {self.salary['to']} в городе {self.address['city']}. Ссылка: {self.url}'

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

class Vacancies_File():

    def __init__(self, row_file_path, source_file_path):

        self.row_file_path = row_file_path
        self.source_file_path = source_file_path


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
                if vacancy['salary'] == None:
                    added_position['salary'] = {'from': 0, 'to': 0, "currency": "RUR", "gross": True}
                elif vacancy['salary']['from'] == None:
                    added_position['salary'] = {'from': 0, 'to': vacancy['salary']['to'], "currency": "RUR", "gross": True}
                else:
                    added_position['salary'] = vacancy['salary']
                added_position['employer'] = vacancy['employer']
                added_position['snippet'] = vacancy['snippet']

                vacancies_to_source.append(added_position)

        with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
            json.dump(vacancies_to_source, source_file, ensure_ascii=False)

    def add_vacancy(self, new_vacancy):
        """ Метод записи новой вакании в итоговый файл"""

        # Проверим соответствует ли новая вакансия формату класса Vacanse
        if issubclass(type(new_vacancy), Vacance):

            vacansies = []
            new_vacancy = {'id': new_vacancy.id,
                           'name': new_vacancy.name,
                           'url': new_vacancy.url,
                           'address': new_vacancy.address,
                           'salary': new_vacancy.salary,
                           'employer': new_vacancy.employer,
                           'snippet': new_vacancy.snippet}

            with open(self.source_file_path, 'rt', encoding = 'utf-8') as source_file:
                vacancies = json.load(source_file)

            with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
                vacancies.append(new_vacancy)
                json.dump(vacancies, source_file, ensure_ascii=False)
            # with open(self.result_file_path, 'wt', encoding='utf-8') as source_file:
            #     vacancies.append(new_vacancy)
            #     json.dump(vacancies, source_file, ensure_ascii=False)

        else:
            raise ValueError('Вы добавляете вакансию некорректного формата')

    def remove_vacancy(self, vacancy_id):
        """ Метод для удаления выкансии по нужному ID из файла с ваканчиями"""

        with open(self.source_file_path, 'rt', encoding='utf-8') as source_file:
            vacancies = json.load(source_file)
            for vacancy in vacancies:
                if vacancy['id'] == str(vacancy_id):
                    vacancies.remove(vacancy)

        # with open(self.result_file_path, 'wt', encoding='utf-8') as result_file:
        #     json.dump(vacancies, result_file, ensure_ascii=False)
        with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
            json.dump(vacancies, source_file, ensure_ascii=False)

    def sort_vacancy(self):
        """ Метод сортировки вакансий в файле"""

        vacancies = []

        with open(self.source_file_path, 'rt', encoding='utf-8') as source_file:
            vacancies = json.load(source_file)

        # Заполняем вакансии, для которых не указан уровень ЗП
        for vacancy in vacancies:

            if vacancy['salary'] == None:
                vacancy['salary'] = {'from': 0, 'to': 0, "currency": "RUR", "gross": True}


        vacancies.sort(key=lambda e: e['salary']['from'], reverse=True)


        # with open(self.result_file_path, 'wt', encoding='utf-8') as result_file:
        #     json.dump(vacancies, result_file, ensure_ascii=False)
        with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
            json.dump(vacancies, source_file, ensure_ascii=False)


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

        # with open(self.result_file_path, 'wt', encoding='utf-8') as result_file:
        #     json.dump(vacancies_found, result_file, ensure_ascii==False)
        with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
            json.dump(vacancies_found, source_file, ensure_ascii==False)

        return vacancies_found


