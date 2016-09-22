import csv
#
# with open("data.csv") as open_file:
#     contents = csv.reader(open_file, delimiter="|")
#     print(list(contents))

# clean_data = [row.replace("\n", "").split(",") for row in contents]

with open("date.csv") as open_file:
    contents = csv.DictReader(open_file)
    print(list(contents[1]["Water Temp"]))
