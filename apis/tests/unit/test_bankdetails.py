import pytest

from core.schemas.bankdetails import BankDetails

def test_bank_details_creation():
    """ Test the creation of a new bank details """
    bank_details = BankDetails(
        agency="1234",
        account="123456",
        bank="Test Bank",
    )

    assert bank_details.agency == "1234"
    assert bank_details.account == "123456"
    assert bank_details.bank == "Test Bank"

def test_bank_details_creation_with_invalid_agency():
    """ Test the creation of a new bank details with invalid agency """
    with pytest.raises(ValueError):
        BankDetails(
            agency="abcde", # Non-digit agency
            account="123456",
            bank="Test Bank",
        )

def test_bank_details_creation_with_invalid_account():
    """ Test the creation of a new bank details with invalid account """
    with pytest.raises(ValueError):
        BankDetails(
            agency="1234",
            account="abcde", # Non-digit account
            bank="Test Bank",
        )