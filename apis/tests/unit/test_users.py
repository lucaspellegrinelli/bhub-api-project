import pytest
import datetime

from core.schemas.user import User

def test_user_creation():
    """ Test the creation of a new user """
    user = User(
        corporate_name="Test",
        phone="123456789",
        address="Test address",
        registration_date="01/01/2021",
        declared_revenue=1000.00,
        bank_details=[],
    )

    assert user.corporate_name == "Test"
    assert user.phone == "123456789"
    assert user.address == "Test address"
    assert user.registration_date == datetime.date(2021, 1, 1)
    assert user.declared_revenue == 1000.00
    assert user.bank_details == []

def test_user_creation_with_bank_details():
    """ Test the creation of a new user with bank details """
    user = User(
        corporate_name="Test",
        phone="123456789",
        address="Test address",
        registration_date="01/01/2021",
        declared_revenue=1000.00,
        bank_details=[
            {
                "id": 1,
                "bank": "Test Bank",
                "agency": "1234",
                "account": "123456",
            }
        ],
    )

    assert user.corporate_name == "Test"
    assert user.phone == "123456789"
    assert user.address == "Test address"
    assert user.registration_date == datetime.date(2021, 1, 1)
    assert user.declared_revenue == 1000.00
    assert user.bank_details[0].bank == "Test Bank"
    assert user.bank_details[0].agency == "1234"
    assert user.bank_details[0].account == "123456"


def test_user_creation_with_invalid_registration_date():
    """ Test the creation of a new user with invalid registration date """
    with pytest.raises(ValueError):
        User(
            corporate_name="Test",
            phone="123456789",
            address="Test address",
            registration_date="0101/2021", # Missing / between day and month
            declared_revenue=1000.00,
            bank_details=[],
        )

def test_user_creation_with_invalid_phone():
    """ Test the creation of a new user with invalid phone """
    with pytest.raises(ValueError):
        User(
            corporate_name="Test",
            phone="abcdefghij", # Not numeric
            address="Test address",
            registration_date="01/01/2021",
            declared_revenue=1000.00,
            bank_details=[],
        )
