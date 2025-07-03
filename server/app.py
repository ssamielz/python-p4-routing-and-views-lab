#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'{param}'

@app.route('/count/<int:param>')
def count(param):
    return '\n'.join(str(n) for n in range(param)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation =='+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Unsupported operation'

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
