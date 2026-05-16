from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from pymongo.errors import PyMongoError

from app.models import Category
from app.database import category_collection

router = APIRouter()


@router.post("/categories/")
def create_category(category: Category):

    # CHECK EXISTING CATEGORY
    existing_category = category_collection.find_one(
        {"category_name": category.category_name}
    )

    if existing_category:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )

    # GET LAST CATEGORY
    last_category = category_collection.find_one(
        sort=[("category_id", -1)]
    )

    # AUTO INCREMENT ID
    if last_category and "category_id" in last_category:
        category_id = last_category["category_id"] + 1
    else:
        category_id = 1

    # CATEGORY DATA
    category_data = {
        "category_id": category_id,
        "category_name": category.category_name,
        "monthly_budget": category.monthly_budget,
        "priority": category.priority,
        "active_status": category.active_status
    }

    # INSERT INTO DATABASE
    category_collection.insert_one(category_data)

    # REMOVE MONGODB OBJECT ID
    category_data.pop("_id", None)

    return {
        "success": True,
        "message": "Category created successfully",
        "data": category_data
    }
# GET ALL CATEGORIES
@router.get("/categories/")
def get_categories(
    category_name: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    active_status: Optional[bool] = Query(None),
    category_id: Optional[int] = Query(None),
    min_monthly_budget: Optional[float] = Query(None, alias="min_budget"),
    max_monthly_budget: Optional[float] = Query(None, alias="max_budget"),
):
    query = {}

    if category_name is not None:
        query["category_name"] = category_name
    if priority is not None:
        query["priority"] = priority
    if active_status is not None:
        query["active_status"] = active_status
    if category_id is not None:
        query["category_id"] = category_id

    if min_monthly_budget is not None or max_monthly_budget is not None:
        budget_filter = {}
        if min_monthly_budget is not None:
            budget_filter["$gte"] = min_monthly_budget
        if max_monthly_budget is not None:
            budget_filter["$lte"] = max_monthly_budget
        query["monthly_budget"] = budget_filter

    try:
        categories = list(category_collection.find(query))
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc

    # REMOVE OBJECT ID
    for category in categories:
        category.pop("_id", None)

    return {
        "success": True,
        "data": categories
    }