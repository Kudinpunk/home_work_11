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
        choice_menu()
    elif shoise_menu == 2:
        add_contact()
        choice_menu()
    elif shoise_menu == 3:
        find_contact()
        choice_menu()
    elif shoise_menu == 4:
        change_contact()
        choice_menu()
    elif shoise_menu == 5:
        delete_contact()
        choice_menu()
    elif shoise_menu == 6:
        return print('До свидания!')
    else:
        print('ошибка ввода, попробуете еще раз..')
        choice_menu()
    
def choice_menu():
    choice_user_menu = int(input("\nДля возврата в главное меню введите 0. Для выхода введите 6."))
    if choice_user_menu == 0:
        menu()
    elif choice_user_menu == 6:
        return print('До свидания!')
    else:
        print('ошибка ввода, попробуете еще раз..')
        choice_menu()


def create_file():
    data = open(PAHT,'a', encoding='UTF8')
    data.close

def show_phonebook():
    print('\n--список контактов--\n')
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
    request = input('Введите часть данных контакта для поиска: ').capitalize()
    my_contacts = data.readlines()
    i = 0
    find_of_contact = []
    for item in my_contacts:
        if request in item:
            i += 1
            print(f'По вашему запросу найдено: {item}')
    if i == 0:
        print('данных не найдено\n')
    data.close()

def change_contact():
    data = open(PAHT,'r', encoding='UTF8')
    my_contacts = data.readlines()
    data.close()
    my_contacts_dict = {}
    i = 1
    for item in my_contacts:
            my_contacts_dict[i] = item.strip()
            i += 1
    print(my_contacts_dict)
    num_del_contact = int(input('Выберите номер контакта, которых хотите изменить:'))
    keys_contacts = [key for key in my_contacts_dict]
    if num_del_contact in keys_contacts:
        print('Введите новые данные контакта:')
        name = input('Введите имя: ').capitalize()
        surname = input('Введите фамилию: ').capitalize()
        middle_name = input('Введите отчество: ').capitalize()
        phone = input('Введите телефон: ')
        my_contacts_dict[num_del_contact] = (f'{surname} {name} {middle_name} {phone}')
        print('Контакт был изменен.')
        data = open(PAHT,'w', encoding='UTF8')
        for value in my_contacts_dict.values():
            data.write(f'{value}\n')
        data.close()
    else:
        print('Ошибка выбора.')
    data.close()


def delete_contact():
    data = open(PAHT,'r', encoding='UTF8')
    my_contacts = data.readlines()
    data.close()
    my_contacts_dict = {}
    i = 1
    for item in my_contacts:
            my_contacts_dict[i] = item.strip()
            i += 1
    print(my_contacts_dict)
    num_del_contact = int(input('Выберите номер контакта, которых хотите удалить:'))
    keys_contacts = [key for key in my_contacts_dict]
    if num_del_contact in keys_contacts:
        del my_contacts_dict[num_del_contact]
        print('Контакт был удален.')
        data = open(PAHT,'w', encoding='UTF8')
        for value in my_contacts_dict.values():
            data.write(f'{value}\n')
        data.close()
    else:
        print('Ошибка выбора.')
    data.close()

menu()


