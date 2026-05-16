from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class CategoryBase(BaseModel):
    category_name: str = Field(..., alias="name", example="Food")
    monthly_budget: float = Field(..., example=5000.0)
    priority: str = Field(..., example="High")
    active_status: bool = Field(default=True)

    model_config = {
        "populate_by_name": True,
    }


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
    }


class ExpenseBase(BaseModel):
    title: str = Field(..., example="Lunch")
    amount: float = Field(..., example=15.5)
    category: str = Field(..., example="Food")
    date: datetime = Field(default_factory=datetime.now)


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    date: Optional[datetime] = None


class Expense(ExpenseBase):
    id: str

    model_config = {
        "from_attributes": True,
    }
