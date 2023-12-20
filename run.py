import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('data-analys')

def add_data():
    """
    Ask the user to add the data in the terminal
    """
    print('Please answer the questions.')

    your_gender = input("Your gender: \n")
    your_age = input("Your age: \n")
    delivery_sat = input("How satisfied are you from our delivery? (1 - 5): \n")
    missing_goods = input("Were any missing/damaged goods?: \n")
    contact_method = input("Did you contact to our customer service or did you complain through our website?: \n")
    service_sat = input("How satisfied are you from our customer service/online services? (1 - 5): \n")

    print(f"The data you provided is: {your_gender}, {your_age}, {delivery_sat}, {missing_goods}, {contact_method}, {service_sat}\n")

add_data()

