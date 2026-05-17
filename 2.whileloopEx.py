no_of_students = int(input("Enter the number of students: "))
i = 1 
student_names = {} #empty dictionary to store student names 
while i <= no_of_students: #condition
    name = input("Enter name of the student: ") #input name of the student
    print("The name of the student {} is {}".format(i, name)) 
    i += 1 #incrementing the value of i by 1
    student_names[i] = name #it adds the name of the student to the dictionary Student_names with the key as the value of i

print(student_names)
  
while True:
    print("This is an infinite loop. Press Ctrl+C to stop it.")