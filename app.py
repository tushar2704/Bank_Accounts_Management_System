#© 2023 Tushar Aggarwal. All rights reserved. github.com/tushar2704
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





dummy_customers = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe'},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith'}
]

@app.route('/customers')
def customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)





from flask_sqlalchemy import SQLAlchemy
import config
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

db.create_all()






from app import db, Customer

# Create dummy customers
dummy_customers = [
    Customer(first_name='John', last_name='Doe'),
    Customer(first_name='Jane', last_name='Smith')
]

# Add customers to the database
for customer in dummy_customers:
    db.session.add(customer)
db.session.commit()



@app.route('/transactions')
def transactions():
    transactions = [
        {'id': 1, 'type': 'Deposit', 'amount': 100},
        {'id': 2, 'type': 'Withdrawal', 'amount': 50}
    ]
    return render_template('transactions.html', transactions=transactions)





from flask_login import LoginManager, UserMixin, login_required

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    return User()

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')




@app.route('/make_transaction', methods=['GET', 'POST'])
@login_required
def make_transaction():
    if request.method == 'POST':
        # Process transaction logic here
        flash('Transaction successful', 'success')
        return redirect('/transactions')
    return render_template('transaction_form.html')








@app.route('/reports')
@login_required
def reports():
    return render_template('reports.html')
