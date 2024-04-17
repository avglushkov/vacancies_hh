

def main_menu():
    """ функция выбора пункта основного меню """
    print('Введите номер пункта меню:\n'
          '1. Найти вакансию по ключевому слову\n'
          '2. Вывести ТОП N вакансий по ЗП\n'
          '3. Добавить новую вакансию\n'
          '4. Удалить вакансию')

    selected_point = input('\n')
    return selected_point

def menu_search_word():
    """ функция выбора поиска вакансий по ключевому слову """

    search_word = input('Введите ключевое слово для поиска вакансии: ')
    vacancies_number = int(input('Введите количество вакансий в поиске: '))

    return [search_word, vacancies_number]

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