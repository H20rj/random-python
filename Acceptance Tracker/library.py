# ### Library for functions in Acceptance tracker. OU, CSU, CU Boulder, Texas Tech,
# # Colorado School of Mines, Trinity, and University of Denver
#
# import time
#
# ou_status = 'Under Review'
# csu_status = 'Under Review'
# cu_status = 'Under Review'
# tt_status = 'Under Review'
# tr_status = 'Under Review'
# du_status = 'Under Review'
# mi_status = 'Under Review'
#
# def change_status():
#     global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
#     print("What school would you like to change?")
#     print("     1. OU")
#     print("     2. CSU")
#     print("     3. CU Boulder")
#     print("     4. Texas Tech")
#     print("     5. Trinity")
#     print("     6. DU")
#     print("     7. Mines")
#     school = input("Enter choice here (1/2/3/4/5/6/7): ")
#
#
#     while not school in ['1', '2', '3', '4', '5', '6', '7']:
#         print("Invalid input.")
#         school = input("Enter choice here: ")
#
#
#     if school == '1':
#         school = 'OU'
#
#         print("What would you like to change the status to?")
#         print("       1. Accepted")
#         print("       2. Rejected")
#         print("       3. Under Review")
#         print("       4. Waitlisted")
#         print("       5. Deferred")
#         ou_status = input("Enter choice here (1/2/3/4/5): ")
#         while not ou_status in ['1', '2', '3', '4', '5']:
#             print("Invalid input.")
#             ou_status = input("Enter choice here (1/2/3/4/5): ")
#         if ou_status == '1':
#             ou_status = 'Accepted'
#         if ou_status == '2':
#             ou_status = 'Rejected'
#         if ou_status == '3':
#             ou_status = 'Under Review'
#         if ou_status == '4':
#             ou_status = 'Waitlisted'
#         if ou_status == '5':
#             ou_status = 'Deferred'
#         print(f"{school} status now set to {ou_status}.")
#     elif school == '2':
#         school = 'CSU'
#
#         print("What would you like to change the status to?")
#         print("       1. Accepted")
#         print("       2. Rejected")
#         print("       3. Under Review")
#         print("       4. Waitlisted")
#         print("       5. Deferred")
#         csu_status = input("Enter choice here (1/2/3/4/5): ")
#
#         while not csu_status in ['1', '2', '3', '4', '5']:
#             print("Invalid input.")
#             csu_status = input("Enter choice here (1/2/3/4/5): ")
#
#         if csu_status == '1':
#             csu_status = 'Accepted'
#         if csu_status == '2':
#             csu_status = 'Rejected'
#         if csu_status == '3':
#             csu_status = 'Under Review'
#         if csu_status == '4':
#             csu_status = 'Waitlisted'
#         if csu_status == '5':
#             csu_status = 'Deferred'
#
#         print(f"{school} status now set to {csu_status}.")
#     elif school == '3':
#         school = 'CU Boulder'
#
#         print("What would you like to change the status to?")
#         print("       1. Accepted")
#         print("       2. Rejected")
#         print("       3. Under Review")
#         print("       4. Waitlisted")
#         print("       5. Deferred")
#         cu_status = input("Enter choice here (1/2/3/4/5): ")
#         while not cu_status in ['1', '2', '3', '4', '5']:
#             print("Invalid input.")
#             cu_status = input("Enter choice here (1/2/3/4/5): ")
#
#         if cu_status == '1':
#             cu_status = 'Accepted'
#         if cu_status == '2':
#             cu_status = 'Rejected'
#         if cu_status == '3':
#             cu_status = 'Under Review'
#         if cu_status == '4':
#             cu_status = 'Waitlisted'
#         if cu_status == '5':
#             cu_status = 'Deferred'
#         print(f"{school} status now set to {cu_status}.")
#     elif school == '4':
#         school = 'Texas Tech'
#
#         print("What would you like to change the status to?")
#         print("       1. Accepted")
#         print("       2. Rejected")
#         print("       3. Under Review")
#         print("       4. Waitlisted")
#         print("       5. Deferred")
#         tt_status = input("Enter choice here (1/2/3/4/5): ")
#         while not tt_status in ['1', '2', '3', '4', '5']:
#             print("Invalid input.")
#             tt_status = input("Enter choice here (1/2/3/4/5): ")
#         if tt_status == '1':
#             tt_status = 'Accepted'
#         if tt_status == '2':
#             tt_status = 'Rejected'
#         if tt_status == '3':
#             tt_status = 'Under Review'
#         if tt_status == '4':
#             tt_status = 'Waitlisted'
#         if tt_status == '5':
#             tt_status = 'Deferred'
#         print(f"{school} status now set to {tt_status}.")
#     elif school == '5':
#         school = 'Trinity'
#
#         print("What would you like to change the status to?")
#         print("        1. Accepted")
#         print("        2. Rejected")
#         print("        3. Under Review")
#         print("        4. Waitlisted")
#         print("        5. Deferred")
#         tr_status = input("Enter choice here (1/2/3/4/5): ")
#
#         while not tr_status in ['1', '2', '3', '4', '5']:
#             print("Invalid input.")
#             tr_status = input("Enter choice here (1/2/3/4/5): ")
#         if tr_status == '1':
#             tr_status = 'Accepted'
#         if tr_status == '2':
#             tr_status = 'Rejected'
#         if tr_status == '3':
#             tr_status = 'Under Review'
#         if tr_status == '4':
#             tr_status = 'Waitlisted'
#         if tr_status == '5':
#             tr_status = 'Deferred'
#         print(f"{school} status now set to {tr_status}.")
#     elif school == '6':
#         school = 'DU'
#
#         print("What would you like to change the status to?")
#         print("         1. Accepted")
#         print("         2. Rejected")
#         print("         3. Under Review")
#         print("         4. Waitlisted")
#         print("         5. Deferred")
#         du_status = input("Enter choice here (1/2/3/4/5): ")
#         while not du_status in ['1', '2', '3', '4', '5']:
#             print("Invalid input.")
#             du_status = input("Enter choice here (1/2/3/4/5): ")
#         if du_status == '1':
#             du_status = 'Accepted'
#         if du_status == '2':
#             du_status = 'Rejected'
#         if du_status == '3':
#             du_status = 'Under Review'
#         if du_status == '4':
#             du_status = 'Waitlisted'
#         if du_status == '5':
#             du_status = 'Deferred'
#         print(f"{school} status now set to {du_status}.")
#     elif school == '7':
#         school = 'Mines'
#
#         print("What would you like to change the status to?")
#         print("          1. Accepted")
#         print("          2. Rejected")
#         print("          3. Under Review")
#         print("          4. Waitlisted")
#         print("          5. Deferred")
#         mi_status = input("Enter choice here (1/2/3/4/5): ")
#         while not mi_status in ['1', '2', '3', '4', '5']:
#             print("Invalid input.")
#             mi_status = input("Enter choice here (1/2/3/4/5): ")
#         if mi_status == '1':
#             mi_status = 'Accepted'
#         if mi_status == '2':
#             mi_status = 'Rejected'
#         if mi_status == '3':
#             mi_status = 'Under Review'
#         if mi_status == '4':
#             mi_status = 'Waitlisted'
#         if mi_status == '5':
#             mi_status = 'Deferred'
#         print(f"{school} status now set to {mi_status}.")
#
# def view_status():
#     global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
#     print(f"OU: {ou_status}\n")
#     time.sleep(0.1)
#     print(f"CSU: {csu_status}\n")
#     time.sleep(0.1)
#     print(f"CU Boulder: {cu_status}\n")
#     time.sleep(0.1)
#     print(f"Texas tech: {tt_status}\n")
#     time.sleep(0.1)
#     print(f"Trinity: {tr_status}\n")
#     time.sleep(0.1)
#     print(f"DU: {du_status}\n")
#     time.sleep(0.1)
#     print(f"Mines: {mi_status}\n")
#     time.sleep(0.1)
#
# def save_status():
#     with open('status.txt', 'w') as file:
#         file.write(f"OU status: {ou_status}\n")
#         file.write(f"CSU status: {csu_status}\n")
#         file.write(f"CU Boulder status: {cu_status}\n")
#         file.write(f"Texas tech status: {tt_status}\n")
#         file.write(f"Trinity status: {tr_status}\n")
#         file.write(f"DU Status: {du_status}\n")
#         file.write(f"Mines status: {mi_status}\n")
#
# def load_status():
#     global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
#     with open('status.txt', 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             if 'OU status' in line:
#                 ou_status = line.split(':')[1].strip()
#             elif 'CSU status' in line:
#                 csu_status = line.split(':')[1].strip()
#             elif 'CU Boulder status' in line:
#                 cu_status = line.split(':')[1].strip()
#             elif 'Texas tech status' in line:
#                 tt_status = line.split(':')[1].strip()
#             elif 'Trinity status' in line:
#                 tr_status = line.split(':')[1].strip()
#             elif 'DU Status' in line:
#                 du_status = line.split(':')[1].strip()
#             elif 'Mines status' in line:
#                 mi_status = line.split(':')[1].strip()
#
# def default():
#     global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
#     ou_status = 'Under Review'
#     csu_status = 'Under Review'
#     cu_status = 'Under Review'
#     tt_status = 'Under Review'
#     tr_status = 'Under Review'
#     du_status = 'Under Review'
#     mi_status = 'Under Review'
#
# def opening():
#     print("Welcome to the Acceptance Tracker!")
#     print("The acceptance tracker is an exciting tool that allows me to keep track of where I am in my acceptance process.")

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
    with open('status.txt', 'w') as file:
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
        with open('status.txt', 'r') as file:
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

    with open('credentials.txt') as f:
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
        with open('credentials.txt', 'w') as f:
            f.write(f"{correct_username}\n{correct_password}")
        print("Credentials saved successfully.")