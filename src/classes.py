import json
import requests
import re

from abc import ABC, abstractmethod
from typing import Any
from operator import itemgetter

class Abs_APIVacancy(ABC):
    """ Абстрактный класс для одъектов класса вакансия и его наследников """
    @abstractmethod
    def __init__(self) -> None:
        pass

class From_hh_api(Abs_APIVacancy):
    """ Класс для запроса данных с сайта hh.ru """

    def __init__(self) -> None:
        self.api_url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_text, vacancies_number) -> None:
        """ метод позволяющий запрашивать записи с сайта hh, содержащие текст search_text и записывать его в файл в формате json """

        response = requests.get(self.api_url, params={'text': search_text, 'per_page': vacancies_number})
        print(response)
        print(response.status_code)

        vacancies = response.json()

        with open('data/hh_vacancies_raw.json', 'wt', encoding='utf-8') as data_file:
            json.dump(vacancies['items'], data_file, ensure_ascii=False)


class Vacancy():
    """класс объекта Вакансия"""

    id: int
    name: str
    url: str
    salary: dict
    address: dict
    employer: dict
    snippet: dict

    def __init__(self, id, name, url, salary, address, employer, snippet) -> None:

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

    def __repr__(self) -> str:
        return f'{self.id}, {self.name}, {self.url}, {self.salary}, {self.address},{self.employer},{self.snippet}'

    def __str__(self) -> str:

        return f'{self.id}, {self.name} в "{self.employer['name']}" с доходом от {self.salary['from']} до {self.salary['to']} в городе {self.address['city']}. Ссылка: {self.url}. Требования: {self.snippet['requirement']}'

    def __le__(self, other) -> bool:
        if self.salary['from'] <= other.salary['from']:
            return True
        else:
            return False
    def __ge__(self, other) -> bool:

        if self.salary['from'] >= other.salary['from']:
            return True
        else:
            return False

class Abs_Vacancies_File(ABC):
    """ Абстрактный класс для одъектов класса взаимодействия с файлами """
    @abstractmethod
    def __init__(self) -> None:
        pass

class Vacancies_File():

    def __init__(self, raw_file_path, source_file_path) -> None:

        self.raw_file_path = raw_file_path
        self.source_file_path = source_file_path

    def from_raw_file(self) -> None:
        """  метод, который позволяет из исходного файла, полученного импортом с сайта hh.ru,
        получить файл в котором записи вакансий добавляются в формате класса Vacancy"""

        vacancies_to_source = []

        with open(self.raw_file_path, 'rt', encoding='utf-8') as raw_file:
            vacancies = json.load(raw_file)

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

    def add_vacancy(self, new_vacancy) -> None:
        """ Метод записи новой вакании в итоговый файл"""

        # Проверим соответствует ли новая вакансия формату класса Vacanse
        if issubclass(type(new_vacancy), Vacancy):
            vacansies: list
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

        else:
            raise ValueError('Вы добавляете вакансию некорректного формата')

    def remove_vacancy(self, vacancy_id) -> None:
        """ Метод для удаления выкансии по нужному ID из файла с ваканcиями"""

        id_list = []

        with open(self.source_file_path, 'rt', encoding='utf-8') as source_file:
            vacancies = json.load(source_file)

            for vacancy in vacancies:
                id_list.append(vacancy['id'])

            if vacancy_id in id_list:
                for vacancy in vacancies:
                    if vacancy['id'] == str(vacancy_id):
                        vacancies.remove(vacancy)
                        print(f'Вакансия {vacancy['id']} удалена из списка')


                with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
                    json.dump(vacancies, source_file, ensure_ascii=False)
            else:
                print(f'Вакансии с ID {vacancy_id} нет в списке')
                with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
                    json.dump(vacancies, source_file, ensure_ascii=False)

    def sort_vacancy(self, top_number) -> None:
        """ Метод сортировки вакансий в файле"""

        vacancies = []
        top_vacancies = []

        with open(self.source_file_path, 'rt', encoding='utf-8') as source_file:
            vacancies = json.load(source_file)

        # Заполняем вакансии, для которых не указан уровень ЗП
        for vacancy in vacancies:

            if vacancy['salary'] == None:
                vacancy['salary'] = {'from': 0, 'to': 0, "currency": "RUR", "gross": True}


        vacancies.sort(key=lambda e: e['salary']['from'], reverse=True)

        top_vacancies = vacancies[0 : top_number]

        with open(self.source_file_path, 'wt', encoding='utf-8') as source_file:
            json.dump(top_vacancies, source_file, ensure_ascii=False)


    def filter_vacancy_by_city(self,search_city) -> None:
        """ Метод получения списка вакансий из файла, соответствующий введенным критериям"""

        vacancies_found = []
        cities_list = []

        with open(self.source_file_path, 'rt', encoding='utf-8') as file:
            vacancies = json.load(file)

            for vacancy in vacancies:
                if vacancy['address'] != None:
                    cities_list.append(vacancy['address']['city'])

            if search_city in cities_list:
                for vacancy in vacancies:
                    if vacancy['address'] != None:
                        if search_city == vacancy['address']['city']:
                            vacancies_found.append(vacancy)
                with open(self.source_file_path, 'wt', encoding='utf-8') as file:
                    json.dump(vacancies_found, file, ensure_ascii=False)

            else:
                print(f'В городе {search_city} вакансий не найдено\n')
                with open(self.source_file_path, 'wt', encoding='utf-8') as file:
                    json.dump(vacancies, file, ensure_ascii=False)

    def filter_vacancy_by_word(self,search_word) -> None:
        """ Метод получения списка вакансий из файла, соответствующий введенным критериям"""

        vacancies_found = []

        with open(self.source_file_path, 'rt', encoding='utf-8') as file:
            vacancies = json.load(file)


        for vacancy in vacancies:
            # Если требования или ответственность не заполены, то заполняем их заглушками
            if vacancy['snippet']['requirement'] == None:
                vacancy['snippet']['requirement'] = 'Требования'

            if vacancy['snippet']['responsibility'] == None:
                vacancy['snippet']['responsibility'] = 'Ответственность'

            vacancy_name = vacancy['name'].lower()
            vacancy_requirement = vacancy['snippet']['requirement'].lower()
            vacancy_responsibility = vacancy['snippet']['responsibility'].lower()

            # очищаем текст от знаков
            symbols_to_remove = ",!?."
            for symbol in symbols_to_remove:
                vacancy_name = vacancy_name.replace(symbol, "")
                vacancy_responsibility = vacancy_responsibility.replace(symbol, "")
                vacancy_requirement = vacancy_requirement.replace(symbol, "")

            add_name = vacancy_name.split()
            add_requirement = vacancy_requirement.split()
            add_responsibility = vacancy_responsibility.split()

            # собираем текст краткого наименования, требований и ответственности в список слов для проверки
            words_list = []

            for m in add_name:
                words_list.append(m)
            for i in add_requirement:
                words_list.append(i)
            for j in add_responsibility:
                words_list.append(j)

            # проверяем соответствие слова для поиска тексту вакансии
            if search_word.lower() in words_list:
                vacancies_found.append(vacancy)


        if len(vacancies_found) == 0:
            print(f'Вакании, содержащте ключевое слово {search_word} не найдены\n'
                  f'Попробуйте запустить поиск снова\n')

        else:
            with open(self.source_file_path, 'wt', encoding='utf-8') as file:
                json.dump(vacancies_found, file, ensure_ascii=False)





