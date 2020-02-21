import csv

try:
    f = open('database.csv','r')
    f.close()
except:
    with open('database.csv','w', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['Date','Student_Name'])

def writeCsvFile(data):
    with open('database.csv','a',encoding='UTF-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(data)

def checkName(Temp_name):
    with open("Student_information.csv", "r") as f:
        reader = csv.reader(f)
        for i in reader:
            if i[0] == Temp_name:
                return True
        return False

Menu = int(input("Select Menu: 1:Show the attendance sheet, 2:Enroll the student attendace"))

if Menu == 2:
    # Checking whether leader or not. Assume : Leader is SangJun.
    Name = input("Your_Name: ")
    Password = int(input("Password: "))

    if Name == "SangJun" and Password == 39:
        with open('Student_information.csv','r', newline='') as f:
            reader = csv.reader(f)
            while True:
                menu = input("c: check absences \nq: finish!")

                if menu == "c":
                    data = []
                    data.append(input("Date: "))
                    Temp_name = input("Student_Name: ")
                    if checkName(Temp_name):
                        data.append(Temp_name)
                        writeCsvFile(data)
                    else:
                        print("Error : Wrong Name!")

                elif menu == "q":
                    break

                else :
                    print("Error: You can only choose between c and q")

    if Name == "Ben" and Password == 4:
        with open('Student_information.csv','r', newline='') as f:
            reader = csv.reader(f)
            while True:
                menu = input("c: check absences \nq: finish!")

                if menu == "c":
                    data = []
                    data.append(input("Date: "))
                    Temp_name = input("Student_Name: ")
                    if checkName(Temp_name):
                        data.append(Temp_name)
                        writeCsvFile(data)
                    else:
                        print("Error : Wrong Name!")

                elif menu == "q":
                    break

                else :
                    print("Error: You can only choose between c and q")






elif Menu == 1:
    Option = int(input("1: Date criteria    2: Student criteria    3: Total data"))

    if Option == 1:
        with open("database.csv","r") as f:
            reader = csv.reader(f)
            Wanted_date = input("Wanted_date: ")
            print("Date | Student_Name")
            print("===============================")
            for i in reader:
                if i[0] == Wanted_date:
                    print(i[0],"|",i[1])

    elif Option == 2:
        with open("database.csv","r") as f:
            reader = csv.reader(f)
            Wanted_name = input("Wanted_name: ")
            if checkName(Wanted_name):
                print("Date | Student_Name")
                print("===============================")
                for i in reader:
                    if i[1] == Wanted_name:
                        print(i[0], "|", i[1])

            else:
                print("Error: Wrong Name!")

    elif Option == 3:
        with open('database.csv','r', newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                print(i[0], "|",i[1])
                if i == ['Date','Student_Name'] :
                    print("===============================")