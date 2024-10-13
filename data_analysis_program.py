# this program is used to get the statistics for different test

from collections import Counter
from pandas import read_csv

FILENAME = "tests_results.csv"

df = read_csv(FILENAME, comment="#")
tests = list(df.columns)[1:]

def print_dict(dictionary: dict):
    dictionary_list = [(key, value) for key, value in dictionary.items()]
    dictionary_list = sorted(dictionary_list, key=lambda x: x[1], reverse=True)
    for test, values in dictionary_list:
        if type(test) == float:
            test = round(test, 3)
        if type(values) == float:
             values = round(values, 3)
        print(test, values)
    print("")

accuracy_for_each_test = dict()
data_points_for_each_test = dict()
for test in tests:
    included_results = 0
    correct_guesses = 0
    for index, result in enumerate(df[test]):
        incomplete = False
        results = result.split(";")
        for result in results:
            if result == "XXXX":
                incomplete = True
        if df.iloc[index]["type"] == "XXXX":
            incomplete = True
        if incomplete:
            continue
        included_results += len(results)
        for result in results:
            if result == df.iloc[index]["type"]:
                correct_guesses += 1
    accuracy_for_each_test[test] = correct_guesses/included_results
    data_points_for_each_test[test] = included_results

print_dict(accuracy_for_each_test)
print_dict(data_points_for_each_test)

participants = df[list(df.columns)[0]]
participation_count = Counter(participants)

print_dict(participation_count)