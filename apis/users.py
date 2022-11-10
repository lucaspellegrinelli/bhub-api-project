from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from dateutil.parser import parse

from core.schemas import User as UserSchema
from core.models import User as UserModel, BankDetails as BankDetailsModel

from core.sqlalchemy import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[UserSchema])
def read_all_users(
    corporate_name: str | None = Query(default=None, description="The corporate name of the user."),
    phone: str | None = Query(default=None, description="The phone number of the user."),
    address: str | None = Query(default=None, description="The address of the user."),
    registration_date: str | None = Query(default=None, description="The registration date of the user."),
    declared_revenue: float | None = Query(default=None, description="The declared revenue of the user."),
    db: Session = Depends(get_db)
):
    """
    Returns a list of all users.
    """
    # creates the filters dictionary
    filters = {
        "corporate_name": corporate_name,
        "phone": phone,
        "address": address,
        "registration_date": parse(registration_date).date() if registration_date is not None else None,
        "declared_revenue": declared_revenue
    }

    # removes the None values from the filters dictionary
    filters = {k: str(v) for k, v in filters.items() if v is not None}

    # creates the query
    query_results = db.query(UserModel).filter_by(**filters).all()
    pydantic_models = [UserSchema.from_orm(r) for r in query_results]
    return pydantic_models

@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Returns the information for a specific user.
    """
    query_result = db.query(UserModel).filter(UserModel.id == user_id).first()
    if query_result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserSchema.from_orm(query_result)

@router.post("/", response_model=UserSchema)
def insert_user(user: UserSchema, db: Session = Depends(get_db)):
    """
    Inserts a new user into the database.
    """
    # Creating new bank details objects in database
    db_bank_details = [BankDetailsModel(**bank.dict()) for bank in user.bank_details]
    
    # Creating new user object in database
    user_data = user.dict()
    user_data.pop("bank_details")
    db_user = UserModel(**user_data)

    # Adding new user and bank details to database
    db.add(db_user)
    db.add_all(db_bank_details)
    db.commit()
    return UserSchema.from_orm(db_user)

@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    """
    Updates the information for a specific user.
    """
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.corporate_name = user.corporate_name
    db_user.phone = user.phone
    db_user.address = user.address
    db_user.registration_date = user.registration_date
    db_user.declared_revenue = user.declared_revenue
    db.commit()
    db.refresh(db_user)
    return UserSchema.from_orm(db_user)

@router.delete("/{user_id}", response_model=UserSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Deletes a specific user from the database.
    """
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return UserSchema.from_orm(db_user)