ToDo API using Flask and Flask-RESTful.

Description:
- GET /tasks          — retrieve all tasks
- GET /tasks/<id>     — retrieve a task by id
- POST /tasks         — add a new task (json: {"name": "Task name"})
- PUT /tasks/<id>     — update a task (json: {"name": "...", "done": true/false})
- DELETE /tasks/<id>  — delete a task by id

Usage:
$ python app.py
Server will run at http://localhost:8080