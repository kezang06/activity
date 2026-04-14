# Student Information Management System

# create list and dictionary
students = [] # save student names in list
student_data = {} # save student details (name,age and grade) in dict

# add student name,age and grade
name = input("Enter name: ") # enter the name of the students
age = input("Enter age: ")  #enter the age of the students
student_grade = input("Enter grade: ") # enter the grade of the students

# check if student already exists or not
if name in student_data: # to check student exist or not
    print("already exists.") #print "already exists."
else:
    students.append(name) # add new student names
    student_data[name] = {"age": age, "grade": student_grade} #add details(age and grade)
    print("Student added.") #print "student added."

# display student records
print(" Student Details") # print "Student Details"

if student_data: # check if student records in dict
    for s in student_data: 
        print("Name:", s) # print student name
        print("Age:", student_data[s]["age"]) #print age
        print("Grade:", student_data[s]["grade"]) #print grade
else:
    print("Student not found.") #print "No student records found"

# Name searching
name_s = input("Enter name to search: ") #enter name to search

if name_s in student_data: # check if the name is in the dict
    print("Record found:") #print "Record found"
    print("Name:", name_s) # print the name of the student
    print("Age:", student_data[name_s]["age"]) #print the age of the student
    print("Grade:", student_data[name_s]["grade"]) #print the grade of the students
else:
    print("Student not found.") #print "Student not found"

# remove students 
remove_name = input("Enter name to remove: ") # enter name to remove

if remove_name in student_data: #check if the name is in the dict or not
    students.remove(remove_name) #remove name
    del student_data[remove_name] #delete info in dict
    print("Student record deleted.") #print "Student record deleted"
else: #check if the name in dict 
    print("Student not found.") #print "Student not found." 