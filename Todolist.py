from tabulate import tabulate
import os
import csv


FileName = 'Todo.csv'

def main():
    print("\n To-Do List \n")
    running = True
    check_file = os.path.isfile(FileName)
    if not (check_file):
        Create_Csv_File()

    while running:
        action = get_input()
        if action == "V":
            view()
            _ = input("Enter Any Key For Main Menu: ")
        elif action == "A":
            Add()
        elif action == "U":
            updateAction = Get_updateActionInput()
            if updateAction == "T":
                UpdateTask()
            elif updateAction == "S":
                UpdateStatus()
            else:
                _=0
        elif action == "D":
           delete()
        else:
            running = False



def Get_updateActionInput():
    instructions = [{"Key": "T", "Action": "To Change Task"},
                    {"Key": "S", "Action": "TO Change Status"},]
    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_grid", maxcolwidths=[None, 30]))
        action = input("What do you want to do?: ").upper()
        if action in ["T", "S"]:
            return action
        else:
            print("Invalid Input, Please Select the Key Value.")



def get_input():
    instructions = [{"Key": "V", "Action": "View Tasks"},
                    {"Key": "A", "Action": "Add a Task"},
                    {"Key": "U", "Action": "Update a Task"},
                    {"Key": "D", "Action": "Delete a Task"},
                    {"Key": "E", "Action": "Exit"}]
    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_grid", maxcolwidths=[None, 30]))
        action = input("What do you want to do?: ").upper()
        if action in ["V", "A", "U", "D", "E"]:
            return action
        else:
            print("Invalid Input, Please Select the Key Value.")



def Create_Csv_File():
    with open(FileName , 'w') as file:
        writer = csv.DictWriter(file ,fieldnames=["Id","Task","Status"])
        writer.writerow({"Id": "Id", "Task":"Task" , "Status": "Status" })



def view():
    database =[]
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})
    print(tabulate(database , headers="keys" ,tablefmt="rounded_grid"))



def Add():
    i=1
    database =[]
    lastid = ''
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file )
        for row in reader:
            database.append({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})
            i = i+1
            lastid=row["Id"]
        if lastid == str(i):
            i = i+1
        file.close()

    task = input("Task: ")
    database.append({"Id":i ,"Task":task , "Status":'pending'})
    with open(FileName, 'w', newline='') as file:
        writer = csv.DictWriter(file ,fieldnames=["Id","Task","Status"])
        writer.writerow({"Id": "Id", "Task":"Task" , "Status": "Status" })
        for row in database :
            writer.writerow({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})


def delete():
    numbers = []
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file )
        for row in reader:
            if row["Id"]=="Id":
                _=0
            else:
                numbers.append(int(row["Id"]))

    while True:
        view()
        try:
            i = int(input("Enter Task Id To Delete The Task: "))
            if i in numbers:
                break
            else:
                print("Invalid task ID, try again.")

        except ValueError:
            print("Invalid input, try again.")


    database =[]
    databasenew =[]
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file )
        for row in reader:
            database.append({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})
        file.close()

    for j in database:
        if j["Id"] == str(i):
            _=0
        else:
            databasenew.append({"Id":j["Id"] ,"Task":j["Task"],"Status":j["Status"]})

    with open(FileName, 'w', newline='') as file:
        writer = csv.DictWriter(file ,fieldnames=["Id","Task","Status"])
        writer.writerow({"Id": "Id", "Task":"Task" , "Status": "Status" })
        for row in databasenew :
            writer.writerow({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})

def UpdateTask():
    numbers = []
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file )
        for row in reader:
            if row["Id"]=="Id":
                _=0
            else:
                numbers.append(int(row["Id"]))

    while True:
        view()
        try:
            i = int(input("Enter Task Id To Change Task: "))
            if i in numbers:
                break
            else:
                print("Invalid task ID, try again.")

        except ValueError:
            print("Invalid input, try again.")


    database =[]
    databasenew =[]
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file )
        for row in reader:
            database.append({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})
        file.close()

    for j in database:
        if j["Id"] == str(i):
            task = input("Updated Task: ")
            databasenew.append({"Id":j["Id"] ,"Task":task,"Status":j["Status"]})
        else:
            databasenew.append({"Id":j["Id"] ,"Task":j["Task"],"Status":j["Status"]})

    with open(FileName, 'w', newline='') as file:
        writer = csv.DictWriter(file ,fieldnames=["Id","Task","Status"])
        writer.writerow({"Id": "Id", "Task":"Task" , "Status": "Status" })
        for row in databasenew :
            writer.writerow({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})

def UpdateStatus():
    numbers = []
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file )
        for row in reader:
            if row["Id"]=="Id":
                _=0
            else:
                numbers.append(int(row["Id"]))

    while True:
        view()
        try:
            i = int(input("Enter Task Id To Change Task Status: "))
            if i in numbers:
                break
            else:
                print("Invalid task ID, try again.")

        except ValueError:
            print("Invalid input, try again.")


    database =[]
    databasenew =[]
    with open(FileName, newline='') as file:
        reader = csv.DictReader(file )
        for row in reader:
            database.append({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})
        file.close()

    for j in database:
        if j["Id"] == str(i):
            status = input("Updated Status: ")
            databasenew.append({"Id":j["Id"] ,"Task":j["Task"],"Status":status})
        else:
            databasenew.append({"Id":j["Id"] ,"Task":j["Task"],"Status":j["Status"]})

    with open(FileName, 'w', newline='') as file:
        writer = csv.DictWriter(file ,fieldnames=["Id","Task","Status"])
        writer.writerow({"Id": "Id", "Task":"Task" , "Status": "Status" })
        for row in databasenew :
            writer.writerow({"Id":row["Id"] ,"Task":row["Task"],"Status":row["Status"]})



if __name__ == "__main__":
    main()