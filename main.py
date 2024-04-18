import requests
import json
from src.classes import From_hh_api, Vacanse, Vacansies_File
from src.functions import main_menu, menu_new_vacancy, menu_search_params, print_vacancies




menu_point = main_menu()

if menu_point == 1:
    search_param = menu_search_params()
    hh_api = From_hh_api()
    hh_api.get_vacancies(search_param[0], search_param[1])
    test_file = Vacansies_File('data/hh_vacancies_row.json',
                               'data/hh_vacancies_source.json',
                               'data/hh_vacancies_result.json')
    test_file.from_row_file()
    print_vacancies()



elif menu_point == 2:
    pass

elif menu_point == 3:
    pass

elif menu_point == 4:
    pass

else:
    print('В меню нет такого пункта')
    #
    # main_menu()

# interface()
#
# test_file = Vacansies_File('data/hh_vacancies_row.json','data/hh_vacancies_source.json', 'data/hh_vacancies_result.json')
# test_file.from_row_file()
