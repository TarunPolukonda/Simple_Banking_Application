from flask import Flask,redirect,request,url_for,render_template
app=Flask(__name__)
balance=20000
@app.route('/')
def home():
    return render_template(url_for('b_home.html'))
@app.route('/balance')
def balance():
    balance=20000
    return f'your balance is {balance}'
@app.route('/withdraw/<int:amt>')
def withdraw(amt):
    amt=request.form['amt']
    if amt<=balance:
        balance-=amt
        print(f'Your withdraw amount is {amt}')
    else:
        return f'Insufficient Funds'
    return "Please remove your card"
@app.route('/deposit/<int:amt>')
def deposit(amt):
    if amt>0:
        balance=2000
        balance+=amt
        return "you succesfully deposited"
    else:
        return "Amount must be positive"
    return "Please remove your card"    
app.run(debug=True)