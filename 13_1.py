"""Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
Use the prior prime number exercise as a starting point.
For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31.
The response must be in the format of {"Number":31, "isPrime":true}."""
from flask import Flask, request
app = Flask(__name__)
@app.route('/primenumber')
def prime_number(user):
    args = request.args
    if (user > 0 and user <= 3):
        number= int(args.get("number"))
        primenumber=number
        return str(primenumber)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


