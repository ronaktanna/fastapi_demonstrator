# FastAPI CRUD Demonstrator

A demonstration project showcasing how to build a RESTful API using FastAPI with CRUD operations over a SQLite database.

## Project Overview

This project serves as a practical example of implementing a FastAPI application with:
- Complete CRUD (Create, Read, Update, Delete) operations
- SQLite database integration using SQLAlchemy
- Pydantic models for request/response validation
- Proper project structure and organization

## Project Structure

```
py_fastapi_demonstrator/
│
├── .venv/                  # Virtual environment directory
├── Application/           
│   ├── __init__.py        # Package initializer
│   ├── crud.py            # CRUD operation implementations
│   ├── database.py        # Database configuration and session management
│   ├── main.py            # FastAPI application entry point
│   ├── models.py          # SQLAlchemy ORM models
│   └── schemas.py         # Pydantic models for request/response
│
└── sql_app.db             # SQLite database file
```

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/ronaktanna/py_fastapi_demonstrator.git
cd py_fastapi_demonstrator
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

4. Run the application
```bash
uvicorn Application.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

The following endpoints are available:

- `GET /items/` - List all items
- `GET /items/{item_id}` - Get a specific item
- `POST /items/` - Create a new item
- `PUT /items/{item_id}` - Update an existing item
- `DELETE /items/{item_id}` - Delete an item

## API Documentation

FastAPI provides automatic interactive API documentation using Swagger UI and ReDoc:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

This project uses:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type annotations
- [SQLite](https://www.sqlite.org/index.html) - Lightweight, serverless database

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
