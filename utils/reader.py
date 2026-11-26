import csv


def read_users_csv():
    with open("data/users.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)