from sqlalchemy import create_engine, Column, Integer, String, \
    Text, func, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///store.db")
BASE = declarative_base()

class Category(BASE):

    __tablename__ = "categories"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    description = Column(Text())
    discout = Column(String())
    createdAt = Column(DateTime(), default=datetime.now())

# BASE.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

