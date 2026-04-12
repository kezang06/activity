students_list = []        
grades_set = set()        
students_dict = {}        

students_list.append("Kezang")
grades_set.add("k")
students_dict["Kezang"] = {"Age": 23, "Grade": "K"}

students_list.append("Dechen")
grades_set.add("D")
students_dict["Dechen"] = {"Age": 22, "Grade": "D"}

students_list.append("Jigme")
grades_set.add("J")
students_dict["Jigme"] = {"Age": 21, "Grade": "J"}

students_list.append("Yoezer")
grades_set.add("Y")
students_dict["Yoezer"] = {"Age": 23, "Grade": "Y"}

search_name = input("Enter the name of the student to search: ")
if search_name in students_list:
    print(f"Student found! Name: {search_name}, Age: {students_dict[search_name]['Age']}, Grade: {students_dict[search_name]['Grade']}")
else:
    print("Student not found.")

remove_name = input("Enter the name of the student to remove or press Enter to skip: ")
if remove_name in students_list:
    remove_grade = students_dict[remove_name]["Grade"]
    
    students_list.remove(remove_name)
    del students_dict[remove_name]

    if remove_grade not in [info["Grade"] for info in students_dict.values()]:
        grades_set.remove(remove_grade)

    print("Student removed successfully.")
    print("Students available along with their details:", students_dict)
    print("Just available student names:", students_list)
    print("Just the grades available:", grades_set)

else:
    print("Student not found.")
