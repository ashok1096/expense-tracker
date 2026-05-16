from datetime import date
from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from pymongo.errors import PyMongoError
from app.database import category_collection, expenses_collection

router = APIRouter()


@router.get("/expenses/summary")
def expenses_summary():
    try:
        expenses = list(expenses_collection.find())
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc

    total_spent = sum(expense.get("amount", 0) for expense in expenses)

    # Category-wise total
    category_summary = {}
    for expense in expenses:
        try:
            cat = category_collection.find_one({"category_id": expense.get("category_id")})
        except PyMongoError as exc:
            raise HTTPException(status_code=503, detail="Database unavailable") from exc
        name = cat.get("category_name") if cat else "Unknown"
        category_summary.setdefault(name, 0)
        category_summary[name] += expense.get("amount", 0)

    # Highest expense
    highest_expense = max(expenses, key=lambda x: x.get("amount", 0)) if expenses else None

    # Budget warnings
    warnings = []
    try:
        categories = list(category_collection.find())
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc

    for category in categories:
        try:
            category_expenses = list(expenses_collection.find({"category_id": category.get("category_id")}))
        except PyMongoError as exc:
            raise HTTPException(status_code=503, detail="Database unavailable") from exc
        total = sum(item.get("amount", 0) for item in category_expenses)
        if total > category.get("monthly_budget", 0):
            warnings.append(f'{category.get("category_name")} exceeded budget')

    return {
        "success": True,
        "total_spent": total_spent,
        "category_wise_spending": category_summary,
        "highest_expense": highest_expense,
        "budget_warnings": warnings,
    }


@router.get("/expenses/")
def get_expenses(
    category_id: Optional[int] = Query(None),
    payment_mode: Optional[str] = Query(None),
    min_amount: Optional[float] = Query(None),
    max_amount: Optional[float] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
):
    query = {}

    if category_id is not None:
        query["category_id"] = category_id
    if payment_mode is not None:
        query["payment_mode"] = payment_mode
    if min_amount is not None or max_amount is not None:
        amount_filter = {}
        if min_amount is not None:
            amount_filter["$gte"] = min_amount
        if max_amount is not None:
            amount_filter["$lte"] = max_amount
        query["amount"] = amount_filter
    if start_date is not None or end_date is not None:
        date_filter = {}
        if start_date is not None:
            date_filter["$gte"] = start_date
        if end_date is not None:
            date_filter["$lte"] = end_date
        query["date"] = date_filter

    try:
        expenses = list(expenses_collection.find(query))
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc

    for expense in expenses:
        expense.pop("_id", None)

    return {
        "success": True,
        "data": expenses
    }