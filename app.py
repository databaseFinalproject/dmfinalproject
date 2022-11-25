
from flask import Flask, request, render_template, redirect, session
from datetime import datetime
import config
from flask_migrate import Migrate
from exts import db
from models import Customers,Product,Region,Store,Salespersons,Transactions
app=Flask(__name__)


app.config.from_object(config)

db.init_app(app)

migrate=Migrate(app,db)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs =conn.execute("select 1")
#         print(rs.fetchone())






@app.route('/')
def main():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method =='GET':
        return render_template("register.html")
    else:
        register = request.form["op"]
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        address = request.form["address"]
        kind = request.form["kind"]
        if register == "register":
            customer=Customers(name=name,password=password,email=email,address=address
                               ,kind=kind)
            db.session.add(customer)
            db.session.commit()
            return redirect("/")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        login=request.form["op"]
        name=request.form["name"]
        password=request.form["password"]
        customer=Customers.query.filter_by(name=name).first()
        if login == "login":
            if not customer:
                return redirect("/register")
            else:
                if password==customer.password:
                    session['customer_id']=customer.id
                    return redirect("/")
                else:
                    return redirect("/login")

# @app.route('/user')
# def user():
#     user=request.args.get("user", default=1,type=int)
#     return f'user :{user}'
#
#
# @app.route('/user/<user_id>')
# def userDetail(user_id):
#     return render_template('userDetail.html', user_id=user_id ,user_name="foreverever")
#
#
# @app.route('/product')
# def product():
#     return 'product'
#
#
# @app.route('/product/<int:product_id>')
# def productDetail(product_id):
#     return 'product: %s' % product_id
#
# @app.route('/shop')
# def shop():
#     return 'shop'
#
#
# @app.route('/shop/<int:shop_id>')
# def shopDetail(shop_id):
#     return 'shop: %s' % shop_id
#
# @app.route('/order')
# def order():
#     return 'order'
#
# @app.route('/order/<int:order_id>')
# def orderDetail(order_id):
#     return 'order: %s'% order_id




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)