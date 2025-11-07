# Mood Tracker API 🎭

A RESTful API built with FastAPI for tracking daily moods and analyzing emotional well-being. This project demonstrates modern Python web development with proper validation, documentation, and REST principles.

## 🚀 Features

- **CRUD Operations**: Create, read mood entries
- **Data Validation**: Strict input validation using Pydantic
- **Auto-generated Documentation**: Interactive Swagger UI and ReDoc
- **RESTful Design**: Clean API endpoints following REST principles
- **Error Handling**: Proper HTTP status codes and error messages

## 📋 API Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `GET` | `/` | Home page 
| `GET` | `/moods` | Get all mood entries
| `GET` | `/mood/{id}` | Get specific mood by ID | `id` (path parameter) 
| `POST` | `/moods/add` | Create new mood entry | JSON body 

## 🛠️ Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation and settings management
- **Python** - Programming language
- **Type Hints** - Enhanced code clarity and IDE support

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd mood-tracker-api
2. Install dependencies
   ```
   pip install fastapi uvicorn
4. Run the application
   ```
   uvicorn main:app 
6. Access the API
API: http://localhost:8000
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

🎯 Usage Examples
Create a new mood entry
```
curl -X POST "http://localhost:8000/moods/add" \
     -H "Content-Type: application/json" \
     -d '{
       "mood": "happy",
       "mark": 9,
       "note": "Great day at work!",
       "created_at": "2024-01-20"
     }'
```
Get all mood entries
curl "http://localhost:8000/moods"

Get specific mood entry
curl "http://localhost:8000/mood/1"

🔮 Future Enhancements
Database integration (SQLite/PostgreSQL)
-User authentication
-Mood statistics and analytics
-Date-based filtering
-Docker containerization
