from sqlalchemy.orm import sessionmaker
from db.models import engine, Category, Product

session = sessionmaker(bind=engine)()


food = Category(name="Food", description="Delicasies", discout=0)
electronics = Category(name="Electronics", description="Boom boom", discout=0)

session.add_all( [food, electronics] )
session.commit()