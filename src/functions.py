import requests
import json
from src.classes import Vacanse, Vacansies_File, From_hh_api


def main_menu():
    """ функция выбора пункта основного меню """

    print('\nОСНОВНОЕ МЕНЮ:\n'
          '1. Найти вакансию по ключевому слову\n'
          '2. Вывести ТОП N вакансий по ЗП\n'
          '3. Добавить новую вакансию\n'
          '4. Удалить вакансию\n'
          '5. Закончить работу')

    selected_point = int(input('Введите номер пункта меню: '))

    if selected_point == 1:
        menu_search_params()

    elif selected_point == 2:
        pass

    elif selected_point== 3:
        pass

    elif selected_point == 4:
        menu_remove_vacancy()

    elif selected_point == 5:
        print('Мы закончили. Пока!')

    else:
        print('В меню нет такого пункта')



def menu_search_params():
    """ функция выбора поиска вакансий по ключевому слову """

    search_word = input('Введите ключевое слово для поиска вакансии: ')
    vacancies_number = int(input('Введите количество вакансий в поиске: '))

    hh_api = From_hh_api()
    hh_api.get_vacancies(search_word, vacancies_number)
    test_file = Vacansies_File('data/hh_vacancies_row.json',
                               'data/hh_vacancies_source.json',
                               'data/hh_vacancies_result.json')
    test_file.from_row_file()
    print_vacancies('data/hh_vacancies_source.json')
    main_menu()


def print_vacancies(file_to_print):
    """ Функция вывода списка вакансий"""
    vacancies = []
    with open(file_to_print, 'rt', encoding='utf-8') as source_file:
        vacancies = json.load(source_file)

    for vacancy in vacancies:
        print(str(Vacanse(vacancy['id'],vacancy['name'],vacancy['url'],vacancy['salary'], vacancy['address'], vacancy['employer'], vacancy['snippet'])))


def menu_top_salary(N):
    """ Функция формирования перечня ТОП N вакансий по уровню ЗП"""
    pass

def menu_remove_vacancy():
    """ Функция работы в меню удаления вакансии"""
    print_vacancies('data/hh_vacancies_source.json')

    id_to_remove = input('\nВведите ID вакансии, которую Вы хотите удалить из списка: ')
    vacancies = []
    id_list = []

    with open('data/hh_vacancies_source.json', 'rt', encoding='utf-8') as source:
        vacancies = json.load(source)

        for vacancy in vacancies:
            id_list.append(vacancy['id'])

    if id_to_remove in id_list:
        test_file = Vacansies_File('data/hh_vacancies_row.json',
                                   'data/hh_vacancies_source.json',
                                   'data/hh_vacancies_result.json')
        test_file.remove_vacancy(id_to_remove)

        print_vacancies('data/hh_vacancies_result.json')
        main_menu()

    else:
        print('В списке нет вакансии с этим ID')
        main_menu()


def menu_new_vacancy():
    """ функция вывода меню ввода новой вакансии """

    new_vacancy = {}
    vacancy_address = {}
    vacancy_salary = {}

    vacancy_id = input('Введите ID вакансии (8 цифр): ' )
    vacancy_name = input('Введите краткое название: ' )
    vacancy_url = 'nd'
    vacancy_address_city = input('Введите город: ')
    vacancy_address_street = input('Введите улицу: ')
    vacancy_address_metro = input('Введите ближайшее метро: ')
    vacancy_salary_from = int(input('Зарплата в месяц от (до вычета налогов): '))


    if isinstance(vacancy_salary_from, str):
        vacancy_salary_from = 0

    vacancy_salary_to = int(input('Зарплата в месяц до (до вычета налогов): '))

    while vacancy_salary_from > vacancy_salary_to:
        print(f'Вы указали верхний уровень зарплаты ниже нижнего: {vacancy_salary_from}')
        vacancy_salary_to = int(input('Введите корректное значение ЗП до: '))

    vacancy_salary_currency = input('Валюта выплаты (RUR/USD/EUR): ' )

    vacancy_address = {'city': vacancy_address_city,
                      'street': vacancy_address_street,
                      'metro': vacancy_address_metro}
    vacancy_salary = {'from': vacancy_salary_from,
                      'to': vacancy_salary_to,
                      'currancy': vacancy_salary_currency,
                      "gross": True}

    new_vacancy = {'id': vacancy_id,
                   'name': vacancy_name,
                   'url': vacancy_url,
                   'address': vacancy_adress,
                   'salary': vacancy_salary}

    return new_vacancy






# add_new_vacancy()
# print(add_new_vacancy())