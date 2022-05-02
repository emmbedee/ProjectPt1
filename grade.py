import csv


def determine_grade(score):
    if (score > 100) or (score < 0):
        raise ValueError
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


def input_loop():
    iterable = []
    while True:
        try:
            name = input('Please enter student name: ')
            final_score = input('Please enter student score: ')
            if name.strip().isdigit():
                raise TypeError
            if final_score.strip().isalpha():
                raise TypeError
            final_score = int(final_score)
            iterable.append(name)
            iterable.append(determine_grade(final_score))
        except TypeError:
            print('Please enter student NAME and SCORE in appropriate input locations!')
        except ValueError:
            print('ValueError exception raised, SCORE input should be between 0-100!')


def export_file(iterable):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(iterable)


input_loop()
