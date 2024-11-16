from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.or

Base = declarative_base()

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    price = Column(Integer, nullable = False)
    quantity = Column(Integer, nullable = False)