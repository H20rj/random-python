from math import atan

def get_monitor_size() -> int or float:
    while True:
        monitor_size1 = input("What is your monitor's size?: ")
        try:
            monitor_size1 = float(monitor_size1)
            return monitor_size1

        except ValueError:
            print("Incorrect, value must be a number. Try again>")





def get_monitor_resolution() -> tuple[int, int]:
    while True:
        resolution = input("What is your monitors resolution? (x*y):")
        if '*' in resolution:
            parts = resolution.split("*")
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                x_res, y_res = map(int, parts)
                if x_res > 0 and y_res > 0:
                    return x_res, y_res
                else:
                    print("Correct formatting, however values must be positive integers. Try again.")
            else:
                print("Incorrect formatting, please enter two numbers. Try again.")
        else:
            print("Incorrect formatting, input must include '*' (x*y). Try again.")


def get_lower_left_angle(width, height) -> float:
    angle = atan(height/width)
    return angle

