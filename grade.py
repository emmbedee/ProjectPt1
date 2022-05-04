import csv
import re


def determine_grade(score) -> str:
    """
    Function to determine letter grade from an int/float value.
    :param score: int/float value.
    :return: Letter grade.
    """
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


def check_name(name) -> bool | str:
    """
    Function to check STUDENT NAME user input by filtering any inputs that contain special characters or numbers.
    :param name: A string representing a student's name.
    :return: A stripped string of the students name.
    """
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    numbers = re.findall('[0-9]+', name)
    if numbers:
        return False
    if (regex.search(name.strip())) is None:
        return name.strip()
    else:
        return False


def check_score(score) -> bool | float:
    """
    Function to check STUDENT SCORE user input by filtering any inputs that are non-numeric or outside range (0-100 inclusive).
    :param score: Numeric string between 0-100 (inclusive) representing a student's score.
    :return: A float that is fit to be passed into the determine_grade function.
    """
    if score.strip().isalpha():
        return False
    score = float(score)
    if (score > 100) or (score < 0):
        return False
    else:
        return score


def save_file(iterable) -> None:
    """
    Function to write a new row based on user input and execution of the clicked() function.
    :param iterable: An iterable container containing the row to be written to the output file.
    """
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(iterable)