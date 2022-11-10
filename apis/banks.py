from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.schemas import BankDetails as BankDetailsSchema
from core.models import BankDetails as BankDetailsModel

from core.sqlalchemy import get_db

# Initializes the API router
router = APIRouter(
    prefix="/banks",
    tags=["banks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[BankDetailsSchema])
def read_banks(db: Session = Depends(get_db)):
    """Returns a list of all banks."""
    query_result = db.query(BankDetailsModel).all()
    pydantic_models = [BankDetailsSchema.from_orm(r) for r in query_result]
    return pydantic_models

@router.get("/{bank_id}", response_model=BankDetailsSchema)
def read_bank(bank_id: int, db: Session = Depends(get_db)):
    """Returns a specific bank."""
    query_result = db.query(BankDetailsModel).filter(BankDetailsModel.id == bank_id).first()
    return BankDetailsSchema.from_orm(query_result)

@router.post("/", response_model=BankDetailsSchema)
def create_bank(bank: BankDetailsSchema, db: Session = Depends(get_db)):
    """Creates a new bank."""

    db_bank = BankDetailsModel(
        agency=bank.agency,
        account=bank.account,
        bank=bank.bank,
    )

    db.add(db_bank)
    db.commit()
    db.refresh(db_bank)
    return BankDetailsSchema.from_orm(db_bank)

@router.put("/{bank_id}", response_model=BankDetailsSchema)
def update_bank(bank_id: int, bank: BankDetailsSchema, db: Session = Depends(get_db)):
    """Updates a specific bank."""
    db_bank = db.query(BankDetailsModel).filter(BankDetailsModel.id == bank_id).first()
    db_bank.agency = bank.agency
    db_bank.account = bank.account
    db_bank.bank = bank.bank
    db.commit()
    db.refresh(db_bank)
    return BankDetailsSchema.from_orm(db_bank)

@router.delete("/{bank_id}", response_model=BankDetailsSchema)
def delete_bank(bank_id: int, db: Session = Depends(get_db)):
    """Deletes a specific bank."""
    db_bank = db.query(BankDetailsModel).filter(BankDetailsModel.id == bank_id).first()
    db.delete(db_bank)
    db.commit()
    return BankDetailsSchema.from_orm(db_bank)
    