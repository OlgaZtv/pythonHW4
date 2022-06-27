# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def print_functions_names(function):
    name_function = function.__name__.replace("_", " ").capitalize()
    arguments_name = function.__code__.co_varnames

    if len(arguments_name) != 0:
        arguments_description = f'Список аргументов: {", ".join(arguments_name)}'
    else:
        arguments_description = 'Аргументы отсутствуют'

    print(f'Имя функции {name_function}. {arguments_description}')


for function in (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page):
    print_functions_names(function)
