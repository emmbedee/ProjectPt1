import csv


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


def check_valid(name, score):
    if name.strip().isdigit():
        raise TypeError
    if score.strip().isalpha():  # check if score is not a number, account for spaces
        raise TypeError
    score = float(score)
    if (score > 100) or (score < 0):  # check range
        raise ValueError
    else:
        return name.strip().upper(), determine_grade(score)  # all good


def input_loop():
    iterable = []
    while True:
        try:
            name = input('Please enter student name: ')
            final_score = input('Please enter student score: ')
            iterable.append(check_valid(name, final_score))
        except TypeError:
            print('TypeError exception raised, please enter student NAME and SCORE in appropriate input locations!')
        except ValueError:
            print('ValueError exception raised, SCORE input should be between 0-100!')


def export_file(iterable):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(iterable)


input_loop()
