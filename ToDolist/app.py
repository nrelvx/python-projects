from flask import Flask, request
from flask_restful import Api, Resource

# Create Flask app and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

tasks = {
    1: {"name": "Clean room", "done": False},
    2: {"name": "Buy milk", "done": False}
}


class Task(Resource):

    def get(self, task_id=0):
        """
        GET all tasks or a specific task by task_id.
        - If task_id is 0 or not provided, returns all tasks.
        - If task_id is provided, returns that task if exists.
        """
        if task_id == 0:
            return tasks
        if task_id not in tasks:
            return {"error": "Task not found"}, 404
        return tasks[task_id]

    def post(self):  # Add a new task.
        data = request.get_json()
        new_id = max(tasks.keys()) + 1
        tasks[new_id] = {"name": data["name"], "done": False}
        return tasks[new_id], 201

    def put(self, task_id):  # Update an existing task.
        if task_id not in tasks:
            return {"error": "Task not found"}, 404
        data = request.get_json()
        tasks[task_id].update(data)
        return tasks[task_id]

    def delete(self, task_id):  # Remove a task by task_id.
        if task_id not in tasks:
            return {"error": "Task not found"}, 404
        deleted = tasks.pop(task_id)
        return {"deleted": deleted}


# Define routes
api.add_resource(Task, "/tasks", "/tasks/<int:task_id>")

# Run the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
