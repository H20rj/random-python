"""Formats strings given in format AADCBAEA: answers"""


def main() -> None:
    """Main Function"""
    string = "AADA BCAC DDBA BCBC CBCB DDAA".lower().replace(" ", "")

    answer_dict: dict[str, str] = {}
    iterations = 0
    output = ""
    temp_put = ""
    for i in string:
        iterations += 1
        answer_dict[str(iterations)] = i
        temp_put = f"{iterations}: {i}\n"
        output = output + temp_put
    print(temp_put)


if __name__ == "__main__":
    main()
