import requests

all_tasks = requests.get("http://127.0.0.1:8080/tasks")
new_task = requests.post(
    "http://localhost:8080/tasks",
    json={"name": "Go shopping"}
)
mark = requests.put(
    "http://localhost:8080/tasks/3",
    json={"done": True}
)
del_task = requests.delete("http://localhost:8080/tasks/2")

print(all_tasks.json())
print(new_task.json())
print(mark.json())
print(del_task.json())
