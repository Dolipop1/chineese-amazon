from flask import Flask, redirect, url_for, render_template, request, session as flask_session
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.secret_key = 'your_secret_key'

Base = declarative_base()

class Products(Base):
    __tablename__ = 'Product_name'
    id = Column(Integer, primary_key=True)
    Product_name = Column(String(30), nullable=False)
    Product_owner = Column(String(40), nullable=False)
    price = Column(Float, nullable=False)

    def __str__(self):
        return f'Product_name: {self.Product_name}; Product_owner: {self.Product_owner}; Price: {self.price}'
    
engine = create_engine('sqlite:///Products.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
db_session = Session()

@app.route('/')
def Sign_in():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        flask_session['user'] = username
        return redirect(url_for('user'))
    return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in flask_session:
        subjects = {'Westinghouse Outdoor Power Equipment':'Mark smith', 'SAMSUNG Galaxy':'Samsung'}
        return render_template('user.html', subjects=subjects)
    return redirect(url_for('login'))

@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'

@app.route('/logout')
def logout():
    flask_session.pop('user', None)
    return redirect(url_for('user'))

@app.route('/registration', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        flask_session['user'] = username
        return redirect(url_for('user'))
    return render_template('login.html')
    

@app.route('/amazonproducts', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        Product_name = request.form['Product_name']
        Product_owner = request.form['Product_owner']
        price = request.form['price']
        if Product_name and Product_owner and price:
            try:
                price = float(price)
                new_Product = Products(Product_name=Product_name, Product_owner=Product_owner, price=price)
                db_session.add(new_Product)
                db_session.commit()
                return redirect(url_for('user'))
            except ValueError:
                return 'Invalid input for price'
    return render_template('amazonproducts.html')

if __name__ == "__main__":
    app.run(debug=True)

product1 = Products(Product_name='160 ', 
 Product_owner='Mark Smith', price=150)
db_session.add(product1)
db_session.commit()

product2 = Products(Product_name='150',
 Product_owner='Samsung', price=160)
db_session.add(product2)
db_session.commit()

result = db_session.query(Products).all()
for row in result:
    print(row)

