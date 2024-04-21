import requests
import json
from src.classes import Vacance, Vacancies_File, From_hh_api


def main_menu():
    """ функция выбора пункта основного меню """

    row_file_path = 'data/hh_vacancies_row.json'
    source_file_path = 'data/hh_vacancies_source.json'

    print('\nОСНОВНОЕ МЕНЮ:\n'
          '1. Найти вакансию по ключевому слову\n'
          '2. Вывести ТОП N вакансий по ЗП\n'
          '3. Добавить новую вакансию\n'
          '4. Удалить вакансию\n'
          '5. Закончить работу')

    selected_point = int(input('Введите номер пункта меню: '))

    if selected_point == 1:
        menu_search_params(row_file_path , source_file_path)

    elif selected_point == 2:
        menu_top_salary(row_file_path , source_file_path)

    elif selected_point== 3:
        menu_new_vacancy(row_file_path , source_file_path)

    elif selected_point == 4:
        menu_remove_vacancy(row_file_path , source_file_path)

    elif selected_point == 5:
        print('Мы закончили. Пока!')

    else:
        print('В меню нет такого пункта')

def print_vacancies(file_to_print):
    """ Функция вывода списка вакансий"""

    vacancies = []
    with open(file_to_print, 'rt', encoding='utf-8') as source_file:
        vacancies = json.load(source_file)

    for vacancy in vacancies:
        print(str(Vacance(vacancy['id'],vacancy['name'],vacancy['url'],vacancy['salary'], vacancy['address'], vacancy['employer'], vacancy['snippet'])))


def menu_search_params(row_file_path, source_file_path):
    """ функция выбора поиска вакансий по ключевому слову """

    search_word = input('Введите ключевое слово для поиска вакансии: ')
    vacancies_number = int(input('Введите количество вакансий в поиске: '))

    hh_api = From_hh_api()
    hh_api.get_vacancies(search_word, vacancies_number)
    test_file = Vacancies_File(row_file_path, source_file_path)
    test_file.from_row_file()
    print_vacancies(source_file_path)
    main_menu()

def menu_top_salary(row_file_path, source_file_path):
    """ Функция формирования перечня ТОП N вакансий по уровню ЗП """

    sorting_file = Vacancies_File(row_file_path, source_file_path)
    sorting_file.sort_vacancy()
    print('\nВакансии отсортированные по максимальному уровню нижнего уровня ЗП:')

    print_vacancies(source_file_path)
    main_menu()

def menu_remove_vacancy(row_file_path, source_file_path):
    """ Функция работы в меню удаления вакансии """

    print_vacancies(source_file_path)

    id_to_remove = input('\nВведите ID вакансии, которую Вы хотите удалить из списка: ')
    vacancies = []
    id_list = []

    with open(source_file_path, 'rt', encoding='utf-8') as source:
        vacancies = json.load(source)

        for vacancy in vacancies:
            id_list.append(vacancy['id'])

    if id_to_remove in id_list:
        result_file = Vacancies_File(row_file_path, source_file_path)
        result_file.remove_vacancy(id_to_remove)

        print_vacancies(source_file_path)
        main_menu()

    else:
        print('В списке нет вакансии с этим ID')
        main_menu()


def menu_new_vacancy(row_file_path, source_file_path):
    """ функция вывода меню ввода новой вакансии """

    new_vacancy = {}
    vacancy_address = {}
    vacancy_salary = {}

    # Запрашиваем заполенение данных по вакансии

    vacancy_id = input('Введите ID вакансии (8 цифр): ' )
    vacancy_name = input('Введите краткое название: ' )
    vacancy_url = 'Вакансия добавлена вручную'
    vacancy_address_city = input('Введите город: ')

    # Проверяем корректность ввода нижнего уровня ЗП
    while True:
        vacancy_salary_from = input('Зарплата в рублях в месяц ОТ (до вычета налогов): ')
        try:
            vacancy_salary_from = int(vacancy_salary_from)
        except ValueError:
            print('Уровень ЗП должен быть числом')
            continue
        if vacancy_salary_from == int(vacancy_salary_from):
            break
    # Проверяем корректность ввода верхнего уровня ЗП
    while True:
        vacancy_salary_to = input('Зарплата в рублях в месяц ДО (до вычета налогов): ')
        try:
            vacancy_salary_to = int(vacancy_salary_to)
        except ValueError:
            print('Уровень ЗП должен быть числом')
            continue
        if vacancy_salary_to == int(vacancy_salary_to):
            break
    # Верхний уровень должен быть выше нижнего
    while vacancy_salary_from > vacancy_salary_to:
        print(f'Вы указали верхний уровень зарплаты ниже нижнего')

        while True:
            vacancy_salary_to = input('Зарплата в рублях в месяц ДО (до вычета налогов): ')
            try:
                vacancy_salary_to = int(vacancy_salary_to)
            except ValueError:
                print('Уровень ЗП должен быть числом')
                continue
            if vacancy_salary_to == int(vacancy_salary_to):
                break

    vacancy_employer_name = input('Введите название компании: ')
    vacancy_snippet_requirements = input('Введите ключевые требования: ')
    vacancy_snippet_responsibility = input('Введите описание ответственности: ')

    # Собираем словари
    vacancy_salary = {'from': vacancy_salary_from, 'to': vacancy_salary_to, 'currancy': 'RUR', "gross": True}
    vacancy_snippet = {'requirements': vacancy_snippet_requirements,
                       'responsibility': vacancy_snippet_responsibility}
    vacancy_address = {'city': vacancy_address_city}
    vacancy_employer = {'name': vacancy_employer_name}

    # новая вакансия должна быть экземпляром класса Vacance
    new_vacancy = Vacance(vacancy_id,vacancy_name,vacancy_url,vacancy_salary,vacancy_address,vacancy_employer,vacancy_snippet)

    adding_file = Vacancies_File(row_file_path, source_file_path)
    adding_file.add_vacancy(new_vacancy)

    print_vacancies(source_file_path)
    main_menu()


