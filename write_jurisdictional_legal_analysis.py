import python_interface
import datetime
import time
import csv

start_time_unix_ms = int(time.time() * 1000)
countries = open("jurisdictional_table/country_names.txt").read().split('\n')
print(countries)
laws = python_interface.generate_list("Write a list of controversial laws around the world")
laws += python_interface.generate_list("Write a long list of controversial laws around the world (subject to debate), diverse range")
# laws = python_interface.generate_list("Write a list of laws around the world with contentious issues, laws are subject to intense public debate and differing opinions across various political, cultural, and national lines")
for i in range(len(laws)):
    laws[i] = laws[i].split(":")[0]
    if 'vs.' in laws[i]:
        laws[i] = laws[i].split("vs.")[1]
    laws[i] = laws[i].strip()
print(laws)
res = [["Intended as parody and/or educational on generative llms"], [' '], [' ']]
res.append([""] + countries)
for L in laws:
    print(L, end="", flush=True)
    line = [L]
    for c in countries:
        print(" ", c, end="", flush=True)
        # line.append(python_interface.boolean_question(f"In {c} is {L} generally supported"))
        line.append(python_interface.boolean_question(f"In {c} is {L} endorsed by law"))
    print("\n", line)
    res.append(line)

end_time_unix_ms = int(time.time() * 1000)
formatted_time = str(datetime.timedelta(seconds=int(end_time_unix_ms - start_time_unix_ms) / 1000))[:-7]
time_str = "Chat with RTX Mistral took " + formatted_time + " to generate this"
res.append([' '])
res.append([time_str])
res.insert(1, [time_str])

res = [[1, 2], [3, 4, 5], [6]]
def longest_row(matrix):
    max_length = 0
    for row in matrix:
        if len(row) > max_length:
            max_length = len(row)
    return max_length
lr = longest_row(res)

def pad_subarrays(matrix, n):
    for i in range(len(matrix)):
        if len(matrix[i]) < n:
            additional_length = n - len(matrix[i])
            matrix[i].extend([' '] * additional_length)
    return matrix
res = pad_subarrays(res, lr)

file_path = 'jurisdictional_table/jurisdictional_table.csv'
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(res)
