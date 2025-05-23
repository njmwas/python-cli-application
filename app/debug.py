from sqlalchemy.orm import sessionmaker
from db.models import engine, Category, Product, ProductDetail


if __name__ == "__main__":

    session = sessionmaker(bind=engine)()
