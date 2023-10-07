from flask import Flask, render_template, request, redirect

app = Flask(__name__)

is_quit = False
user = {'pin': 1234, 'balance': 3000}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle the form submission (e.g., PIN verification)
        pin = int(request.form['pin'])
        if pin == user['pin']:
            return redirect('/menu')
        else:
            return "Entered wrong pin"

    return '''
        <form method="post">
            Please enter your four-digit pin: <input type="text" name="pin"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    global is_quit
    if is_quit:
        return "Thank you for choosing Python ATM. Please visit again."

    if request.method == 'POST':
        query = int(request.form['query'])
        if query == 1:
            amount = int(request.form['amount'])
            if amount > user['balance']:
                return "Your account balance is too low! Please enter a lower amount"
            else:
                user['balance'] -= amount
                return f"{amount} Rupees successfully withdrawn. Your remaining balance is {user['balance']} Money<br><a href='/menu'>Back to menu</a>"

        elif query == 2:
            amount = int(request.form['amount'])
            user['balance'] += amount
            return f"{amount} Money successfully deposited. Your remaining balance is {user['balance']} Money<br><a href='/menu'>Back to menu</a>"

        elif query == 3:
            is_quit = True
            return "Thank you for choosing Python ATM. Please visit again."

    return render_template('menu.html', user=user)

if __name__ == '__main__':
    app.run()
