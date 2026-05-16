Expense Tracker API

The Expense Tracker API is a backend application developed using FastAPI and MongoDB that helps users manage and track their daily expenses efficiently. This project provides RESTful APIs to perform CRUD operations such as creating, viewing, updating, and deleting expense records. It is designed to be simple, fast, and beginner-friendly while demonstrating how modern backend applications are built using FastAPI.

The API stores expense details such as title, amount, category, and description in a MongoDB database. FastAPI automatically generates interactive API documentation using Swagger UI, making it easy to test endpoints directly from the browser.

This project is useful for learning:

FastAPI framework
REST API development
MongoDB database integration
CRUD operations
Backend project structure
API testing using Swagger or Postman

The application is lightweight and can be extended with advanced features like:

User authentication and authorization
JWT security
Expense analytics and reports
Monthly and yearly expense tracking
Exporting reports to PDF or Excel
Docker deployment
Folder Structure
expense-tracker/
│
├── app.py                 # Main FastAPI application
├── database.py            # MongoDB database connection
├── models.py              # Pydantic data models
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .env                   # Environment variables
│
├── routers/               # API route files
│   └── expense.py
│
├── services/              # Business logic
│   └── expense_service.py
│
└── utils/                 # Helper functions
    └── helper.py
Features
Create new expense records
View all saved expenses
Update existing expenses
Delete expense records
MongoDB database connectivity
Interactive Swagger API documentation
Clean and modular project structure
Technologies Used
Python
FastAPI
MongoDB
PyMongo
Uvicorn
Installation Steps

Clone the repository:

git clone https://github.com/ashok1096/expense-tracker.git

Move to the project folder:

cd expense-tracker

Create a virtual environment:

python -m venv .venv

Activate the virtual environment:

.venv\Scripts\activate

Install required packages:

pip install -r requirements.txt

Run the FastAPI server:

uvicorn app:app --reload

The server will run at:
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/862ca8e3-56e6-442b-a31c-428970c9202a" />


http://127.0.0.1:8000
API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

<img width="1352" height="595" alt="Screenshot 2026-05-16 174431" src="https://github.com/user-attachments/assets/6e920956-9659-4987-9aec-86e6fee6ec43" />


ReDoc:

http://127.0.0.1:8000/redoc
Author

Ashok Kumar

GitHub: https://github.com/ashok1096
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/2fda2186-a89a-4694-9d19-55a6bdef1fe3" />
