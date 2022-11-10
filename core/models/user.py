from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship

from core.sqlalchemy import Base
from core.models.associations.user_bankdetails import user_bankdetails_association

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    corporate_name = Column(String)
    phone = Column(String)
    address = Column(String)
    registration_date = Column(Date)
    declared_revenue = Column(Float)
    bank_details = relationship("BankDetails", secondary=user_bankdetails_association)