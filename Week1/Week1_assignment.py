print("Welcome to the DPLMS Student Registration System")

courses_list = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]

print("The available courses are:")
for index, course in enumerate(courses_list):
    print(f"{index + 1}. {course}")

print("\n")

student_name = input("Enter your full name: ")
email = input("Enter your email: ")
age = int(input("Enter your age: "))
selected_course = input("Enter the course you want to study: ")

student_info = {
    "student_name" : student_name,
    "email" : email,
    "age" : age,
    "selected_course" : selected_course
}

print("\n")

if student_info["selected_course"] in courses_list:
    print("Registration Successfull!!")
    print("The description of the student is: ")
    print(f"Name : {student_name}")
    print(f"Email : {email}")
    print(f"age: {age}")
    print(f"Selected Course: {selected_course}")
else:
    print("Course Not Available")


