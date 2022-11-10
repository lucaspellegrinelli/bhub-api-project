from core.sqlalchemy import Base
from sqlalchemy import Column, Integer, String

class BankDetails(Base):
    __tablename__ = "bank_details"

    id = Column(Integer, primary_key=True, index=True)
    agency = Column(String)
    account = Column(String)
    bank = Column(String)