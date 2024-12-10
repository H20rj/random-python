print("Bow Aim Calculator")
print("(For 60 lb Diamond edge xt with stock sight)")

target_distance = int(input("How far are you from the target? (min 10ya): "))
print("")
print(target_distance)
off_by = int(input("How far was the shot off by on the target (Inches)?: "))
while 10 > target_distance or target_distance > 30:
    print("Value must be between 10 and 30")
    target_distance = int(input("How far are you from the target? (min 10ya): "))

if 10 <= target_distance < 15:   # 10-15 yards (One full tick = "")
    print("10 - 15 yard range selected.")
    print("In this range, one full tick on the sight equals '' ")



elif 15 <= target_distance < 20:   #15-20 yards (One full tick = "")
    print("15 - 20 yard range selected.")
    print("In this range, one full tick on the sight equals '' ")

elif 25 <= target_distance < 25:   #20-25 yards (One full tick = "")
    print("20 - 25 yard range selected.")
    print("In this range, one full tick on the sight equals '' ")


elif 25 <= target_distance < 30:
    print("25 - 30 yard range selected.")
    print("In this range, one full tick on the sight equals '' ")


