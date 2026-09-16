#conditional statement 

# if condition/scenario:
#     statement/block of code to be executed 

# age = 10
# if age > 18:
#     print("you can vote")
# else:
#     print("You cannot vote")

# password = "nepal12366"

# if password=="nepal123":
#     print("login success, password matched")
# else:
#     print("Login failed, password didnt matched")

# marks = 71

# if marks >= 90:
#     print("A+ aayo")
# elif marks >= 80:
#     print("A aayo")
# elif marks >=70:
#     print("B+ aayo")
# else:
#     print("fail vaiyo")

#LOGIN system --> email, passsword 
# email, password -- both correct xa vane , login else failed

# email = "hello@gmail.com"
# password = "hello1233434"

# if email == "hello@gmail.com":
#     if password == "hello123":
#         print("Login succesfull, match vayo")

# if email=="hello@gmail.com" or password=="hello123":
#     print("Login successfull, match vayo")
# else:
#     print("Login failed")

# logged_in = False 

# if not logged_in:
#     print("Please login")


# for i in range(5):
#     print(i)

# for i in range(2,11,4):
#     print(i)

# for i in range(10,0,-2):
#     print(i)


countries = ["japan","usa","nepal"]

# for country in countries:
#     print(country)


prediction_scores = [77,99,23,67]

# loop predicton_scores , and jasko value greater than 80 xa teslai good vanera print garne else not good score


for score in prediction_scores:
    if score > 80:
        print(score,"Good score")
    else:
        print(score,"Bad score")

emails_lists = [
    "Bhatbhateeni ma discount", 
    "Yeti airlines free ticket congrats jityo", 
    "What is the project update guys?",
    "Congratulationss, you won rolex watch" 
]

for email in emails_lists:
    if "congrats" in email or "Congratulationss" in email or "discount" in email : 
        print("Spam ho:", email)
    else:
        print("Not spam", email)