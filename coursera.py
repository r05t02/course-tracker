#importing the course list

import json

with open('courses.json','r') as f:
    enrolled = json.load(f)


#To check if course_name is in the 'enrolled' dictionary
def validity_check(course_name):
    
    for key, value in enrolled.items():
        if course_name == key or course_name in value:
            print("VALID")
            return True
    print("INVALID")
    return False
            

#progress bar printer - prints empty progress bar
def progress_bar(mods, mods_finished):
    if mods == mods_finished:
        print("Course finished!!")
        progress_bar = "█" * mods_finished 
        print(progress_bar)
    else:
        progress_bar = "█" * mods_finished +"▒" * (mods - mods_finished)
        print(progress_bar)


        
# course progress to be tracked
def course_progress_check(course_name):
    #modules in course
    #redundant to ask user everytime, make a data structure which maps all courses to modules included in that course
    modules_in_course = int(input(f"How many modules are there in {course_name}?  "))

    modules_DONE = int(input(f"How many modules of {course_name} are complete?  "))

    prog_per = ((modules_DONE/modules_in_course) * 100)

    #progress
    progress_bar(modules_in_course, modules_DONE)
    print(f"Course completion percentage: {prog_per} %")





def specialization_progress(specialization_name):
    no_of_courses = len(enrolled[specialization_name])
    print(f"There are {no_of_courses} in {specialization_name}.")

    courses_DONE = int(input("how many courses have you completed?  "))

    #specialization progress
    
    prog_percentage = ((courses_DONE / no_of_courses) * 100)
    print(f"Specialization completion percentage = {prog_percentage} % ")
    progress_bar(no_of_courses, courses_DONE)



course_or_specialization = input("Enter course/ specialization to track progress:  ")

if validity_check(course_or_specialization):
    for key, val in enrolled.items():
        if course_or_specialization == key:
           specialization_progress(course_or_specialization)
           break
        elif course_or_specialization in val:
            course_progress_check(course_or_specialization)
            break


#load the data on first usage to json file AND read it from json file for next usage of program


#spec data
#  courses_DONE = int(input("how many courses have you completed?  "))

#course data
# modules_in_course = int(input(f"How many modules are there in {course_name}?  "))
# modules_DONE = int(input(f"How many modules of {course_name} are complete?  "))



