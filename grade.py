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
    return print("Grade = {}".format(grade))

def check_valid(score):
    if score.strip().isalpha():  # check if input is not a number, account for spaces
        return print('Invalid score.')
    score = float(score)  # if number, change to float
    if (score > 100) or (score < 0):  # check if range is valid
        return print('Invalid score.')
    else:
        return determine_grade(score)  # all good