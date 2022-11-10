from datetime import date
from dateutil.parser import parse
from pydantic import BaseModel, validator

from core.schemas.bankdetails import BankDetails

class User(BaseModel):
    """Data model for a BHub user."""
    corporate_name: str
    phone: str
    address: str
    registration_date: date
    declared_revenue: float
    bank_details: list[BankDetails]

    @validator("registration_date", pre=True)
    def parse_registration_date(cls, value):
        """Converts a string to a date object."""
        if isinstance(value, str):
            return parse(value).date()
        return value

    @validator("phone")
    def validate_phone(cls, value):
        """Ensures that the phone is valid."""
        if not value.isdigit():
            raise ValueError("Phone must contain only digits.")
        return value

    class Config:
        # ORM mode allows pydantic to convert from a database model to a pydantic model
        orm_mode = True