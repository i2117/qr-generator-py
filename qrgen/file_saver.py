import os

path = '/temporary_marks/'

def save_temp_marks_to_dir(marks, directory):
    if not os.path.exists(path + directory):
        os.makedirs(path + directory)
    for mark in marks:
        mark.save()

