
from typing import List
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def update_data(file, last_name):
    data = read_file(file)
    updated_data = []
    for line in data:
        if last_name.lower() in line.split(', ')[1].lower():
            print(f'Введите новые данные контакта ({line.strip()}):')
            first_name = input('Введите имя: ')
            new_last_name = input('Введите фамилию: ')
            patronymic = input('Введите отчество: ')
            phone_number = input('Введите номер телефона: ')
            updated_data.append(f'{first_name}, {new_last_name}, {patronymic}, {phone_number}\n')
        else:
            updated_data.append(line)
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(updated_data)

def delete_data(file, last_name):
    data = read_file(file)
    deleted_data = [line for line in data if last_name.lower() not in line.split(', ')[1].lower()]
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(deleted_data)

def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - изменить запись')
        print('5 - удалить запись')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            last_name = input('Введите фамилию для изменения: ')
            update_data(file_name, last_name)
        elif answer == '5':
            last_name = input('Введите фамилию для удаления: ')
            delete_data(file_name, last_name)    

if __name__ == '__main__':
    main()
