import csv
import re


def determine_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def check_name(name):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if name.strip().isdigit():
        return False
    if (regex.search(name.strip())) is None:
        return name
    else:
        return False


def check_score(score):
    if score.strip().isalpha():
        return False
    score = float(score)
    if (score > 100) or (score < 0):
        return False
    else:
        return score


def save_file(iterable):
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(iterable)

