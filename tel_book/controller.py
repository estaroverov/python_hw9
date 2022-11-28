from import_data import import_data
from export_data import export_data
from print_data import *
from search_data import *
import streamlit as st
import del_row as dr

def greeting():
    st.write("Добро пожаловать в телефонный справочник")


def input_data():
    last_name = st.text_input("Введите фамилию: ")
    first_name = st.text_input("Введите имя: ")
    middle_name = st.text_input("Введите отчество: ")
    brith_name = st.text_input("Введите дату рождения: ")
    phone_number = st.text_input("Введите номер: ")
    note = st.text_input("Введите комментарий: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]


def choice_sep():
    sep = st.text_input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep


def choice_todo():
    st.text("Доступные операции с телефонным справочником:\n")
    ch = st.radio("Выберите", ('Добавить контакт',
                  'Показать все контакты', 'Поиск контакта', 'Поиск контакта по столбцу',"Удаление"))
    if ch:
        filename = st.text_input("Введите имя файла: ", "db.csv")
    if ch == 'Добавить контакт':
        sep = choice_sep()
        input_row = input_data()
        accept = st.button("Отправить")
        if accept:
            import_data(input_row, filename, sep)
    elif ch == 'Показать все контакты':
        accept = st.button("Отправить")
        if accept:
            data = export_data(filename)
            print_all_data(data)
    elif ch == 'Поиск контакта':
        word = st.text_input("Введите данные для поиска: ")
        search = st.button('Поиск')
        if search:
            data = export_data(filename)
            item = search_data(word, data)
            print_found_rows(item)
    elif ch == 'Поиск контакта по столбцу':
        word = st.text_input("Введите данные для поиска: ")
        columns = {"Фамилия":0, "Имя":1, "Отчество":2,"Дата рождения":3, "Телефон":4,"Должность":5}
        column = st.selectbox("Выберите столбец: ", ("Фамилия", "Имя", "Отчество","Дата рождения", "Телефон","Комментарий"))
        search = st.button('Поиск')
        if search:
            data = export_data(filename)
            item = search_val(word, data, columns[column])
            print_found_rows(item)
    elif ch == "Удаление":
        data = export_data(filename)
        print_all_data(data)
        row_number = st.text_input("Введите номер строки для удаления: ")
        button_del = st.button('Удалить')
        if button_del:
            st.text(f"Удалена строка: {dr.del_row(filename,data,int(row_number))}" )