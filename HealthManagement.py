import datetime
import os

print("Welcome to Health Management System")
print("How can we help you?: Press\n\t1 for store Diet or Workout of an individual"
      "\n\t2 for display Diet or Exercise of an individual")
store_or_retrieve = int(input(">>"))


# It will return date and time of diet or exercise
def getdate():
    return datetime.datetime.now()


# This function will store diet or workout of an individual at a time
def store_diet_exercise_plan(name, file_name):
    print("Here is the details of", name)
    print("please enter what do you want to lock. To finish enter 'done'")
    with open(file_name, 'a') as file:
        while True:
            lock_task = input(">>")
            if not lock_task.lower() == "done":
                file.write((str(getdate()) + " " + lock_task + "\n"))
            else:
                break


# This function will display diet or workout of an individual at a time
def retrieve_diet_exercise_plan(name, filename):
    if os.path.isfile("./" + filename):  # It checks whether the file exist or not
        print("Here is the details of: ", name)
        with open(filename, 'r') as file:
            if file.read():
                print(file.read())
            else:
                print("Sorry ! File is empty")
    else:
        print("File does not exist")


if store_or_retrieve == 1:
    print("You can lock Diet or Exercise of a person")
    print("Enter:\n\t1 for Harry\n\t2 for Rohan\n\t3 for Hammad")
    person_choice = int(input(">>"))
    diet_or_exercise = 0
    if person_choice in [1,2,3]:
        print("Which thing do you want to lock? \n\t1 for Diet\n\t2 for Exercise")
        diet_or_exercise = int(input(">>"))
        if person_choice == 1:
            if diet_or_exercise == 1:
                store_diet_exercise_plan("Harry", "harry_diet.txt")
            elif diet_or_exercise == 2:
                store_diet_exercise_plan("Harry", "harry_exercise.txt")
            else:
                print("invalid choice")

        elif person_choice == 2:
            if diet_or_exercise == 1:
                store_diet_exercise_plan("Rohan", "rohan_diet.txt")
            elif diet_or_exercise == 2:
                store_diet_exercise_plan("Rohan", "rohan_exercise.txt")
            else:
                print("invalid choice")

        elif person_choice == 3:
            if diet_or_exercise == 1:
                store_diet_exercise_plan("Hammad", "hammad_diet.txt")
            elif diet_or_exercise == 2:
                store_diet_exercise_plan("Hammad", "hammad_exercise.txt")
            else:
                print("invalid choice")
    else:
        print("invalid Choice")


elif store_or_retrieve == 2:
    print("To see data, please Enter:\n\t1 for Harry\n\t2 for Rohan\n\t3 for Hammad")
    person_choice = int(input(">>"))
    if person_choice in [1, 2, 3]:
        print("Which thing do you want to display?\n\t1 for Diet\n\t2 for Exercise")
        diet_or_exercise = int(input(">>"))
        if person_choice == 1:
            if diet_or_exercise == 1:
                retrieve_diet_exercise_plan("Harry", "harry_diet.txt")
            elif diet_or_exercise == 2:
                retrieve_diet_exercise_plan("Harry", "harry_exercise.txt")
            else:
                print("invalid choice")

        elif person_choice == 2:
            if diet_or_exercise == 1:
                retrieve_diet_exercise_plan("Rohan", "rohan_diet.txt")
            elif diet_or_exercise == 2:
                retrieve_diet_exercise_plan("Rohan", "rohan_exercise.txt")
            else:
                print("invalid choice")

        elif person_choice == 3:
            if diet_or_exercise == 1:
                retrieve_diet_exercise_plan("Hammad", "hammad_diet.txt")
            elif diet_or_exercise == 2:
                retrieve_diet_exercise_plan("Hammad", "hammad_exercise.txt")
            else:
                print("invalid choice")
    else:
        print("invalid Choice")
else:
    print("Invalid Choice")








