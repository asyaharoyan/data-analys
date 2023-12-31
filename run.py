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
    "Did you contact to our customer service or did you complain through our website?(CS/W/NA): ",
    "How satisfied are you from our services? (1 - 5): ",
    ]
    while True:
        print('Please answer the questions.')

        for question in questions:
            answer = input(question)
            
            user_input.append(answer)
            
        if validate_data(user_input):
            print(f'The data has been validated.')
            break
        
    return user_input
    


def validate_data(values):
    """
    Validates the data provided by the user. 
    """
    try:
        int(values[2])
        int(values[5])
        values[0].upper()
        values[3].upper()
        values[4].upper()
        if (values[0] not in ['W', 'M', 'NONE']
        and not values[1].isdigit()
        and not (1 >= values[2] <= 5) 
        and values[3] not in ['Y', 'N']
        and values[4] not in ['CS', 'W', 'NA'] 
        and not (1 >= values[5] <= 5) or values == ''):
            print('Invalid input.')
        
    except ValueError as e:
        print(f'Invalid data {e}, please try again.\n') 
        return False
    return True



def update_analyse_data(user_data):
    """
    Updates the anayse sheet when the user input is validated
    """
    print('Updating the data... \n')
    data_analyse_worksheet = SHEET.worksheet('delivery')
    print(user_answers)
    data_analyse_worksheet.append_row(user_data)
    print('The worksheet has been updates successfully...\n')



user_answers = add_data()
update_analyse_data(user_answers)

