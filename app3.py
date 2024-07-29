from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
accounts={'12345':{'pin':'111','balance':3000},
          '45678':{'pin':'222','balance':6000}}
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        accno=request.form['accno']
        pinno=request.form['pinno']
        initial_balance=int(request.form.get('balance',0))
        if accno in accounts:
            return 'Account Already existed',400
        accounts[accno]={'pin':pinno,'balance':initial_balance}
        return 'Account created successfully'
    return render_template('home.html')
@app.route('/data')
def data():
    accounts_list=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
    return accounts_list
@app.route('/alreadyacc',methods=['GET','POST'])
def alreadyacc():
    if request.method=='POST':
        accno=int(request.form['accno'])
        pinno=request.form['pinno']
        if accno in accounts:
            accounts_list=[{'account_id':accno,'pinno':details['pin']} for accno,details in accounts.items()]
            if pinno==accounts[accno]['pinno']:
                return redirect(url_for('panel',accno=accno,pinno=pinno))
            else:
                return 'Invalid Pin'
        else:
            return "Invalid Account_no",400
    return render_template('login.html')
@app.route('/panel/<accno>/<pinno>',methods=['GET','POST'])
def panel(accno,pinno):
    return render_template("options.html",accno=accno,pinno=pinno)
@app.route('/deposit/<accno>/<pinno>',methods=["GET","POST"])
def deposit(accno,pinno):
    if request.method=="POST":
        amt=int(request.form['amt'])
        balance=[{'account_no':accno,'balance':details['balance']} for accno,details in accounts.items()]
        if balance[0]['account_no']==accno:
            balance=int(balance[0]['balance'])
            n_balance=balance+amt
            print("Amount Deposited Successfully...")
            return f"Your Available Balance is {n_balance}"
    return render_template("deposit.html",accno=accno,pinno=pinno)
@app.route('/withdraw/<accno>/<pinno>',methods=['GET','POST'])
def withdraw(accno,pinno):
    if request.method=='POST':
        amt=int(request.form['amt'])
        balance=[{'account_no':accno,'balance':details['balance']} for accno,details in accounts.items()]
        if balance[0]['account_no']==accno:
            balance=int(balance[0]['balance'])
            if balance>=amt and amt>0:
                n_balance=balance-amt
                print("Your Trasaction Completed Sucessfully...")
                return f"Your balance is {n_balance}"
            else:
                return "Insufficient Funds"
    return render_template("withdraw.html",accno=accno,pinno=pinno)
@app.route('/balance/<accno>/<pinno>',methods=['GET','POST'])
def balance(accno,pinno):
    if request.method=='GET':
        balance=[{'account_no':accno,'balance':details['balance']} for accno,details in accounts.items()]
        bal=balance[0]['balance']
        return f"Your balance is {bal}"
    return "Failde..."
app.run(debug=True,use_reloader=True)