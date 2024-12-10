#string = 'AADA BCAC DDBA BCBC CBCB DDAA'.replace(' ','')
string = input("Enter a string of answers, no commas: \n").replace(" ", "")
iterations = 0
string_len= range(len(string))

for i in string_len:
    iterations += 1
    jump_to = input("Enter a number to jump to question: ")


    if jump_to.isdigit():
        jump_to_index = int(jump_to) - 1
        if jump_to_index in string_len:
            print(f'Answer for {jump_to}: {string[int(jump_to_index)]}')
            iterations = jump_to_index + 1
        else:
            print(f"Invalid question number: {jump_to}")
    elif jump_to == 'q':
        exit(1)
    else:
        if iterations-1 > max(string_len):
            print("no more answers")
            exit(2)
        print(f"Answer for question {iterations}: {string[iterations-1]}")

