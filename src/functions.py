import requests
import json
from src.classes import Vacancy, Vacancies_File, From_hh_api


def main_menu():
    """ функция выбора пункта основного меню """

    raw_file_path = 'data/hh_vacancies_raw.json'
    source_file_path = 'data/hh_vacancies_source.json'

    print('\nОСНОВНОЕ МЕНЮ:\n'
          '1. Загрузить вакансии с сайта\n'
          '2. Отсортировать вакансий по ЗП\n'
          '3. Отфильтровать вакансии по городу\n'
          '4. Отфильтровать вакансии по ключевому слову\n'          
          '5. Добавить новую вакансию\n'
          '6. Удалить вакансию\n'
          '7. Закончить работу')

    selected_point = int(input('Введите номер пункта меню: '))

    if selected_point == 1:
        menu_search_params(raw_file_path, source_file_path)

    elif selected_point == 2:
        menu_top_salary(raw_file_path , source_file_path)

    elif selected_point== 3:
        menu_filter_by_city(raw_file_path , source_file_path)

    elif selected_point== 4:
        menu_filter_by_word(raw_file_path , source_file_path)

    elif selected_point== 5:
        menu_new_vacancy(raw_file_path , source_file_path)

    elif selected_point == 6:
        print_vacancies(source_file_path)
        id_to_remove = input('\nВведите ID вакансии, которую Вы хотите удалить из списка: ')
        menu_remove_vacancy(raw_file_path , source_file_path, id_to_remove)

    elif selected_point == 7:
        print('Мы закончили. Пока!')

    else:
        print('В меню нет такого пункта')

def print_vacancies(file_to_print):
    """ Функция вывода списка вакансий"""

    vacancies = []
    with open(file_to_print, 'rt', encoding='utf-8') as source_file:
        vacancies = json.load(source_file)

    for vacancy in vacancies:
        print(str(Vacancy(vacancy['id'],vacancy['name'],vacancy['url'],vacancy['salary'], vacancy['address'], vacancy['employer'], vacancy['snippet'])))


def menu_search_params(raw_file_path, source_file_path):
    """ функция загрузки вакансий по ключевому слову с указанием количества"""

    search_word = input('Введите ключевое слово для поиска вакансий: ')
    vacancies_number = int(input('Введите количество вакансий в поиске: '))

    hh_api = From_hh_api()
    hh_api.get_vacancies(search_word, vacancies_number)

    file = Vacancies_File(raw_file_path, source_file_path)
    file.from_raw_file()
    print_vacancies(source_file_path)
    main_menu()

def menu_top_salary(raw_file_path, source_file_path):
    """ Функция сортировки вакансия по уровню ЗП """

    sorting_file = Vacancies_File(raw_file_path, source_file_path)
    sorting_file.sort_vacancy()
    print('\nВакансии отсортированные по максимальному уровню нижнего уровня ЗП:')

    print_vacancies(source_file_path)
    main_menu()

def menu_filter_by_city(raw_file_path , source_file_path):
    """ Функция фильтрации вакансий по названию города"""

    search_word = input('Введите город: ')

    filtered_file = Vacancies_File(raw_file_path, source_file_path)
    filtered_file.filter_vacancy_by_city(search_word)

    print_vacancies(source_file_path)
    main_menu()

def menu_filter_by_word(raw_file_path , source_file_path):
    """ Функция фильтрации вакансий по ключевому слову"""

    search_word = input('Слово для поиска: ')

    filtered_file = Vacancies_File(raw_file_path, source_file_path)
    filtered_file.filter_vacancy_by_word(search_word)

    print_vacancies(source_file_path)
    main_menu()

def menu_remove_vacancy(raw_file_path, source_file_path, id_to_remove):
    """ Функция работы в меню удаления вакансии """
    #
    # id_to_remove = input('\nВведите ID вакансии, которую Вы хотите удалить из списка: ')
    vacancies = []
    vacancies_result = []
    id_list = []

    with open(source_file_path, 'rt', encoding='utf-8') as source:
        vacancies = json.load(source)

        for vacancy in vacancies:
            id_list.append(vacancy['id'])

    if id_to_remove in id_list:
        file = Vacancies_File(raw_file_path, source_file_path)
        file.remove_vacancy(id_to_remove)

        print_vacancies(source_file_path)
        main_menu()

    else:
        print('В списке нет вакансии с этим ID')
        main_menu()


def menu_new_vacancy(raw_file_path, source_file_path):
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
    vacancy_snippet_requirement = input('Введите ключевые требования: ')
    vacancy_snippet_responsibility = input('Введите описание ответственности: ')

    # Собираем словари
    vacancy_salary = {'from': vacancy_salary_from, 'to': vacancy_salary_to, 'currancy': 'RUR', "gross": True}
    vacancy_snippet = {'requirement': vacancy_snippet_requirement,
                       'responsibility': vacancy_snippet_responsibility}
    vacancy_address = {'city': vacancy_address_city}
    vacancy_employer = {'name': vacancy_employer_name}

    # новая вакансия должна быть экземпляром класса Vacancy
    new_vacancy = Vacancy(vacancy_id,vacancy_name,vacancy_url,vacancy_salary,vacancy_address,vacancy_employer,vacancy_snippet)

    file = Vacancies_File(raw_file_path, source_file_path)
    file.add_vacancy(new_vacancy)

    print_vacancies(source_file_path)
    main_menu()


