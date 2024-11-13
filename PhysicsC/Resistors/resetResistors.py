"""
Used for resetting the resistance_save.txt file.
"""

def reset_resistors():


    try:
        with open('resistance_save.txt', 'r') as f:
            current_save = f.read()

        if current_save == "":
            print("save already empty")
            print("No save yet. Please create one in resistors.py")
        else:
            with open('resistance_save.txt', 'w') as f:
                f.write("No resistors save yet. Please make one in resistors.py")

    except FileNotFoundError:
        print("file not found please create a file called:\nresistance_save.txt")


if __name__ == "__main__":
    reset_resistors()