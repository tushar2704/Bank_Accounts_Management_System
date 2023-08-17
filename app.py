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
    return render_template('customers.html', customers=dummy_customers)
