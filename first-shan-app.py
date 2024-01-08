import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def sum():
   
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return str(result)
    else:
        return '''
            <form method="post">
                <p>Enter first number:</p>
                <p><input type="text" name="num1" /></p>
                <p>Enter second number:</p>
                <p><input type="text" name="num2" /></p>
                <p><input type="submit" value="Sum" /></p>
            </form>
        '''

if __name__ == '__main__':
   app.run()
