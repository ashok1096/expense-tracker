from fastapi import FastAPI
from app.routers.category import router as category_router
from app.routers.expenses import router as expense_router

app = FastAPI(title="Personal Expense Tracker")


# INCLUDE ROUTERS
app.include_router(category_router)
app.include_router(expense_router)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Personal Expense Tracker API Running"
    }