# Requires a signup.txt file in order to work

def main():
    sentry = True
    forms = 0
    while sentry == True:
        print("\u0332".join("WELCOME TO THE SIGN UPS FOR THE CLUB"))
        print("")
        
        fName = input("Please enter your first name >>> ")
        lName = input("Please enter your last name >>> ")
        gender = input("Please enter your gender >>> ")
        schoolForm = input("Please enter your full form name >>> ")

        file = open("signup.txt","a")
        if fName and lName and gender and schoolForm:
            form = ['\n',forms,".",'  First name: '+fName , '\n'
                    '   Last name: ' + lName , '\n'
                    '   Gender: ' +gender , '\n'
                    '   Form: ' +schoolForm , '\n'
                    ]
            for i in form:
                with open("signup.txt","a") as file:
                    file.write(str(i))
                    file.close()
        
        redo = input("Do you wish to input another form? (Y/N) >>> ").upper()
        if redo == "Y":
            forms = forms + 1
        else:
            exit()
main()
