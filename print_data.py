import streamlit as st
import pandas as pd


def print_all_data(data):
    if data == None:
        st.text("No such file!")
        return None
    if len(data) > 0:
        st.dataframe(print_data(data))
    else:
        st.text("База пуста!")


def print_data(data):
    return pd.DataFrame(
        {
            "Фамилия": [item[0] for item in data],
            "Имя": [item[1] for item in data],
            "Отчество": [item[2] for item in data],
            "Дата рождения": [item[3] for item in data],
            "Телефон": [item[4] for item in data],
            "Должность": [item[5] for item in data]

        })
    

def print_found_rows(found):
    if found == None:
        st.text("No such file!")
        return None
    if found != None or found != []:
        st.dataframe(print_data(found))
    else:
        st.text("Данные не обнаружены")
