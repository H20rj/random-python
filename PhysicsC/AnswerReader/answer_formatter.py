STRING = "AADA BCAC DDBA BCBC CBCB DDAA".lower().replace(" ", "")


answerDict: dict[str, str] = {}
ITERATIONS = 0
OUTPUT = ""
TEMP_PUT = ""
for i in STRING:
    ITERATIONS += 1
    answerDict[str(ITERATIONS)] = i
    TEMP_PUT = f"{ITERATIONS}: {i}\n"
    OUTPUT = OUTPUT + TEMP_PUT
print(TEMP_PUT)
