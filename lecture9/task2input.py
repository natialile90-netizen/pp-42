def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list


for i in range(3):
    task = input("Enter a task: ")
    print(add_task(task))




