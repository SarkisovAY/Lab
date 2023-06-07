import streamlit as st
import csv
import pandas as pd
from io import StringIO
#import io from StringIO


def read_from_file_to_text(filename):
    file = open(filename, mode='r')
    text = file.read()
#    data = csv.DictReader(file)
#    print(text)
    return text

def convert_to_csv(text):
    data = csv.DictReader(StringIO(text))
    return data


def price(text_data):
    min_price_male = 0
    max_price_male = 0
    midl_price_male = 0
    all_price_male = 0
    min_price_female = 0
    max_price_female = 0
    midl_price_female = 0
    all_price_female = 0
    #csv_reader = read_file(filename)
    csv_reader = convert_to_csv(text_data)
    print(csv_reader)
    line_count = 0
    cont_male = 0
    cont_female = 0
    for row in csv_reader:
              #print(row)
              if row["Sex"] == "male":
                cont_male += 1
                all_price_male += float(row["Fare"])
                if float(row["Fare"]) > max_price_male:
                    max_price_male = float(row["Fare"])
                if float(row["Fare"]) < min_price_male or min_price_male == 0:
                    min_price_male = float(row["Fare"])
              if row["Sex"] == "female":
                cont_female += 1
                all_price_female += float(row["Fare"])
              if float(row["Fare"]) > max_price_female:
                max_price_female = float(row["Fare"])
              if float(row["Fare"]) < min_price_female or min_price_female == 0:
                min_price_female = float(row["Fare"])
    if (cont_male > 0):
        midl_price_male = all_price_male / cont_male
    else:
        midl_price_male = 0
    midl_price_female = all_price_female / cont_female
    return midl_price_male, midl_price_female, min_price_male, max_price_male, min_price_female, max_price_female

def sarkisov_cod(filename):
    st.title ("Титаник")
    st.write("---")
    variables = [" ", "Мужчины", "Женщины"]
    default_variable = variables[0]
    #with open('data.csv', mode='r') as csv_file:
    text_from_file = read_from_file_to_text(filename)
    midl_price_male, midl_price_female, min_price_male, max_price_male, min_price_female, max_price_female = price(text_from_file)
    #print(midl_price_male, midl_price_female, min_price_male, max_price_male, min_price_female, max_price_female)

    selected_variable = st.selectbox("Выберите пол:", variables, index=variables.index(default_variable))
    if selected_variable == "Мужчины":
            st.write("Минимальная цена билета для пассажиров мужского пола: {:.2f}".format(min_price_male))
            st.write("Максимальная цена билета для пассажиров мужского пола: {:.2f}".format(max_price_male))
            st.write("Средняя цена  билета для пассажиров мужского пола: {:.2f}".format(midl_price_male))
    elif selected_variable == "Женщины":
            st.write("Минимальная цена билета для пассажиров женского пола: {:.2f}".format(min_price_female))
            st.write("Максимальная цена билета для пассажиров женского пола: {:.2f}".format(max_price_female))
            st.write("Средняя цена билета для пассажиров женского пола: {:.2f}".format(midl_price_female))



sarkisov_cod('data.csv')

