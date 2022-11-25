from exts import db
from datetime import datetime

class Customers(db.Model):
    __tablename__= "customers"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=False)
    kind=db.Column(db.String(10),nullable=False)
    business_cateory=db.Column(db.String(10))
    annual_income=db.Column(db.String(10))
    marriage_status=db.Column(db.Boolean)
    gender=db.Column(db.String(10))
    age=db.Column(db.Integer)
    income=db.Column(db.Integer)
    create_at=db.Column(db.DateTime,default=datetime.now)


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    inventory_amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    kind=db.Column(db.String(10),nullable=False)
    create_at=db.Column(db.DateTime,default=datetime.now)


class Region(db.Model):
    __tablename__ = "region"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    manager = db.Column(db.String(100))


class Store(db.Model):
    __tablename__ = "store"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address=db.Column(db.String(100),nullable=False)
    manager = db.Column(db.String(100), nullable=False)
    salersperson_number=db.Column(db.Integer)
    region_id=db.Column(db.Integer,db.ForeignKey("region.id"))
    region=db.relationship("Region",backref="store")


class Salespersons(db.Model):
    __tablename__ = "salespersons"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    job_titel = db.Column(db.String(10), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    store_id=db.Column(db.Integer,db.ForeignKey("store.id"))
    store=db.relationship("Store",backref="salespersons")


class Transactions(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_number=db.Column(db.Integer,nullable=False)
    product_id=db.Column(db.Integer,db.ForeignKey("product.id"))
    buyer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    salespersons_id=db.Column(db.Integer, db.ForeignKey("salespersons.id"))
    create_at=db.Column(db.DateTime,default=datetime.now)
    product=db.relationship("Product",backref="transaction")
    customer=db.relationship("Customers",backref="transaction")
    salespersons = db.relationship("Salespersons", backref="transaction")









