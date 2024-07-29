from flask import Flask,redirect,request,url_for,render_template
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
    
        acc=request.form['acct']
        pin=request.form['pinno']
        accountno=123
        pinno=567
        balance=0
        if int(acc)==int(accountno):
            if int(pin)==int(pinno):
                return render_template('service.html')
            return render_template('service.html')
        else:
            return 'invalid'
    return render_template('home.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/balance')
def balance():
    balance=2000
    return f'your balance is {balance}'
@app.route('/withdraw/<balance>',methods=['POST'])
def withdraw():
    render_template('withdraw.html')
    amt=request.form['amt']
    if amt<=balance:
        balance-=amt
        print(f'Your withdraw amount is {amt}')
    else:
        return f'Insufficient Funds'
    return "Please remove your card"
@app.route('/deposit/<balance>',methods=['POST'])
def deposit():
    amt=render_template('deposit.html')
    if amt>0:
        balance=2000
        balance+=amt
        return "you succesfully deposited"
    else:
        return "Amount must be positive"
    return render_template('back.html')    
app.run(debug=True)