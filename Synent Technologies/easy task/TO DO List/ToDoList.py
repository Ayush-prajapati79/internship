print ("Ayush Prajapati's TO DO LIST")

def task():
    tasks = []
    print("welcome to TO DO LIST MANAGEMENT APPLICATION")

    total_task = int(input("ENTER HOW MANY TASKS YOU WANT TO ADD : "))
    for i in range(1 ,total_task +1):
        task_name= input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"today's task are : \n {tasks} ")

    while True:
        operation = int(input(" Enter 1- add \n Enter 2- update \n Enter 3- delete \n Enter 4- view \n Enter 5- exit \n "))
        if operation == 1:
            add = input("the the task you want to add :")
            tasks.append(add)
            print(f"task  {add} is added successfully")
        elif operation == 2:
            update_val =input("enter the task you want to Update ")
            if update_val  in tasks:
                up =input("add new task = ")
                ind = tasks.index(update_val)
                tasks[ind] =up
                print(f" task {up} UPDATED SUCCESSFULLY ")

        elif operation == 3:
            del_val =  input("which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"task {del_val}  is successfully deleted!!!")

        elif operation == 4:
            print(f"total task = {tasks}")

        elif operation == 5:
            print("closing the application ")
            break

        else :
            print("invalid input!!! please enter between 1 to 4 ")


task()