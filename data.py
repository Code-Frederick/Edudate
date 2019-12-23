import csv
import os.path
from tutors import *

def get_data():
    tutors = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data/StudentTutors.csv")
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                tutor = Tutor()
                tutor.id = str(line_count)
                tutor.name = row[0]
                tutor.grade = row[1]
                tutor.personality = row[2]
                tutor.image = row[3]
                tutor.school = row[4]
                tutor.bio = row[5]
                tutor.email = row[6]
                tutor.subject = row[7]
                tutors.append(tutor)
                line_count += 1
        print(f'Processed ' + str(len(tutors)) + ' lines.')
    return tutors