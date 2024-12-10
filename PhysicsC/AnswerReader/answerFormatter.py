string = "AADA BCAC DDBA BCBC CBCB DDAA".lower().replace(" ", "")


answerDict: dict[str, str] = {}
iterations = 0
output = ''
for i in string:
    iterations += 1
    answerDict[str(iterations)] = i
    temp_put = f"{iterations}: {i}\n"
    output = output + temp_put

print(output)