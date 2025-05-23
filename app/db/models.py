from sqlalchemy import create_engine, Column, Integer, String, \
    Text, func, DateTime, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

engine = create_engine("sqlite:///db/store.db")
BASE = declarative_base()

class Category(BASE):

    __tablename__ = "categories"

    id = Column(Integer(), primary_key=True)
    name = Column(String())#, nullable=False
    description = Column(Text())
    discout = Column(String())
    createdAt = Column(DateTime(), default=datetime.now())

    products = relationship("Product", backref="category")

    def __repr__(self):
        return f"{self.name} id:{self.id}"

class Product(BASE):
    __tablename__ = "products"

    id = Column(Integer(), primary_key=True)
    name = Column(String)
    price = Column(Float(), default=0.0)
    quantity = Column(Integer())

    category_id = Column(Integer(), ForeignKey("categories.id"))
    # One-to-one relationship
    detail = relationship("ProductDetail", back_populates="product", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"{self.name} id:{self.id}"
    

class ProductDetail(BASE):
    __tablename__ = 'product_details'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    manufacturer = Column(String(100))
    warranty_period = Column(Integer)  # months
    expiry_date = Column(Date)
    barcode = Column(String(50))

    # One-to-one relationship
    product = relationship("Product", back_populates="detail")
