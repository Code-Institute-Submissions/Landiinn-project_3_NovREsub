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
SHEET = GSPREAD_CLIENT.open('project_3')

inventory = SHEET.worksheet('inventory')

input(type("What do you want to do?"))
print("1. Add items to inventory")
print("2. Remove items from inventory")
print("3. View Inventory")


def add_item():

    if type == int(1):
        print("What items do you want to add, and how many?")

        user_input = input("Enter: ")

        inventory = user_input

    return inventory

   
def update_inventory(data):

    print("Adding items to inventory...\n")
    inventory_worksheet = SHEET.worksheet("inventory")
    inventory_worksheet.append_row(data)
    print("Items added to inventory\n")


data = add_item()
update_inventory(inventory)