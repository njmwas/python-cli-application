from sqlalchemy.orm import sessionmaker
from db.models import Category, Product, engine
from prettytable import PrettyTable

session = sessionmaker(bind=engine)()


def get_categories():
    categories = session.query(Category).all()
    table = PrettyTable(["Name", "Description"])
    for category in categories:
        table.add_row([category.name, category.description])
    print(table)

def get_products():
    products = session.query(Product).all()    
    table = PrettyTable(["Name", "Manufacturer", "Price"])
    for product in products:
        table.add_row([product.name, product.detail.manufacturer, product.price])
    print(table)

def add_category(data):
    category = Category(**data)
    session.add(category)
    session.commit()