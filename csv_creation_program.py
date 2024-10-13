# This program is used for easily adding entries to the csv file with the test results

from pandas import read_csv

FILENAME = "tests_results.csv"
INCLUDE_COMMENTS = True
PERSONALITY_TYPES = ["INTJ", 
                     "INTP", 
                     "ENTJ",
                     "ENTP",
                     "INFJ",
                     "INFP",
                     "ENFJ",
                     "ENFP",
                     "ISTJ",
                     "ISFJ",
                     "ESTJ",
                     "ESFJ",
                     "ISTP",
                     "ISFP",
                     "ESTP",
                     "ESFP",
                     "XXXX"]

df = read_csv(FILENAME, comment="#")
test_options = list(df.columns)[1:]

while True:
    new_row = []

    while True:
        input_type = input("Enter the personality type of the user: ")
        input_type = input_type.upper()
        if input_type in PERSONALITY_TYPES:
            break
        print("Incorrect input")
    
    new_row.append(input_type)

    for test in test_options:
        cell = []
        print(test.replace("_", " "))
        while True:
            while True:
                type = input(f"choose the personality type result: ")
                type = type.upper()
                if type in PERSONALITY_TYPES+["EXIT", ""]:
                    break
                print("Incorrect type")
            if type == "EXIT" or type == "":
                break
            cell.append(type)
        if cell == [] or cell == "":
            cell = ["XXXX"]
        new_row.append(";".join(cell))
    
    df.loc[len(df)] = new_row

    if INCLUDE_COMMENTS:
        with open(FILENAME, "w") as f:
            f.write("# file compiled by u/KomornikBank\n")
    df.to_csv(FILENAME, mode="a", index=False)