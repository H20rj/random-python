import time
from datetime import datetime
from os import system
from os.path import exists
from sys import platform
from library import (
    csu_status,
    cu_status,
    du_status,
    mi_status,
    ou_status,
    tr_status,
    tt_status,
)

import customtkinter
from colorama import Fore


if platform == "darwin":
    if not exists("saves/version.txt"):
        with open("saves/version.txt", "w") as f:
            f.write(str(datetime.now()))
        system("python3 -m pip install -r saves/requirements.txt")
if platform == "win32":
    if not exists("saves/version.txt"):
        with open("saves/version.txt", "w") as f:
            f.write(str(datetime.now()))
        system("py -m pip install -r saves/requirements.txt")
try:
    with open("saves/status.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "OU status" in line:
                ou_status = line.split(":")[1].strip()
            elif "CSU status" in line:
                csu_status = line.split(":")[1].strip()
            elif "CU Boulder status" in line:
                cu_status = line.split(":")[1].strip()
            elif "Texas Tech status" in line:
                tt_status = line.split(":")[1].strip()
            elif "Trinity status" in line:
                tr_status = line.split(":")[1].strip()
            elif "DU status" in line:
                du_status = line.split(":")[1].strip()
            elif "Mines status" in line:
                mi_status = line.split(":")[1].strip()
    print(Fore.GREEN + "Status loaded successfully.")
    with open("saves/credentials.txt", "r") as f:
        correct_username, correct_password = f.read().split("\n")
    print(Fore.GREEN + "Credentials loaded successfully.")
except FileNotFoundError:
    print(Fore.RED + "No saved status found. Using default values.")


def login():
    user = user_var.get()
    password = pass_var.get()

    print(user, password)
    if user == correct_username and password == correct_password:
        time.sleep(0.5)
        login_page.destroy()
        main_gui_open()  # Open the main GUI only on successful login
    else:
        try_again = customtkinter.CTkLabel(
            master=frame, text="Incorrect Username or Password", text_color="red"
        )
        try_again.pack(padx=0, pady=0)


# Main GUI function
def main_gui_open():
    global main_gui, ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
    main_gui = customtkinter.CTkToplevel()
    main_gui.title("Application Tracker")
    main_gui.geometry("300x600+620+160")
    mainframe = customtkinter.CTkFrame(master=main_gui)
    mainframe.pack(pady=20, padx=20, fill="both", expand=True)
    status_frame = customtkinter.CTkFrame(master=mainframe, width=225, height=250)
    status_frame.pack(pady=5, padx=20, fill="both", expand=True)
    status_frame.place(relx=0.5, rely=0.3, anchor="center")
    status = customtkinter.CTkLabel(
        master=status_frame,
        text=f"OU Status: {ou_status}\n\n"
        f"CSU Status: {csu_status}\n\n"
        f"CU Status: {cu_status}\n\n"
        f"Texas Tech Status: {tt_status}\n\n"
        f"Trinity Status: {tr_status}\n\n"
        f"DU Status: {du_status}\n\n"
        f"Mines Status: {mi_status}\n\n",
        text_color="white",
    )
    status.place(relx=0.50, rely=0.52, anchor="center")

    def reset_to_default():
        global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
        ou_status = "Under Review"
        csu_status = "Under Review"
        cu_status = "Under Review"
        tt_status = "Under Review"
        tr_status = "Under Review"
        du_status = "Under Review"
        mi_status = "Under Review"
        with open("saves/status.txt", "w") as file:
            file.write(f"OU status: {ou_status}\n")
            file.write(f"CSU status: {csu_status}\n")
            file.write(f"CU Boulder status: {cu_status}\n")
            file.write(f"Texas Tech status: {tt_status}\n")
            file.write(f"Trinity status: {tr_status}\n")
            file.write(f"DU status: {du_status}\n")
            file.write(f"Mines status: {mi_status}\n")
        print("Successfully reset to defaults.")

    button_frame = customtkinter.CTkFrame(master=mainframe, width=225, height=100)
    button_frame.pack(pady=15, padx=15, fill="both", expand=False)
    button_frame.place(relx=0.5, rely=0.8, anchor="center")
    change_status = customtkinter.CTkButton(
        master=button_frame, text="Change status", command=change_status_gui
    )
    change_status.pack(pady=12, padx=10)
    default_button = customtkinter.CTkButton(
        master=button_frame, text="Reset to default", command=reset_to_default
    )
    default_button.pack(pady=12, padx=10)
    change_pw_button = customtkinter.CTkButton(
        master=button_frame, text="Change Password", command=change_password
    )
    change_pw_button.pack(pady=12, padx=10)

    quit_button = customtkinter.CTkButton(
        master=button_frame, text="Quit", command=quit
    )
    quit_button.pack(pady=12, padx=10)


def change_status_gui():
    global change_status_page
    main_gui.withdraw()
    change_status_page = customtkinter.CTkToplevel()
    change_status_page.title("Change Status")
    change_status_page.geometry("225x300+670+260")
    change_frame = customtkinter.CTkFrame(master=change_status_page)
    change_frame.pack(pady=15, padx=15, fill="both", expand=True)

    def school_dropdown_callback(school):
        print(f"School: {school}")

    def status_dropdown_callback(status):
        print(f"Status: {status}")

    school_dropdown_var = customtkinter.StringVar(value="Select school")
    school_dropdown = customtkinter.CTkOptionMenu(
        master=change_frame,
        values=["OU", "CSU", "CU Boulder", "Texas Tech", "Trinity", "DU", "Mines"],
        command=school_dropdown_callback,
        variable=school_dropdown_var,
    )
    school_dropdown.pack(pady=12, padx=10)
    school_dropdown.place(relx=0.5, rely=0.2, anchor="center")
    status_dropdown_var = customtkinter.StringVar(value="Select status")
    status_dropdown = customtkinter.CTkOptionMenu(
        master=change_frame,
        values=[
            "Accepted",
            "Rejected",
            "Under Review",
            "Waitlisted",
            "Deferred",
            "Committed",
            "Pending Scholarship",
        ],
        command=status_dropdown_callback,
        variable=status_dropdown_var,
    )
    status_dropdown.pack(pady=12, padx=10)
    status_dropdown.place(relx=0.5, rely=0.4, anchor="center")

    def save_change_status():
        global ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status
        if school_dropdown_var.get() == "OU":
            ou_status = status_dropdown_var.get()
        elif school_dropdown_var.get() == "CSU":
            csu_status = status_dropdown_var.get()
        elif school_dropdown_var.get() == "CU Boulder":
            cu_status = status_dropdown_var.get()
        elif school_dropdown_var.get() == "Texas Tech":
            tt_status = status_dropdown_var.get()
        elif school_dropdown_var.get() == "Trinity":
            tr_status = status_dropdown_var.get()
        elif school_dropdown_var.get() == "DU":
            du_status = status_dropdown_var.get()
        elif school_dropdown_var.get() == "Mines":
            mi_status = status_dropdown_var.get()
        with open("saves/status.txt", "w") as file:
            file.write(f"OU status: {ou_status}\n")
            file.write(f"CSU status: {csu_status}\n")
            file.write(f"CU Boulder status: {cu_status}\n")
            file.write(f"Texas Tech status: {tt_status}\n")
            file.write(f"Trinity status: {tr_status}\n")
            file.write(f"DU status: {du_status}\n")
            file.write(f"Mines status: {mi_status}\n")
        print("saved")

    save_button = customtkinter.CTkButton(
        master=change_frame, text="Save", command=save_change_status
    )
    save_button.pack(pady=12, padx=10)
    save_button.place(relx=0.50, rely=0.65, anchor="center")
    exit_button = customtkinter.CTkButton(
        master=change_frame, text="Exit", command=exit_change_status
    )
    exit_button.pack(pady=12, padx=10)
    exit_button.place(relx=0.50, rely=0.85, anchor="center")


def exit_change_status():
    time.sleep(0.4)
    change_status_page.destroy()
    main_gui_open()


def quit_gui():
    with open("saves/status.txt", "w") as file:
        file.write(f"OU status: {ou_status}\n")
        file.write(f"CSU status: {csu_status}\n")
        file.write(f"CU Boulder status: {cu_status}\n")
        file.write(f"Texas Tech status: {tt_status}\n")
        file.write(f"Trinity status: {tr_status}\n")
        file.write(f"DU status: {du_status}\n")
        file.write(f"Mines status: {mi_status}\n")
    print("saved")
    time.sleep(0.4)
    main_gui.destroy()
    change_status_page.destroy()
    print("quit")


def change_password():
    global correct_username, correct_password
    with open("saves/credentials.txt", "r") as f:
        correct_username, correct_password = f.read().split("\n")
    print(Fore.GREEN + "Credentials loaded successfully.")

    old_user_var = customtkinter.StringVar()
    old_pw_var = customtkinter.StringVar()
    new_user_var = customtkinter.StringVar()
    new_pw_var = customtkinter.StringVar()

    main_gui.withdraw()
    change_pw_page = customtkinter.CTkToplevel()
    change_pw_page.title("Change Password")
    change_pw_page.geometry("300x550+600+150")
    change_pw_page.resizable(False, False)
    change_pw_frame = customtkinter.CTkFrame(master=change_pw_page)
    change_pw_frame.pack(pady=10, padx=10, fill="both", expand=True)
    change_pw_label = customtkinter.CTkLabel(
        master=change_pw_frame, text="Change Password", font=("", 24)
    )
    change_pw_label.pack(pady=12, padx=10)

    old_user_label = customtkinter.CTkLabel(master=change_pw_frame, text="Old Username")
    old_user_label.pack(pady=2, padx=10)
    entry_old_user = customtkinter.CTkEntry(
        master=change_pw_frame, textvariable=old_user_var
    )
    entry_old_user.pack(pady=12, padx=10)

    old_pw_label = customtkinter.CTkLabel(master=change_pw_frame, text="Old Password")
    old_pw_label.pack(pady=2, padx=10)
    entry_old_pw = customtkinter.CTkEntry(
        master=change_pw_frame, textvariable=old_pw_var, show="*"
    )
    entry_old_pw.pack(pady=12, padx=10)

    new_user_label = customtkinter.CTkLabel(master=change_pw_frame, text="New Username")
    new_user_label.pack(pady=2, padx=10)
    entry_new_user = customtkinter.CTkEntry(
        master=change_pw_frame, textvariable=new_user_var
    )
    entry_new_user.pack(pady=2, padx=10)
    new_pw_label = customtkinter.CTkLabel(master=change_pw_frame, text="New Password")
    new_pw_label.pack(pady=2, padx=10)
    entry_new_pw = customtkinter.CTkEntry(
        master=change_pw_frame, textvariable=new_pw_var, show="*"
    )
    entry_new_pw.pack(pady=2, padx=10)

    def check_password():
        if (
            old_user_var.get() == correct_username
            and old_pw_var.get() == correct_password
        ):
            print(new_user_var.get(), new_pw_var.get())
            success_label = customtkinter.CTkLabel(
                master=change_pw_frame,
                text="Correct username and password",
                text_color="green",
            )
            success_label.pack(pady=12, padx=10)
            try:
                with open("saves/credentials.txt", "w") as f:
                    f.write(f"{new_user_var.get()}\n{new_pw_var.get()}")
                print(Fore.GREEN + "New Password saved successfully.")
            except FileNotFoundError:
                print("Password not saved. Please try again later.")

        else:
            error_label = customtkinter.CTkLabel(
                master=change_pw_frame,
                text="Incorrect username or password",
                text_color="red",
            )
            error_label.pack(pady=12, padx=10)

    enter_button = customtkinter.CTkButton(
        master=change_pw_frame, text="Enter", command=check_password
    )
    enter_button.pack(pady=12, padx=10)

    def quit_change_pw():
        change_pw_page.destroy()
        time.sleep(0.4)
        main_gui_open()

    quit_change_pw_button = customtkinter.CTkButton(
        master=change_pw_frame, text="Exit", command=quit_change_pw
    )
    quit_change_pw_button.pack(pady=12, padx=10)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initialize the login page
login_page = customtkinter.CTk()
login_page.title("Login Page")
login_page.geometry("300x380+620+225")
login_page.resizable(False, False)

# Variables for username and password
user_var = customtkinter.StringVar()
pass_var = customtkinter.StringVar()


# Create the login frame
frame = customtkinter.CTkFrame(master=login_page)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=frame, text=f"Application Tracker \n Login", font=("", 24)
)
label.pack(pady=12, padx=10)

# Username Entry
user_label = customtkinter.CTkLabel(master=frame, text="Username")
user_label.pack(pady=2, padx=10)
entry = customtkinter.CTkEntry(
    master=frame, textvariable=user_var, placeholder_text="Username"
)
entry.pack(pady=12, padx=10)

# Password Entry
pass_label = customtkinter.CTkLabel(master=frame, text="Password")
pass_label.pack(pady=2, padx=10)
entryp = customtkinter.CTkEntry(
    master=frame, placeholder_text="Password", show="*", textvariable=pass_var
)
entryp.pack(pady=12, padx=10)

# Login Button
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

login_page.mainloop()
