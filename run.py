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
    user_input = []

    questions = [
    "Your gender(W/M/None): ",
    "Your age: ",
    "How satisfied are you from our delivery? (1 - 5): ",
    "Were any missing/damaged goods?(Y/N): ",
    "Did you contact to our customer service or did you complain through our website?(CS/W): ",
    "How satisfied are you from our customer service/online services? (1 - 5): ",
    ]

    print('Please answer the questions.')

    for question in questions:
        answer = input(question)
        
        user_input.append(answer)
        
    validate_data(user_input)


def validate_data(values):
    """
    Validates the data provided by the user. 
    """
    try:
        if (values[0].upper() not in ['W', 'M', 'NONE'] 
        and not values[1].isdigit()
        and not 1 >= int(values[2]) <= 5 
        and values[3].upper() not in ['Y', 'N']
        and values[4].upper() not in ['CS', 'W'] 
        and not 1 >= int(values[5]) <= 5):
            print('Invalid input.')
        else:
            print('The data has been validated.\n')
    except ValueError as e:
        print(f'Invalid data {e}, please try again.\n') 

add_data()

