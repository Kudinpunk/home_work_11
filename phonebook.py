# открыть файл
# сохранить файл
# показать тк
# добавить контакт
# найти контакт
# изменить контакт
# удалить контакт
# выход
PAHT = 'phonebook.txt'


def menu():
    create_file()
    print(f'ГЛАВНОЕ МЕНЮ\n'
        f'1 => показать все контакты\n'
        f'2 => добавить контакт\n'
        f'3 => найти контакт\n'
        f'4 => изменить контакт\n'
        f'5 => удалить контакт\n'
        f'6 => выход')

    shoise_menu = int(input('Выберете пункт меню:'))

    if shoise_menu == 1:
        show_phonebook()
        menu()
    elif shoise_menu == 2:
        add_contact()
        menu()
    elif shoise_menu == 3:
        find_contact()
        menu()
    elif shoise_menu == 4:
        change_contact()
        menu()
    elif shoise_menu == 5:
        delete_contact()
        menu()
    elif shoise_menu == 6:
        return print('До свидания!')

def create_file():
    data = open(PAHT,'a', encoding='UTF8')
    data.close

def show_phonebook():
    data = open(PAHT,'r', encoding='UTF8')
    print(data.read())
    data.close()

def add_contact():
    data = open(PAHT,'a', encoding='UTF8')
    name = input('Введите имя: ').capitalize()
    surname = input('Введите фамилию: ').capitalize()
    middle_name = input('Введите отчество: ').capitalize()
    phone = input('Введите телефон: ')
    data.write(f'{surname} {name} {middle_name} {phone}\n')
    data.close()


def find_contact():
    data = open(PAHT,'r', encoding='UTF8')
    request = input('Введите параметр поиска: ').capitalize()
    my_contacts = data.readlines()
    i = 0
    for item in my_contacts:
        if request in item:
            i += 1
            print(f'По вашему запросу найдено: {item}')
    if i == 0:
        print('данных не найдено\n')
    data.close()

def change_contact():
    pass

def delete_contact():
    pass


menu()
