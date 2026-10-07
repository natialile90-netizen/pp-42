def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list


print(add_task("Attend the lesson"))
print(add_task("Do homework"))
print(add_task("Go for a walk"))



def add_task(task_name, task_list=None):
    if task_list is None:
        task_list = []

    task_list.append(task_name)
    return task_list


print(add_task("Attend the lesson."))
print(add_task("Do homework"))
print(add_task("Go for a walk"))

my_tasks = ["Do homework"]
print(add_task("Go for a walk", task_list=my_tasks))

#პირველ ვარიანტში ერთი სია იქმნება და ყოველ ჯერზე იქ ემატება ახალი დავალება. 
# ყველა გამოძახებისას რაც კი დავალება გვქონდა დამატებული, ყველა სიასში რჩება


#მეორე ვარიანტში თუ არ გადავცემთ სიას, ყოველ ჯერზე შეიქმნება ახალი სია
#და ამის გამო სულ ახალი დამატებული დავალებებია ყოველ გაშვებაზე