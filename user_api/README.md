# My Flask API
# Flask REST API - Learning Project

> ⚠️ **Note:** I am currently learning Python and Flask.  
> This project was created as part of a learning process by following a tutorial video.  
> I did not write all of the code completely on my own.  

## Project Overview

This is a simple REST API built with **Flask**, **Flask-RESTful**, and **SQLAlchemy**.  
It allows you to:

- GET `/api/users/` — retrieve all users  
- POST `/api/users/` — add a new user (JSON body required)
> You need to use the extension **Thunder Client** (VS Code) or Postman to test the API. 

There is also a simple home route at `/`.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nrelvx/user_api.git
cd user_api
```
2. Create a virtual environment and activate it. In the project folder, run:

python -m venv .venv

3. Then install all dependencies from requirements.txt:

pip install -r requirements.txt

Now the project is ready to run. To start the Flask server, execute:
python api.py

| The server will run at http://127.0.0.1:5000/. Open this URL in your browser to see the home page, or use Thunder Client (VS Code) / Postman to test the API endpoints |

---Notes---
The SQLite database database.db is created automatically on first run.
Do not commit the database file to GitHub.
This project is for learning purposes only.
