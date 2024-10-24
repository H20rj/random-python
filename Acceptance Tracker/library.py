## Acceptance tracker library

import time
from colorama import Fore
import pwinput
ou_status = 'Under Review'
csu_status = 'Under Review'
cu_status = 'Under Review'
tt_status = 'Under Review'
tr_status = 'Under Review'
du_status = 'Under Review'
mi_status = 'Under Review'


def change_status():
    global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
    print(Fore.CYAN + "What school would you like to change?")
    print(Fore.YELLOW + """
        1. OU
        2. CSU
        3. CU Boulder
        4. Texas Tech
        5. Trinity
        6. DU
        7. Mines
    """)
    school = input(Fore.GREEN + "Enter choice here (1/2/3/4/5/6/7): ")

    while school not in ['1', '2', '3', '4', '5', '6', '7']:
        print(Fore.RED + "Invalid input.")
        school = input(Fore.GREEN + "Enter choice here (1/2/3/4/5/6/7): ")

    school_dict = {
        '1': 'OU',
        '2': 'CSU',
        '3': 'CU Boulder',
        '4': 'Texas Tech',
        '5': 'Trinity',
        '6': 'DU',
        '7': 'Mines'
    }

    print(Fore.CYAN + "What would you like to change the status to?")
    print(Fore.YELLOW + """
       1. Accepted
       2. Rejected
       3. Under Review
       4. Waitlisted
       5. Deferred
    """)

    new_status = input(Fore.GREEN + "Enter choice here (1/2/3/4/5): ")

    while new_status not in ['1', '2', '3', '4', '5']:
        print(Fore.RED + "Invalid input.")
        new_status = input(Fore.GREEN + "Enter choice here (1/2/3/4/5): ")

    status_mapping = {
        '1': 'Accepted',
        '2': 'Rejected',
        '3': 'Under Review',
        '4': 'Waitlisted',
        '5': 'Deferred'
    }

    new_status = status_mapping[new_status]

    if school == '1':
        global ou_status
        ou_status = new_status
    elif school == '2':
        global csu_status
        csu_status = new_status
    elif school == '3':
        global cu_status
        cu_status = new_status
    elif school == '4':
        global tt_status
        tt_status = new_status
    elif school == '5':
        global tr_status
        tr_status = new_status
    elif school == '6':
        global du_status
        du_status = new_status
    elif school == '7':
        global mi_status
        mi_status = new_status

    print(Fore.GREEN + f"{school_dict[school]} status now set to {new_status}.")


def view_status():
    print(Fore.CYAN + f"OU: {ou_status}")
    time.sleep(0.1)
    print(Fore.CYAN + f"CSU: {csu_status}")
    time.sleep(0.1)
    print(Fore.CYAN + f"CU Boulder: {cu_status}")
    time.sleep(0.1)
    print(Fore.CYAN + f"Texas Tech: {tt_status}")
    time.sleep(0.1)
    print(Fore.CYAN + f"Trinity: {tr_status}")
    time.sleep(0.1)
    print(Fore.CYAN + f"DU: {du_status}")
    time.sleep(0.1)
    print(Fore.CYAN + f"Mines: {mi_status}")
    time.sleep(0.1)


def save_status():
    with open('saves/status.txt', 'w') as file:
        file.write(f"OU status: {ou_status}\n")
        file.write(f"CSU status: {csu_status}\n")
        file.write(f"CU Boulder status: {cu_status}\n")
        file.write(f"Texas Tech status: {tt_status}\n")
        file.write(f"Trinity status: {tr_status}\n")
        file.write(f"DU status: {du_status}\n")
        file.write(f"Mines status: {mi_status}\n")
    print(Fore.GREEN + "Status saved successfully.")


def load_status():
    global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
    try:
        with open('saves/status.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if 'OU status' in line:
                    ou_status = line.split(':')[1].strip()
                elif 'CSU status' in line:
                    csu_status = line.split(':')[1].strip()
                elif 'CU Boulder status' in line:
                    cu_status = line.split(':')[1].strip()
                elif 'Texas Tech status' in line:
                    tt_status = line.split(':')[1].strip()
                elif 'Trinity status' in line:
                    tr_status = line.split(':')[1].strip()
                elif 'DU status' in line:
                    du_status = line.split(':')[1].strip()
                elif 'Mines status' in line:
                    mi_status = line.split(':')[1].strip()
        print(Fore.GREEN + "Status loaded successfully.")
    except FileNotFoundError:
        print(Fore.RED + "No saved status found. Using default values.")
        default()


def default():
    global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
    ou_status = 'Under Review'
    csu_status = 'Under Review'
    cu_status = 'Under Review'
    tt_status = 'Under Review'
    tr_status = 'Under Review'
    du_status = 'Under Review'
    mi_status = 'Under Review'
    print(Fore.GREEN + "Status reset to defaults.")


def opening():
    print(Fore.CYAN + """
    ╔═════════════════════════════════════════════════╗
    ║   Welcome to the Acceptance Tracker!            ║
    ║   Track your college application status         ║
    ╚═════════════════════════════════════════════════╝
    """)


def authentication():

    with open('saves/credentials.txt') as f:
        correct_username, correct_password = f.read().split('\n')
    print(correct_username, correct_password)
    print("Please enter your username and password below.")
    username = input("Username: ")
    password = pwinput.pwinput("Password: ", "*")

    if username == correct_username and password == correct_password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed. Please try again.")
        return False

def set_user_pw():

    check = authentication()
    if check:
        correct_username = input("Enter a new username: ")
        correct_password = pwinput.pwinput("Enter a new password: ", "*")
        with open('saves/credentials.txt', 'w') as f:
            f.write(f"{correct_username}\n{correct_password}")
        print("Credentials saved successfully.")