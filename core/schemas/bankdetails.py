from pydantic import BaseModel, validator

class BankDetails(BaseModel):
    """Data model for bank details."""
    agency: str
    account: str
    bank: str

    @validator("account")
    def validate_account(cls, value):
        """Ensures that the account is valid."""
        if not value.isdigit():
            raise ValueError("Account must contain only digits.")
        return value

    @validator("agency")
    def validate_agency(cls, value):
        """Ensures that the agency is valid."""
        if not value.isdigit():
            raise ValueError("Agency must contain only digits.")
        return value