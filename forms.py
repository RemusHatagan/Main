print("WELCOME TO THE SIGN UPS FOR THE CLUB")
print("")
 
fName = input("Please enter your first name >>> ")
lName = input("Please enter your last name >>> ")
gender = input("Please enter your gender >>> ")
schoolForm = input("Please enter your full form name >>> ")

while fName and lName and gender and schoolForm:
    forms = 0
    forms = forms + 1 
    form = '\nFirst name : '+fName+'\nLast name : ' + lName + '\nGender : ' +gender+ '\nForm : ' +schoolForm 
    file = open("signup.txt","a")
    file.write(form)
    file.close()
    
