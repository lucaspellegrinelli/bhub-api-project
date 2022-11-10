from core.sqlalchemy import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

user_bankdetails_association = Table(
    "user_bankdetails_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("bankdetails_id", Integer, ForeignKey("bank_details.id"), primary_key=True),
)